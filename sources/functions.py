import random
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from database.connection import connect
from datetime import datetime

def sendMessage(vk_session, id_type, id, message = None, keyboard = None):
    vk_session.method('messages.send', {id_type: id, 'message': message, 'random_id': random.randint(-2147483648, 2147483648), 'keyboard': keyboard})

def ttFullDelChecker(word):
    length = len(word.split())
    if length != 2:
        return 1337
    else:
        num = word.split()[1]
        connection = connect()
        with connection:
            cur = connection.cursor()
            cur.execute(f'USE heroku_775a68534d5d9c7')
            cur.execute(f'SELECT * FROM timetable WHERE num = %s', (num))
            results = cur.fetchall()
            if len(results) == 0:
                return 228

def ttShowChecker(word):
    length = len(word.split())
    if length != 2:
        return 1337
    else:
        num = word.split()[1]
        connection = connect()
        with connection:
            cur = connection.cursor()
            cur.execute(f'USE heroku_775a68534d5d9c7')
            cur.execute(f'SELECT * FROM timetable WHERE num = %s', (num))
            results = cur.fetchall()
            if len(results) == 0:
                return 228

def ttCreateChecker(word):
    length = len(word.split())
    if length != 5:
        return 1337
    else:
        num = word.split()[1]
        day = word.split()[2]
        names = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        count = 0
        i = 0
        while(count == 0 and i < 6):
            if day == names[i]:
                count = 1
            else:
                i += 1
        if (num.isdigit() != True) or (int(num) <= 0):
            return 1488
        elif count != 1:
            return 777

def ttModChecker(word):
    num = word.split()[1]
    day = word.split()[2]
    names = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    count = 0
    i = 0
    while (count == 0 and i < 6):
        if day == names[i]:
            count = 1
        else:
            i += 1
    if (num.isdigit() != True) or (int(num) <= 0):
        return 1488
    elif count != 1:
        return 777

def clCreateChecker(word):
    lenght = len(word.split())
    if lenght !=4:
        return 1337
    else:
        date = word.split()[1]
        time = word.split()[2]
        checker1 = 0
        checker2 = 0

        for i in date:
            if i == '.':
                checker1 += 1

        for i in time:
            if i == ':':
                checker2 += 1

        if checker1 != 2 and checker2 != 2:
            return 228
        else:
            year = date.split()[0]
            months = date.split('.')[1]
            day = date.split('.')[2]
            if int(months) >= 12 and int(months) < 0  and int(day) > 31  and int(day) < 0 and int(year) >= 3000 and\
                    int(year) <= 2019 and year.isdigit != True and months.isdigit != True and day.isdigit != True and \
                    ((months == 2 and day > 28) or (months == 4 and day > 30) or (months == 6 and day > 30) or  \
                    (months == 9 and day > 30) or (months == 11 and day > 30)):
                return 228

            hour = time.split(':')[0]
            minute = time.split(':')[1]
            second = time.split(':')[2]

            if int(hour) > 24 and int(hour) < 0  and int(minute) > 60  and int(minute) < 0 and int(second) >= 60 and \
                    int(second) <= 0 and hour.isdigit != True and minute.isdigit != True and second.isdigit != True:
                return 228

            format = '%Y.%m.%d'
            datetime_str = datetime.strptime(date, format)
            if type(datetime_str) == "<class 'datetime.datetime'>":
                print(type(datetime_str))
            else:
                print(12)

def clDelCheck(word):
    lenght = len(word.split())
    if lenght != 1:
        return 1337
    else:
        num = word.split()[1]
        checker = num.isdigit()
        if checker == False:
            return 228
        else:
            connection = connect()
            with connection:
                cur = connection.cursor()
                cur.execute(f'USE heroku_775a68534d5d9c7')
                cur.execute(f'SELECT * FROM timetable WHERE num = %s', (num))
                results = cur.fetchall()
                if len(results) == 0:
                    return 228

def clShowCheck(word):
    lenght = len(word.split())
    if lenght != 3:
        return 1337
    else:
        frdate = word.split()[1]
        todate = word.split()[2]
        checker1 = 0
        checker2 = 0
        for i in frdate:
            if i == '.':
                checker1 += 1

        for i in todate:
            if i == '.':
                checker2 += 1

        if checker1 != 2 and checker2 != 2:
            return 228
        else:
            year = frdate.split()[0]
            months = frdate.split('.')[1]
            day = frdate.split('.')[2]
            year1 = todate.split()[0]
            months1 = todate.split('.')[1]
            day1 = todate.split('.')[2]
            if int(months) >= 12 and int(months) < 0 and int(day) > 31 and int(day) < 0 and int(year) >= 3000 and  \
                    int(year) <= 2019 and int(months1) >= 12 and int(months1) < 0 and int(day1) > 31 and int(day1) \
                    < 0 and int(year1) >= 3000 and int(year1) <= 2019:
                return 228

def createKeyboard(response):
    keyboard = VkKeyboard(one_time = False)
    if response == "начать" or response == "назад":
        keyboard.add_button('РАСПИСАНИЕ', color = VkKeyboardColor.POSITIVE)
        keyboard.add_button('TODO ЛИСТ', color = VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('МЕРОПРИЯТИЯ', color = VkKeyboardColor.POSITIVE)
        keyboard.add_button('МИНИ ИГРЫ', color = VkKeyboardColor.POSITIVE)

    elif response == "расписание" or response == "создать новое расписание" or response == "редактировать текущее расписание" or response == "удалить текущее расписание" or response == "просмотреть расписание":
        keyboard.add_button('СОЗДАТЬ НОВОЕ РАСПИСАНИЕ', color = VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('РЕДАКТИРОВАТЬ ТЕКУЩЕЕ РАСПИСАНИЕ', color = VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('УДАЛИТЬ ТЕКУЩЕЕ РАСПИСАНИЕ', color = VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('ПРОСМОТРЕТЬ РАСПИСАНИЕ', color = VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('НАЗАД', color = VkKeyboardColor.NEGATIVE)

    elif response == "мероприятия" or response == "добавить новое мероприятие" or response == "удалить мероприятие" or response == "просмотреть мероприятия":
        keyboard.add_button('ДОБАВИТЬ НОВОЕ МЕРОПРИЯТИЕ', color = VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('УДАЛИТЬ МЕРОПРИЯТИЕ', color = VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('ПРОСМОТРЕТЬ МЕРОПРИЯТИЯ', color = VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('НАЗАД', color = VkKeyboardColor.NEGATIVE)

    elif response == "todo лист" or response == "добавить задачу" or response == "удалить задачу" or response == "просмотреть список задач":
        keyboard.add_button('ДОБАВИТЬ ЗАДАЧУ', color = VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('УДАЛИТЬ ЗАДАЧУ', color = VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('ПРОСМОТРЕТЬ СПИСОК ЗАДАЧ', color = VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('НАЗАД', color=VkKeyboardColor.NEGATIVE)

    keyboard = keyboard.get_keyboard()
    return keyboard