# Quick Start Guide - ShadowCaster

## Get Started in 30 Seconds

### 1. Navigate to the project
```bash
cd /home/aaryan/Projects/ShadowCaster
```

### 2. Verify everything is set up
```bash
python3 setup.py
```

### 3. Run ShadowCaster
```bash
python3 main.py
```

Or use the shell script:
```bash
./shadowcaster.sh
```

## First Command

### Building a Network Scan

1. **Main Menu** → Select `1. Build New Command`
2. **Tool Selection** → Choose `Nmap`
3. **Enter Target** → Type `192.168.1.100`
4. **Select Categories** → Choose:
   - `1. Scan Types` 
   - `4. Timing Templates`
5. **Scan Type** → Select `2. TCP SYN scan (-sS)`
6. **Timing** → Select `5. Aggressive (-T4)`
7. **Options** → View command, then:
   - `1. Copy to Clipboard` - Copy the command
   - `2. Save to File` - Create executable script
   - `3. Save as Template` - Save for later use
   - `5. Execute Command` - Run (with confirmation!)

## Common Workflows

### Scan & Save
```
Build Command → Nmap → Enter target → Select options → Save as Template
```

### Quick Test
```
Load Template → Choose saved template → Copy to Clipboard → Paste in terminal
```

### WordPress Security Check
```
Build Command → WPScan → Enter URL → Enumerate all → Execute
```

## Menu Navigation

- Use **numbers** to select options
- Type **comma-separated numbers** for multiple selections (when allowed)
- Press **Enter** to confirm
- Use **Ctrl+C** to interrupt (will ask to confirm exit)

## Output Examples

### Nmap Command
```
nmap -sS -p 80,443 -T4 -sV 192.168.1.100
```

### Hydra Brute Force
```
hydra -l admin -P wordlist.txt -t 8 ssh 192.168.1.50
```

### WPScan WordPress
```
wpscan --url "http://target.com" --enumerate p,t,u
```

### Gobuster Directory Scan
```
gobuster dir -u http://target.com -w wordlist.txt -t 50
```

## Tips & Tricks

1. **Enable Hint Mode** for explanations
   ```
   Main Menu → Settings → Toggle Hint Mode
   ```

2. **Save Reusable Templates**
   ```
   After building → Save as Template → Name it "fast-scan" or "brute-force-ssh"
   ```

3. **View Saved Templates**
   ```
   Main Menu → Manage Templates
   ```

4. **Export Scripts**
   ```
   After building → Save to File → Get executable .sh script
   ```

5. **Use with Automation**
   ```bash
   # Build in ShadowCaster, then use in scripts
   sudo $(cat command_*.sh)
   ```

## Files Generated

When you save commands, they go to the `templates/` directory:

```
templates/
├── my-scan.json              # Saved template
└── command_20241018_120000.sh # Exported script
```

## Common Commands to Build

### Network Reconnaissance
- Nmap: Quick TCP SYN scan (T4)
- Nmap: Full port scan (T2)
- Gobuster: Web directory enumeration

### Authentication Testing
- Hydra: SSH brute force
- Hydra: HTTP form login attempt
- Hydra: FTP credential testing

### Web Application Security
- SQLMap: Parameter injection testing
- WPScan: WordPress vulnerability check
- Gobuster: Hidden directory discovery

### Wireless Security
- Aircrack-ng: WPA2 cracking
- Aircrack-ng: WEP analysis

## Important Reminders

⚠️ **Before Running Any Command:**
1. ✅ Review the command carefully
2. ✅ Understand what it does
3. ✅ Ensure you have authorization
4. ✅ Confirm execution when prompted

⚠️ **Legal Compliance:**
- Only test systems you own or have permission to test
- Unauthorized testing is illegal
- Always obtain written authorization
- Document all testing activities
- Report findings responsibly

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| Enter | Confirm/Select |
| 1-9 | Choose menu option |
| 1,3,5 | Multiple selections |
| Ctrl+C | Interrupt (with confirmation) |

## Troubleshooting

**Q: Command not found when executing?**
A: Install the tool first (e.g., `sudo apt install nmap`)

**Q: Can't copy to clipboard?**
A: Install xclip: `sudo apt install xclip`

**Q: Settings not saving?**
A: Settings are per-session by design; templates save permanently

**Q: How do I add a new tool?**
A: Create config file + builder class, see IMPLEMENTATION.md

## Files to Explore

- **README.md** - Full documentation
- **USAGE.md** - Detailed usage guide  
- **IMPLEMENTATION.md** - Technical implementation details
- **test_shadowcaster.py** - Test examples
- **examples.py** - Code examples

## Next Steps

1. **Explore** the tool by building a test command
2. **Practice** with hint mode enabled
3. **Save** commands you use frequently as templates
4. **Integrate** into your security testing workflow
5. **Extend** with custom tools (see IMPLEMENTATION.md)

## Need Help?

- See **USAGE.md** for detailed tool guides
- Check **README.md** for features and tools
- Run **setup.py** to verify installation
- Review **examples.py** for code samples
- Check **test_shadowcaster.py** for test cases

---

**Happy Testing! 🛡️**

Remember: With great power comes great responsibility. Use ShadowCaster ethically and legally.
