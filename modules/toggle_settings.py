import json
import os

settings = {
    "simulation_mode": True
}

def load_settings(path='data/settings.json'):
    global settings
    try:
        with open(path, 'r') as f:
            settings = json.load(f)
    except FileNotFoundError:
        print("[WARN] settings.json not found. Using defaults.")

def save_settings(path='data/settings.json'):
    with open(path, 'w') as f:
        json.dump(settings, f, indent=2)

def get_setting(key, default=None):
    return settings.get(key, default)
