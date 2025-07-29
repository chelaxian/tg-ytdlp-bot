#!/usr/bin/env python3
# Simple Architecture Test

import os
import sys

# Add project root to Python path for imports
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

def test_file_exists(file_path, description):
    if os.path.exists(file_path):
        print(f"✅ {file_path} - {description}")
        return True
    else:
        print(f"❌ {file_path} - {description} - File not found")
        return False

def test_file_content(file_path, required_content, description):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        missing = []
        for item in required_content:
            if item not in content:
                missing.append(item)
        
        if not missing:
            print(f"✅ {file_path} - {description}")
            return True
        else:
            print(f"❌ {file_path} - {description} - Missing: {', '.join(missing)}")
            return False
    except Exception as e:
        print(f"❌ {file_path} - {description} - Error: {str(e)}")
        return False

def test_decorators(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if '@app.on_message' in content or '@app.on_callback_query' in content:
            print(f"❌ {file_path} - Found old @app decorators")
            return False
        elif '@on_message' in content or '@on_callback_query' in content:
            print(f"✅ {file_path} - Using registry decorators")
            return True
        else:
            print(f"✅ {file_path} - No decorators found")
            return True
    except Exception as e:
        print(f"❌ {file_path} - Error reading file: {str(e)}")
        return False

print("🔍 Starting Simple Architecture Test...")
print("=" * 50)

# Test critical files
print("\n📁 Critical files:")
test_file_exists('../magic.py', 'Main entry point')
test_file_exists('../CONFIG/__init__.py', 'CONFIG package')
test_file_exists('../HELPERS/__init__.py', 'HELPERS package')
test_file_exists('../DATABASE/__init__.py', 'DATABASE package')
test_file_exists('../COMMANDS/__init__.py', 'COMMANDS package')
test_file_exists('../URL_PARSERS/__init__.py', 'URL_PARSERS package')
test_file_exists('../DOWN_AND_UP/__init__.py', 'DOWN_AND_UP package')

# Test CONFIG files
print("\n⚙️ CONFIG files:")
test_file_exists('../CONFIG/config.py', 'Main configuration')
test_file_exists('../CONFIG/commands.py', 'Commands configuration')
test_file_exists('../CONFIG/messages.py', 'Messages configuration')
test_file_exists('../CONFIG/domains.py', 'Domains configuration')
test_file_exists('../CONFIG/limits.py', 'Limits configuration')

# Test HELPERS files
print("\n🛠️ HELPERS files:")
test_file_exists('../HELPERS/app_instance.py', 'App instance management')
test_file_exists('../HELPERS/handler_registry.py', 'Handler registry')
test_file_exists('../HELPERS/decorators.py', 'Decorators')
test_file_exists('../HELPERS/logger.py', 'Logging')
test_file_exists('../HELPERS/safe_messeger.py', 'Safe messaging')

# Test magic.py architecture
print("\n🌟 Magic.py architecture:")
test_file_content('../magic.py', 
                ['from CONFIG.config import Config',
                 'from HELPERS.app_instance import set_app',
                 'from HELPERS.handler_registry import apply_all_handlers',
                 'set_app(app)',
                 'apply_all_handlers(app)'],
                'Core architecture elements')

# Test decorator usage
print("\n🎯 Decorator usage:")
test_decorators('../COMMANDS/admin_cmd.py')
test_decorators('../COMMANDS/other_handlers.py')
test_decorators('../COMMANDS/tag_cmd.py')
test_decorators('../URL_PARSERS/video_extractor.py')
test_decorators('../URL_PARSERS/url_extractor.py')
test_decorators('../DOWN_AND_UP/always_ask_menu.py')

print("\n🎉 Test completed!") 