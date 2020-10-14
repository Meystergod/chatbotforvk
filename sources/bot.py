import vk_api
from vk_api.longpoll import VkEventType, VkLongPoll
from functions import sendMessage, createKeyboard, ttCreateChecker, ttShowChecker, ttFullDelChecker, clCreateChecker, clDelCheck, clShowCheck
from timetable import creatett, showtt, deltt, modifytt, delNumTt
from calendarlist import createCalendar, showCalendar, delElemOfCalendar
from todolist import createList, showList , delElemToDo, checkerDelElemToDo

vk_session = vk_api.VkApi(token = "cd9b406a92ec88229e1cc7ee74fabf972d3a461bac8d94d2b6c088d42edff9080708c8b29c9c660ae010e")
vk_session.get_api()
longpoll = VkLongPoll(vk_session)

back = "назад"
hello = "начать"
timetable = "расписание"
calendar = "мероприятия"
tDList = "todo лист"

ttSucDel = "Расписание успешно удалено!"
ttSucCreate = "Вы успешно добавили новую запись!"
ttSucModifyMod = "Значение записи успешно изменено!"
ttSucModifyDel = "Запись успешно удалена!"

unknownCommand = "Простите, но вы используете неизвестную мне команду!"
helloAns = "Привет, выбери нужную опцию!"
timetableAns = "Теперь необходимо выбрать то, что вы хотите сделать!"
argError = "Неверное количество аргументов!"
argOptionError = "Неверное количество аргументов, неверный аргумент или неверная опция!"
optionError = "Неверная опция!"
dayValueError = "Неверный день недели!"
numValueError = "Некорректный номер расписания!"
numValueErrorToDO = "Некорректный номер!"
priorityValueError = "Некорректное значение приоритета (допустимые значения 1 или 2)!"
emptyError = "Такого расписания не существует!"
emptyTDError = "Такого to do листа не существует!"
emptyToDoError = "Список пуст!"
areaChangeError = "Неверное поле для изменения!"
error = "Ошибка!"
emptyList = "Такого поля не существует!"
priorityMes = "Приоритет может быть равен только 1 (высокий приоритет) или 2 (низкий приоритет) !"

commandCrateTt = "создать новое расписание"
commandModTt = "редактировать текущее расписание"
commandDelTt = "удалить текущее расписание"
commandShowTt = "просмотреть расписание"
commandCreateCal = "добавить новое мероприятие"
commandDelCal = "удалить мероприятие"
commandShowCal = "просмотреть мероприятия"
commandCreateTodo = "добавить задачу"
commandDelTodo = "удалить задачу"
commandShowTodo = "просмотреть список задач"

infoCreateTt = "Для создания расписания вам необходимо использовать команду:\n!ctt [Номер р-я] [День] [Предмет] [Время начала]"
infoModTt = "Для редактирования расписания вам необходимо использовать команду:\n1. Для изменения конкретного поля:\n!mtt [mod] [Номер р-я] [День] [Время начала] [Предмет / Время] [Новое значение]\n2. Для удаления конкретного поля:\n!mtt [del] [Номер р-я] [День] [Время начала]"
infoDelTt = "Для удаления всего конкретного расписания вам необходимо использовать:\n!dtt [Номер расписания]"
infoShowTt = "Для просмотра расписания вам необходимо использовать команду:\n!stt [Номер расписания]"
infoCreateCal = "Для создания мероприятия вам необходимо использовать команду:\n!ccal [Дата мероприятия] [Время мероприятия] [Название мероприятия]"
infoDelCal = "Для удаления мероприятия вам необходимо использовать команду:\n!dcal [Номер мероприятия]"
infoShowCal = "Для просмотра мероприятий вам необходимо использовать команду:\n!scal [Начальная дата] [Конечная дата]"
infoDelTodo = "Для удаления задачи вам необходимо использовать команду:\n!dtodo [Номер задачи]"
infoCreateTodo = "Для добавления задачи вам необходимо использовать команду:\n!ctodo [Дата] [Название задачи] [Приоритет]"
infoShowTodo = "Для вывода списка задач вам необходимо использовать команду:\n!stodo"

createTt = "!ctt"
showTt = "!stt"
modTt = "!mtt"
deleteTt = "!dtt"

createCal = "!ccal"
showCal = "!scal"
deleteCal = "!dcal"

createToDo = "!ctodo"
showToDo = "!stodo"
deletetodo = "!dtodo"

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            response = event.text.lower()
            keyboard = createKeyboard(response)
            command = response.split()[0]
            word = event.text
            if event.from_user:
                if response == hello:
                    sendMessage(vk_session, 'user_id', event.user_id, message = helloAns, keyboard = keyboard)
                elif response == timetable:
                    sendMessage(vk_session, 'user_id', event.user_id, message = timetableAns, keyboard = keyboard)
                elif response == back:
                    sendMessage(vk_session, 'user_id', event.user_id, message = helloAns, keyboard = keyboard)
                elif response == calendar:
                    sendMessage(vk_session, 'user_id', event.user_id, message=timetableAns, keyboard = keyboard)
                elif response == tDList:
                    sendMessage(vk_session, 'user_id', event.user_id, message=timetableAns, keyboard = keyboard)

                elif response == commandCrateTt:
                    sendMessage(vk_session, 'user_id', event.user_id, message = infoCreateTt, keyboard = keyboard)
                elif response == commandModTt:
                    sendMessage(vk_session, 'user_id', event.user_id, message=infoModTt, keyboard = keyboard)
                elif response == commandDelTt:
                    sendMessage(vk_session, 'user_id', event.user_id, message=infoDelTt, keyboard = keyboard)
                elif response == commandShowTt:
                    sendMessage(vk_session, 'user_id', event.user_id, message=infoShowTt, keyboard = keyboard)
                elif response == commandCreateCal:
                    sendMessage(vk_session, 'user_id', event.user_id, message=infoCreateCal, keyboard = keyboard)
                elif response == commandDelCal:
                    sendMessage(vk_session, 'user_id', event.user_id, message=infoDelCal, keyboard = keyboard)
                elif response == commandShowCal:
                    sendMessage(vk_session, 'user_id', event.user_id, message=infoShowCal, keyboard = keyboard)
                elif response == commandCreateTodo:
                    sendMessage(vk_session, 'user_id', event.user_id, message=infoCreateTodo, keyboard = keyboard)
                elif response == commandDelTodo:
                    sendMessage(vk_session, 'user_id', event.user_id, message=infoDelTodo, keyboard = keyboard)
                elif response == commandShowTodo:
                    sendMessage(vk_session, 'user_id', event.user_id, message=infoShowTodo, keyboard = keyboard)

                elif command == createTt:
                    mes = ttCreateChecker(word)
                    if mes == 1337:
                        sendMessage(vk_session, 'user_id', event.user_id, message=argError)
                    elif mes == 1488:
                        sendMessage(vk_session, 'user_id', event.user_id, message=numValueError)
                    elif mes == 777:
                        sendMessage(vk_session, 'user_id', event.user_id, message=dayValueError)
                    else:
                        uid = event.user_id
                        num = word.split()[1]
                        day = word.split()[2]
                        lesson = word.split()[3]
                        timestart = word.split()[4]
                        creatett(uid, day, lesson, timestart, num)
                        sendMessage(vk_session, 'user_id', event.user_id, message=ttSucCreate)
                elif command == showTt:
                    uid = event.user_id
                    mes = ttShowChecker(word)
                    if mes == 1337:
                        sendMessage(vk_session, 'user_id', event.user_id, message=argError)
                    elif mes == 228:
                        sendMessage(vk_session, 'user_id', event.user_id, message=emptyError)
                    else:
                        num = word.split()[1]
                        count = 0
                        message = ""
                        names = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
                        while (count < 6):
                            name = names[count]
                            per = showtt(uid, num, names[count])
                            message += (name + ":\n" + per + "\n")
                            count += 1
                        sendMessage(vk_session, 'user_id', event.user_id, message = message)
                elif command == modTt:
                    uid = event.user_id
                    length = len(word.split())
                    if (length == 7) and (word.split()[1] == "mod"):
                        num = word.split()[2]
                        day = word.split()[3]
                        timestart = word.split()[4]
                        if word.split()[5] == "Предмет":
                            field = "Предмет"
                            text = word.split()[6]
                            mes = modifytt(uid, num, day, timestart, field, text)
                            if mes == 228:
                                sendMessage(vk_session, 'user_id', event.user_id, message=emptyList)
                            else:
                                sendMessage(vk_session, 'user_id', event.user_id, message=ttSucModifyMod)
                        elif word.split()[5] == "Время":
                            field = "Время"
                            text = word.split()[6]
                            mes = modifytt(uid, num, day, timestart, field, text)
                            if mes == 228:
                                sendMessage(vk_session, 'user_id', event.user_id, message=emptyList)
                            else:
                                sendMessage(vk_session, 'user_id', event.user_id, message=ttSucModifyMod)
                        else:
                            sendMessage(vk_session, 'user_id', event.user_id, message=areaChangeError)
                    elif (length == 5) and (word.split()[1] == "del"):
                        num = word.split()[2]
                        day = word.split()[3]
                        timestart = word.split()[4]
                        mes = deltt(uid, num, day, timestart)
                        if mes == 228:
                            sendMessage(vk_session, 'user_id', event.user_id, message=emptyList)
                        else:
                            sendMessage(vk_session, 'user_id', event.user_id, message=ttSucModifyDel)
                    else:
                        if length != 5 or length != 7:
                            sendMessage(vk_session, 'user_id', event.user_id, message=argOptionError)
                elif command == deleteTt:
                    uid = event.user_id
                    mes = ttFullDelChecker(word)
                    if mes == 228:
                        sendMessage(vk_session, 'user_id', event.user_id, message=emptyError)
                    elif mes == 1337:
                        sendMessage(vk_session, 'user_id', event.user_id, message=argError)
                    else:
                        num = word.split()[1]
                        delNumTt(uid, num)
                        sendMessage(vk_session, 'user_id', event.user_id, message=ttSucDel)
                elif command == createCal:
                    check = clCreateChecker(word)
                    if check == 228:
                        sendMessage(vk_session, 'user_id', event.user_id, message=argError)
                    elif check == 1337:
                        sendMessage(vk_session, 'user_id', event.user_id, message=argError)
                    else:
                        uid = event.user_id
                        date = word.split()[1]
                        time = word.split()[2]
                        name = word.split()[3]
                        createCalendar(uid, time, name, date)
                        sendMessage(vk_session, 'user_id', event.user_id, "Вы успешно добавили новое событие!")
                elif command == showCal:
                    uid = event.user_id
                    check = clShowCheck(word)
                    if check == 228:
                        sendMessage(vk_session, 'user_id', event.user_id, emptyList)
                    elif check == 1337:
                        sendMessage(vk_session, 'user_id', event.user_id, argError)
                    else:
                        date1 = word.split()[1]
                        date2 = word.split()[2]
                        mes = showCalendar(date1, date2, uid)
                        if mes == 228:
                            sendMessage(vk_session, 'user_id', event.user_id, message="Календарь пуст")
                        else:
                            sendMessage(vk_session, 'user_id', event.user_id, message=mes)
                elif command == deleteCal:
                    uid = event.user_id
                    check = clDelCheck(word)
                    if (check == 228):
                        sendMessage(vk_session, 'user_id', event.user_id,
                                    message="Введено некоректное значение! Попробуйте снова.")
                    elif (check == 1337):
                        sendMessage(vk_session, 'user_id', event.user_id, message=argError)
                    else:
                        num = word.split()[1]
                        delElemOfCalendar(num, uid)
                        sendMessage(vk_session, 'user_id', event.user_id, message="Событие успешно удалено!")
                elif command == createToDo:
                    length = len(word.split())
                    if length != 4:
                        sendMessage(vk_session, 'user_id', event.user_id, message=argError)
                    else:
                        uid = event.user_id
                        date = word.split()[1]
                        name = word.split()[2]
                        priority = word.split()[3]
                        if (priority.isdigit() != True) or (int(priority) <= 0):
                            sendMessage(vk_session, 'user_id', event.user_id, message=priorityValueError)
                        else:
                            if priority != "1" and priority != "2":
                                sendMessage(vk_session, 'user_id', event.user_id, message=priorityMes)
                            else:
                                createList(uid, date, name, priority)
                                sendMessage(vk_session, 'user_id', event.user_id, message=ttSucCreate)
                elif command == showToDo:
                    length = len(word.split())
                    if length == 1:
                        u_id = event.user_id
                        mes = showList(u_id)
                        if mes == 228:
                            sendMessage(vk_session, 'user_id', event.user_id, message=emptyToDoError)
                        else:
                            sendMessage(vk_session, 'user_id', event.user_id, message=mes)
                    else:
                        sendMessage(vk_session, 'user_id', event.user_id, message=argError)
                elif command == deletetodo:
                    u_id = event.user_id
                    length = len(word.split())
                    if length != 2:
                        sendMessage(vk_session, 'user_id', event.user_id, message=argError)
                    elif (word.split()[1].isdigit() != True) or (int(word.split()[1]) <= 0):
                        sendMessage(vk_session, 'user_id', event.user_id, message=numValueErrorToDO)
                    else:
                        num = word.split()[1]
                        mes = checkerDelElemToDo(num, u_id)
                        if mes == 228:
                            sendMessage(vk_session, 'user_id', event.user_id, message=emptyTDError)
                        else:
                            delElemToDo(num, u_id)
                            sendMessage(vk_session, 'user_id', event.user_id, message=ttSucModifyDel)