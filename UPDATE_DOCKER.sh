#!/bin/bash
# Version 1.0.0
# Скрипт для быстрого обновления Docker-окружения проекта
# Останавливает контейнеры, обновляет код, пересобирает и запускает заново

set -e  # Остановка при ошибке

# Цвета для вывода
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Флаги
SKIP_UPDATE=false
NO_CACHE=false
REMOVE_VOLUMES=false

# Парсинг аргументов
while [[ $# -gt 0 ]]; do
    case $1 in
        --skip-update)
            SKIP_UPDATE=true
            shift
            ;;
        --no-cache)
            NO_CACHE=true
            shift
            ;;
        --remove-volumes)
            REMOVE_VOLUMES=true
            shift
            ;;
        --help|-h)
            echo "Использование: $0 [OPTIONS]"
            echo ""
            echo "Опции:"
            echo "  --skip-update      Пропустить обновление кода, только пересобрать контейнеры"
            echo "  --no-cache         Собрать образы без использования кеша"
            echo "  --remove-volumes   Удалить volumes при остановке (осторожно! удалит warp-data)"
            echo "  --help, -h         Показать эту справку"
            echo ""
            echo "Примеры:"
            echo "  $0                 Полное обновление: остановка -> обновление кода -> сборка -> запуск"
            echo "  $0 --skip-update   Только пересборка и перезапуск без обновления кода"
            echo "  $0 --no-cache      Полное обновление с пересборкой без кеша"
            exit 0
            ;;
        *)
            echo -e "${RED}❌ Неизвестный аргумент: $1${NC}"
            echo "Используйте --help для справки"
            exit 1
            ;;
    esac
done

# Функция для вывода сообщений
log_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

log_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

log_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

log_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Проверка рабочей директории
if [ ! -f "docker-compose.yml" ]; then
    log_error "docker-compose.yml не найден"
    echo "Запустите скрипт из корневой директории проекта"
    exit 1
fi

if [ ! -f "magic.py" ]; then
    log_error "magic.py не найден"
    echo "Запустите скрипт из корневой директории проекта"
    exit 1
fi

# Проверка наличия docker и docker compose
if ! command -v docker &> /dev/null; then
    log_error "Docker не установлен"
    exit 1
fi

if ! docker compose version &> /dev/null && ! docker-compose version &> /dev/null; then
    log_error "Docker Compose не установлен"
    exit 1
fi

# Определяем команду docker compose
if docker compose version &> /dev/null; then
    DOCKER_COMPOSE="docker compose"
else
    DOCKER_COMPOSE="docker-compose"
fi

log_info "Используется команда: $DOCKER_COMPOSE"

echo ""
log_info "🚀 Начало обновления Docker-окружения"
echo "=========================================="

# Шаг 1: Остановка и удаление контейнеров
echo ""
log_info "Шаг 1/4: Остановка и удаление контейнеров..."

if [ "$REMOVE_VOLUMES" = true ]; then
    log_warning "Будут удалены volumes (включая warp-data)"
    read -p "Продолжить? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        log_info "Отменено пользователем"
        exit 0
    fi
    $DOCKER_COMPOSE down -v
else
    $DOCKER_COMPOSE down
fi

log_success "Контейнеры остановлены и удалены"

# Шаг 2: Обновление кода (если не пропущено)
if [ "$SKIP_UPDATE" = false ]; then
    echo ""
    log_info "Шаг 2/4: Обновление кода из репозитория..."
    
    if [ ! -f "update_from_repo.py" ]; then
        log_error "update_from_repo.py не найден"
        exit 1
    fi
    
    if ! command -v python3 &> /dev/null; then
        log_error "python3 не установлен"
        exit 1
    fi
    
    # Запускаем обновление кода
    if python3 update_from_repo.py; then
        log_success "Код успешно обновлен"
    else
        log_error "Ошибка при обновлении кода"
        exit 1
    fi
else
    echo ""
    log_warning "Шаг 2/4: Обновление кода пропущено (--skip-update)"
fi

# Шаг 3: Сборка образов
echo ""
log_info "Шаг 3/4: Сборка Docker образов..."

BUILD_ARGS=""
if [ "$NO_CACHE" = true ]; then
    BUILD_ARGS="--no-cache"
    log_info "Сборка без кеша"
fi

if $DOCKER_COMPOSE build $BUILD_ARGS; then
    log_success "Образы успешно собраны"
else
    log_error "Ошибка при сборке образов"
    exit 1
fi

# Шаг 4: Запуск контейнеров
echo ""
log_info "Шаг 4/4: Запуск контейнеров..."

if $DOCKER_COMPOSE up -d; then
    log_success "Контейнеры успешно запущены"
else
    log_error "Ошибка при запуске контейнеров"
    exit 1
fi

# Финальная информация
echo ""
echo "=========================================="
log_success "Обновление завершено успешно!"
echo ""
log_info "Статус контейнеров:"
$DOCKER_COMPOSE ps

echo ""
log_info "Для просмотра логов используйте:"
echo "  $DOCKER_COMPOSE logs -f"
echo ""
log_info "Для просмотра логов конкретного сервиса:"
echo "  $DOCKER_COMPOSE logs -f bot"
echo "  $DOCKER_COMPOSE logs -f dashboard"
echo "  $DOCKER_COMPOSE logs -f warp"

