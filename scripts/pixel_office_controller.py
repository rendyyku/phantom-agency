"""
Phantom Intelligence — Pixel Agents Office Controller
Controls the 5 autonomous agents in the Pixel Agents HQ workspace.
"""
import os
import sys
import time
import json
import random
import urllib.request
import urllib.error

TOKEN = "40f05fe0-7bde-4ea9-8ef1-e82dd8bb8b58"
PORT = 3200
BASE_URL = f"http://127.0.0.1:{PORT}"
CWD = "C:/Users/phantom/Desktop/PHANTOM/phantom-agency"

AGENTS = [
    {
        "id": "hermes-ceo",
        "name": "Hermes CEO",
        "team": "Phantom Intelligence",
        "activities": [
            ("WebSearch", {"query": "US Fed Interest Rate Decision & Gold Reserves"}),
            ("Bash", {"command": "python scripts/audit_daily_funnel.py"}),
            ("SendMessage", {"recipient": "Telegram Owner: Daily Pipeline Summary"}),
        ]
    },
    {
        "id": "macro-intel",
        "name": "Macro Intel",
        "team": "Phantom Intelligence",
        "activities": [
            ("WebSearch", {"query": "Strait of Hormuz Oil & XAUUSD Safe Haven Flow"}),
            ("Bash", {"command": "curl -s https://forexfactory.com/calendar"}),
            ("Write", {"file_path": "data/macro_daily_brief.json"}),
        ]
    },
    {
        "id": "video-creator",
        "name": "Video Creator",
        "team": "Phantom Intelligence",
        "activities": [
            ("Write", {"file_path": "remotion/src/scenes/HormuzGoldShock.tsx"}),
            ("Bash", {"command": "npx remotion render src/index.ts XAUUSD_9x16 out/video.mp4"}),
            ("SendMessage", {"recipient": "Telegram Owner: Video Preview Review"}),
        ]
    },
    {
        "id": "telegram-propaganda",
        "name": "Tele Propaganda",
        "team": "Phantom Intelligence",
        "activities": [
            ("Bash", {"command": "python scripts/generate_market_graphic.py --topic hormuz"}),
            ("SendMessage", {"recipient": "t.me/phantomsmcid: London Liquidity Sweep Update"}),
            ("SendMessage", {"recipient": "t.me/phantomsmcid: [⚡ Akses PRO Gratis]"}),
        ]
    },
    {
        "id": "onboarding-closer",
        "name": "Onboarding Lead",
        "team": "Phantom Intelligence",
        "activities": [
            ("Read", {"file_path": "data/pending_mt5_bindings.json"}),
            ("Bash", {"command": "python scripts/verify_exness_account.py --account 1928374"}),
            ("SendMessage", {"recipient": "User: MT5 Connected. Unlimited Access Granted."}),
        ]
    }
]

def send_hook_event(session_id: str, event_name: str, **kwargs):
    payload = {
        "session_id": session_id,
        "hook_event_name": event_name,
        "cwd": CWD,
        **kwargs
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        f"{BASE_URL}/api/hooks/claude",
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {TOKEN}"
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=3) as resp:
            return resp.read().decode("utf-8")
    except Exception as e:
        return str(e)

def init_office():
    print(f"🏢 Initializing Phantom Intelligence Pixel Office on {BASE_URL}...")
    for agent in AGENTS:
        # Start session
        res = send_hook_event(agent["id"], "SessionStart")
        print(f"  ✓ {agent['name']} initialized: {res}")
        time.sleep(0.5)

def run_cycle():
    init_office()
    print("\n🚀 All 5 agents active in Pixel Office! Running activity cycles...")
    try:
        while True:
            for agent in AGENTS:
                tool_name, tool_input = random.choice(agent["activities"])
                # Start tool
                send_hook_event(agent["id"], "PreToolUse", tool_name=tool_name, tool_input=tool_input)
                print(f"  [{agent['name']}] -> {tool_name}")
                time.sleep(2)
                # End tool
                send_hook_event(agent["id"], "PostToolUse", tool_name=tool_name, tool_output="Success")
                time.sleep(1)
            time.sleep(4)
    except KeyboardInterrupt:
        print("\nStopping office controller.")

if __name__ == "__main__":
    run_cycle()
