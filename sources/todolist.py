from database.connection import connect

def createList(u_id, date, name, priority):
    connection = connect()
    with connection:
        cur = connection.cursor()
        cur.execute(f'USE heroku_775a68534d5d9c7')
        cur.execute(
            f'INSERT INTO todotable(u_id, date, name, priority) VALUES("{u_id}", "{date}", "{name}", "{priority}")')
        connection.commit()
    connection.close()

def showList(u_id):
    ret = ""
    connection = connect()
    with connection:
        cur = connection.cursor()
        cur.execute(f'USE heroku_775a68534d5d9c7')
        cur.execute(f'SELECT * FROM todotable WHERE u_id = %s ORDER BY priority', (u_id))
        results = cur.fetchall()
        count = 1
        if len(results) == 0:
            return 228
        else:
            for row in results:
                date = row["date"]
                name = row["name"]
                # num = row["num"]
                priority = row["priority"]
                if priority == 1:
                    ret += ("№" + str(count) + ' ' + name + " до " + str(date) + " | ВЫСОКИЙ ПРИОРИТЕТ!" + "\n")
                else:
                    ret += ("№" + str(count) + ' ' + name + " до " + str(date) + "\n")
                count += 1
            return ret
    connection.close()

def delElemToDo(num, u_id):
    connection = connect()
    with connection:
        cur = connection.cursor()
        cur.execute(f'USE heroku_775a68534d5d9c7')
        cur.execute(f'DELETE from todotable WHERE num = %s AND u_id = %s', (num, u_id))
    connection.close()

def checkerDelElemToDo(num, u_id):
    connection = connect()
    with connection:
        cur = connection.cursor()
        cur.execute(f'USE heroku_775a68534d5d9c7')
        cur.execute(f'SELECT * from todotable WHERE num = %s AND u_id = %s', (num, u_id))
        results = cur.fetchall()
        if len(results) == 0:
            return 228
    connection.close()