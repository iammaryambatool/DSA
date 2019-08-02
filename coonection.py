import pymysql

con = pymysql.connect(host="localhost", user='root',
                           passwd='myadmin',
                           database='DSA')

with con:
    cur = con.cursor()

