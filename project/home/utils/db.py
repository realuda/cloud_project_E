import pymysql.cursors

_db = None

def init_db():
    global _db
    if _db is None:
        _db = pymysql.connect(host='localhost', user='root', password='hshadow189', database='khustagram', charset='utf8')

def get_cursor():
    init_db()
    return _db.cursor()

def commit():
    _db.commit()

def select_one(sql):
    cursor = get_cursor()
    cursor.execute(sql)
    return cursor.fetchone()

def select_all(sql):
    cursor = get_cursor()
    cursor.execute(sql)
    return cursor.fetchall()

def insert(sql):
    cursor = get_cursor()
    cursor.execute(sql)
    commit()

