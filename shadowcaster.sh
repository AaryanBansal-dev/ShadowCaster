#!/bin/bash
# ShadowCaster Launch Script

set -e

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Check Python version
PYTHON_CMD=$(command -v python3 || command -v python)

if [ -z "$PYTHON_CMD" ]; then
    echo "Error: Python 3 is not installed"
    exit 1
fi

# Run the application
"$PYTHON_CMD" "$SCRIPT_DIR/main.py"
