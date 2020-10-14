from database.connection import connect
import datetime

def createCalendar(u_id, time, name, date):
    connection = connect()
    with connection:
        cur = connection.cursor()
        cur.execute(f'USE heroku_775a68534d5d9c7')
        cur.execute(f'SELECT * from calendartable')
        results = cur.fetchall()
        if(len(results) == 0):
            num = 0
        else:
            cur.execute(f'SELECT MAX(num) from calendartable')
            for row in results:
                num = row["num"]
        cur.execute(f'INSERT INTO calendartable(u_id, time, name, date, num) VALUES("{u_id}", "{time}", "{name}", "{date}", "{num + 1}")')
        connection.commit()
    connection.close()

def showCalendar(frDate, toDate, uid):
    ret = ""
    connection = connect()
    with connection:
        cur = connection.cursor()
        cur.execute(f'USE heroku_775a68534d5d9c7')
        cur.execute(f'SELECT * FROM calendartable WHERE date > %s and date < %s and u_id = %s ORDER BY num', (frDate, toDate, uid))
        results = cur.fetchall()
        if len(results) > 0:
            for row in results:
                num = row["num"]
                time = row["time"]
                name = row["name"]
                date = row["date"]
                ret += ("№" + str(num) + ". " + str(date) + " в " + str(time) + " - " + name + "\n")
            return ret
        else:
            return 228

def delElemOfCalendar(num, uid):
    connection = connect()
    with connection:
        cur = connection.cursor()
        cur.execute(f'USE heroku_775a68534d5d9c7')
        cur.execute(f'DELETE from calendartable WHERE num = %s and u_id = %s', (num, uid))
        cur.execute(f'UPDATE calendartable SET num = num - 1 WHERE num > %s and u_id = %s', (num, uid))
    connection.close()

