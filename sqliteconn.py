from sqlite3 import connect

# Replace username with your own A2 Hosting account username:
database = r'C:\sqlite\sqlite-tools-win32-x86-3280000\DSA.db'
conn = connect(database)
curs = conn.cursor()
#curs.execute("CREATE TABLE employees (firstname varchar(32), lastname varchar(32), title varchar(32));")
#conn.commit()
#conn.close()