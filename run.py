#!/usr/bin/env python3
"""
ShadowCaster - Quick Setup and Run Script
"""

import sys
import subprocess
from pathlib import Path

def check_requirements():
    """Check if required packages are installed"""
    try:
        import json
        print("✓ json module available")
        return True
    except ImportError as e:
        print(f"✗ Missing required module: {e}")
        return False

def main():
    """Run the application"""
    script_dir = Path(__file__).parent
    main_py = script_dir / "main.py"
    
    if not main_py.exists():
        print("Error: main.py not found")
        sys.exit(1)
    
    print("Starting ShadowCaster...")
    subprocess.run([sys.executable, str(main_py)])

if __name__ == '__main__':
    if not check_requirements():
        sys.exit(1)
    
    main()
