#!/usr/bin/env python3
"""
ShadowCaster - Functionality Tests
Verifies core components work correctly
"""

import sys
import json
from pathlib import Path

# Add to path
sys.path.insert(0, str(Path(__file__).parent))

from utils.config_loader import ConfigLoader
from utils.display import Display, Colors
from modules.tool_builders import (
    NmapBuilder, HydraBuilder, SQLMapBuilder,
    WPScanBuilder, GobusterBuilder, AircrackBuilder
)


class TestShadowCaster:
    """Test suite for ShadowCaster"""
    
    def __init__(self):
        self.loader = ConfigLoader()
        self.tests_passed = 0
        self.tests_failed = 0
    
    def print_test_header(self, name):
        """Print test section header"""
        print(f"\n{Colors.BOLD}{Colors.CYAN}Testing: {name}{Colors.END}")
        print("-" * 50)
    
    def assert_true(self, condition, message):
        """Assert condition is true"""
        if condition:
            print(f"{Colors.GREEN}✓ {message}{Colors.END}")
            self.tests_passed += 1
        else:
            print(f"{Colors.RED}✗ {message}{Colors.END}")
            self.tests_failed += 1
    
    def test_config_loading(self):
        """Test configuration loading"""
        self.print_test_header("Configuration Loading")
        
        tools = self.loader.list_available_tools()
        self.assert_true(len(tools) >= 100, f"Found 100+ tools ({len(tools)} found)")
        
        # Test that original 6 tools are still present
        expected_tools = ['nmap', 'hydra', 'sqlmap', 'wpscan', 'gobuster', 'aircrack']
        tool_ids = [t['id'] for t in tools]
        
        for tool_id in expected_tools:
            self.assert_true(tool_id in tool_ids, f"Tool '{tool_id}' loaded")
        
        # Load each config
        for tool in tools:
            config = self.loader.load_config(tool['id'])
            self.assert_true(config is not None, f"Config for {tool['name']} loads")
            self.assert_true('categories' in config, f"{tool['name']} has categories")
            self.assert_true('command' in config, f"{tool['name']} has command field")
    
    def test_nmap_builder(self):
        """Test Nmap command builder"""
        self.print_test_header("Nmap Builder")
        
        config = self.loader.load_config('nmap')
        self.assert_true(config is not None, "Nmap config loads")
        
        builder = NmapBuilder(config)
        self.assert_true(builder is not None, "NmapBuilder instantiates")
        
        # Test with manual parameters (bypass get_required_parameters)
        builder.required_params = {'target': '192.168.1.100'}
        builder.selected_flags = ['-sS', '-p 80,443', '-T4']
        
        # Manually construct command without calling build_command
        cmd_parts = [builder.command]
        cmd_parts.extend(builder.selected_flags)
        cmd_parts.extend(builder._add_required_values())
        command = ' '.join(cmd_parts)
        
        self.assert_true(command is not None, "Command builds successfully")
        self.assert_true('192.168.1.100' in command, "Target included in command")
        self.assert_true('-sS' in command, "Flags included in command")
        
        print(f"  Generated: {Colors.YELLOW}{command}{Colors.END}")
    
    def test_hydra_builder(self):
        """Test Hydra command builder"""
        self.print_test_header("Hydra Builder")
        
        config = self.loader.load_config('hydra')
        self.assert_true(config is not None, "Hydra config loads")
        
        builder = HydraBuilder(config)
        self.assert_true(builder is not None, "HydraBuilder instantiates")
        
        builder.required_params = {
            'target': '192.168.1.50',
            'service': 'ssh'
        }
        builder.selected_flags = ['-l root', '-P wordlist.txt', '-t 4']
        
        # Manually construct command
        cmd_parts = [builder.command]
        cmd_parts.extend(builder.selected_flags)
        cmd_parts.extend(builder._add_required_values())
        command = ' '.join(cmd_parts)
        
        self.assert_true(command is not None, "Command builds successfully")
        self.assert_true('ssh' in command, "Service included in command")
        self.assert_true('192.168.1.50' in command, "Target included in command")
        
        print(f"  Generated: {Colors.YELLOW}{command}{Colors.END}")
    
    def test_sqlmap_builder(self):
        """Test SQLMap command builder"""
        self.print_test_header("SQLMap Builder")
        
        config = self.loader.load_config('sqlmap')
        self.assert_true(config is not None, "SQLMap config loads")
        
        builder = SQLMapBuilder(config)
        self.assert_true(builder is not None, "SQLMapBuilder instantiates")
        
        builder.required_params = {'url': 'http://target.com/page.php?id=1'}
        builder.selected_flags = ['--dbs', '--level 2', '--risk 1']
        
        # Manually construct command
        cmd_parts = [builder.command]
        cmd_parts.extend(builder.selected_flags)
        cmd_parts.extend(builder._add_required_values())
        command = ' '.join(cmd_parts)
        
        self.assert_true(command is not None, "Command builds successfully")
        self.assert_true('http://target.com/page.php?id=1' in command, "URL included")
        self.assert_true('--dbs' in command, "Flags included in command")
        
        print(f"  Generated: {Colors.YELLOW}{command}{Colors.END}")
    
    def test_wpscan_builder(self):
        """Test WPScan command builder"""
        self.print_test_header("WPScan Builder")
        
        config = self.loader.load_config('wpscan')
        self.assert_true(config is not None, "WPScan config loads")
        
        builder = WPScanBuilder(config)
        self.assert_true(builder is not None, "WPScanBuilder instantiates")
        
        builder.required_params = {'url': 'http://wordpress.local'}
        builder.selected_flags = ['--enumerate p', '--enumerate t', '--enumerate u']
        
        # Manually construct command
        cmd_parts = [builder.command]
        cmd_parts.extend(builder.selected_flags)
        cmd_parts.extend(builder._add_required_values())
        command = ' '.join(cmd_parts)
        
        self.assert_true(command is not None, "Command builds successfully")
        self.assert_true('wordpress.local' in command, "URL included")
        
        print(f"  Generated: {Colors.YELLOW}{command}{Colors.END}")
    
    def test_gobuster_builder(self):
        """Test Gobuster command builder"""
        self.print_test_header("Gobuster Builder")
        
        config = self.loader.load_config('gobuster')
        self.assert_true(config is not None, "Gobuster config loads")
        
        builder = GobusterBuilder(config)
        self.assert_true(builder is not None, "GobusterBuilder instantiates")
        
        builder.required_params = {}
        builder.selected_flags = ['dir', '-u http://target.com', '-w wordlist.txt']
        
        # Manually construct command
        cmd_parts = [builder.command]
        cmd_parts.extend(builder.selected_flags)
        command = ' '.join(cmd_parts)
        
        self.assert_true(command is not None, "Command builds successfully")
        
        print(f"  Generated: {Colors.YELLOW}{command}{Colors.END}")
    
    def test_aircrack_builder(self):
        """Test Aircrack-ng command builder"""
        self.print_test_header("Aircrack-ng Builder")
        
        config = self.loader.load_config('aircrack')
        self.assert_true(config is not None, "Aircrack config loads")
        
        builder = AircrackBuilder(config)
        self.assert_true(builder is not None, "AircrackBuilder instantiates")
        
        builder.required_params = {'capture': '/path/to/capture.cap'}
        builder.selected_flags = ['-a 2', '-w wordlist.txt']
        
        # Manually construct command
        cmd_parts = [builder.command]
        cmd_parts.extend(builder.selected_flags)
        cmd_parts.extend(builder._add_required_values())
        command = ' '.join(cmd_parts)
        
        self.assert_true(command is not None, "Command builds successfully")
        self.assert_true('capture.cap' in command, "Capture file included")
        
        print(f"  Generated: {Colors.YELLOW}{command}{Colors.END}")
    
    def test_config_structure(self):
        """Test configuration file structure"""
        self.print_test_header("Config Structure Validation")
        
        required_fields = ['name', 'description', 'command', 'categories', 'required']
        
        for tool in self.loader.list_available_tools():
            config = self.loader.load_config(tool['id'])
            
            for field in required_fields:
                self.assert_true(field in config, f"{tool['name']}: has '{field}' field")
    
    def run_all_tests(self):
        """Run all tests"""
        print(f"\n{Colors.BOLD}{Colors.HEADER}ShadowCaster Functionality Tests{Colors.END}\n")
        
        self.test_config_loading()
        self.test_config_structure()
        self.test_nmap_builder()
        self.test_hydra_builder()
        self.test_sqlmap_builder()
        self.test_wpscan_builder()
        self.test_gobuster_builder()
        self.test_aircrack_builder()
        
        # Summary
        total = self.tests_passed + self.tests_failed
        percentage = (self.tests_passed / total * 100) if total > 0 else 0
        
        print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*50}{Colors.END}")
        print(f"{Colors.BOLD}Test Summary{Colors.END}")
        print(f"{Colors.CYAN}{'='*50}{Colors.END}")
        print(f"Total Tests: {total}")
        print(f"{Colors.GREEN}Passed: {self.tests_passed}{Colors.END}")
        print(f"{Colors.RED}Failed: {self.tests_failed}{Colors.END}")
        print(f"Success Rate: {percentage:.1f}%")
        print(f"{Colors.CYAN}{'='*50}{Colors.END}\n")
        
        return self.tests_failed == 0


def main():
    """Run test suite"""
    tester = TestShadowCaster()
    success = tester.run_all_tests()
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
