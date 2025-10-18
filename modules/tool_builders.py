"""
Tool Builders Module
Contains specific command builders for each penetration testing tool

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

from typing import List, Dict, Any
from utils.command_builder import CommandBuilder
from utils.display import Display, Menu


class NmapBuilder(CommandBuilder):
    """Build Nmap commands interactively"""
    
    def _add_required_values(self) -> List[str]:
        """Add target to command"""
        target = self.required_params.get('target', '')
        return [target] if target else []


class HydraBuilder(CommandBuilder):
    """Build Hydra commands interactively"""
    
    def get_required_parameters(self) -> bool:
        """Get required parameters - target and service"""
        Display.print_subheader(f"Required Parameters for {self.tool_name}")
        
        for param_name, param_config in self.required.items():
            prompt = param_config.get('prompt')
            description = param_config.get('description', '')
            
            if self.hint_mode:
                Display.print_info(description)
            
            value = Menu.get_text_input(prompt)
            self.required_params[param_name] = value
        
        return len(self.required_params) == len(self.required)
    
    def _add_required_values(self) -> List[str]:
        """Add service, target to command"""
        parts = []
        
        service = self.required_params.get('service', '')
        target = self.required_params.get('target', '')
        
        if service:
            parts.append(service)
        if target:
            parts.append(target)
        
        return parts


class SQLMapBuilder(CommandBuilder):
    """Build SQLMap commands interactively"""
    
    def _add_required_values(self) -> List[str]:
        """Add URL to command"""
        url = self.required_params.get('url', '')
        return [f'-u "{url}"'] if url else []


class WPScanBuilder(CommandBuilder):
    """Build WPScan commands interactively"""
    
    def _add_required_values(self) -> List[str]:
        """Add URL to command"""
        url = self.required_params.get('url', '')
        return [f'--url "{url}"'] if url else []


class GobusterBuilder(CommandBuilder):
    """Build Gobuster commands interactively"""
    
    def get_optional_parameters(self):
        """Override to handle mode selection first"""
        if not self.categories:
            return
        
        Display.print_subheader("Mode Selection")
        
        # Handle mode selection specially
        mode_options = self.categories.get('Mode', {}).get('options', [])
        if mode_options:
            Display.print_subheader("Gobuster Mode")
            selected = Menu.display_options("Mode", mode_options)
            for option in selected:
                self.selected_flags.insert(0, option.get('flag'))
        
        # Get other categories
        categories_to_process = [cat for cat in self.categories.keys() if cat != 'Mode']
        
        if categories_to_process:
            selected_categories = []
            for cat in categories_to_process:
                if Menu.confirm(f"Configure {cat}?"):
                    selected_categories.append(cat)
            
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
                        prompt_text = option.get('prompt_text', f"Enter value: ")
                        value = Menu.get_text_input(prompt_text, required=False)
                        
                        if value:
                            flag = option.get('flag')
                            self.selected_flags.append(f'{flag} "{value}"')
                    else:
                        self.selected_flags.append(option.get('flag'))
    
    def _add_required_values(self) -> List[str]:
        """No specific required values for gobuster"""
        return []


class AircrackBuilder(CommandBuilder):
    """Build Aircrack-ng commands interactively"""
    
    def _add_required_values(self) -> List[str]:
        """Add capture file to command"""
        capture = self.required_params.get('capture', '')
        return [capture] if capture else []
