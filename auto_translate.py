#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Автоматический перевод непереведенных строк в файлах локализации.
Использует построчный анализ для точной замены только значений строк,
сохраняя структуру файла, имена переменных и синтаксис Python.
"""

import sys
import re
import importlib.util
from pathlib import Path
from typing import Dict, Tuple, Optional
from deep_translator import GoogleTranslator

# Путь к папке с файлами локализации
LANGUAGES_DIR = Path(__file__).parent / "CONFIG" / "LANGUAGES"
EN_FILE = LANGUAGES_DIR / "messages_EN.py"

# Маппинг кодов языков для Google Translate
LANGUAGE_CODES = {
    'KK': 'kk',  # Казахский
    'FA': 'fa',  # Персидский
    'IT': 'it',  # Итальянский
    'JA': 'ja',  # Японский
    'TL': 'tl',  # Тагальский
    'UK': 'uk',  # Украинский
    'TR': 'tr',  # Турецкий
    'TH': 'th',  # Тайский
    'HA': 'ha',  # Хауса
    'ID': 'id',  # Индонезийский
    'UR': 'ur',  # Урду
    'KO': 'ko',  # Корейский
    'AR': 'ar',  # Арабский
    'IN': 'hi',  # Хинди
    'RU': 'ru',  # Русский
}

# Исключения - строки, которые не нужно переводить
SKIP_PATTERNS = [
    # Убрали паттерн "только эмодзи" - теперь строки с эмодзи будут переводиться
    r'^[\d\s%\.]+$',  # Только цифры, пробелы, точки
    r'^[A-Z_]+$',  # Только заглавные буквы и подчеркивания (без текста)
    r'^users/\{user_id\}/cookie\.txt$',
    r'^formats_\{user_id\}\.txt$',
    r'^\[.*\]$',  # Лог-сообщения
    r'^generic:.*$',
    r'^youtube$',
    r'^tiktok$',
    r'^instagram$',
    r'^twitter$',
    r'^custom$',
    r'^MESSAGE_ID_INVALID$',
    r'^MESSAGE_DELETE_FORBIDDEN$',
    r'^True$',
    r'^False$',
]

# Переменные, которые не нужно переводить (по суффиксу)
SKIP_SUFFIXES = [
    '_EMOJI',
    # Убрали '_BUTTON_MSG' - теперь кнопки будут переводиться
    '_INACTIVE_MSG',
    '_UNAVAILABLE_MSG',
    '_VALUES',
    '_FILE_NAME_MSG',
]


def load_messages_class(file_path: Path) -> Optional[type]:
    """Загружает класс Messages из файла."""
    try:
        spec = importlib.util.spec_from_file_location("messages_module", file_path)
        if spec is None or spec.loader is None:
            return None
        module = importlib.util.module_from_spec(spec)
        sys.modules['messages_module'] = module
        spec.loader.exec_module(module)
        if not hasattr(module, 'Messages'):
            return None
        return module.Messages
    except Exception:
        return None


def get_class_attributes(cls: type) -> Dict[str, any]:
    """Извлекает все атрибуты класса."""
    attributes = {}
    for attr_name in dir(cls):
        if attr_name.startswith('_'):
            continue
        attr_value = getattr(cls, attr_name)
        if callable(attr_value):
            continue
        attributes[attr_name] = attr_value
    return attributes


def should_skip_translation(var_name: str, value: str) -> bool:
    """Проверяет, нужно ли пропустить перевод этой переменной."""
    value_str = str(value)
    
    # Проверяем суффиксы
    if any(var_name.endswith(suffix) for suffix in SKIP_SUFFIXES):
        return True
    
    # Проверяем паттерны
    for pattern in SKIP_PATTERNS:
        if re.match(pattern, value_str):
            return True
    
    # Пропускаем очень короткие строки (менее 2 символов), но только если это не эмодзи с текстом
    # Удаляем эмодзи, HTML теги и переменные для проверки длины текста
    text_without_emoji = re.sub(r'[\U0001F300-\U0001F9FF\U00002600-\U000027BF\U0001F600-\U0001F64F\U0001F680-\U0001F6FF\U00002700-\U000027BF]+', '', value_str)
    text_without_html = re.sub(r'<[^>]+>', '', text_without_emoji)  # Удаляем HTML теги
    text_without_vars = re.sub(r'\{[^}]+\}', '', text_without_html)  # Удаляем переменные
    if len(text_without_vars.strip()) < 2 and len(value_str.strip()) < 8:
        # Если после удаления эмодзи, HTML и переменных осталось меньше 2 символов - пропускаем
        return True
    
    # Пропускаем только многострочные строки с тройными кавычками
    # Строки с экранированными \n (однострочные) будут переводиться
    if value_str.startswith('"""') or value_str.startswith("'''"):
        return True
    
    return False


def protect_variables(text: str) -> Tuple[str, Dict[str, str]]:
    """
    Защищает переменные в фигурных скобках от перевода.
    Возвращает (защищенный текст, словарь замен)
    Использует уникальный маркер, который не может встретиться в тексте.
    """
    replacements = {}
    protected_text = text
    counter = 0
    
    # Находим все {variable_name} и заменяем их на плейсхолдеры
    # Используем уникальный маркер с нулевой шириной пробела для избежания конфликтов
    pattern = r'\{([^}]+)\}'
    matches = list(re.finditer(pattern, protected_text))
    
    # Обрабатываем в обратном порядке, чтобы не сбить индексы
    for match in reversed(matches):
        # Используем уникальный маркер с нулевой шириной пробела
        placeholder = f"\u200B__VAR_{counter}__\u200B"
        replacements[placeholder] = match.group(0)  # Сохраняем {variable_name}
        protected_text = protected_text[:match.start()] + placeholder + protected_text[match.end():]
        counter += 1
    
    return protected_text, replacements


def restore_variables(text: str, replacements: Dict[str, str]) -> str:
    """Восстанавливает переменные из плейсхолдеров."""
    if text is None:
        return ""
    restored = text
    for placeholder, original in replacements.items():
        restored = restored.replace(placeholder, original)
    return restored


def parse_string_value(line: str) -> Optional[Tuple[str, str, str, bool]]:
    """
    Парсит строку присваивания и извлекает имя переменной, значение и формат.
    Возвращает (var_name, value, quote_type, is_fstring) или None.
    Работает только с однострочными строками.
    """
    # Пропускаем строки, которые явно многострочные (с тройными кавычками)
    if '"""' in line or "'''" in line:
        return None
    
    # Пропускаем строки, которые заканчиваются на = (начало многострочного присваивания)
    if line.rstrip().endswith('=') or line.rstrip().endswith('=('):
        return None
    
    # Проверяем, является ли это f-string
    is_fstring = line.strip().startswith('f') or line.strip().startswith('F')
    
    # Паттерн: VAR_NAME = "value" или VAR_NAME = 'value' или f"value" (однострочная строка)
    # Учитываем, что значение может содержать \n как символы, но не реальные переносы
    pattern = r'^(\s*)(?:f|F)?([A-Z][A-Z0-9_]*)\s*=\s*(?:f|F)?(["\'])(.*?)(["\'])$'
    match = re.match(pattern, line.rstrip(), re.DOTALL)
    if match:
        var_name = match.group(2)
        quote_char = match.group(3)
        value = match.group(4)
        
        # Проверяем, что это действительно однострочная строка
        # Если в исходной строке есть реальные переносы (не \n), пропускаем
        if '\n' in line and not line.rstrip().endswith(quote_char):
            return None
        
        # Обрабатываем экранированные кавычки
        value = value.replace(f'\\{quote_char}', quote_char)
        # Обрабатываем экранированные переносы строк
        value = value.replace('\\n', '\n')
        value = value.replace('\\t', '\t')
        
        return (var_name, value, quote_char, is_fstring)
    
    return None


def translate_string(text: str, target_lang: str, max_retries: int = 3) -> str:
    """Переводит строку на целевой язык с защитой переменных в фигурных скобках."""
    # Защищаем переменные
    protected_text, replacements = protect_variables(text)
    
    # Переводим защищенный текст
    for attempt in range(max_retries):
        try:
            translator = GoogleTranslator(source='en', target=target_lang)
            translated = translator.translate(protected_text)
            
            # Если перевод вернул None (например, для строк только с эмодзи), возвращаем исходный текст
            if translated is None:
                # Восстанавливаем переменные из исходного текста
                result = restore_variables(text, replacements)
                if result is None:
                    result = text
                result = result.replace('\u200B', '')
                return result
            
            # Восстанавливаем переменные
            translated = restore_variables(translated, replacements)
            
            # Проверяем, что результат не None
            if translated is None:
                translated = text
            
            # Удаляем невидимые символы (zero-width-space), которые могли появиться
            translated = translated.replace('\u200B', '')
            
            return translated
        except Exception as e:
            if attempt < max_retries - 1:
                import time
                time.sleep(1)  # Пауза перед повтором
                continue
            print(f"        ⚠️  Ошибка перевода: {e}")
            # Восстанавливаем переменные даже при ошибке
            result = restore_variables(text, replacements)
            if result is None:
                result = text
            result = result.replace('\u200B', '')
            return result
    
    # Если все попытки не удались, возвращаем исходный текст
    result = restore_variables(text, replacements)
    if result is None:
        result = text
    result = result.replace('\u200B', '')
    return result


def auto_translate_file(lang_file: Path, lang_code: str, dry_run: bool = False, batch_size: int = 20, start_line: Optional[int] = None, end_line: Optional[int] = None) -> int:
    """Автоматически переводит непереведенные строки в файле."""
    print(f"\n🌐 Обработка: {lang_file.name} ({lang_code})")
    
    # Загружаем эталонный файл
    en_messages = load_messages_class(EN_FILE)
    if en_messages is None:
        print("    ❌ Не удалось загрузить эталонный файл")
        return 0
    
    en_attributes = get_class_attributes(en_messages)
    
    # Загружаем целевой файл
    lang_messages = load_messages_class(lang_file)
    if lang_messages is None:
        print("    ❌ Не удалось загрузить файл")
        return 0
    
    lang_attributes = get_class_attributes(lang_messages)
    
    # Находим непереведенные строки
    untranslated = {}
    for var_name, en_value in en_attributes.items():
        if var_name in lang_attributes:
            lang_value = lang_attributes[var_name]
            if lang_value == en_value and not should_skip_translation(var_name, str(en_value)):
                untranslated[var_name] = str(en_value)
    
    if not untranslated:
        print("    ✅ Все строки переведены!")
        return 0
    
    print(f"    📊 Найдено непереведенных строк: {len(untranslated)}")
    
    # Получаем код языка для перевода
    target_lang_code = LANGUAGE_CODES.get(lang_code, lang_code.lower())
    
    # Читаем содержимое файла построчно
    with open(lang_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Определяем диапазон строк для обработки (индексы начинаются с 0)
    if start_line is not None:
        start_idx = max(0, start_line - 1)  # Конвертируем в 0-based индекс
        print(f"    📍 Начало диапазона: строка {start_line}")
    else:
        start_idx = 0
    
    if end_line is not None:
        end_idx = min(len(lines), end_line)  # end_line уже 1-based, но не включается
        print(f"    📍 Конец диапазона: строка {end_line}")
    else:
        end_idx = len(lines)
    
    if start_line is not None or end_line is not None:
        print(f"    📊 Обработка строк {start_idx + 1}-{end_idx} из {len(lines)}")
    
    translated_count = 0
    i = start_idx
    
    # Обрабатываем файл построчно в указанном диапазоне
    while i < end_idx and i < len(lines):
        line = lines[i]
        
        # Парсим строку (только однострочные)
        parsed = parse_string_value(line)
        if parsed:
            var_name, value, quote_char, is_fstring = parsed
            
            # Проверяем, нужно ли переводить эту переменную
            if var_name in untranslated:
                # Пропускаем строки с реальными переносами строк (многострочные)
                if '\n' in value and value.count('\n') > 0:
                    # Проверяем, это реальные переносы или экранированные \n
                    # Если в исходной строке есть реальные переносы, пропускаем
                    if line.count('\n') > 1 or (line.rstrip().endswith(quote_char) and '\n' in line):
                        i += 1
                        continue
                
                # Проверяем f-string без переменных - пропускаем такие строки
                if is_fstring:
                    # Проверяем, есть ли переменные в строке
                    if not re.search(r'\{[^}]+\}', value):
                        # f-string без переменных - пропускаем
                        i += 1
                        continue
                
                print(f"    🔄 Перевод {var_name} (строка {i+1})...", end=' ')
                
                # Переводим
                translated_value = translate_string(value, target_lang_code)
                
                # Проверяем, что перевод не вернул None
                if translated_value is None:
                    translated_value = value
                    print("⚠️  (перевод вернул None, оставлено оригинальное значение)")
                
                if translated_value != value:
                    # Экранируем специальные символы для Python строки
                    # Восстанавливаем \n и \t обратно в экранированные формы
                    escaped_value = translated_value.replace('\\', '\\\\')  # Сначала экранируем обратные слеши
                    escaped_value = escaped_value.replace('\n', '\\n')  # Затем переносы строк
                    escaped_value = escaped_value.replace('\t', '\\t')  # Затем табуляции
                    escaped_value = escaped_value.replace(quote_char, f'\\{quote_char}')  # Затем кавычки
                    
                    # Заменяем значение в строке
                    # Учитываем f-string префикс
                    f_prefix = 'f' if is_fstring else ''
                    # Используем более точное регулярное выражение
                    pattern = r'=\s*(?:f|F)?' + re.escape(quote_char) + r'.*?' + re.escape(quote_char)
                    new_line = re.sub(
                        pattern,
                        f'= {f_prefix}{quote_char}{escaped_value}{quote_char}',
                        line,
                        count=1
                    )
                    
                    # Если была f-string, но после перевода нет переменных, убираем f
                    if is_fstring and not re.search(r'\{[^}]+\}', escaped_value):
                        new_line = new_line.replace('= f', '= ', 1).replace('= F', '= ', 1)
                    
                    if not dry_run:
                        lines[i] = new_line
                    
                    translated_count += 1
                    print("✅")
                else:
                    print("⏭️  (без изменений)")
        
        i += 1
        
        # Ограничиваем количество переводов за один запуск
        if translated_count >= batch_size:
            print(f"    ⏸️  Достигнут лимит ({batch_size} переводов за раз)")
            break
    
    # Сохраняем файл
    if not dry_run and translated_count > 0:
        with open(lang_file, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print(f"    💾 Сохранено {translated_count} переводов")
    
    return translated_count


def main():
    """Основная функция."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Автоматический перевод непереведенных строк')
    parser.add_argument('--lang', help='Код языка для перевода (например, KK, FA)')
    parser.add_argument('--dry-run', action='store_true', help='Только показать, что будет переведено')
    parser.add_argument('--batch', type=int, default=20, help='Количество переводов за раз (по умолчанию 20)')
    parser.add_argument('--start-line', type=int, help='Начальная строка для обработки (1-based, включительно)')
    parser.add_argument('--end-line', type=int, help='Конечная строка для обработки (1-based, включительно)')
    
    args = parser.parse_args()
    
    if args.lang:
        lang_code = args.lang.upper()
        lang_file = LANGUAGES_DIR / f"messages_{lang_code}.py"
        if not lang_file.exists():
            print(f"❌ Файл {lang_file} не найден")
            return 1
        
        # Валидация диапазона строк
        if args.start_line is not None and args.start_line < 1:
            print(f"❌ Начальная строка должна быть >= 1")
            return 1
        
        if args.end_line is not None and args.end_line < 1:
            print(f"❌ Конечная строка должна быть >= 1")
            return 1
        
        if args.start_line is not None and args.end_line is not None:
            if args.start_line > args.end_line:
                print(f"❌ Начальная строка ({args.start_line}) не может быть больше конечной ({args.end_line})")
                return 1
        
        count = auto_translate_file(lang_file, lang_code, args.dry_run, args.batch, args.start_line, args.end_line)
        print(f"\n✅ Переведено строк: {count}")
        if count > 0:
            print(f"💡 Запустите снова для перевода следующих {args.batch} строк")
    else:
        parser.print_help()
        return 1
    
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\n⚠️  Прервано пользователем")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Критическая ошибка: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
