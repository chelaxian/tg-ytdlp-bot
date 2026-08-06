#!/usr/bin/env python3
"""
Скрипт для создания бэкапа всех модулей перед исправлениями
"""

import os
import sys
import shutil
import datetime
from pathlib import Path

# This script lives in <project_root>/scripts/. Resolve the project root (one
# level up) and chdir there so all relative paths below (COMMANDS/, CONFIG/,
# magic.py, backups, ...) resolve against the project root regardless of where
# the script is invoked from.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(PROJECT_ROOT)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

def create_backup():
    """Создать бэкап всех модулей"""
    
    print("💾 СОЗДАНИЕ БЭКАПА ВСЕХ МОДУЛЕЙ")
    print("=" * 50)
    
    # Создаем папку для бэкапа
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = f"backup_before_fixes_{timestamp}"
    
    try:
        os.makedirs(backup_dir, exist_ok=True)
        print(f"📁 Создана папка бэкапа: {backup_dir}")
        
        # Список папок и файлов для бэкапа
        items_to_backup = [
            'COMMANDS/',
            'HELPERS/',
            'DATABASE/',
            'URL_PARSERS/',
            'DOWN_AND_UP/',
            'CONFIG/',
            'PATCH/',
            'scripts/',
            'magic.py'
        ]
        
        backed_up_count = 0
        
        for item in items_to_backup:
            if os.path.exists(item):
                if os.path.isdir(item):
                    # Копируем папку
                    dest_path = os.path.join(backup_dir, item)
                    shutil.copytree(item, dest_path)
                    print(f"📁 Скопирована папка: {item}")
                    backed_up_count += 1
                else:
                    # Копируем файл
                    dest_path = os.path.join(backup_dir, item)
                    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                    shutil.copy2(item, dest_path)
                    print(f"📄 Скопирован файл: {item}")
                    backed_up_count += 1
            else:
                print(f"⚠️  Не найден: {item}")
        
        print(f"\n✅ БЭКАП СОЗДАН УСПЕШНО!")
        print(f"   📁 Папка бэкапа: {backup_dir}")
        print(f"   📊 Скопировано элементов: {backed_up_count}")
        print(f"   🕒 Время создания: {timestamp}")
        
        # Создаем файл с информацией о бэкапе
        backup_info = f"""БЭКАП СОЗДАН: {timestamp}
===============================

Цель: Бэкап перед исправлением проблем с 'name messages is not defined'
Содержимое: Все модули и файлы проекта
Количество элементов: {backed_up_count}

Для восстановления:
1. Остановите бота
2. Удалите поврежденные файлы
3. Скопируйте файлы из этой папки обратно в проект
4. Запустите бота

ВНИМАНИЕ: Этот бэкап создан автоматически перед исправлениями!
"""
        
        with open(os.path.join(backup_dir, "BACKUP_INFO.txt"), 'w', encoding='utf-8') as f:
            f.write(backup_info)
        
        print(f"📝 Создан файл с информацией: {backup_dir}/BACKUP_INFO.txt")
        
        return backup_dir
        
    except Exception as e:
        print(f"❌ Ошибка при создании бэкапа: {e}")
        return None

if __name__ == "__main__":
    backup_dir = create_backup()
    if backup_dir:
        print(f"\n🎉 Бэкап готов! Папка: {backup_dir}")
    else:
        print("\n❌ Ошибка создания бэкапа!")
