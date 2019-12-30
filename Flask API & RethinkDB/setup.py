import json
import rethinkdb as rdb 
from flask import Flask, g, render_template, abort, request
from rethinkdb.errors import RqlDriverError
r = rdb.RethinkDB()


RDB_HOST = 'localhost'
RDB_PORT = 28015
DB = 'climb'

app = Flask(__name__)
app.config.from_object(__name__)

@app.before_request
def before_request():
	try:
		g.rdb_conn = r.connect(host=RDB_HOST, port=RDB_PORT, db=DB)
	except RqlDriverError:
		abort(503, 'No database connection.')

@app.route('/')
def home():
	return render_template('template.html')
	
@app.route('/api/v1/routes', methods=['GET'])
def get_all():
	routes = list(r.table('routes').run(g.rdb_conn))
	return json.dumps(routes)



if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5001)