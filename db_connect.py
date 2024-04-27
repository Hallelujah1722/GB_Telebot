import psycopg2
from psycopg2 import Error  # обработчик ошибок
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

try:
    # Подключение к бд PostgeSQL
    connection = psycopg2.connect(user="user",
                                  dbname="telebot_db",
                                  password="password",
                                  host="telebot_db",
                                  port="5432")

    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)  # кажется это автосохранение измененный данных)
    # создаю курсор
    cursor = connection.cursor()
    print("Подключение к PostgreSQL...")
    # print(connection.get_dsn_parameters(), "\n")
    print("Вы подключены к - PostgreSQL 16.0 ", "\n")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)  # вывод ошибок
finally:
    if connection:
        cursor.close()
        # connection.close()
        # print("Соединение с PostgreSQL закрыто")


def insert_in_db(answers_list, answers_date):  # функция заносит результаты в базу
    cursor = connection.cursor()
    cursor.execute("INSERT INTO survey_data(timestamp, question_1, question_2, question_3, question_4, question_5)"
                   "VALUES(%s,%s,%s,%s,%s,%s)",
                   (answers_date, answers_list[0], answers_list[1], answers_list[2], answers_list[3], answers_list[4]))
    print("Данные успешно занесены в базу")


