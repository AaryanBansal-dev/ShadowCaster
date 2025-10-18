# ShadowCaster - Penetration Testing Command Generator

A comprehensive CLI/TUI application for building penetration testing commands safely and interactively.

## Features

✓ **Interactive Command Building** - Walk through prompts to build accurate commands  
✓ **Multiple Tools Supported** - Nmap, Hydra, SQLMap, WPScan, Gobuster, Aircrack-ng  
✓ **Command Preview** - Review commands before execution  
✓ **Clipboard Integration** - Copy commands to clipboard  
✓ **Template System** - Save and reuse command templates  
✓ **File Export** - Export commands as executable scripts  
✓ **Hint Mode** - Beginner-friendly explanations  
✓ **Modular Design** - Easy to add new tools  
✓ **Safe by Default** - No execution without explicit confirmation  

## Installation

### Requirements
- Python 3.8+
- Linux/Mac (Windows with WSL recommended)

### Optional Dependencies (for clipboard support)
- `xclip` (Linux X11) - `sudo apt install xclip`
- `xsel` (Linux wayland) - `sudo apt install xsel`
- `pbcopy` (macOS) - built-in

### Setup

```bash
# Clone or navigate to the project
cd ShadowCaster

# Make scripts executable
chmod +x shadowcaster.sh run.py

# Run the application
./shadowcaster.sh
# or
python3 main.py
```

## Project Structure

```
ShadowCaster/
├── main.py                 # Main application
├── run.py                  # Python launch script
├── shadowcaster.sh         # Bash launch script
├── configs/                # Tool configurations
│   ├── nmap_config.json
│   ├── hydra_config.json
│   ├── sqlmap_config.json
│   ├── wpscan_config.json
│   ├── gobuster_config.json
│   └── aircrack_config.json
├── modules/                # Tool builders
│   ├── __init__.py
│   └── tool_builders.py
├── utils/                  # Utility modules
│   ├── __init__.py
│   ├── command_builder.py  # Base builder class
│   ├── config_loader.py    # Config file management
│   ├── display.py          # UI/Display utilities
│   └── file_manager.py     # File operations
└── templates/              # Saved command templates

```

## Usage

### Starting ShadowCaster

```bash
python3 main.py
```

You'll see a menu with options:
1. **Build New Command** - Interactively create a command
2. **Load Template** - Use a saved template
3. **Manage Templates** - View/edit/delete templates
4. **Settings** - Configure hint mode and other options
5. **Exit** - Quit application

### Building a Command

1. Select a tool from the available options
2. Enter required parameters (e.g., target IP)
3. Choose optional flags from categories
4. Preview and handle the generated command

### Command Options

After building a command, you can:
- **Preview** - Display the full command
- **Copy to Clipboard** - Ready to paste elsewhere
- **Save to File** - Export as executable script
- **Save as Template** - Reuse later with a custom name
- **Execute** - Run the command (with confirmation)

### Hint Mode

Enable in Settings for explanations of each flag and option. Great for learning!

## Supported Tools

### Nmap
Network discovery and security auditing
- Scan type selection (SYN, TCP, UDP, etc.)
- Port specification
- Timing templates (T0-T5)
- Service detection
- Output formats (Normal, XML, Greppable)

### Hydra
Network logon cracker
- Protocol selection
- Login name/file selection
- Password file
- Performance tuning
- Verbosity control

### SQLMap
SQL injection detection and exploitation
- Target URL specification
- Injection techniques
- Detection level and risk
- Database enumeration options
- Multi-threading support

### WPScan
WordPress vulnerability scanner
- Target URL
- Plugin/theme/user enumeration
- Detection modes
- Custom headers
- Output formats

### Gobuster
Directory/DNS/VHOST enumeration
- Multiple modes (dir, dns, vhost)
- Wordlist configuration
- Status code filtering
- Custom headers
- Performance tuning

### Aircrack-ng
Wireless network security suite
- WEP/WPA attack modes
- Dictionary attack support
- Target BSSID/SSID selection
- GPU acceleration options

## Examples

### Nmap Scan
```
Build New Command → Select Nmap
Target: 192.168.1.100
Select: TCP SYN scan, Ports: 1-1000, Timing: Aggressive
Output: nmap -sS -p 1-1000 -T4 192.168.1.100
```

### SSH Brute Force with Hydra
```
Build New Command → Select Hydra
Target: 192.168.1.50
Service: ssh
Username: root
Wordlist: /path/to/wordlist.txt
Output: hydra -l root -P /path/to/wordlist.txt ssh 192.168.1.50
```

### WordPress Scan with WPScan
```
Build New Command → Select WPScan
URL: http://target.com
Enumerate: Plugins, Themes, Users
Output: wpscan --url "http://target.com" --enumerate p,t,u
```

## Configuration

### Adding New Tools

1. Create `configs/newtool_config.json` with tool options
2. Create builder class in `modules/tool_builders.py` extending `CommandBuilder`
3. Add to `TOOL_BUILDERS` dict in `main.py`

Example config structure:
```json
{
  "name": "ToolName",
  "description": "Tool description",
  "command": "tool-command",
  "categories": {
    "Category Name": {
      "options": [
        {
          "flag": "-flag",
          "description": "Flag description",
          "variable": false
        }
      ]
    }
  },
  "required": {
    "param": {
      "prompt": "Enter param:",
      "description": "Param description"
    }
  }
}
```

## Command Line Arguments (Future)

Currently the app runs interactively. Command-line arguments support coming soon.

## Security Notes

- **NO commands are executed without explicit user confirmation**
- Always review commands before execution
- Only use in authorized testing environments
- Respect scope and rules of engagement
- Keep audit trails of your testing activities

## Troubleshooting

### "xclip/xsel not found" error
The application can't copy to clipboard. Install:
- **Ubuntu/Debian**: `sudo apt install xclip`
- **Fedora**: `sudo dnf install xclip`
- **Arch**: `sudo pacman -S xclip`

### Templates directory permissions
If templates don't save, ensure the `templates/` directory exists and is writable:
```bash
mkdir -p templates/
chmod 755 templates/
```

### Config not loading
Check that all JSON config files are valid:
```bash
python3 -m json.tool configs/nmap_config.json
```

## License

Use for authorized penetration testing only. Ensure you have proper authorization before testing any system.

## Contributing

To add features or tools:
1. Create config file in `configs/`
2. Implement builder in `modules/tool_builders.py`
3. Update documentation

## Author

Created as a cybersecurity tool for ethical hacking practice.

---

**⚠️ DISCLAIMER**: This tool is for authorized security testing only. Unauthorized access to computer systems is illegal. Always obtain written permission before testing. The author is not responsible for any misuse.
