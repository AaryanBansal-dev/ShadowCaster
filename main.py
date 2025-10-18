"""
ShadowCaster - Penetration Testing Command Generator
Main Application

Copyright (C) 2025

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import sys
import os
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils.config_loader import ConfigLoader
from utils.display import Display, Menu, Colors
from utils.file_manager import FileManager, ClipboardManager
from utils.command_builder import CommandBuilder
from modules.tool_builders import (
    NmapBuilder, HydraBuilder, SQLMapBuilder,
    WPScanBuilder, GobusterBuilder, AircrackBuilder
)


class ShadowCaster:
    """Main application class"""
    
    TOOL_BUILDERS = {
        'nmap': NmapBuilder,
        'hydra': HydraBuilder,
        'sqlmap': SQLMapBuilder,
        'wpscan': WPScanBuilder,
        'gobuster': GobusterBuilder,
        'aircrack': AircrackBuilder
    }
    
    def __init__(self):
        """Initialize ShadowCaster"""
        self.config_loader = ConfigLoader()
        self.file_manager = FileManager()
        self.hint_mode = False
        self.current_command = None
    
    def print_banner(self):
        """Print application banner"""
        banner = f"""
{Colors.BOLD}{Colors.RED}
  ███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗ ██████╗ █████╗ ███████╗████████╗███████╗██████╗ 
  ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
  ███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║██║     ███████║███████╗   ██║   █████╗  ██████╔╝
  ╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║██║     ██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
  ███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝╚██████╗██║  ██║███████║   ██║   ███████╗██║  ██║
  ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝  ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
{Colors.END}

{Colors.CYAN}{Colors.BOLD}Penetration Testing Command Generator{Colors.END}
{Colors.YELLOW}Build commands for ethical hacking tools safely{Colors.END}
        """
        print(banner)
    
    def main_menu(self):
        """Display main menu"""
        Display.print_header("ShadowCaster - Main Menu")
        
        options = [
            ("Build New Command", "Interactively build a penetration testing command"),
            ("Load Template", "Load a previously saved command template"),
            ("Manage Templates", "View, edit, or delete saved templates"),
            ("Settings", "Configure application settings"),
            ("Exit", "Quit ShadowCaster")
        ]
        
        indices = Menu.display_menu("Main Menu", options)
        return indices[0]
    
    def settings_menu(self):
        """Display settings menu"""
        Display.print_subheader("Settings")
        
        options = [
            ("Toggle Hint Mode", f"Currently: {'ON' if self.hint_mode else 'OFF'}"),
            ("Clear All Templates", "Delete all saved templates"),
            ("Back to Main Menu", "")
        ]
        
        indices = Menu.display_menu("Settings", options)
        
        if indices[0] == 0:
            self.hint_mode = not self.hint_mode
            Display.print_success(f"Hint mode turned {'ON' if self.hint_mode else 'OFF'}")
            input(f"{Colors.BOLD}Press Enter to continue...{Colors.END}")
        
        elif indices[0] == 1:
            if Menu.confirm("Are you sure you want to delete all templates?"):
                templates = self.file_manager.list_templates()
                for template in templates:
                    self.file_manager.delete_template(template['name'])
                Display.print_success(f"Deleted {len(templates)} templates")
            input(f"{Colors.BOLD}Press Enter to continue...{Colors.END}")
    
    def build_command(self):
        """Build a new command"""
        # Get available tools
        tools = self.config_loader.list_available_tools()
        
        if not tools:
            Display.print_error("No tools configured. Check configs directory.")
            return
        
        Display.print_subheader("Available Tools")
        tool_index = Menu.display_tools(tools)
        selected_tool = tools[tool_index]
        tool_id = selected_tool['id']
        
        # Load tool configuration
        config = self.config_loader.load_config(tool_id)
        if not config:
            Display.print_error(f"Could not load configuration for {selected_tool['name']}")
            return
        
        # Create builder
        builder_class = self.TOOL_BUILDERS.get(tool_id, CommandBuilder)
        builder = builder_class(config)
        builder.set_hint_mode(self.hint_mode)
        
        # Build command
        command = builder.build_command()
        
        if not command:
            Display.print_error("Command building failed")
            return
        
        self.current_command = command
        self.handle_command_options(builder, command)
    
    def handle_command_options(self, builder, command: str):
        """Handle options for completed command"""
        while True:
            Display.clear_screen()
            Display.print_header(f"{builder.tool_name} - Command Built Successfully")
            Display.print_command(command)
            
            options = [
                ("Preview Command", "Display the command in detail"),
                ("Copy to Clipboard", "Copy command to system clipboard"),
                ("Save to File", "Save command as executable script"),
                ("Save as Template", "Save command as reusable template"),
                ("Execute Command", "Run the command (with confirmation)"),
                ("Build Another", "Create a new command"),
                ("Back to Main Menu", "Return to main menu")
            ]
            
            indices = Menu.display_menu("Command Options", options)
            choice = indices[0]
            
            if choice == 0:
                builder.preview_command(command)
                input(f"{Colors.BOLD}Press Enter to continue...{Colors.END}")
            
            elif choice == 1:
                if ClipboardManager.copy_to_clipboard(command):
                    Display.print_success("Command copied to clipboard!")
                else:
                    Display.print_error("Failed to copy to clipboard. Install xclip or xsel.")
                input(f"{Colors.BOLD}Press Enter to continue...{Colors.END}")
            
            elif choice == 2:
                filename = Menu.get_text_input("Enter filename (optional): ", required=False)
                path = self.file_manager.save_command_to_file(command, filename if filename else None)
                if path:
                    Display.print_success(f"Command saved to: {path}")
                else:
                    Display.print_error("Failed to save command")
                input(f"{Colors.BOLD}Press Enter to continue...{Colors.END}")
            
            elif choice == 3:
                template_name = Menu.get_text_input("Enter template name: ")
                description = Menu.get_text_input("Enter description (optional): ", required=False)
                path = self.file_manager.save_template(template_name, builder.tool_name.lower(), command, description)
                if path:
                    Display.print_success(f"Template saved: {template_name}")
                else:
                    Display.print_error("Failed to save template")
                input(f"{Colors.BOLD}Press Enter to continue...{Colors.END}")
            
            elif choice == 4:
                Display.clear_screen()
                Display.print_warning("EXECUTION WARNING")
                print("You are about to execute a system command. Make sure you:")
                print("  • Understand what this command does")
                print("  • Have proper authorization")
                print("  • Are in an appropriate testing environment\n")
                
                if builder.execute_command(command):
                    Display.print_success("Command executed successfully")
                
                input(f"{Colors.BOLD}Press Enter to continue...{Colors.END}")
            
            elif choice == 5:
                self.build_command()
                return
            
            else:
                return
    
    def load_template(self):
        """Load and use a saved template"""
        templates = self.file_manager.list_templates()
        
        if not templates:
            Display.print_info("No saved templates found")
            input(f"{Colors.BOLD}Press Enter to continue...{Colors.END}")
            return
        
        Display.print_subheader("Saved Templates")
        
        options = [(t['name'], f"{t['tool']}: {t['description']}") for t in templates]
        indices = Menu.display_menu("Select Template", options)
        selected_template = templates[indices[0]]
        
        self.current_command = selected_template['command']
        
        # Create a dummy builder for display
        builder = CommandBuilder({'name': selected_template['tool'].title(), 'command': ''})
        self.handle_command_options(builder, self.current_command)
    
    def manage_templates(self):
        """Manage saved templates"""
        templates = self.file_manager.list_templates()
        
        if not templates:
            Display.print_info("No saved templates found")
            input(f"{Colors.BOLD}Press Enter to continue...{Colors.END}")
            return
        
        while True:
            Display.print_subheader("Template Management")
            
            options = [(t['name'], f"{t['tool']}: {t['description']}") for t in templates]
            options.append(("Back to Main Menu", ""))
            
            indices = Menu.display_menu("Select Template", options)
            choice = indices[0]
            
            if choice == len(options) - 1:
                break
            
            selected_template = templates[choice]
            
            Display.clear_screen()
            Display.print_header(f"Template: {selected_template['name']}")
            Display.print_info(f"Tool: {selected_template['tool']}")
            Display.print_info(f"Description: {selected_template['description']}")
            print()
            Display.print_command(selected_template['command'])
            
            options = [
                ("Use This Template", "Load and prepare this command"),
                ("Delete Template", "Remove this template"),
                ("Back", "")
            ]
            
            indices = Menu.display_menu("Template Actions", options)
            
            if indices[0] == 0:
                self.current_command = selected_template['command']
                builder = CommandBuilder({'name': selected_template['tool'].title(), 'command': ''})
                self.handle_command_options(builder, self.current_command)
                return
            
            elif indices[0] == 1:
                if Menu.confirm("Delete this template?"):
                    self.file_manager.delete_template(selected_template['name'])
                    Display.print_success("Template deleted")
                    templates = self.file_manager.list_templates()
                    input(f"{Colors.BOLD}Press Enter to continue...{Colors.END}")
    
    def run(self):
        """Main application loop"""
        self.print_banner()
        
        while True:
            try:
                choice = self.main_menu()
                
                if choice == 0:
                    self.build_command()
                
                elif choice == 1:
                    self.load_template()
                
                elif choice == 2:
                    self.manage_templates()
                
                elif choice == 3:
                    self.settings_menu()
                
                elif choice == 4:
                    Display.print_success("Goodbye!")
                    break
            
            except KeyboardInterrupt:
                print(f"\n{Colors.YELLOW}Interrupted by user{Colors.END}")
                if Menu.confirm("Exit ShadowCaster?"):
                    Display.print_success("Goodbye!")
                    break
            
            except Exception as e:
                Display.print_error(f"An error occurred: {e}")
                input(f"{Colors.BOLD}Press Enter to continue...{Colors.END}")


def main():
    """Entry point"""
    app = ShadowCaster()
    app.run()


if __name__ == '__main__':
    main()
