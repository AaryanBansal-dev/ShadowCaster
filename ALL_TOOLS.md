# ShadowCaster - Complete Tool List

This document lists ALL tools supported by ShadowCaster, including the initial 6 tools and the 16+ additional tools added in the second phase.

## 🔐 Password & Authentication Tools (3)

### 1. **John the Ripper**
- **Category**: Password Cracking
- **Command**: `john`
- **Description**: Fast password cracker commonly used to detect weak passwords
- **Key Features**:
  - Custom wordlist support
  - Word mangling rules
  - Multiple hash format support (NT, raw-md5, SHA-512)
  - Incremental/brute-force mode
- **Config File**: `configs/john_config.json`

### 2. **Hashcat**
- **Category**: Password Recovery
- **Command**: `hashcat`
- **Description**: World's fastest password recovery utility supporting hundreds of hash types
- **Key Features**:
  - 300+ hash types supported
  - Multiple attack modes (dictionary, combination, brute-force)
  - GPU acceleration support
  - Workload profiling (1-4)
  - Hybrid modes
- **Config File**: `configs/hashcat_config.json`

### 3. **Hydra** ⭐ *Original*
- **Category**: Network Login Auditor
- **Command**: `hydra`
- **Description**: Fast network logon cracker supporting many protocols
- **Key Features**:
  - 6+ protocols (SSH, FTP, HTTP, MySQL, SMB, etc.)
  - Multi-threading support
  - Custom authentication options
  - Verbosity control
- **Config File**: `configs/hydra_config.json`

### 4. **Medusa**
- **Category**: Parallel Login Auditor
- **Command**: `medusa`
- **Description**: Parallel network login auditor supporting many protocols
- **Key Features**:
  - Protocol support: SSH, FTP, HTTP, MSSQL, MySQL, SMB
  - Parallel task execution
  - Retry mechanism
  - Output reporting
- **Config File**: `configs/medusa_config.json`

---

## 🌐 HTTP & Web Testing (7)

### 5. **Nmap** ⭐ *Original*
- **Category**: Network Scanning
- **Command**: `nmap`
- **Description**: Network discovery and security auditing tool
- **Key Features**:
  - 7 scan types (SYN, TCP, UDP, ACK, Xmas, etc.)
  - Port selection and ranges
  - Timing templates (T0-T5)
  - Service version detection
  - OS detection
  - Multiple output formats (Normal, XML, Greppable)
- **Config File**: `configs/nmap_config.json`

### 6. **Nikto**
- **Category**: Web Server Scanner
- **Command**: `nikto`
- **Description**: Comprehensive web server scanner for vulnerabilities and misconfigurations
- **Key Features**:
  - Plugin-based scanning
  - SSL/TLS support
  - HTTP authentication
  - Multiple output formats
  - Customizable test sets
- **Config File**: `configs/nikto_config.json`

### 7. **Gobuster** ⭐ *Original*
- **Category**: Directory/DNS Enumeration
- **Command**: `gobuster`
- **Description**: Directory/DNS/VHOST enumeration tool
- **Key Features**:
  - 3 modes: dir, dns, vhost
  - Status code filtering
  - Custom headers
  - Performance tuning
  - Output reporting
- **Config File**: `configs/gobuster_config.json`

### 8. **FFUF**
- **Category**: Web Fuzzer
- **Command**: `ffuf`
- **Description**: Fast web fuzzer written in Go for content discovery
- **Key Features**:
  - Response filtering (size, status code, regex)
  - Multiple output formats (json, csv, html)
  - Multi-threading with rate limiting
  - Colorized output
  - Pattern matching
- **Config File**: `configs/ffuf_config.json`

### 9. **SQLMap** ⭐ *Original*
- **Category**: SQL Injection Testing
- **Command**: `sqlmap`
- **Description**: Automatic SQL injection and database takeover tool
- **Key Features**:
  - 5 injection techniques (Boolean, Error, Union, Stacked, Time)
  - Multiple risk levels (1-3)
  - Database enumeration
  - Multi-threading
  - Cookie/POST data support
- **Config File**: `configs/sqlmap_config.json`

### 10. **Dirsearch**
- **Category**: Web Path Scanner
- **Command**: `dirsearch`
- **Description**: Web path scanner with better accuracy than dirb
- **Key Features**:
  - Comprehensive wordlist support
  - File extension testing
  - Custom headers/cookies
  - Status code filtering
  - Performance tuning
- **Config File**: `configs/dirsearch_config.json`

### 11. **Feroxbuster**
- **Category**: Content Discovery
- **Command**: `feroxbuster`
- **Description**: Fast content discovery tool with advanced recursion
- **Key Features**:
  - Advanced recursion with configurable depth
  - Multi-threading (default 50)
  - Status code filtering
  - Output reporting
  - Rate limiting
- **Config File**: `configs/feroxbuster_config.json`

---

## 🕵️ Reconnaissance & Enumeration (3)

### 12. **Amass**
- **Category**: OSINT/Asset Discovery
- **Command**: `amass`
- **Description**: In-depth attack surface mapping and external asset discovery
- **Key Features**:
  - Subdomain enumeration
  - Brute-force capabilities
  - Data source information
  - Recursive searching
  - Multiple output formats
- **Config File**: `configs/amass_config.json`

### 13. **Sublist3r**
- **Category**: Subdomain Enumeration
- **Command**: `sublist3r`
- **Description**: Fast subdomain discovery using multiple search engines
- **Key Features**:
  - Multiple search engine support
  - Brute-force option
  - Port-based verification
  - Multi-threading
  - Output file support
- **Config File**: `configs/sublist3r_config.json`

### 14. **WPScan** ⭐ *Original*
- **Category**: WordPress Security
- **Command**: `wpscan`
- **Description**: WordPress vulnerability scanner
- **Key Features**:
  - Plugin enumeration
  - Theme enumeration
  - User enumeration
  - Vulnerability detection
  - Detection modes (passive, aggressive, mixed)
- **Config File**: `configs/wpscan_config.json`

---

## ⚔️ Post-Exploitation & Lateral Movement (1)

### 15. **CrackMapExec (CME)**
- **Category**: Windows/AD Pentesting
- **Command**: `cme`
- **Description**: Swiss army knife for pentesting Windows/Active Directory environments
- **Key Features**:
  - Multiple protocols: SMB, SSH, RDP, MSSQL
  - Module support (mimikatz, enum_shares)
  - Hash-based authentication
  - Local authentication option
  - Verbose output
- **Config File**: `configs/cme_config.json`

---

## 📡 Network & Port Scanning (2)

### 16. **Masscan**
- **Category**: Fast Port Scanner
- **Command**: `masscan`
- **Description**: Fastest internet port scanner (entire internet in <6 minutes)
- **Key Features**:
  - Configurable packet rate
  - Banner grabbing
  - Target list support
  - Multiple output formats (XML, list, greppable)
  - Port range scanning
- **Config File**: `configs/masscan_config.json`

### 17. **Netcat**
- **Category**: Network Utility
- **Command**: `nc`
- **Description**: Network Swiss Army knife for reading/writing across networks
- **Key Features**:
  - Listen mode
  - Command execution after connection
  - Port specification
  - Timeout control
  - DNS lookup options
  - Zero-I/O mode (port scan)
- **Config File**: `configs/netcat_config.json`

---

## 🔓 Wireless & Bluetooth Security (1)

### 18. **Aircrack-ng** ⭐ *Original*
- **Category**: Wireless Network Assessment
- **Command**: `aircrack-ng`
- **Description**: Wireless network security suite
- **Key Features**:
  - WEP/WPA attack modes
  - Dictionary attack support
  - BSSID/SSID targeting
  - GPU acceleration options
  - CPU core selection
- **Config File**: `configs/aircrack_config.json`

---

## 📁 File & Data Analysis (2)

### 19. **ExifTool**
- **Category**: Metadata Analysis
- **Command**: `exiftool`
- **Description**: Read, write, and edit metadata in various file formats
- **Key Features**:
  - View all metadata
  - Modify metadata fields
  - Binary extraction
  - Grouped output
  - JSON export
  - Duplicate tag detection
- **Config File**: `configs/exiftool_config.json`

### 20. **Binwalk**
- **Category**: Binary Analysis
- **Command**: `binwalk`
- **Description**: Search and analyze binary images for embedded files
- **Key Features**:
  - Signature scanning
  - Entropy analysis
  - Embedded file extraction
  - Recursive scanning
  - Matryoshka scan (nested files)
  - Multiple output formats
- **Config File**: `configs/binwalk_config.json`

---

## 📊 Summary

| Category | Count | Tools |
|----------|-------|-------|
| Password & Auth | 4 | John, Hashcat, Hydra, Medusa |
| HTTP & Web | 7 | Nmap, Nikto, Gobuster, FFUF, SQLMap, Dirsearch, Feroxbuster |
| Reconnaissance | 3 | Amass, Sublist3r, WPScan |
| Post-Exploitation | 1 | CrackMapExec |
| Network & Scanning | 2 | Masscan, Netcat |
| Wireless & BT | 1 | Aircrack-ng |
| File & Data | 2 | ExifTool, Binwalk |
| **TOTAL** | **20** | **All Tools** |

---

## 🎯 Tools by Phase

### Phase 1: Initial Release ⭐ (6 Tools)
1. Nmap
2. Hydra
3. SQLMap
4. WPScan
5. Gobuster
6. Aircrack-ng

### Phase 2: Expansion (14+ Tools)
1. John the Ripper
2. Hashcat
3. Medusa
4. Nikto
5. FFUF
6. Masscan
7. Netcat
8. CrackMapExec
9. ExifTool
10. Binwalk
11. Dirsearch
12. Feroxbuster
13. Amass
14. Sublist3r

---

## 📝 Usage

Each tool can be accessed through the interactive ShadowCaster menu:

```bash
python3 main.py
```

Then:
1. Select "Build New Command"
2. Choose tool from the list (now 20 tools!)
3. Follow interactive prompts
4. Preview, copy, save, or execute

---

## 🔄 Future Tools (Planned)

### Additional Security Tools to Consider:
- **Metasploit Framework** (msfvenom, msfconsole)
- **SearchSploit** (Exploit-DB offline)
- **Kismet** (Wireless network detection)
- **Bluelog** (Bluetooth scanning)
- **Btlejack** (BLE hijacking)
- **Sherlock** (Social media OSINT)
- **theHarvester** (Email/OSINT)
- **LinEnum.sh** / **linux-smart-enumeration**
- **enum4linux** / **rpcclient** (SMB enumeration)

---

## ✨ Tool Configuration Format

All tools use standardized JSON configuration:

```json
{
  "name": "Tool Name",
  "description": "Description",
  "command": "command-name",
  "categories": {
    "Category": {
      "options": [
        {
          "flag": "-flag",
          "description": "Description",
          "variable": false
        }
      ]
    }
  },
  "required": {
    "parameter": {
      "prompt": "Prompt:",
      "description": "Description"
    }
  }
}
```

---

## 🚀 Adding New Tools

To add a new tool:

1. Create `configs/toolname_config.json` with tool configuration
2. Add corresponding builder class to `modules/tool_builders.py` (if needed)
3. Register in `main.py` TOOL_BUILDERS dictionary
4. Update this file (ALL_TOOLS.md)

---

## 📄 Documentation Files

- **README.md** - Full project documentation
- **QUICKSTART.md** - Quick start guide
- **USAGE.md** - Detailed usage guide
- **IMPLEMENTATION.md** - Technical details
- **PROJECT_SUMMARY.txt** - Executive summary
- **NEW_TOOLS.md** - New tools specifications
- **ALL_TOOLS.md** - This file (complete tool list)

---

**Last Updated**: October 18, 2025  
**Total Tools**: 20  
**Total Configurations**: 20  
**Status**: ✅ Production Ready
