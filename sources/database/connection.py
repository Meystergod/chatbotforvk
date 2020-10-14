import pymysql.cursors

def connect():
    connection = pymysql.connect(host = '******',
                                 user = '******',
                                 password = '******',
                                 db = '******',
                                 cursorclass = pymysql.cursors.DictCursor
                                 )
    return connection

connect()