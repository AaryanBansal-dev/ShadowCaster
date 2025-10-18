"""
Display and UI utilities for interactive command building

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

from typing import List, Dict, Any, Tuple
import os


class Colors:
    """ANSI color codes for terminal output"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    GRAY = '\033[90m'


class Display:
    """Handles terminal output and formatting"""
    
    @staticmethod
    def clear_screen():
        """Clear the terminal screen"""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    @staticmethod
    def print_header(text: str):
        """Print a formatted header"""
        print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.CYAN}{text.center(60)}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.END}\n")
    
    @staticmethod
    def print_subheader(text: str):
        """Print a formatted subheader"""
        print(f"\n{Colors.BOLD}{Colors.BLUE}▸ {text}{Colors.END}")
        print(f"{Colors.GRAY}{'-'*55}{Colors.END}\n")
    
    @staticmethod
    def print_info(text: str):
        """Print info message"""
        print(f"{Colors.CYAN}ℹ {text}{Colors.END}")
    
    @staticmethod
    def print_success(text: str):
        """Print success message"""
        print(f"{Colors.GREEN}✓ {text}{Colors.END}")
    
    @staticmethod
    def print_error(text: str):
        """Print error message"""
        print(f"{Colors.RED}✗ {text}{Colors.END}")
    
    @staticmethod
    def print_warning(text: str):
        """Print warning message"""
        print(f"{Colors.YELLOW}⚠ {text}{Colors.END}")
    
    @staticmethod
    def print_command(command: str):
        """Print a command in highlighted format"""
        print(f"\n{Colors.BOLD}{Colors.GREEN}Command:{Colors.END}")
        print(f"{Colors.YELLOW}{command}{Colors.END}\n")


class Menu:
    """Handles interactive menu display and selection"""
    
    @staticmethod
    def display_menu(title: str, options: List[Tuple[str, str]], allow_multiple: bool = False) -> List[int]:
        """
        Display a menu and get user selection(s)
        
        Args:
            title: Menu title
            options: List of (key, description) tuples
            allow_multiple: If True, allow comma-separated selections
        
        Returns:
            List of selected indices
        """
        Display.print_subheader(title)
        
        for i, (key, desc) in enumerate(options, 1):
            print(f"  {Colors.BOLD}{i}{Colors.END}. {Colors.CYAN}{key}{Colors.END}")
            if desc:
                print(f"     {Colors.GRAY}{desc}{Colors.END}")
        
        print()
        
        while True:
            try:
                if allow_multiple:
                    user_input = input(f"{Colors.BOLD}Select options (comma-separated, e.g., 1,3,5) [1-{len(options)}]: {Colors.END}").strip()
                    selections = [int(x.strip()) - 1 for x in user_input.split(',')]
                    
                    if all(0 <= s < len(options) for s in selections):
                        return selections
                    else:
                        Display.print_error("Invalid selection. Please try again.")
                else:
                    user_input = input(f"{Colors.BOLD}Select an option [1-{len(options)}]: {Colors.END}").strip()
                    selection = int(user_input) - 1
                    
                    if 0 <= selection < len(options):
                        return [selection]
                    else:
                        Display.print_error("Invalid selection. Please try again.")
            
            except ValueError:
                Display.print_error("Please enter valid numbers.")
    
    @staticmethod
    def display_tools(tools: List[Dict[str, str]]) -> int:
        """Display available tools and get selection"""
        options = [(t['name'], t['description']) for t in tools]
        indices = Menu.display_menu("Select a Tool", options)
        return indices[0]
    
    @staticmethod
    def display_categories(categories: Dict[str, Any]) -> List[str]:
        """Display tool categories and get selections"""
        options = [(cat, "") for cat in categories.keys()]
        indices = Menu.display_menu("Select Categories (you can select multiple)", options, allow_multiple=True)
        return [list(categories.keys())[i] for i in indices]
    
    @staticmethod
    def get_text_input(prompt: str, required: bool = True, hint: str = None) -> str:
        """Get text input from user"""
        full_prompt = f"{Colors.BOLD}{prompt}{Colors.END}"
        if hint:
            full_prompt += f" {Colors.GRAY}({hint}){Colors.END}"
        
        while True:
            value = input(full_prompt).strip()
            
            if not value and required:
                Display.print_error("This field is required.")
                continue
            
            return value
    
    @staticmethod
    def confirm(message: str) -> bool:
        """Ask for yes/no confirmation"""
        response = input(f"{Colors.BOLD}{message} [y/N]: {Colors.END}").strip().lower()
        return response in ['y', 'yes']
    
    @staticmethod
    def display_options(category_name: str, options: List[Dict[str, Any]]) -> List[str]:
        """Display options for a category and get selections"""
        opt_list = []
        for opt in options:
            flag = opt.get('flag', '')
            desc = opt.get('description', '')
            opt_list.append((flag, desc))
        
        indices = Menu.display_menu(f"Select options for {category_name}", opt_list, allow_multiple=True)
        selected_options = [options[i] for i in indices]
        
        return selected_options
