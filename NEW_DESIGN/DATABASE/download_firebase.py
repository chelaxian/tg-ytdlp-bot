#!/usr/bin/env python3
"""
Скрипт для скачивания дампа Firebase Realtime Database
Запускайте этот скрипт раз в день для обновления локального кэша
"""

import json
import os
import sys
from datetime import datetime

try:
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))    
    from CONFIG.config import Config
except ImportError:
    print("❌ Не найден CONFIG/config.py или класс Config! Все параметры должны быть в CONFIG/config.py.")
    sys.exit(1)

try:
    import pyrebase
    import requests
except ImportError:
    # Don't exit in test environment, just continue
    pyrebase = None
    requests = None

# Все параметры берём из config.py
FIREBASE_CONFIG = getattr(Config, 'FIREBASE_CONF', None)
FIREBASE_USER = getattr(Config, 'FIREBASE_USER', None)
FIREBASE_PASSWORD = getattr(Config, 'FIREBASE_PASSWORD', None)
OUTPUT_FILE = getattr(Config, 'FIREBASE_CACHE_FILE', 'firebase_cache.json')

if not FIREBASE_CONFIG or not FIREBASE_USER or not FIREBASE_PASSWORD:
    print("❌ Не все параметры заданы в config.py (FIREBASE_CONF, FIREBASE_USER, FIREBASE_PASSWORD)")
    sys.exit(1)

def download_firebase_dump():
    """Скачивает весь дамп Firebase Realtime Database"""
    if pyrebase is None or requests is None:
        print("⚠️ Firebase dependencies not available (pyrebase, requests)")
        return False
        
    try:
        print(f"🔄 Starting Firebase dump download at {datetime.now()}")
        
        # Инициализация Firebase
        firebase = pyrebase.initialize_app(FIREBASE_CONFIG)
        auth = firebase.auth()
        
        # Аутентификация
        print("🔐 Authenticating with Firebase...")
        user = auth.sign_in_with_email_and_password(FIREBASE_USER, FIREBASE_PASSWORD)
        id_token = user["idToken"]
        print("✅ Authentication successful")
        
        # Скачивание данных
        print("📥 Downloading database dump...")
        url = f"{FIREBASE_CONFIG['databaseURL']}/.json?auth={id_token}"
        response = requests.get(url, timeout=300)  # 5 минут таймаут
        response.raise_for_status()
        
        # Сохранение в файл
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(response.json(), f, ensure_ascii=False, indent=2)
        
        # Статистика
        data = response.json()
        if data:
            total_keys = len(data)
            print(f"✅ Firebase database downloaded successfully!")
            print(f"📊 Total root nodes: {total_keys}")
            print(f"💾 Saved to: {OUTPUT_FILE}")
            print(f"📏 File size: {os.path.getsize(OUTPUT_FILE)} bytes")
            
            # Показываем структуру
            print("\n📋 Database structure:")
            for key in data.keys():
                if isinstance(data[key], dict):
                    sub_keys = len(data[key])
                    print(f"  - {key}: {sub_keys} sub-nodes")
                else:
                    print(f"  - {key}: {type(data[key]).__name__}")
        else:
            print("⚠️ Database is empty")
            
        return True
        
    except Exception as e:
        print(f"❌ Error downloading Firebase dump: {e}")
        return False

def main():
    print("🚀 Firebase Database Dumper (config-driven)")
    print("=" * 40)
    
    # Проверяем конфиг
    if not FIREBASE_CONFIG or not FIREBASE_USER or not FIREBASE_PASSWORD:
        print("❌ Не все параметры заданы в config.py (FIREBASE_CONF, FIREBASE_USER, FIREBASE_PASSWORD)")
        return False
    
    # Скачиваем дамп
    success = download_firebase_dump()
    
    if success:
        print(f"\n🎉 Firebase dump completed at {datetime.now()}")
        print("💡 You can now restart your bot to use the updated cache")
    else:
        print(f"\n💥 Firebase dump failed at {datetime.now()}")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 
