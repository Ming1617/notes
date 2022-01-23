#file:mysite3/init.py
import pymysql

#让django用pymysql对mysql服务器进行操作
pymysql.install_as_MySQLdb()