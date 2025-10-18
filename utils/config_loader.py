"""
Config Loader Utility
Loads and manages tool configurations from JSON files

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

import json
import os
from pathlib import Path
from typing import Dict, Any, Optional


class ConfigLoader:
    """Loads and manages configuration files for various tools"""
    
    def __init__(self, config_dir: str = None):
        """Initialize config loader with config directory path"""
        if config_dir is None:
            config_dir = os.path.join(os.path.dirname(__file__), '..', 'configs')
        self.config_dir = Path(config_dir)
    
    def load_config(self, tool_name: str) -> Optional[Dict[str, Any]]:
        """Load configuration for a specific tool"""
        config_file = self.config_dir / f"{tool_name}_config.json"
        
        if not config_file.exists():
            return None
        
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error parsing config file: {e}")
            return None
    
    def list_available_tools(self) -> list:
        """List all available tools from config files"""
        tools = []
        
        if not self.config_dir.exists():
            return tools
        
        for config_file in self.config_dir.glob("*_config.json"):
            try:
                with open(config_file, 'r') as f:
                    config = json.load(f)
                    tools.append({
                        'id': config_file.stem.replace('_config', ''),
                        'name': config.get('name'),
                        'description': config.get('description')
                    })
            except json.JSONDecodeError:
                continue
        
        return sorted(tools, key=lambda x: x['name'])
    
    def get_tool_categories(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Get categories from tool configuration"""
        return config.get('categories', {})
    
    def get_required_params(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Get required parameters for a tool"""
        return config.get('required', {})
