#!/usr/bin/env python3
import os
import json
import sys

def format_all_json():
    target_dirs = ["device", "source"]
    formatted_count = 0
    
    for target_dir in target_dirs:
        if not os.path.exists(target_dir):
            print(f"Warning: {target_dir} directory not found, skipping.")
            continue
            
        for root, _, files in os.walk(target_dir):
            for file in files:
                if file.endswith(".json"):
                    file_path = os.path.join(root, file)
                    display_path = file_path.replace("\\", "/")
                    print(f"Formatting {display_path}")
                
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            data = json.load(f)
                        
                        # Sort keys and indent 4 spaces, preserving UTF-8
                        formatted_content = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
                        
                        # Ensure single trailing newline
                        formatted_content = formatted_content.rstrip() + "\n"
                        
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(formatted_content)
                        
                        formatted_count += 1
                    except Exception as e:
                        print(f"Error formatting {display_path}: {e}", file=sys.stderr)
                        sys.exit(1)
                    
    print(f"Formatted {formatted_count} JSON files")

if __name__ == "__main__":
    format_all_json()
