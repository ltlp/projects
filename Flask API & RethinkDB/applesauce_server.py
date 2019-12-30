import os

os.startfile(r'C:\Users\Laura\rethinkdb-2.3.6\rethinkdb.exe')



import rethinkdb as r

d = r.RethinkDB()
connection = d.connect(host='localhost', port=28015, db='applesauce').repl()
print(connection)