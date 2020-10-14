from database.connection import connect

def creatett(u_id, day, lesson, time_start, num):
    connection = connect()
    with connection:
        cur = connection.cursor()
        cur.execute(f'USE heroku_775a68534d5d9c7')
        cur.execute(f'INSERT INTO timetable(u_id, day, lesson, time_start, num) VALUES("{u_id}", "{day}", "{lesson}", "{time_start}", "{num}")')
        connection.commit()
    connection.close()

def showtt(uid, num, day):
    ret = ""
    connection = connect()
    with connection:
        cur = connection.cursor()
        cur.execute(f'USE heroku_775a68534d5d9c7')
        cur.execute(f'SELECT * FROM timetable WHERE num = %s AND day = %s AND u_id = %s ORDER BY time_start', (num, day, uid))
        results = cur.fetchall()
        print(len(results))
        for row in results:
            lesson = row["lesson"]
            timestart = row["time_start"]
            ret += (str(timestart) + " - " + lesson + "\n")
        return ret

def deltt(uid, num, day, timestart):
    connection = connect()
    with connection:
        cur = connection.cursor()
        cur.execute(f'USE heroku_775a68534d5d9c7')
        cur.execute(f'SELECT * FROM timetable WHERE num = %s AND day = %s AND time_start = %s AND u_id = %s', (num, day, timestart, uid))
        results = cur.fetchall()
        if len(results) == 0:
            return 228
        else:
            cur.execute(f'DELETE FROM timetable WHERE num = %s AND day = %s AND time_start = %s AND u_id = %s', (num, day, timestart, uid))
    connection.close()

def modifytt(uid, num, day, timestart, field, perem):
    connection = connect()
    with connection:
        cur = connection.cursor()
        cur.execute(f'USE heroku_775a68534d5d9c7')
        if field == "Предмет":
            cur.execute(f'SELECT * FROM timetable WHERE num = %s AND day = %s AND time_start = %s AND u_id = %s', (num, day, timestart, uid))
            results = cur.fetchall()
            if len(results) == 0:
                return 228
            else:
                cur.execute(f'UPDATE timetable SET lesson = %s WHERE num = %s AND day = %s AND time_start = %s AND u_id = %s', (perem, num, day, timestart, uid))
        elif field == "Время":
            cur.execute(f'SELECT * FROM timetable WHERE num = %s AND day = %s AND time_start = %s AND u_id = %s', (num, day, timestart, uid))
            results = cur.fetchall()
            if len(results) == 0:
                return 228
            else:
                cur.execute(f'UPDATE timetable SET time_start = %s WHERE num = %s AND day = %s AND time_start = %s AND u_id = %s', (perem, num, day, timestart, uid))
        else:
            connection.close()
    connection.close()

def delNumTt(uid, num):
    connection = connect()
    with connection:
        cur = connection.cursor()
        cur.execute(f'USE heroku_775a68534d5d9c7')
        cur.execute(f'DELETE from timetable WHERE num = %s AND u_id = %s', (num, uid))
    connection.close()