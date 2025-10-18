"""
Command Builder Base Class
Provides common functionality for all tool builders
"""

from typing import Dict, List, Any, Optional
from utils.display import Display, Menu, Colors
import subprocess


class CommandBuilder:
    """Base class for building tool-specific commands"""
    
    def __init__(self, config: Dict[str, Any]):
        """Initialize command builder with tool configuration"""
        self.config = config
        self.tool_name = config.get('name')
        self.command = config.get('command')
        self.categories = config.get('categories', {})
        self.required = config.get('required', {})
        self.hint_mode = False
        self.selected_flags = []
        self.required_params = {}
    
    def set_hint_mode(self, enabled: bool):
        """Enable/disable hint mode"""
        self.hint_mode = enabled
    
    def get_required_parameters(self) -> bool:
        """Get required parameters from user"""
        Display.print_subheader(f"Required Parameters for {self.tool_name}")
        
        for param_name, param_config in self.required.items():
            prompt = param_config.get('prompt')
            description = param_config.get('description', '')
            
            if self.hint_mode:
                Display.print_info(description)
            
            value = Menu.get_text_input(prompt)
            self.required_params[param_name] = value
        
        return len(self.required_params) == len(self.required)
    
    def build_command(self) -> Optional[str]:
        """Build the complete command"""
        try:
            # Get required parameters first
            if not self.get_required_parameters():
                Display.print_error("Missing required parameters")
                return None
            
            # Get optional parameters
            self.get_optional_parameters()
            
            # Construct the command
            cmd_parts = [self.command]
            
            # Add flags
            cmd_parts.extend(self.selected_flags)
            
            # Add required parameters based on tool
            cmd_parts.extend(self._add_required_values())
            
            return ' '.join(cmd_parts)
        
        except Exception as e:
            Display.print_error(f"Error building command: {e}")
            return None
    
    def get_optional_parameters(self):
        """Interactively get optional parameters"""
        if not self.categories:
            return
        
        Display.print_subheader(f"Optional Parameters for {self.tool_name}")
        
        selected_categories = Menu.display_categories(self.categories)
        
        for category in selected_categories:
            options = self.categories[category].get('options', [])
            
            if not options:
                continue
            
            Display.print_subheader(f"Options in {category}")
            selected_options = Menu.display_options(category, options)
            
            for option in selected_options:
                if self.hint_mode:
                    Display.print_info(option.get('description', ''))
                
                if option.get('variable'):
                    prompt_text = option.get('prompt_text', f"Enter value for {option.get('flag')}: ")
                    value = Menu.get_text_input(prompt_text, required=False)
                    
                    if value:
                        flag = option.get('flag')
                        self.selected_flags.append(f'{flag} "{value}"')
                else:
                    self.selected_flags.append(option.get('flag'))
    
    def _add_required_values(self) -> List[str]:
        """Add required parameter values to command (tool-specific)"""
        # Default implementation - override in subclasses
        return []
    
    def preview_command(self, command: str):
        """Display command preview"""
        Display.clear_screen()
        Display.print_header(f"{self.tool_name} Command Preview")
        Display.print_command(command)
    
    def execute_command(self, command: str) -> bool:
        """Execute command with user confirmation"""
        Display.print_warning("This will execute a command on your system!")
        
        if not Menu.confirm("Are you sure you want to execute this command?"):
            Display.print_info("Command execution cancelled.")
            return False
        
        try:
            subprocess.run(command, shell=True)
            return True
        except Exception as e:
            Display.print_error(f"Error executing command: {e}")
            return False
