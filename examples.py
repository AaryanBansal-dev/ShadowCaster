"""
Example: Building an Nmap command
This script demonstrates how to use ShadowCaster programmatically
"""

import sys
from pathlib import Path

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent))

from utils.config_loader import ConfigLoader
from utils.display import Display, Colors
from modules.tool_builders import NmapBuilder


def example_nmap_build():
    """Build an Nmap command programmatically"""
    
    print(f"\n{Colors.BOLD}{Colors.CYAN}ShadowCaster - Programmatic Example{Colors.END}\n")
    
    # Load Nmap configuration
    loader = ConfigLoader()
    config = loader.load_config('nmap')
    
    if not config:
        print("Error: Could not load nmap config")
        return
    
    # Create builder
    builder = NmapBuilder(config)
    builder.set_hint_mode(True)
    
    # Manually set parameters for demo
    print(f"{Colors.BOLD}Building command with manual parameters...{Colors.END}\n")
    
    # Set required params
    builder.required_params = {
        'target': '192.168.1.0/24'
    }
    
    # Set selected flags
    builder.selected_flags = [
        '-sS',           # TCP SYN scan
        '-p 1-1000',     # Ports 1-1000
        '-T4',           # Aggressive timing
        '-sV',           # Service detection
        '-oX output.xml' # XML output
    ]
    
    # Build command
    command = builder.build_command()
    
    if command:
        Display.print_success("Command built successfully!")
        Display.print_command(command)
    else:
        Display.print_error("Failed to build command")


if __name__ == '__main__':
    example_nmap_build()
