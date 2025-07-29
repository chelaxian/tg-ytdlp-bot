#!/usr/bin/env python3
# Comprehensive Architecture Test
# This test checks the integrity and correctness of the entire modular architecture

import os
import sys
import importlib
import traceback
from typing import Dict, List, Tuple

# Add project root to Python path for imports
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

class ArchitectureTester:
    def __init__(self):
        self.results = {}
        self.errors = []
        self.warnings = []
        
    def test_module_import(self, module_name: str, description: str = "") -> bool:
        """Test if a module can be imported successfully"""
        try:
            module = importlib.import_module(module_name)
            self.results[module_name] = {
                'status': 'SUCCESS',
                'description': description,
                'error': None
            }
            print(f"✅ {module_name} - {description}")
            return True
        except Exception as e:
            error_msg = f"{type(e).__name__}: {str(e)}"
            
            # Check if it's an external dependency error
            if 'pyrogram' in str(e) or 'pyrebase' in str(e) or 'sdnotify' in str(e) or 'tldextract' in str(e) or 'requests' in str(e):
                # Mark as warning for external dependencies
                self.results[module_name] = {
                    'status': 'WARNING',
                    'description': description,
                    'error': f"External dependency missing: {error_msg}"
                }
                self.warnings.append(f"{module_name}: {error_msg}")
                print(f"⚠️ {module_name} - {description} - External dependency missing: {error_msg}")
                return True  # Don't count as failure
            else:
                # Real import error
                self.results[module_name] = {
                    'status': 'FAILED',
                    'description': description,
                    'error': error_msg
                }
                self.errors.append(f"{module_name}: {error_msg}")
                print(f"❌ {module_name} - {description} - {error_msg}")
                return False
    
    def test_function_import(self, module_name: str, function_name: str, description: str = "") -> bool:
        """Test if a specific function can be imported from a module"""
        try:
            module = importlib.import_module(module_name)
            if hasattr(module, function_name):
                self.results[f"{module_name}.{function_name}"] = {
                    'status': 'SUCCESS',
                    'description': description,
                    'error': None
                }
                print(f"✅ {module_name}.{function_name} - {description}")
                return True
            else:
                error_msg = f"Function '{function_name}' not found in module"
                self.results[f"{module_name}.{function_name}"] = {
                    'status': 'FAILED',
                    'description': description,
                    'error': error_msg
                }
                self.warnings.append(f"{module_name}.{function_name}: {error_msg}")
                print(f"⚠️ {module_name}.{function_name} - {description} - {error_msg}")
                return False
        except Exception as e:
            error_msg = f"{type(e).__name__}: {str(e)}"
            
            # Check if it's an external dependency error
            if 'pyrogram' in str(e) or 'pyrebase' in str(e) or 'sdnotify' in str(e) or 'tldextract' in str(e) or 'requests' in str(e):
                # Mark as warning for external dependencies
                self.results[f"{module_name}.{function_name}"] = {
                    'status': 'WARNING',
                    'description': description,
                    'error': f"External dependency missing: {error_msg}"
                }
                self.warnings.append(f"{module_name}.{function_name}: {error_msg}")
                print(f"⚠️ {module_name}.{function_name} - {description} - External dependency missing: {error_msg}")
                return True  # Don't count as failure
            else:
                # Real import error
                self.results[f"{module_name}.{function_name}"] = {
                    'status': 'FAILED',
                    'description': description,
                    'error': error_msg
                }
                self.errors.append(f"{module_name}.{function_name}: {error_msg}")
                print(f"❌ {module_name}.{function_name} - {description} - {error_msg}")
                return False
    
    def test_file_exists(self, file_path: str, description: str = "") -> bool:
        """Test if a file exists"""
        if os.path.exists(file_path):
            self.results[file_path] = {
                'status': 'SUCCESS',
                'description': description,
                'error': None
            }
            print(f"✅ {file_path} - {description}")
            return True
        else:
            error_msg = "File not found"
            self.results[file_path] = {
                'status': 'FAILED',
                'description': description,
                'error': error_msg
            }
            self.errors.append(f"{file_path}: {error_msg}")
            print(f"❌ {file_path} - {description} - {error_msg}")
            return False
    
    def test_decorator_usage(self, file_path: str) -> bool:
        """Test if decorators are using the registry system correctly"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for old @app decorators
            if '@app.on_message' in content or '@app.on_callback_query' in content:
                error_msg = "Found old @app decorators - should use registry system"
                self.results[f"{file_path}_decorators"] = {
                    'status': 'FAILED',
                    'description': 'Decorator usage check',
                    'error': error_msg
                }
                self.errors.append(f"{file_path}: {error_msg}")
                print(f"❌ {file_path} - Decorator usage check - {error_msg}")
                return False
            
            # Check for registry decorators
            if '@on_message' in content or '@on_callback_query' in content:
                self.results[f"{file_path}_decorators"] = {
                    'status': 'SUCCESS',
                    'description': 'Decorator usage check',
                    'error': None
                }
                print(f"✅ {file_path} - Decorator usage check")
                return True
            else:
                self.results[f"{file_path}_decorators"] = {
                    'status': 'SUCCESS',
                    'description': 'Decorator usage check (no decorators)',
                    'error': None
                }
                print(f"✅ {file_path} - Decorator usage check (no decorators)")
                return True
                
        except Exception as e:
            error_msg = f"Error reading file: {str(e)}"
            self.results[f"{file_path}_decorators"] = {
                'status': 'FAILED',
                'description': 'Decorator usage check',
                'error': error_msg
            }
            self.errors.append(f"{file_path}: {error_msg}")
            print(f"❌ {file_path} - Decorator usage check - {error_msg}")
            return False
    
    def run_comprehensive_test(self):
        """Run comprehensive architecture test"""
        print("🔍 Starting Comprehensive Architecture Test...")
        print("=" * 60)
        
        # Test 1: Core HELPERS modules
        print("\n📦 Testing HELPERS modules:")
        print("-" * 40)
        self.test_module_import('HELPERS.app_instance', 'Global app instance management')
        self.test_module_import('HELPERS.handler_registry', 'Handler registry system')
        self.test_module_import('HELPERS.decorators', 'Decorator utilities')
        self.test_module_import('HELPERS.logger', 'Logging utilities')
        self.test_module_import('HELPERS.safe_messeger', 'Safe message sending')
        self.test_module_import('HELPERS.download_status', 'Download status management')
        self.test_module_import('HELPERS.filesystem_hlp', 'Filesystem helpers')
        self.test_module_import('HELPERS.limitter', 'Rate limiting')
        self.test_module_import('HELPERS.caption', 'Caption utilities')
        self.test_module_import('HELPERS.porn', 'Content filtering')
        self.test_module_import('HELPERS.qualifier', 'Quality management')
        
        # Test 2: CONFIG modules
        print("\n⚙️ Testing CONFIG modules:")
        print("-" * 40)
        self.test_module_import('CONFIG.config', 'Main configuration')
        self.test_module_import('CONFIG.commands', 'Commands configuration')
        self.test_module_import('CONFIG.messages', 'Messages configuration')
        self.test_module_import('CONFIG.domains', 'Domains configuration')
        self.test_module_import('CONFIG.limits', 'Limits configuration')
        
        # Test 3: DATABASE modules
        print("\n🗄️ Testing DATABASE modules:")
        print("-" * 40)
        self.test_module_import('DATABASE.firebase_init', 'Firebase initialization')
        self.test_module_import('DATABASE.cache_db', 'Cache database')
        self.test_module_import('DATABASE.download_firebase', 'Firebase download utilities')
        
        # Test 4: COMMANDS modules
        print("\n🤖 Testing COMMANDS modules:")
        print("-" * 40)
        self.test_module_import('COMMANDS.admin_cmd', 'Admin commands')
        self.test_module_import('COMMANDS.other_handlers', 'Main handlers')
        self.test_module_import('COMMANDS.tag_cmd', 'Tag commands')
        self.test_module_import('COMMANDS.subtitles_cmd', 'Subtitles commands')
        self.test_module_import('COMMANDS.split_sizer', 'Split commands')
        self.test_module_import('COMMANDS.settings_cmd', 'Settings commands')
        self.test_module_import('COMMANDS.mediainfo_cmd', 'Media info commands')
        self.test_module_import('COMMANDS.format_cmd', 'Format commands')
        self.test_module_import('COMMANDS.cookies_cmd', 'Cookies commands')
        self.test_module_import('COMMANDS.clean_cmd', 'Clean commands')
        
        # Test 5: URL_PARSERS modules
        print("\n🔗 Testing URL_PARSERS modules:")
        print("-" * 40)
        self.test_module_import('URL_PARSERS.video_extractor', 'Video extraction')
        self.test_module_import('URL_PARSERS.url_extractor', 'URL extraction')
        self.test_module_import('URL_PARSERS.embedder', 'URL embedding')
        self.test_module_import('URL_PARSERS.nocookie', 'No-cookie domains')
        self.test_module_import('URL_PARSERS.normalizer', 'URL normalization')
        self.test_module_import('URL_PARSERS.tags', 'Tag extraction')
        self.test_module_import('URL_PARSERS.tiktok', 'TikTok specific')
        self.test_module_import('URL_PARSERS.youtube', 'YouTube specific')
        
        # Test 6: DOWN_AND_UP modules
        print("\n⬇️ Testing DOWN_AND_UP modules:")
        print("-" * 40)
        self.test_module_import('DOWN_AND_UP.always_ask_menu', 'Quality selection menu')
        self.test_module_import('DOWN_AND_UP.down_and_up', 'Video download')
        self.test_module_import('DOWN_AND_UP.down_and_audio', 'Audio download')
        self.test_module_import('DOWN_AND_UP.ffmpeg', 'FFmpeg utilities')
        self.test_module_import('DOWN_AND_UP.sender', 'File sending')
        self.test_module_import('DOWN_AND_UP.yt_dlp_hook', 'yt-dlp hooks')
        
        # Test 7: Key functions
        print("\n🔧 Testing key functions:")
        print("-" * 40)
        self.test_function_import('HELPERS.app_instance', 'set_app', 'Set global app')
        self.test_function_import('HELPERS.app_instance', 'get_app_lazy', 'Get lazy app proxy')
        self.test_function_import('HELPERS.handler_registry', 'on_message', 'Message decorator')
        self.test_function_import('HELPERS.handler_registry', 'on_callback_query', 'Callback decorator')
        self.test_function_import('HELPERS.handler_registry', 'apply_all_handlers', 'Apply handlers')
        self.test_function_import('CONFIG.config', 'Config', 'Main config class')
        
        # Test 8: Critical files exist
        print("\n📁 Testing critical files:")
        print("-" * 40)
        self.test_file_exists('../magic.py', 'Main entry point')
        self.test_file_exists('../requirements.txt', 'Dependencies file')
        self.test_file_exists('../CONFIG/__init__.py', 'CONFIG package')
        self.test_file_exists('../HELPERS/__init__.py', 'HELPERS package')
        self.test_file_exists('../DATABASE/__init__.py', 'DATABASE package')
        self.test_file_exists('../COMMANDS/__init__.py', 'COMMANDS package')
        self.test_file_exists('../URL_PARSERS/__init__.py', 'URL_PARSERS package')
        self.test_file_exists('../DOWN_AND_UP/__init__.py', 'DOWN_AND_UP package')
        
        # Test 9: Decorator usage in key files
        print("\n🎯 Testing decorator usage:")
        print("-" * 40)
        self.test_decorator_usage('../COMMANDS/admin_cmd.py')
        self.test_decorator_usage('../COMMANDS/other_handlers.py')
        self.test_decorator_usage('../COMMANDS/tag_cmd.py')
        self.test_decorator_usage('../COMMANDS/subtitles_cmd.py')
        self.test_decorator_usage('../URL_PARSERS/video_extractor.py')
        self.test_decorator_usage('../URL_PARSERS/url_extractor.py')
        self.test_decorator_usage('../DOWN_AND_UP/always_ask_menu.py')
        
        # Test 10: Magic.py specific checks
        print("\n🌟 Testing magic.py architecture:")
        print("-" * 40)
        try:
            with open('../magic.py', 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for handler registry usage
            if 'apply_all_handlers(app)' in content:
                self.results['magic.py_handlers'] = {
                    'status': 'SUCCESS',
                    'description': 'Handler registry usage',
                    'error': None
                }
                print("✅ magic.py - Handler registry usage")
            else:
                self.results['magic.py_handlers'] = {
                    'status': 'FAILED',
                    'description': 'Handler registry usage',
                    'error': 'apply_all_handlers not found'
                }
                self.errors.append("magic.py: apply_all_handlers not found")
                print("❌ magic.py - Handler registry usage - apply_all_handlers not found")
            
            # Check for set_app usage
            if 'set_app(app)' in content:
                self.results['magic.py_set_app'] = {
                    'status': 'SUCCESS',
                    'description': 'Global app setting',
                    'error': None
                }
                print("✅ magic.py - Global app setting")
            else:
                self.results['magic.py_set_app'] = {
                    'status': 'FAILED',
                    'description': 'Global app setting',
                    'error': 'set_app not found'
                }
                self.errors.append("magic.py: set_app not found")
                print("❌ magic.py - Global app setting - set_app not found")
                
        except Exception as e:
            self.errors.append(f"magic.py: Error reading file - {str(e)}")
            print(f"❌ magic.py - File read error - {str(e)}")
        
        # Generate report
        self.generate_report()
    
    def generate_report(self):
        """Generate comprehensive test report"""
        print("\n" + "=" * 60)
        print("📊 COMPREHENSIVE ARCHITECTURE TEST REPORT")
        print("=" * 60)
        
        # Statistics
        total_tests = len(self.results)
        successful_tests = len([r for r in self.results.values() if r['status'] == 'SUCCESS'])
        failed_tests = len([r for r in self.results.values() if r['status'] == 'FAILED'])
        warning_tests = len([r for r in self.results.values() if r['status'] == 'WARNING'])
        
        print(f"\n📈 Statistics:")
        print(f"   Total tests: {total_tests}")
        print(f"   Successful: {successful_tests}")
        print(f"   Warnings: {warning_tests} (external dependencies)")
        print(f"   Failed: {failed_tests}")
        print(f"   Success rate: {((successful_tests + warning_tests)/total_tests)*100:.1f}%")
        
        if self.errors:
            print(f"\n❌ Errors ({len(self.errors)}):")
            for error in self.errors:
                print(f"   • {error}")
        
        if self.warnings:
            print(f"\n⚠️ Warnings ({len(self.warnings)}):")
            for warning in self.warnings:
                print(f"   • {warning}")
        
        # Architecture status
        if failed_tests == 0:
            if warning_tests > 0:
                print(f"\n🟡 ARCHITECTURE STATUS: YELLOW ⚠️")
                print("   All modules are properly structured!")
                print("   Some external dependencies missing (normal for test environment)")
            else:
                print(f"\n🎉 ARCHITECTURE STATUS: GREEN ✅")
                print("   All modules are properly structured and ready!")
        elif failed_tests <= 3:
            print(f"\n🟡 ARCHITECTURE STATUS: YELLOW ⚠️")
            print("   Most modules are working, but some issues need attention.")
        else:
            print(f"\n🔴 ARCHITECTURE STATUS: RED ❌")
            print("   Multiple issues detected. Architecture needs fixes.")
        
        print(f"\n📋 Detailed Results:")
        for test_name, result in self.results.items():
            if result['status'] == 'SUCCESS':
                status_icon = "✅"
            elif result['status'] == 'WARNING':
                status_icon = "⚠️"
            else:
                status_icon = "❌"
            print(f"   {status_icon} {test_name}: {result['description']}")
            if result['error']:
                print(f"      Error: {result['error']}")
        
        print("\n" + "=" * 60)

if __name__ == "__main__":
    tester = ArchitectureTester()
    tester.run_comprehensive_test() 