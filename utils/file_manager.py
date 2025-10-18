"""
File and Clipboard utilities
"""

import os
import json
from pathlib import Path
from typing import Dict, Any, Optional
from datetime import datetime


class FileManager:
    """Handles file operations for commands and templates"""
    
    def __init__(self, templates_dir: str = None):
        """Initialize file manager"""
        if templates_dir is None:
            templates_dir = os.path.join(os.path.dirname(__file__), '..', 'templates')
        
        self.templates_dir = Path(templates_dir)
        self.templates_dir.mkdir(exist_ok=True)
    
    def save_command_to_file(self, command: str, filename: str = None) -> Optional[str]:
        """Save command to a file"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"command_{timestamp}.sh"
        
        # Ensure .sh or .txt extension
        if not filename.endswith(('.sh', '.txt')):
            filename += '.sh'
        
        file_path = self.templates_dir / filename
        
        try:
            with open(file_path, 'w') as f:
                f.write("#!/bin/bash\n")
                f.write("# Generated command - Always review before executing\n\n")
                f.write(command)
            
            os.chmod(file_path, 0o755)  # Make executable
            return str(file_path)
        
        except IOError as e:
            print(f"Error saving file: {e}")
            return None
    
    def save_template(self, name: str, tool: str, command: str, description: str = "") -> Optional[str]:
        """Save command template"""
        template = {
            'name': name,
            'tool': tool,
            'command': command,
            'description': description,
            'created': datetime.now().isoformat()
        }
        
        template_file = self.templates_dir / f"{name}.json"
        
        try:
            with open(template_file, 'w') as f:
                json.dump(template, f, indent=2)
            
            return str(template_file)
        
        except IOError as e:
            print(f"Error saving template: {e}")
            return None
    
    def load_template(self, name: str) -> Optional[Dict[str, Any]]:
        """Load a saved template"""
        template_file = self.templates_dir / f"{name}.json"
        
        if not template_file.exists():
            return None
        
        try:
            with open(template_file, 'r') as f:
                return json.load(f)
        
        except json.JSONDecodeError:
            return None
    
    def list_templates(self) -> list:
        """List all saved templates"""
        templates = []
        
        for template_file in self.templates_dir.glob("*.json"):
            try:
                with open(template_file, 'r') as f:
                    template = json.load(f)
                    templates.append({
                        'name': template_file.stem,
                        'tool': template.get('tool'),
                        'description': template.get('description', ''),
                        'command': template.get('command', '')
                    })
            except json.JSONDecodeError:
                continue
        
        return sorted(templates, key=lambda x: x['name'])
    
    def delete_template(self, name: str) -> bool:
        """Delete a template"""
        template_file = self.templates_dir / f"{name}.json"
        
        if template_file.exists():
            try:
                template_file.unlink()
                return True
            except OSError:
                return False
        
        return False


class ClipboardManager:
    """Handles clipboard operations"""
    
    @staticmethod
    def copy_to_clipboard(text: str) -> bool:
        """Copy text to clipboard"""
        try:
            import subprocess
            
            # Try different clipboard managers
            if os.system('which xclip > /dev/null 2>&1') == 0:
                process = subprocess.Popen(['xclip', '-selection', 'clipboard'],
                                         stdin=subprocess.PIPE)
                process.communicate(text.encode('utf-8'))
                return True
            
            elif os.system('which xsel > /dev/null 2>&1') == 0:
                process = subprocess.Popen(['xsel', '--clipboard', '--input'],
                                         stdin=subprocess.PIPE)
                process.communicate(text.encode('utf-8'))
                return True
            
            elif os.system('which pbcopy > /dev/null 2>&1') == 0:  # macOS
                process = subprocess.Popen(['pbcopy'],
                                         stdin=subprocess.PIPE)
                process.communicate(text.encode('utf-8'))
                return True
            
            else:
                return False
        
        except Exception:
            return False
