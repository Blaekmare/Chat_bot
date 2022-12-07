##библеотека для работы с базой данных postgresql
import psycopg2

##функция для вывода ошибок в других функциях используется как тег через @
def log_error(f):

    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            print(f'Ошибка: {e}')
            raise e

    return inner
##выполнение команды в базе данных с внесением изменений
@log_error
def DID_COMMAND_not_return(comand):
    try:
        #Подключение к существующей базе данных
        connection = psycopg2.connect(user="postgres",## название базы данных
                                      password="1530", ##пароль указанный при
                                      # создании базы данных
                                      host="127.0.0.1", ##ip адрес сервера,
                                      # где запущена база данных,если это локальная
                                      # база данных указывается 127.0.0.1
                                      port="5432", ##
                                      database="postgres")

        cursor = connection.cursor() #Курсор для выполнения операций с базой данных
        cursor.execute(comand) #Выполнение SQL-запроса
        connection.commit() #подтверждение изменений в бд
    finally:
        if connection:
            cursor.close()
            connection.close()

##выполнение команды в базе данных с изъятием данных
@log_error
def DID_COMMAND_INDB(comand):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1530",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres")
        cursor = connection.cursor()
        cursor.execute(comand)
        record = cursor.fetchall()
    finally:
        if connection:
            cursor.close()
            connection.close()
    return record

##преобрахование из кортеджа[str] в строку
def convert_tuple(c_tuple):
    star = ''
    for i in c_tuple:
        star = star + i.strip()
    return star

##преобрахование из кортеджа[int] в строку
def convert_tuple_int(c_tuple):
    strin = ''.join([str(a) for a in c_tuple])
    return strin
