🔐 Password & Authentication Tools
1. John the Ripper
A fast password cracker commonly used to detect weak passwords of users.

Flags to consider:
--wordlist=FILE: Load a custom wordlist
--rules: Enable word mangling rules
--format=FORMAT: Specify hash format (e.g., NT, raw-md5)
2. Hashcat
World’s fastest password recovery utility; supports hundreds of hash types and rules engines.

Flags:
-m <num>: Hash mode (e.g., MD5 = 0, NTLM = 1000)
-a <num>: Attack mode (0 = Straight, 1 = Combination, etc.)
-w <num>: Workload profile (adjusts performance/responsiveness)
3. Medusa
A parallel network login auditor supporting many protocols.

Key flags:
-h TARGET: Host to attack
-u USER: Username or user list
-P PASS_FILE: Password list
-M PROTO: Protocol (ssh, ftp, http, mssql...)
🌐 HTTP & Web Testing
4. Nikto
An open-source web server scanner that performs comprehensive tests.

Flags:
-h HOST: Target hostname/IP
-p PORT(S): Port(s) to scan
-Plugins PLUGIN: Run specific plugins (e.g., apacheusers)
5. Gobuster
Directory/file & DNS busting tool aimed at speed and ease of use.

Important flags:
-u URL: Target URL
-w WORDLIST: Path to wordlist
-x EXTENSIONS: File extensions to check (e.g., .php,.txt)
6. FFUF
Fast web fuzzer written in Go.

Common flags:
-u URL: Target URL with FUZZ keyword
-w FILE: Wordlist file
-c: Colorize output
-fs FILTER_SIZE: Filter responses by size
7. Sqlmap
Automatic SQL injection and database takeover tool.

Core flags:
-u URL: Target URL
--data=DATA: POST data
--level=LEVEL: Test level (1–5)
--risk=RISK: Risk factor (1–3)
--batch: Non-interactive run (skip prompts)
8. BurpSuite Pro (CLI Automation Interface)
Can be used via headless automation for large-scale scanning.

While not a CLI tool per se, consider building wrapper for:
Starting scans programmatically
Triggering active/passive checks
📦 Exploitation & Frameworks
9. Metasploit Framework (msfconsole, msfvenom)
One of the world’s most used exploit development and execution frameworks.

Focus modules:
msfvenom: Generate payloads
-p PAYLOAD: Specify payload type (e.g., windows/meterpreter/reverse_tcp)
-f FORMAT: Output format (exe, elf, raw)
LHOST/LPORT: Local IP and listener port
auxiliary/scanner/* modules
Use search within msfconsole to find scanners*
10. SearchSploit
Offline exploit database maintained by Exploit-DB.

Usage:
searchsploit <term>: Search for exploits
-m ID: Mirror exploit script to local directory
📍 Network Utilities
11. Masscan
One of the fastest internet port scanners (can scan entire Internet in under 6 minutes).

Flags:
-p PORTS: Comma-separated list of ports
-iL FILE: Input target list
--rate=RATE: Packets per second (default 100)
12. Netcat
Network Swiss Army knife used for reading/writing across networks.

Flags:
-l: Listen mode
-p PORT: Specify port
-e CMD: Execute after connection
-v: Verbose
-n: No DNS lookup (for faster response)
⚔️ Post-Exploitation & Lateral Movement
13. CrackMapExec (CME)
Swiss army knife for pentesting Windows/Active Directory environments.

Common flags:
-u USER: Username(s)
-p PASS: Password(s)
-M MODULE: Run module like mimikatz or enum_shares
--local-auth: Use local credentials
14. BloodHound
Graph-based analysis tool for identifying high-risk paths in AD.

While GUI-focused, ingest data using:
SharpHound collector scripts
BloodHound.py
15. Impacket Tools (psexec, secretsdump, smbclient)
Python class-based collection for Windows network protocol exploitation.

Tools:
secretsdump.py: Extract password hashes from SAM/LSA secrets
psexec.py: Execute commands on remote Windows machines
smbclient.py: Interact with SMB shares
📁 Content Discovery & Enumeration
16. Dirsearch
Web path scanner with better accuracy and reporting features than dirb.

Flags:
-u URL: Target base URL
-w WORDLIST: Wordlist path
-e EXTENSIONS: Extensions to test (php,asp)
17. Feroxbuster
Fast content discovery tool similar to Gobuster but with advanced recursion.

Flags:
-u URL: Base URL
-w FILE: Wordlist
-t THREADS: Number of concurrent threads
18. Amass
In-depth Attack Surface mapping and External Asset Discovery.

Flags:
-d DOMAIN: Target domain
-brute: Perform brute-force subdomain enumeration
-src: Print sources of discovered assets
19. Sublist3r
Subdomain enumeration tool designed for fast subdomain discovery.

Flags:
-d DOMAIN: Domain to Enumerate
-b: Brute-force subdomains
-o OUTPUT: Output file for subdomains
🔒 Wireless & Bluetooth Security
20. Kismet
Wireless network detector, sniffer, and intrusion detection system.

Main usage:
Starts as background daemon with -c INTERFACE
Logs findings in pcap/db/log formats
21. Bluelog
Simple Bluetooth scanner for discovery and monitoring.

Scans continuously on one or more interfaces
Logs discovered devices
22. Btlejack
Bluetooth Low Energy (BLE) connection hijacking tool.

Useful for reverse engineering BLE communications
Requires Bluetooth hardware capable of BLE monitoring
🧰 File and Data Analysis
23. ExifTool
Reads, writes, and edits meta information in a wide variety of files.

Common usages:
exiftool image.jpg: View metadata
exiftool -Artist='New Artist' image.jpg: Modify metadata
24. Binwalk
Tool for searching a given binary image for embedded files and executable code.

Usage:
binwalk firmware.bin: Analyze firmware
binwalk -e: Extract embedded files
🤖 Red Teaming & C2 Frameworks (Advanced Integration)
25. Covenant
.NET-based C2 framework used for red team operations.

26. Cobalt Strike
Commercial C2 framework (used extensively in red teams and adversarial simulations).

Note: These require special consideration; direct command-line control is limited due to licensing and architecture complexity.

🖥️ OSINT and OS Enumeration
27. Sherlock
Hunt down social media accounts by username across social networks.

28. theHarvester
E-mail, subdomain, and people names harvester for OSINT.

29. LinEnum.sh / linux-smart-enumeration
Useful scripts for local privilege escalation checks.

30. enum4linux / rpcclient
SMB share enumeration, user listing, RID cycling, etc.