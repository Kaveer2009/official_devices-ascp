#!/usr/bin/env python3
import os
import json
import sys
from fix_busted_json import repair_json


def format_all_json():
    target_dirs = ["device", "source"]
    formatted_count = 0

    for target_dir in target_dirs:
        if not os.path.exists(target_dir):
            print(f"Warning: {target_dir} directory not found, skipping.")
            continue

        for root, _, files in os.walk(target_dir):
            for file in files:
                if not file.endswith(".json"):
                    continue

                file_path = os.path.join(root, file)
                display_path = file_path.replace("\\", "/")
                print(f"Formatting {display_path}")

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()

                    # Try normal JSON parsing first
                    try:
                        data = json.loads(content)
                    except json.JSONDecodeError:
                        print(f"Invalid JSON detected in {display_path}, attempting repair...")

                        repaired = repair_json(content)

                        # Verify repaired JSON
                        data = json.loads(repaired)

                        # Optional backup of original
                        backup_path = file_path + ".bak"
                        with open(backup_path, "w", encoding="utf-8") as bf:
                            bf.write(content)

                        print(f"Created backup: {backup_path}")

                    formatted_content = (
                        json.dumps(
                            data,
                            indent=4,
                            sort_keys=True,
                            ensure_ascii=False
                        ).rstrip()
                        + "\n"
                    )

                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(formatted_content)

                    formatted_count += 1

                except Exception as e:
                    print(f"Error formatting {display_path}: {e}", file=sys.stderr)
                    sys.exit(1)

    print(f"Formatted {formatted_count} JSON files")


if __name__ == "__main__":
    format_all_json()
