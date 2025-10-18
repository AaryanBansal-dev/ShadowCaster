# ShadowCaster - Usage Guide

## Quick Start

### First Time Setup

```bash
# Run verification
python3 setup.py

# Make scripts executable
chmod +x shadowcaster.sh run.py

# Launch the application
python3 main.py
```

## Main Menu

After launching, you'll see the main menu with these options:

```
┌────────────────────────────────────────────────────┐
│         ShadowCaster - Main Menu                   │
└────────────────────────────────────────────────────┘

1. Build New Command        - Interactively build commands
2. Load Template            - Use saved templates
3. Manage Templates         - View/Edit/Delete templates
4. Settings                 - Configure options
5. Exit                     - Quit application
```

## Building Commands

### Step-by-Step Process

1. **Select Tool**
   ```
   Choose from: Nmap, Hydra, SQLMap, WPScan, Gobuster, Aircrack-ng
   ```

2. **Enter Required Parameters**
   ```
   Target IP: 192.168.1.100
   Service: ssh
   ```

3. **Select Categories** (optional)
   ```
   ▸ Select Categories
   1. Scan Types
   2. Port Options
   3. Timing Templates
   4. Output Options
   ```

4. **Choose Options from Category**
   ```
   ▸ Select options for Scan Types
   1. TCP SYN scan (-sS)
   2. TCP connect scan (-sT)
   3. UDP scan (-sU)
   ```

5. **Provide Values for Variable Options**
   ```
   Enter port range (e.g., 22,80,443 or 1-65535): 80,443,8080
   ```

6. **Review and Execute**
   ```
   Command: nmap -sS -p 80,443,8080 192.168.1.100
   
   Options:
   1. Preview Command
   2. Copy to Clipboard
   3. Save to File
   4. Save as Template
   5. Execute Command
   6. Build Another
   7. Back to Main Menu
   ```

## Detailed Tool Guides

### Nmap - Network Scanning

**Typical Use Case**: Scan a network for open ports and services

```
Step 1: Enter target
Target: 192.168.1.0/24

Step 2: Select categories
- Scan Types (required)
- Port Options
- Timing Templates
- Output Options

Step 3: Choose options
Scan Type: TCP SYN scan (-sS)
Ports: 1-1000
Timing: Aggressive (-T4)
Service Detection: -sV
Output: -oX results.xml
```

**Result**: `nmap -sS -p 1-1000 -T4 -sV -oX results.xml 192.168.1.0/24`

### Hydra - Brute Force

**Typical Use Case**: Attempt to crack service credentials

```
Step 1: Enter target and service
Target: 192.168.1.50
Service: ssh

Step 2: Select categories
- Authentication
- Performance
- Verbosity

Step 3: Choose options
Username: -l admin
Password file: -P /path/to/wordlist.txt
Threads: -t 8
Verbose: -V
```

**Result**: `hydra -l admin -P /path/to/wordlist.txt -t 8 -V ssh 192.168.1.50`

### SQLMap - SQL Injection Detection

**Typical Use Case**: Test web application for SQL injection

```
Step 1: Enter target URL
URL: http://target.com/product.php?id=1

Step 2: Select categories
- Injection
- Detection
- Enumeration

Step 3: Choose options
Parameter: -p id
Risk Level: --risk 2
Level: --level 2
Enumerate: --dbs
```

**Result**: `sqlmap -u "http://target.com/product.php?id=1" -p id --risk 2 --level 2 --dbs`

### WPScan - WordPress Scanning

**Typical Use Case**: Identify WordPress vulnerabilities

```
Step 1: Enter WordPress URL
URL: http://wordpress-site.com

Step 2: Select categories
- Reconnaissance
- Detection

Step 3: Choose options
Enumerate: --enumerate a (plugins, themes, users)
Detection mode: --detection-mode aggressive
```

**Result**: `wpscan --url "http://wordpress-site.com" --enumerate a --detection-mode aggressive`

### Gobuster - Directory Brute Force

**Typical Use Case**: Enumerate hidden directories on a web server

```
Step 1: Enter mode
Mode: dir (directory brute force)

Step 2: Enter target
URL: http://target.com

Step 3: Select categories
- Wordlist
- HTTP Options
- Performance

Step 3: Choose options
Wordlist: -w /usr/share/wordlists/dirb/common.txt
Status codes: -s 200,204,301,302
Threads: -t 50
```

**Result**: `gobuster dir -u "http://target.com" -w /usr/share/wordlists/dirb/common.txt -s 200,204,301,302 -t 50`

### Aircrack-ng - Wireless Cracking

**Typical Use Case**: Crack WPA2 password from captured handshake

```
Step 1: Enter capture file
File: /path/to/capture.cap

Step 2: Select categories
- Attack Mode
- Dictionary Attack
- Target Selection

Step 3: Choose options
Attack: -a 2 (WPA/WPA2)
BSSID: -b AA:BB:CC:DD:EE:FF
Wordlist: -w wordlist.txt
```

**Result**: `aircrack-ng -a 2 -b "AA:BB:CC:DD:EE:FF" -w wordlist.txt /path/to/capture.cap`

## Template Management

### Save a Template

After building a command:

```
1. Copy to Clipboard     ✓
2. Save to File          ✓
3. Save as Template      ← Choose this
```

Enter template name: `fast-http-scan`
Enter description: `Quick HTTP service scan with timing`

The template is saved and can be reused later.

### Load a Template

```
Main Menu → Load Template → Select template → Use This Template
```

This loads the saved command for review and execution.

### Manage Templates

```
Main Menu → Manage Templates → Select template → View/Use/Delete
```

View all saved templates and their commands.

## Settings

### Hint Mode

Enable for detailed explanations of each flag:

```
Settings → Toggle Hint Mode → ON
```

When enabled, descriptions appear before each option:

```
ℹ TCP SYN scan (default for privileged users)

▸ Select options for Scan Types
1. TCP SYN scan (-sS)
```

### Clear Templates

```
Settings → Clear All Templates → Confirm
```

Deletes all saved templates permanently.

## Command Options

After building a command, you have several options:

### 1. Preview Command
Displays the full command in a highlighted format:
```
nmap -sS -p 80,443 192.168.1.100
```

### 2. Copy to Clipboard
Copies the command to your system clipboard (requires xclip/xsel)

### 3. Save to File
Exports command as executable script:
```
#!/bin/bash
# Generated command

nmap -sS -p 80,443 192.168.1.100
```

### 4. Save as Template
Save the command with a friendly name for future use

### 5. Execute Command
⚠️ **Caution**: Runs the command on your system
- Shows warning first
- Requires explicit confirmation
- Only use in authorized environments

### 6. Build Another
Start building a new command without leaving the app

### 7. Back to Main Menu
Return to main menu

## Advanced Features

### Programmatic Usage

Use ShadowCaster in your own Python scripts:

```python
from utils.config_loader import ConfigLoader
from modules.tool_builders import NmapBuilder

loader = ConfigLoader()
config = loader.load_config('nmap')
builder = NmapBuilder(config)

# Set parameters
builder.required_params = {'target': '192.168.1.100'}
builder.selected_flags = ['-sS', '-p 1-1000', '-T4']

# Build
command = builder.build_command()
print(command)
```

### Adding Custom Tools

1. Create config file: `configs/mytool_config.json`
2. Create builder: `modules/tool_builders.py`
3. Register in `main.py`

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `Ctrl+C` | Interrupt/Cancel (confirm exit) |
| `Enter` | Select/Confirm |
| Numbers | Menu selection |

## Troubleshooting

### Issue: Clipboard not working

**Solution**: Install clipboard utility
```bash
# Linux
sudo apt install xclip

# Or
sudo apt install xsel
```

### Issue: Templates not saving

**Solution**: Check directory permissions
```bash
chmod 755 templates/
```

### Issue: Config file errors

**Solution**: Validate JSON
```bash
python3 -m json.tool configs/nmap_config.json
```

### Issue: Command not found when executing

**Reason**: Tool not installed on system
**Solution**: Install the required tool first
```bash
# Example: Install nmap
sudo apt install nmap

# Install hydra
sudo apt install hydra
```

## Best Practices

1. **Always Review Commands**
   - Never blindly execute commands
   - Understand what each flag does

2. **Test Scope**
   - Only test systems you have permission to
   - Define clear scope before testing

3. **Save Templates**
   - Create templates for common scans
   - Name them clearly (e.g., "fast-http-scan")

4. **Use Hint Mode**
   - Enable when learning new tools
   - Helps understand flag purposes

5. **Keep Audit Trail**
   - Save commands to files
   - Document your testing

6. **Ethical Testing**
   - Get written authorization
   - Respect privacy and laws
   - Report findings responsibly

## Example Workflows

### Workflow 1: Quick Network Scan

```
1. Build New Command
2. Select Nmap
3. Target: 192.168.1.100
4. Select: Scan Types → TCP SYN
5. Select: Timing → Aggressive
6. Copy to Clipboard
7. Paste in terminal with sudo
```

### Workflow 2: Save Reusable Scan

```
1. Build New Command
2. Select Nmap
3. Configure full scan options
4. Save as Template: "full-tcp-scan"
5. Later: Load Template → "full-tcp-scan"
6. Modify parameters as needed
7. Execute
```

### Workflow 3: WordPress Enumeration

```
1. Build New Command
2. Select WPScan
3. Enter WordPress URL
4. Select: Enumerate Users
5. Select: Enumerate Plugins
6. Save to File: "wpscan_results.sh"
7. Review script before executing
```

## Support & Resources

- **Nmap**: https://nmap.org/
- **Hydra**: https://github.com/vanhauser-thc/thc-hydra
- **SQLMap**: http://sqlmap.org/
- **WPScan**: https://wpscan.com/
- **Gobuster**: https://github.com/OJ/gobuster
- **Aircrack-ng**: https://www.aircrack-ng.org/

## Contact & Feedback

Report issues or suggest improvements through the project repository.

---

**Remember**: Always use these tools ethically and legally. Unauthorized testing is illegal.
