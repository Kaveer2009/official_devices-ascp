import os
import json
import time
import re
import requests
import sys
from datetime import datetime

PROJECT_NAME = "project-ascp"
STATS_FILE = "source/download_stats.json"
DEVICES_JSON = "device/devices.json"
BASE_URL = f"https://sourceforge.net/projects/{PROJECT_NAME}/files/"
RSS_URL = f"https://sourceforge.net/projects/{PROJECT_NAME}/rss?path=/"
PROJECT_STATS_URL = f"https://sourceforge.net/projects/{PROJECT_NAME}/stats/json"
STATS_URL_TEMPLATE = "https://sourceforge.net/projects/{project}/files/{path}/stats/json"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": f"https://sourceforge.net/projects/{PROJECT_NAME}/files/",
    "X-Requested-With": "XMLHttpRequest",
}


def save_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )
        f.write("\n")


class StatsUpdater:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)

    def fetch(self, url, params=None, retries=3):
        for i in range(retries):
            try:
                response = self.session.get(url, params=params, timeout=30)
                if response.status_code == 403:
                    print(f"DEBUG: 403 Forbidden for {url} (Attempt {i + 1}/{retries})")
                response.raise_for_status()
                return response
            except Exception as e:
                if i == retries - 1:
                    print(f"Error fetching {url}: {e}")
                    return None
                time.sleep(5 * (i + 1))
        return None

    def get_discovery_list(self):
        print(f"Discovering devices from {BASE_URL}...")

        page = self.fetch(BASE_URL)
        if page:
            devices = re.findall(
                r'href="/projects/' + re.escape(PROJECT_NAME) + r'/files/([^/"]+)/"',
                page.text
            )
            devices = [f for f in set(devices) if f not in ("stats", "index_ajax")]
            if devices:
                print(f"Discovered {len(devices)} devices via HTML.")
                return devices

        print("HTML discovery failed or empty. Trying RSS...")

        rss = self.fetch(RSS_URL)
        if rss:
            devices = re.findall(r"<title>/([^/]+)/", rss.text)
            if devices:
                devices = list(set(devices))
                print(f"Discovered {len(devices)} devices via RSS.")
                return devices

        print("Falling back to local devices.json...")

        try:
            if os.path.exists(DEVICES_JSON):
                with open(DEVICES_JSON, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return [d["codename"] for d in data.get("devices", [])]
        except Exception as e:
            print(f"Warning: Could not read {DEVICES_JSON}: {e}")

        return []

    def run(self):
        params = {
            "start_date": "2010-01-01",
            "end_date": datetime.now().strftime("%Y-%m-%d")
        }

        devices = self.get_discovery_list()
        if not devices:
            print("CRITICAL: No devices found.")
            sys.exit(1)

        stats_data = {}

        if os.path.exists(STATS_FILE):
            try:
                with open(STATS_FILE, "r", encoding="utf-8") as f:
                    stats_data = json.load(f)
            except Exception:
                stats_data = {}

        print(f"Fetching global project stats from {PROJECT_STATS_URL}...")

        global_resp = self.fetch(PROJECT_STATS_URL, params=params)

        if global_resp:
            try:
                global_resp.json()
                print("DEBUG: Global stats fetched successfully.")
            except Exception:
                print("Warning: Global stats response not valid JSON.")

        print(f"Processing {len(devices)} devices...")

        updated_count = 0

        for device in sorted(devices):
            print(f"  {device}...", end=" ", flush=True)

            url = STATS_URL_TEMPLATE.format(
                project=PROJECT_NAME,
                path=device
            )

            resp = self.fetch(url, params=params)

            if resp:
                try:
                    count = resp.json().get("total", 0)
                    stats_data[device] = count
                    print(f"Done ({count})")
                    updated_count += 1
                except Exception:
                    print("JSON Error.")
            else:
                print("Failed.")
                if device not in stats_data:
                    stats_data[device] = 0

            time.sleep(1)

        save_json(STATS_FILE, stats_data)

        print(
            f"Successfully updated {STATS_FILE} "
            f"({updated_count} devices updated)"
        )


if __name__ == "__main__":
    updater = StatsUpdater()
    updater.run()
