#!/usr/bin/env python3
# Architecture Integrity Test
# Simplified test that doesn't depend on external libraries

import os
import sys
import importlib
import re
from typing import Dict, List, Tuple

# Add project root to Python path for imports
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

class IntegrityTester:
    def __init__(self):
        self.results = {}
        self.errors = []
        self.warnings = []
        
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
    
    def test_file_content(self, file_path: str, required_content: List[str], description: str = "") -> bool:
        """Test if file contains required content"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            missing_items = []
            for item in required_content:
                if item not in content:
                    missing_items.append(item)
            
            if not missing_items:
                self.results[f"{file_path}_content"] = {
                    'status': 'SUCCESS',
                    'description': description,
                    'error': None
                }
                print(f"✅ {file_path} - {description}")
                return True
            else:
                error_msg = f"Missing: {', '.join(missing_items)}"
                self.results[f"{file_path}_content"] = {
                    'status': 'FAILED',
                    'description': description,
                    'error': error_msg
                }
                self.errors.append(f"{file_path}: {error_msg}")
                print(f"❌ {file_path} - {description} - {error_msg}")
                return False
                
        except Exception as e:
            error_msg = f"Error reading file: {str(e)}"
            self.results[f"{file_path}_content"] = {
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
    
    def test_import_structure(self, file_path: str, required_imports: List[str], description: str = "") -> bool:
        """Test if file has proper import structure"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            missing_imports = []
            for imp in required_imports:
                if imp not in content:
                    missing_imports.append(imp)
            
            if not missing_imports:
                self.results[f"{file_path}_imports"] = {
                    'status': 'SUCCESS',
                    'description': description,
                    'error': None
                }
                print(f"✅ {file_path} - {description}")
                return True
            else:
                error_msg = f"Missing imports: {', '.join(missing_imports)}"
                self.results[f"{file_path}_imports"] = {
                    'status': 'FAILED',
                    'description': description,
                    'error': error_msg
                }
                self.errors.append(f"{file_path}: {error_msg}")
                print(f"❌ {file_path} - {description} - {error_msg}")
                return False
                
        except Exception as e:
            error_msg = f"Error reading file: {str(e)}"
            self.results[f"{file_path}_imports"] = {
                'status': 'FAILED',
                'description': description,
                'error': error_msg
            }
            self.errors.append(f"{file_path}: {error_msg}")
            print(f"❌ {file_path} - {description} - {error_msg}")
            return False
    
    def run_integrity_test(self):
        """Run integrity test"""
        print("🔍 Starting Architecture Integrity Test...")
        print("=" * 60)
        
        # Test 1: Critical files exist
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
        
        # Test 2: CONFIG files
        print("\n⚙️ Testing CONFIG files:")
        print("-" * 40)
        self.test_file_exists('../CONFIG/config.py', 'Main configuration')
        self.test_file_exists('../CONFIG/commands.py', 'Commands configuration')
        self.test_file_exists('../CONFIG/messages.py', 'Messages configuration')
        self.test_file_exists('../CONFIG/domains.py', 'Domains configuration')
        self.test_file_exists('../CONFIG/limits.py', 'Limits configuration')
        
        # Test 3: HELPERS files
        print("\n🛠️ Testing HELPERS files:")
        print("-" * 40)
        self.test_file_exists('../HELPERS/app_instance.py', 'App instance management')
        self.test_file_exists('../HELPERS/handler_registry.py', 'Handler registry')
        self.test_file_exists('../HELPERS/decorators.py', 'Decorators')
        self.test_file_exists('../HELPERS/logger.py', 'Logging')
        self.test_file_exists('../HELPERS/safe_messeger.py', 'Safe messaging')
        self.test_file_exists('../HELPERS/download_status.py', 'Download status')
        self.test_file_exists('../HELPERS/filesystem_hlp.py', 'Filesystem helpers')
        self.test_file_exists('../HELPERS/limitter.py', 'Rate limiting')
        self.test_file_exists('../HELPERS/caption.py', 'Caption utilities')
        self.test_file_exists('../HELPERS/porn.py', 'Content filtering')
        self.test_file_exists('../HELPERS/qualifier.py', 'Quality management')
        
        # Test 4: DATABASE files
        print("\n🗄️ Testing DATABASE files:")
        print("-" * 40)
        self.test_file_exists('../DATABASE/firebase_init.py', 'Firebase initialization')
        self.test_file_exists('../DATABASE/cache_db.py', 'Cache database')
        self.test_file_exists('../DATABASE/download_firebase.py', 'Firebase download')
        
        # Test 5: COMMANDS files
        print("\n🤖 Testing COMMANDS files:")
        print("-" * 40)
        self.test_file_exists('../COMMANDS/admin_cmd.py', 'Admin commands')
        self.test_file_exists('../COMMANDS/other_handlers.py', 'Main handlers')
        self.test_file_exists('../COMMANDS/tag_cmd.py', 'Tag commands')
        self.test_file_exists('../COMMANDS/subtitles_cmd.py', 'Subtitles commands')
        self.test_file_exists('../COMMANDS/split_sizer.py', 'Split commands')
        self.test_file_exists('../COMMANDS/settings_cmd.py', 'Settings commands')
        self.test_file_exists('../COMMANDS/mediainfo_cmd.py', 'Media info commands')
        self.test_file_exists('../COMMANDS/format_cmd.py', 'Format commands')
        self.test_file_exists('../COMMANDS/cookies_cmd.py', 'Cookies commands')
        self.test_file_exists('../COMMANDS/clean_cmd.py', 'Clean commands')
        
        # Test 6: URL_PARSERS files
        print("\n🔗 Testing URL_PARSERS files:")
        print("-" * 40)
        self.test_file_exists('../URL_PARSERS/video_extractor.py', 'Video extraction')
        self.test_file_exists('../URL_PARSERS/url_extractor.py', 'URL extraction')
        self.test_file_exists('../URL_PARSERS/embedder.py', 'URL embedding')
        self.test_file_exists('../URL_PARSERS/nocookie.py', 'No-cookie domains')
        self.test_file_exists('../URL_PARSERS/normalizer.py', 'URL normalization')
        self.test_file_exists('../URL_PARSERS/tags.py', 'Tag extraction')
        self.test_file_exists('../URL_PARSERS/tiktok.py', 'TikTok specific')
        self.test_file_exists('../URL_PARSERS/youtube.py', 'YouTube specific')
        
        # Test 7: DOWN_AND_UP files
        print("\n⬇️ Testing DOWN_AND_UP files:")
        print("-" * 40)
        self.test_file_exists('../DOWN_AND_UP/always_ask_menu.py', 'Quality selection menu')
        self.test_file_exists('../DOWN_AND_UP/down_and_up.py', 'Video download')
        self.test_file_exists('../DOWN_AND_UP/down_and_audio.py', 'Audio download')
        self.test_file_exists('../DOWN_AND_UP/ffmpeg.py', 'FFmpeg utilities')
        self.test_file_exists('../DOWN_AND_UP/sender.py', 'File sending')
        self.test_file_exists('../DOWN_AND_UP/yt_dlp_hook.py', 'yt-dlp hooks')
        
        # Test 8: Magic.py architecture
        print("\n🌟 Testing magic.py architecture:")
        print("-" * 40)
        self.test_file_content('../magic.py', 
                             ['from CONFIG.config import Config',
                              'from HELPERS.app_instance import set_app',
                              'from HELPERS.handler_registry import apply_all_handlers',
                              'set_app(app)',
                              'apply_all_handlers(app)'],
                             'Core architecture elements')
        
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
        
        # Test 10: Import structure in key files
        print("\n📦 Testing import structure:")
        print("-" * 40)
        self.test_import_structure('../COMMANDS/admin_cmd.py',
                                 ['from HELPERS.app_instance import get_app_lazy',
                                  'from HELPERS.handler_registry import on_message',
                                  'from pyrogram import filters',
                                  'from CONFIG.config import Config'],
                                 'Admin commands imports')
        
        self.test_import_structure('../HELPERS/app_instance.py',
                                 ['def set_app',
                                  'def get_app_lazy'],
                                 'App instance functions')
        
        self.test_import_structure('../HELPERS/handler_registry.py',
                                 ['def on_message',
                                  'def on_callback_query',
                                  'def apply_all_handlers'],
                                 'Handler registry functions')
        
        # Generate report
        self.generate_report()
    
    def generate_report(self):
        """Generate integrity test report"""
        print("\n" + "=" * 60)
        print("📊 ARCHITECTURE INTEGRITY TEST REPORT")
        print("=" * 60)
        
        # Statistics
        total_tests = len(self.results)
        successful_tests = len([r for r in self.results.values() if r['status'] == 'SUCCESS'])
        failed_tests = len([r for r in self.results.values() if r['status'] == 'FAILED'])
        
        print(f"\n📈 Statistics:")
        print(f"   Total tests: {total_tests}")
        print(f"   Successful: {successful_tests}")
        print(f"   Failed: {failed_tests}")
        print(f"   Success rate: {(successful_tests/total_tests)*100:.1f}%")
        
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
            status_icon = "✅" if result['status'] == 'SUCCESS' else "❌"
            print(f"   {status_icon} {test_name}: {result['description']}")
            if result['error']:
                print(f"      Error: {result['error']}")
        
        print("\n" + "=" * 60)

if __name__ == "__main__":
    tester = IntegrityTester()
    tester.run_integrity_test() 