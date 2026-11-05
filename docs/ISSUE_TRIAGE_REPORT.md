# Триаж и обновление tg-ytdlp-bot — 22 октября 2026 года

## Результат

- Проанализированы 39 открытых issue; 37 закрыты как completed, 2 оставлены открытыми с частичными исправлениями.
- Начальная ветка вложенного рабочего клона: `main`, HEAD `fe34487`. После fetch всех remote refs выбран актуальный `proger4ever-prs` (`055bf25`).
- Значительный патч изолирован в `fix/issues-468-487-reliability`; `main` и `proger4ever-prs` автоматически не изменялись.
- Коммиты кода: [`0516767`](https://github.com/chelaxian/tg-ytdlp-bot/commit/0516767) и [`4915b08`](https://github.com/chelaxian/tg-ytdlp-bot/commit/4915b08). Оба отправлены в origin.
- DE: CT108, systemd `tg-ytdlp-bot`; код обновлён штатным `scripts/update_from_repo.py`, сервис перезапущен.
- Финальный запуск: **22.10.2026 23:05:46 MSK**, `active`, `NRestarts=0` при проверке.
- `.update-branch` на DE закрепляет тестовую ветку; `.deployed_commit` содержит полный SHA `4915b08a1480fecce41c697dc1ff877ff72f3b23`. Это важно: следующий апдейт не должен вернуть старый main.
- IT/UAE/FR/UK и админ-бот CT102 не изменялись.

## Проверки

- `python scripts/run_offline_smoke.py`: **11/11 наборов PASS** на ПК и в venv DE.
- Локально не выполнялись запросы к Telegram/YouTube/Firebase. Тесты используют mocks, AST-isolated реальные ветки и синтетические файлы.
- Проверены синтаксис, совместимость RPCError imports, дифф и сигнатуры секретов в добавленных строках; секретные конфиги не коммитились.
- При первом деплое 55 изменённых файлов кода сверены по SHA-256 с коммитом, с нормализацией CRLF/LF; ошибок не было. Окончательные изменённые файлы дополнительно проверены до рестарта.
- На DE `/ping` PO-провайдера успешен. YouTube metadata через yt-dlp с настройками PO из бота: **49 форматов**, duration 213; без скачивания видео.
- Реальный Firebase dump на DE: **29 804 588 байт**, успешно завершён 22.10.2026 23:07:03 MSK.
- Прямой standalone import полного metadata-пути бота потребовал Telegram app для регистрации обработчиков и не прошёл; это не сквозной тест бота. Вместо запуска второго клиента проверен yt-dlp/PO путь.
- Первый серверный mock-прогон обнаружил зависимость числа 403 попыток от curl_cffi; исправлена в `4915b08`, окончательный прогон полностью успешен.
- Независимое агентное ревью несколько раз прерывалось API 429 и не дало результата; выполнены собственная проверка диффа, pyflakes, offline suites и серверный smoke. Независимое ревью не выдаётся за выполненное.

## Закрытые issue — GROUP1

В этих задачах исправлено поведение проекта: retry, обработка ошибок, состояние, файловый цикл, диагностика или UX. Наличие upstream-триггера не служило основанием для wontfix. Реальные исторические URL/состояния воспроизведены не для каждого issue.

### [316](https://github.com/chelaxian/tg-ytdlp-bot/issues/316) — completed
Найдены неатомарные writers JSON в LocalDBAdapter, cache_db, geo-cache, sessions и девяти кэшах Always Ask. Запись переведена на временный файл + os.replace; дочерние LocalDBAdapter разделяют файловую блокировку. Ошибка сериализации/квоты сохраняет предыдущий файл. Точный путь из обобщённого исходного лога восстановить нельзя.

### [328](https://github.com/chelaxian/tg-ytdlp-bot/issues/328) — completed
Facebook Cannot parse data теперь останавливает форматный каскад и отображается как локализованная ошибка экстрактора. Сырой текст не выводится в меню. Изменение внешнего экстрактора Facebook не имитируется: недоступный контент по-прежнему может не скачиваться.

### [331](https://github.com/chelaxian/tg-ytdlp-bot/issues/331) — completed
send_videos сохраняет thread-local причину каждого отказа вместо необъяснённого None; вызывающий код её логирует. Неуспешная отправка не считается успешной и не записывается в кэш. Реальная доставка каждого исторического файла не воспроизводилась.

### [352](https://github.com/chelaxian/tg-ytdlp-bot/issues/352) — completed
Members-only распознаётся в обеих формулировках yt-dlp: одна extraction вместо каскада cookies/proxy/formats, отдельное понятное сообщение в Always Ask.

### [355](https://github.com/chelaxian/tg-ytdlp-bot/issues/355) — completed
Кэш HTTP 429 субтитров отделён от очищаемого кэша доступных языков. Первый 429 прекращает вложенные циклы timedtext/formats/proxy и блокирует повтор субтитров этой ссылки для пользователя на час; видео может отправляться без субтитров.

### [360](https://github.com/chelaxian/tg-ytdlp-bot/issues/360) — completed
Проверка возраста, включая take a few minutes to verify your age, завершает extraction без форматного каскада. В меню используется сообщение AGE_RESTRICTED, а не общий отказ.

### [362](https://github.com/chelaxian/tg-ytdlp-bot/issues/362) — completed
На download-пути добавлен один fallback bv*+ba/b; его отказ завершает каскад. Terminal metadata dict прекращает отдельную extraction. Без альтернативного proxy route идентичная extraction не повторяется.

### [384](https://github.com/chelaxian/tg-ytdlp-bot/issues/384) — completed
При преждевременном EOF добавлены ограниченные задержки, continuedl и один resume при наличии непустого .part. Повторный EOF прекращает каскад; наличие постороннего финального файла не считается успехом. Реальные сетевые обрывы этим не исключаются.

### [385](https://github.com/chelaxian/tg-ytdlp-bot/issues/385) — completed
Удаление больше не ориентируется на изменяемый последний каталог меню пользователя. Активные download/merge/split/send каталоги защищены refcount; /clean их пропускает. Janitor удаляет только неактивные временные task-каталоги старше 48 часов. Опасная dashboard find-delete отключена.

### [386](https://github.com/chelaxian/tg-ytdlp-bot/issues/386) — completed
Fresh cookies получает один проход по доступным cookies, затем понятное сообщение COOKIES_REQUIRED. Убраны вложенные fallback-циклы и повторная no-cookie попытка, если исходная уже выполнялась без cookies.

### [394](https://github.com/chelaxian/tg-ytdlp-bot/issues/394) — completed
Ошибки YouTube not a bot обрабатываются как terminal для текущего запроса: без cookies/proxy/форматного каскада. Исправлен сброс счётчика неудач меню. Дополнительно устранён ложный health-probe 400: провайдер проверяется через /ping. На DE провайдер работоспособен, публичный YouTube-ролик извлёкся с 49 форматами. Это не обещание отсутствия будущих YouTube challenges.

### [436](https://github.com/chelaxian/tg-ytdlp-bot/issues/436) — completed
Page needs to be reloaded и INNERTUBE_CONTEXT завершают текущую extraction без повторного каскада. Удалены рекурсивные/идентичные повторные запросы. Провайдер PO на DE проверен; ошибочные root-probe 400 устранены. Неподконтрольные боту challenges YouTube остаются возможны.

### [451](https://github.com/chelaxian/tg-ytdlp-bot/issues/451) — completed
Каталог загрузки пересоздаётся непосредственно перед downloader operation. ENOENT write/rename допускает один recovery retry; исходный DownloadError аудио больше не заворачивается в обычный Exception. Активные task-каталоги защищены от очистки.

### [460](https://github.com/chelaxian/tg-ytdlp-bot/issues/460) — completed
Добавлена плановая очистка только stale users/*/downloads/<task> старше 48 часов с блокировками активных пользователей и каталогов. Настройки и root-файлы пользователей не удаляются. Опасная очистка из dashboard отключена, предложены bot /clean и janitor. В момент аудита DE: 76% диска, 11 ГБ свободно; аварийная массовая чистка не выполнялась.

### [463](https://github.com/chelaxian/tg-ytdlp-bot/issues/463) — completed
ChannelGuard использует три попытки с backoff 2/8 секунд, правильный app loop и отмену ожидающего future при timeout. Окончательный отказ выделяется событием BAN_FAILED_TIMEOUT, не выдаётся за успешный ban. Длительный сбой Telegram всё ещё может препятствовать операции.

### [464](https://github.com/chelaxian/tg-ytdlp-bot/issues/464) — completed
Рекурсивный YouTube timeout retry заменён одним ограниченным повтором. Firebase использует connect/read (10,30)/(10,60), общий deadline и ограниченные повторы идемпотентных запросов; POST push автоматически не повторяется. На DE реальный дамп Firebase успешно сохранён: 29 804 588 байт.

### [465](https://github.com/chelaxian/tg-ytdlp-bot/issues/465) — completed
Подтверждено на DE: /ping и /get_pot работоспособны. HTTP 400 возникал от собственного healthcheck бота к корню bgutil, а не означал отказ выдачи токена. Проверки бота и provider-update скрипта переведены на /ping; состояние логируется при изменении.

### [468](https://github.com/chelaxian/tg-ytdlp-bot/issues/468) — completed
Cookie retry аудио получает реально созданный users/<uid>/cookie.txt через thread-local override вместо устаревшего task-пути из closure. Файл проверяется перед использованием; ENOENT/local-file errors прекращают перебор источников.

### [469](https://github.com/chelaxian/tg-ytdlp-bot/issues/469) — completed
Ошибка json.loads(dict) относится к экстрактору odnoklassniki в yt-dlp, а не к json.loads в боте. На DE уже установлен yt-dlp 2026.10.21.233146.dev0 с upstream-исправлением. В боте добавлена terminal EXTRACTOR_ERROR обработка: без повторов через proxy и без сырого текста пользователю.

### [470](https://github.com/chelaxian/tg-ytdlp-bot/issues/470) — completed
Добавлен общий safe_callback_answer для sync/async Pyrogram; подавляется только QueryIdInvalid, прочие RPC-ошибки не скрываются. На helper переведены ответы в меню и остальных обработчиках. Долгие menu-ветки отвечают заранее; удалён бессмысленный ответ искусственному callback без id.

### [471](https://github.com/chelaxian/tg-ytdlp-bot/issues/471) — completed
Установлен тот же upstream-корень, что у ok.ru: экстрактор передавал dict в JSON decoder. На DE актуальный yt-dlp 2026.10.21.233146.dev0. Bot fallback классифицирует этот отказ и не повторяет его по всем proxy.

### [472](https://github.com/chelaxian/tg-ytdlp-bot/issues/472) — completed
Недоступный peer обрабатывается без повторов, предупреждения ограничены по времени; исправлено ложное after 3 attempts при одной попытке. Фото проверяются по размеру, типу и геометрии до альбома; неподходящие отправляются документами. При Telegram photo-invalid ответе финальный альбом переотправляется документами.

### [473](https://github.com/chelaxian/tg-ytdlp-bot/issues/473) — completed
Unsplash 401 выделен в отдельную понятную ошибку; повторов и бесполезного cookie-hint нет. Домен заранее не блокируется, так как отказ зависит от IP. gallery-dl использует анонимный napi и не поддерживает предложенный client-id/API-key. Доступ к заблокированному источнику этим не обещается.

### [474](https://github.com/chelaxian/tg-ytdlp-bot/issues/474) — completed
Отсутствие processing-сообщения в callback-путях штатно. Удаление использует cached message, очищает соответствующую ссылку и не затрагивает новую сессию. Повторное удаление без сообщения — DEBUG/no-op, не ошибка.

### [475](https://github.com/chelaxian/tg-ytdlp-bot/issues/475) — completed
INNERTUBE_CONTEXT от YouTube extractor распознаётся как terminal EXTRACTOR_ERROR. Перебор proxy прекращается; исходная ошибка сохраняется для диагностики, пользователю не показывается KeyError.

### [476](https://github.com/chelaxian/tg-ytdlp-bot/issues/476) — completed
Найден рекурсивный retry без postprocessors без guard. Теперь он один на item, с коротким ASCII-именем и native HLS downloader. Повторный ffmpeg failure завершает каскад. Счётчик download failures записывается один раз на запрос и не сбрасывается успешными метаданными.

### [477](https://github.com/chelaxian/tg-ytdlp-bot/issues/477) — completed
Generic 400/404/405/410/451 завершают обработку сразу. Generic 403 допускает один проход cookies, затем terminal без перебора браузеров, proxy и форматов. Число попыток больше не зависит от установленного набора curl_cffi targets; подтверждено одинаковым тестом на ПК и DE.

### [478](https://github.com/chelaxian/tg-ytdlp-bot/issues/478) — completed
Cookie-файлы валидируются перед YoutubeDL на initial и fallback путях. Повреждённый файл перемещается в .invalid и не используется повторно; missing file даёт no-cookie fallback. Запись cookies атомарная и не обнуляет рабочий файл при квоте/ENOSPC.

### [479](https://github.com/chelaxian/tg-ytdlp-bot/issues/479) — completed
Удалённые/недоступные видео распознаются как terminal до fallback-цепочек. Девять повторных metadata вызовов обслуживаются коротким terminal cache, смена cookiefile сбрасывает запись. В download-пути terminal metadata прекращает отдельную extraction. Явные geo-errors не блокируют настроенный geo-proxy.

### [480](https://github.com/chelaxian/tg-ytdlp-bot/issues/480) — completed
Pinterest No video formats found направляется в существующий gallery-dl fallback; меню объясняет, что пин может содержать изображения, и предлагает /img вместо сырой ошибки. Удалённый пин даёт понятное content-not-found.

### [481](https://github.com/chelaxian/tg-ytdlp-bot/issues/481) — completed
Найдена не просто шумная cache-miss запись: обычный format ID ошибочно считался потерянным hash, после чего читался захардкоженный formats_cache_75170fc2.json. Бесполезная ветка удалена, короткие IDs используются напрямую. Устаревший hashed callback предлагает обновить меню.

### [482](https://github.com/chelaxian/tg-ytdlp-bot/issues/482) — completed
Файл messages_FA существует. Причина — удаление из sys.modules при конкурентном импорте и два экземпляра router под разными именами. Импорт унифицирован, eviction убран, первая загрузка защищена RLock. Добавлен EN fallback для отсутствующих ключей. Все объявленные локали и конкурентная загрузка FA проверены offline.

### [483](https://github.com/chelaxian/tg-ytdlp-bot/issues/483) — completed
Устранён silent-None путь: AV1 precheck больше не отвергает selector с рабочими альтернативами. Сохраняются причина, stage и domain, сбрасывается ошибка предыдущего playlist item; проверяется ненулевой ydl.download returncode. Финальная граница не оставляет необъяснённый None. Все исторические URL не воспроизводились.

### [484](https://github.com/chelaxian/tg-ytdlp-bot/issues/484) — completed
Facebook Cannot parse data теперь terminal и использует локализованное EXTRACTOR_ERROR. Удалён raw original_error из fallback-menu; подробности остаются в диагностике. Исправлена неинициализированная gallery fallback переменная. Сам внешний Facebook extractor не заменялся.

### [485](https://github.com/chelaxian/tg-ytdlp-bot/issues/485) — completed
Старое сообщение ошибочно приписывало любые ffmpeg/output/conversion сбои невалидным символам. Имена санитизируются заранее; единственный recovery использует короткое ASCII-имя. Исправлен retry с неопределённым ytdl и неприменёнными opts. Текст ошибки обработки больше не выдумывает причину.

### [486](https://github.com/chelaxian/tg-ytdlp-bot/issues/486) — completed
Twitter Unavailable/Suspended/Deleted получает понятное сообщение, rate-limit отделён от постоянной недоступности. Исправлены повторные range-загрузки на локализованных fatal-метках и reverse-range. Raw stderr не показывается пользователю; ожидаемые удалённые ресурсы не засоряют LOG_EXCEPTION.

### [487](https://github.com/chelaxian/tg-ytdlp-bot/issues/487) — completed
Retry дампа охватывает GET и чтение всего stream; запись через уникальный tmp с проверкой и заменой, ограниченные timeout/backoff. Ошибка пишет DUMP FAILED в stderr; runner показывает exit code и stderr перед баннером stdout, экранирует HTML и ограничивает длину. Реальный дамп на DE выполнен успешно: 29 804 588 байт.

## Оставлены открытыми

### [326](https://github.com/chelaxian/tg-ytdlp-bot/issues/326)
Частичное исправление: upload worker больше не запускает app.start() параллельно остановке клиента; добавлены ожидание подключения и shutdown flag. Причина отключения через три часа штатной работы не доказана. После деплоя сервис active, NRestarts=0, но исходный длительный сценарий не воспроизведён. Оставляю issue открытым: нужны логи момента отключения/остановки клиента, а не только последующего отказа отправки.

### [372](https://github.com/chelaxian/tg-ytdlp-bot/issues/372)
Частичное исправление: timeout масштабируется по размеру файла, dedup key не освобождается, пока старый upload реально работает, поздний результат логируется. Уже исполняющийся Python thread принудительно не останавливается и сообщение может прийти позднее. Реальная длительная Telegram-загрузка не проверялась; оставляю issue открытым до проверки больших файлов и стратегии безопасного завершения фоновой отправки.

## Важные эксплуатационные изменения

- Ручная опасная очистка файлов из dashboard отключена по принципу fail-closed: отдельный процесс не видит активные загрузки бота. Доступны защищённый `/clean` и janitor.
- Janitor стартует через 10 минут и раз в час удаляет только неактивные task-каталоги `users/<uid>/downloads/<task>/` старше 48 часов; настройки и корень пользователя не удаляются. Protection markers сохраняются.
- Повреждённые Netscape-cookie-файлы сохраняются в `.invalid`, а не подставляются в каждый запрос. Запись cookies/JSON атомарная.
- Недостающие переводы используют EN fallback; локаль FA существует, её проблема была в конкурентном импорте.
- Серверный код перед обновлением сохранён в `/root/Telegram/_code-backups/before-0516767-20261022.tar.gz`; секретные конфиги и runtime JSON исключены. Штатный updater также сохранил свои файловые бэкапы.
- В рабочем журнале после рестарта наблюдался отказ пустой записи плейлиста `No videos found in playlist at index 0`, после которого запись была пропущена. Сервис не упал; полностью пустой runtime-error log не заявляется.

## Следующие проверки

1. Реальная Telegram-доставка больших файлов и поведение позднего upload — issue 372.
2. Диагностика причины отключения основного клиента в рантайме — issue 326.
3. Проверка обычных пользовательских загрузок, альбомов, cookies и работы janitor на реальной нагрузке. Сквозная проверка каждого сайта не выполнялась.
4. Решение о слиянии тестовой ветки в main после проверки. Автоматическое слияние не выполнялось.
