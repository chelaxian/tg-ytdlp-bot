#!/usr/bin/env python3
"""
Очистка узла /bot/tgytdlp_bot/logs в Firebase Realtime Database
Использует firebase-admin SDK с сервисным аккаунтом
"""

import firebase_admin
from firebase_admin import credentials, db
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# Путь к JSON-файлу сервисного аккаунта, скачанному в
# Firebase Console -> Project settings -> Service accounts -> Generate new private key
SERVICE_ACCOUNT_PATH = "serviceAccountKey.json"

# URL вашей RTDB (europe-west1)
DATABASE_URL = "https://newproject-XXXX-default-rtdb.XXXX-XXX1.firebasedatabase.app/"

# Путь к узлу, который нужно очистить
TARGET_PATH = "/bot/tgytdlp_bot/logs"


def init_firebase():
    cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
    firebase_admin.initialize_app(cred, {"databaseURL": DATABASE_URL})
    logger.info("Firebase инициализирован, DB: %s", DATABASE_URL)


def clear_logs(path: str, dry_run: bool = True):
    ref = db.reference(path)

    # Проверяем, что там есть до удаления (для лога/аудита)
    current_data = ref.get(shallow=True)
    if current_data is None:
        logger.info("Узел %s уже пуст, ничего удалять не нужно.", path)
        return

    count = len(current_data) if isinstance(current_data, dict) else 1
    logger.info("В узле %s найдено записей: %s", path, count)

    if dry_run:
        logger.info("DRY RUN: удаление не выполнено. Запустите с dry_run=False для реальной очистки.")
        return

    ref.delete()
    logger.info("Узел %s успешно очищен.", path)


def main():
    init_firebase()
    # Сначала обязательно проверьте dry_run=True, затем поставьте False
    clear_logs(TARGET_PATH, dry_run=False)


if __name__ == "__main__":
    main()