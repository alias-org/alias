import alias as al

def mysql_connect(dbaddress=None, u='', p='', db=None):
    try:
        import mysql.connector
        from mysql.connector import Error
    except ImportError:
        raise ImportError("mysql.connector required for mysql_connect()")

    try:
        if dbaddress:
            if db:
                conn = mysql.connector.connect(host=str(dbaddress), database=db, user=u, password=p)
            else:
                conn = mysql.connector.connect(host=str(dbaddress), database='mysql', user=u, password=p)
        else:
            if db:
                conn = mysql.connector.connect(host='localhost', database=db, user=u, password=p)
            else:
                conn = mysql.connector.connect(host='localhost', database='mysql', user=u, password=p)
    except Error as e:
        print e

    return conn

def to_mysql(af, dbaddress=None, u='', p='', db=None):
    conn = mysql_connect(dbaddress=dbaddress, u=u, p=p, db=db)

def from_mysql():
    pass