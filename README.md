Структура проекта:
app.py - телеграм бот
db_connect.py - подключение к PostgreSQL
docker-compose.yml, Dockerfile - докер файлы для компиляции проекта
dumps - дамп бд для docker
neirmodels - папка с сохраненными весами обуяаемой модели
neiron.py - файл обучения нейронной сети
requirements - зависимости
webapp-vue-main - веб-приложение


Для запуска проекта откройте консоль с заранее установленным Docker и docker-compose,
перейдите по пути папке проекта и введите команду 'docker-compose up -d'
Ожидайте окончания сборки проекта
Телеграм бот доступен по имени @goslingteam_bot
В образе развернут тегерам-бот, СУБД PostgreSQL и Manager PgAdmin4

