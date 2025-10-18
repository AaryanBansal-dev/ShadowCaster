#!/usr/bin/env python3
"""
Installation and setup utility for ShadowCaster
"""

import os
import sys
import subprocess
from pathlib import Path


def check_python_version():
    """Check Python version"""
    if sys.version_info < (3, 8):
        print("Error: Python 3.8+ required")
        return False
    print(f"✓ Python {sys.version.split()[0]} installed")
    return True


def check_clipboard_support():
    """Check for clipboard utilities"""
    clipboard_tools = {
        'xclip': 'X11 clipboard',
        'xsel': 'Wayland clipboard',
        'pbcopy': 'macOS clipboard'
    }
    
    found = []
    for tool, desc in clipboard_tools.items():
        if os.system(f'which {tool} > /dev/null 2>&1') == 0:
            print(f"✓ Found {tool} ({desc})")
            found.append(tool)
    
    if not found:
        print("⚠ No clipboard tools found (optional)")
        print("  Install xclip (xsel) for clipboard support:")
        print("  Ubuntu/Debian: sudo apt install xclip")
        print("  Fedora: sudo dnf install xclip")
        print("  Arch: sudo pacman -S xclip")
    
    return len(found) > 0


def create_directories():
    """Create necessary directories"""
    dirs = ['configs', 'modules', 'utils', 'templates']
    
    for d in dirs:
        path = Path(d)
        if path.exists():
            print(f"✓ {d}/ already exists")
        else:
            path.mkdir(exist_ok=True)
            print(f"✓ Created {d}/")
    
    return True


def verify_configs():
    """Verify configuration files exist"""
    import json
    
    config_files = [
        'configs/nmap_config.json',
        'configs/hydra_config.json',
        'configs/sqlmap_config.json',
        'configs/wpscan_config.json',
        'configs/gobuster_config.json',
        'configs/aircrack_config.json'
    ]
    
    all_valid = True
    for config_file in config_files:
        path = Path(config_file)
        if not path.exists():
            print(f"✗ Missing: {config_file}")
            all_valid = False
        else:
            try:
                with open(path) as f:
                    json.load(f)
                print(f"✓ {config_file} (valid)")
            except json.JSONDecodeError:
                print(f"✗ {config_file} (invalid JSON)")
                all_valid = False
    
    return all_valid


def main():
    """Run setup checks"""
    print("\n" + "="*50)
    print("ShadowCaster - Setup Verification")
    print("="*50 + "\n")
    
    checks = [
        ("Python Version", check_python_version),
        ("Create Directories", create_directories),
        ("Configuration Files", verify_configs),
        ("Clipboard Support", check_clipboard_support),
    ]
    
    results = []
    for name, check_func in checks:
        print(f"\n{name}:")
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print(f"✗ Error: {e}")
            results.append((name, False))
    
    print("\n" + "="*50)
    print("Setup Summary")
    print("="*50)
    
    for name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status} - {name}")
    
    print("\n" + "="*50)
    
    if all(r for _, r in results):
        print("✓ All checks passed!")
        print("\nYou can now run ShadowCaster:")
        print("  python3 main.py")
        return 0
    else:
        print("✗ Some checks failed. Please review above.")
        return 1


if __name__ == '__main__':
    sys.exit(main())
