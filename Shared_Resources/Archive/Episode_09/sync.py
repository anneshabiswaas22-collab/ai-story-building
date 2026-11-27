#!/usr/bin/env python3
"""Episode 09 written handoff synchronization."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.episode_package import sync_cli
if __name__ == '__main__':
    sync_cli(Path(__file__).resolve().parent)
