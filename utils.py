# utils.py
# Nexus Utility Helper

import time
import random
import csv
import os

def random_sleep(min_sec=2, max_sec=5):
    """模拟人类操作延迟"""
    delay = random.uniform(min_sec, max_sec)
    print(f"[System] Sleeping for {delay:.2f} seconds...")
    time.sleep(delay)

def save_to_csv(data_list, filename):
    """追加写入 CSV"""
    if not data_list:
        return
    
    file_exists = os.path.isfile(filename)
    keys = data_list[0].keys()
    
    with open(filename, 'a', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        if not file_exists:
            writer.writeheader()
        writer.writerows(data_list)
    print(f"[IO] Saved {len(data_list)} records to {filename}")

def log(msg):
    print(f"[Nexus] {msg}")