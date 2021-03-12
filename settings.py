

class Dev():
    ENV = 'development'
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@192.168.153.201/mysql_u?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_ECHO = True


