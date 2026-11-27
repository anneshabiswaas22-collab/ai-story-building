#!/usr/bin/env python3
"""Episode 05 source and asset validation."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.episode_package import check_cli
if __name__ == '__main__':
    check_cli(Path(__file__).resolve().parent)
