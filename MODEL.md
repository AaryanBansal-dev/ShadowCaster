You are a cybersecurity expert and Python developer tasked with building a penetration testing command generator tool named ShadowCaster. The purpose of this tool is not to execute tools automatically but to guide the user interactively to construct accurate and effective CLI commands for popular ethical hacking tools like Nmap, Hydra, SQLMap, WPScan, Dirb/Gobuster, and Aircrack-ng.

The tool should present menus and ask for specific inputs related to flags or arguments required for each tool. Based on the user's input, it should dynamically construct a full command string which can then be copied, exported, or optionally executed within controlled and authorized environments.

Here are the functional requirements:

🧩 Features:
Present a main menu where users select which tool they want to build a command for.
After selecting a tool, the user is walked through prompts relevant to that tool’s functionality.
Example: For Nmap: choose scan type, set target, specify ports, timing templates, output format.
Use configuration files (JSON/YAML preferred) to define all options available for each tool so new tools can be added easily.
Display explanations or descriptions of what each flag does during selection.
Provide an option to preview the constructed command.
Allow user to:
Copy the command to clipboard
Save the command as a reusable template
Save the command to a .sh or .txt file
Run the command directly (only under user confirmation in authorized contexts)
Support saving/loading command templates with human-readable names (e.g., "fast-http-scan", "brute-force-ssh").
Include beginner-friendly hint mode that explains each option chosen when enabled.
Keep code modular – one module per supported tool (e.g., nmap_builder.py).
Ensure no commands are executed unless explicitly confirmed by the user.
🛠 Tools to Initially Support:
Nmap
Hydra
SQLMap
WPScan
Dirb/Gobuster
Aircrack-ng Suite
⚙️ Implementation Guidelines:
Write in Python 3.8+
Use argparse or interactive prompts for navigation
Use pyperclip for clipboard integration
Load command flags, options, and descriptions from JSON/YAML config files
Modular design for easy addition of more tools
Safe by default – print command instead of run unless opted-in
🗃 Sample Tool Config Structure (nmap_config.yaml):
yaml



name: Nmap
description: Network discovery and security auditing tool
options:
  - flag: '-sn'
    description: 'Disable port scan - Ping sweep only'
    category: Scan Types
  - flag: '-sS'
    description: 'TCP SYN scan (default for privileged users)'
    category: Scan Types
  - flag: '-p<U>'
    description: 'Ports to scan (-p22 or -p1-65535)'
    variable: U
    prompt_text: 'Specify Port Range:'
    category: Port Options
advanced_section:
  - option: '-oG'
    description: 'Output in greppable format'
📌 Final Deliverables:
Please provide the following:

A folder structure proposal
Core launcher script (main.py)
Basic example (nmap_builder.py) that reads config and walks user through building an Nmap command
Sample config loader utility (config_loader.py)
Utility for displaying help text inline (optional)
Optional: Export script to file or clipboard handler
Emphasize clean separation of concerns, maintainability, and scalability for future additions.