#!/usr/bin/env python
#
# Python code which automatically posts Message in a Telegram Group if any new update is found.
# Intended to be run on every push
# USAGE : python3 post.py
#
import re
import telebot
import os
import json
import datetime
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from time import sleep
from NoobStuffs.libtelegraph import TelegraphHelper
from github import Github

import banner

# Get configs from workflow secrets
def getConfig(config_name: str):
    return os.getenv(config_name)

try:
    BOT_TOKEN = getConfig("BOT_TOKEN")
    CHAT_ID = getConfig("CHAT_ID")
    PRIV_CHAT_ID = getConfig("PRIV_CHAT_ID")
except KeyError:
    print("Fill all the configs plox..\nExiting...")
    exit(0)

# Get the version of ASCP to check for updates
def getASCPVersion():
    VENDOR_REPO = "Project-ASCP/vendor_ascp"
    VERSION_PATH = "config/version.mk"
    VERSION_MAJOR_REGEX = r"PRODUCT_VERSION_MAJOR = (.+)"
    VERSION_MINOR_REGEX = r"PRODUCT_VERSION_MINOR = (.+)"
    try:
        g = Github(getConfig("GH_TOKEN"))
        repo = g.get_repo(VENDOR_REPO)
        content = repo.get_contents(VERSION_PATH).decoded_content.decode()
        major_version = re.search(VERSION_MAJOR_REGEX, content)
        minor_version = re.search(VERSION_MINOR_REGEX, content)
        major = major_version.group(1).strip() if major_version else None
        minor = minor_version.group(1).strip() if minor_version else None
        return f"{major}.{minor}" if major and minor else "5.4"
    except Exception as e:
        print(f"Error fetching version: {e}")
        return "5.4"

# Init bot
bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")
telegraph = TelegraphHelper(
    author_name="ASCP Bot",
    author_url="https://t.me/ascp_news",
    domain="graph.org"
)

# File directories
deviceDir = "device"
idDir = ".github/scripts"
devices_file = "device/devices.json"

def get_device_codenames():
    codenames = []
    if os.path.exists(deviceDir):
        for name in os.listdir(deviceDir):
            if os.path.isdir(os.path.join(deviceDir, name)):
                codenames.append(name)
    return codenames

# Load devices info
def load_devices_info():
    if not os.path.exists(devices_file):
        return []
    with open(devices_file, "r") as f:
        return json.load(f).get("devices", [])

DEVICES_INFO = load_devices_info()

def get_device_info_from_json(codename):
    for device in DEVICES_INFO:
        if device["codename"] == codename:
            return device
    return None

# Store IDs in a file to compare
def update(IDs):
    with open(f"{idDir}/file_ids.txt", "w+") as log:
        for ids in IDs:
            log.write(f"{str(ids)}\n")

# Return IDs of all latest files from json files
def get_new_id():
    file_id = []
    for codename in get_device_codenames():
        full_json_path = os.path.join(deviceDir, codename, "updater", "full.json")
        if os.path.exists(full_json_path):
            with open(full_json_path, "r", encoding="utf-8") as file:
                try:
                    data = json.loads(file.read())['response'][0]
                    file_id.append(data['md5'])
                except (IndexError, KeyError, json.JSONDecodeError):
                    continue
    return file_id

# Return previous IDs
def get_old_id():
    old_id = []
    if not os.path.exists(f"{idDir}/file_ids.txt"):
        return []
    with open(f"{idDir}/file_ids.txt", "r") as log:
        for ids in log.readlines():
            old_id.append(ids.replace("\n", ""))
    return old_id

# Remove elements in 2nd list from 1st, helps to find out which device got an update
def get_diff(new_id, old_id):
    first_set = set(new_id)
    sec_set = set(old_id)
    return list(first_set - sec_set)

# Grab needed info using ID of the file
def get_info(ID):
    found_codename = None
    for codename in get_device_codenames():
        full_json_path = os.path.join(deviceDir, codename, "updater", "full.json")
        if os.path.exists(full_json_path):
            with open(full_json_path, "r", encoding="utf-8") as file:
                try:
                    data = json.loads(file.read())['response'][0]
                    if data['md5'] == ID:
                        found_codename = codename
                        break
                except (IndexError, KeyError, json.JSONDecodeError):
                    continue
    
    if not found_codename:
        return None

    full_json_path = os.path.join(deviceDir, found_codename, "updater", "full.json")
    with open(full_json_path, "r", encoding="utf-8") as f:
        build_info = json.loads(f.read())['response'][0]
        
    device_info = get_device_info_from_json(found_codename)
    
    ASCP_VERSION = build_info.get('version', 'Unknown')
    OEM = device_info['vendor'] if device_info else "Unknown"
    DEVICE_NAME = device_info['model'] if device_info else found_codename
    DEVICE_CODENAME = found_codename
    MAINTAINER = device_info['maintainer_name'] if device_info else "Unknown"
    DATE_TIME = datetime.datetime.fromtimestamp(int(build_info['datetime']))
    DOWNLOAD_URL = build_info['url']
    BUILD_TYPE = "Official"
    SIZE = round(int(build_info['size'])/1073741824, 2)
    MD5 = build_info['md5']
    SHA256 = build_info.get('id', 'N/A')
    
    return {
        "version": ASCP_VERSION,
        "oem": OEM,
        "device_name": DEVICE_NAME,
        "codename": DEVICE_CODENAME,
        "maintainer": MAINTAINER,
        "datetime": DATE_TIME,
        "download": DOWNLOAD_URL,
        "buildtype": BUILD_TYPE,
        "size": SIZE,
        "md5": MD5,
        "sha256": SHA256,
        "xda": "N/A",
        "telegram": "N/A"
    }

# Prepare function for posting message in channel
def send_post(chat_id, image, caption):
    return bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

# Prepare message format for channel
def message_content(information):
    branch = os.getenv("BRANCH_NAME", "16.2")
    msg = ""
    msg += f"<b>ASCP Stable // {information['oem']} {information['device_name']} ({information['codename']})</b>\n\n" 
    msg += f"<u>Download</u>: <a href='{information['''download''']}'>Here</a>\n"
    msg += f"<u>Screenshots</u>: <a href='https://t.me/ascpos_marble/804?single'>Here</a>\n\n"
    msg += f"-> Maintainer: <b>{information['maintainer']}</b>\n"
    msg += f"-> ASCP Version: <code>{information['version']}</code>\n"
    msg += f"-> Changelog: <a href='https://raw.githubusercontent.com/Pixelify-AOSP/official_devices/refs/heads/{branch}/device/{information['''codename''']}/changelogs/changelog.md'>Here</a>\n"

    msg += f"\n#ASCP #Stable #{information['codename']} #Android16 #Official"
    return msg

# Send updates to channel and commit changes in repo
def tg_message():
    commit_message = "Update new IDs and push OTA"
    commit_description = "Data for following device(s) were changed:\n"
    diff = get_diff(get_new_id(), get_old_id())
    if len(diff) == 0:
        print("All are Updated\nNothing to do\nExiting...")
        return
    else:
        print(f"IDs Changed:\n{diff}\n\n")
        for devices in diff:
            info = get_info(devices)
            if not info:
                continue
            # BANNER_PATH = banner.generate_banner(info['oem'], info['device_name'], info['codename'])
            BANNER_PATH = "./assets/banners/template.png"
            if not os.path.exists(BANNER_PATH):
                # Fallback to latest.png if template is missing
                BANNER_PATH = "./assets/banners/latest.png"
            
            with open(BANNER_PATH, "rb") as image:
                send_post(CHAT_ID, image, message_content(info))
            commit_description += f"- {info['device_name']} ({info['codename']})\n"
            # os.remove(BANNER_PATH)
            sleep(5)
    update(get_new_id())
    with open("commit_mesg.txt", "w+") as f:
        f.write(f"ASCP: {commit_message} [BOT]\n\n{commit_description}")

# Prepare function for posting message in private group
def send_log(chat_id, text, button):
    return bot.send_message(
        chat_id=chat_id,
        text=text,
        reply_markup=button,
        disable_web_page_preview=True
    )

# Get all the devices which are in official repo
def get_devices():
    devices = []
    for codename in get_device_codenames():
        full_json_path = os.path.join(deviceDir, codename, "updater", "full.json")
        if os.path.exists(full_json_path):
            device_info = get_device_info_from_json(codename)
            with open(full_json_path, "r", encoding="utf-8") as file:
                try:
                    data = json.loads(file.read())['response'][0]
                    devices.append({
                        "device_name": device_info['model'] if device_info else data.get('device', codename),
                        "codename": codename,
                        "maintainer": device_info['maintainer_name'] if device_info else "Unknown",
                        "version": data['version']
                    })
                except (IndexError, KeyError, json.JSONDecodeError):
                    continue
    return devices

ASCP_VERSION_CHECK = max(device["version"] for device in get_devices())

# Prepare log format for private group
def tg_log():
    Updated = []
    YetToUpdate = []
    buttons = InlineKeyboardMarkup()
    all_devices = get_devices()
    for device in all_devices:
        if device['version'] == ASCP_VERSION_CHECK:
            Updated.append(device)
        else:
            YetToUpdate.append(device)
    count = 1
    msg = ""
    msg += f"<b>ASCP Update Status</b><br><br>"
    msg += f"<b>The following devices have been updated to the version</b> <code>{ASCP_VERSION_CHECK}</code> <b>in the current month:</b> "
    if len(Updated) == 0:
        msg += f"<code>None</code>"
    else:
        for device in Updated:
            msg += f"<br><b>{count}.</b> <code>{device['device_name']} ({device['codename']})</code> <b>-</b> {device['maintainer']}"
            count += 1
    msg += "<br><br>"
    count = 1
    msg += f"<b>The following devices have not been updated to the version</b> <code>{ASCP_VERSION_CHECK}</code> <b>in the current month:</b> "
    if len(YetToUpdate) == 0:
        msg += f"<code>None</code>"
    else:
        for device in YetToUpdate:
            msg += f"<br><b>{count}.</b> <code>{device['device_name']} ({device['codename']})</code> <b>-</b> {device['maintainer']}"
            count += 1
    msg += "<br><br>"
    msg += f"<b>Total Official Devices:</b> <code>{str(len(all_devices))}</code><br>"
    msg += f"<b>Updated during current month:</b> <code>{str(len(Updated))}</code><br>"
    msg += f"<b>Not Updated during current month:</b> <code>{str(len(YetToUpdate))}</code><br><br>"
    msg += f"<b>Information as on:</b> <code>{str(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M'))} hours (UTC)</code>"
    
    text = f"<b>ASCP Devices (v{ASCP_VERSION_CHECK}) Update Status</b>\n\n"
    text += f"<b>Total Official Devices:</b> <code>{str(len(all_devices))}</code>\n"
    text += f"<b>Updated during current month:</b> <code>{str(len(Updated))}</code>\n"
    text += f"<b>Not Updated during current month:</b> <code>{str(len(YetToUpdate))}</code>\n"
    text += f"<b>Information as on:</b> <code>{str(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M'))} hours (UTC)</code>"
    
    try:
        telegph_url = telegraph.create_page(title="ASCP Device Update Status", content=msg)
        button1 = InlineKeyboardButton("More Info", telegph_url['url'])
        buttons.add(button1)
    except Exception as e:
        print(f"Telegraph error: {e}")

    send_log(PRIV_CHAT_ID, text, buttons)

# Final stuffs
tg_message()
tg_log()
print("Successful")
sleep(2)
