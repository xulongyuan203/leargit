import pymysql

conn = pymysql.connect(host='192.168.153.201', user='root', password='123456', database='mysql_u')
cursor = conn.cursor()
# sql = "show tables"
# sql = """CREATE TABLE USER1(id INT auto_increment PRIMARY KEY,
#  name CHAR(10) NOT NULL UNIQUE,
#   age TINYINT NOT NULL)
#   ENGINE=innodb DEFAULT CHARSET=utf8;"""
# cursor.execute(sql)
# sql = "insert into USER1(name, age) values('zpl2', 27), ('glb2', 25);"
# cursor.execute(sql)
# cursor.commit()
sql2 = "select * from USER1"
cursor.execute(sql2)
result = cursor.fetchall()
print(result)
conn.commit()
cursor.close()
conn.close()