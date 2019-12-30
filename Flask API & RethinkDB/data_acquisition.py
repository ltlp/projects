import requests
import pprint
import json
import rethinkdb as rdb 
from rethinkdb.errors import RqlDriverError
r = rdb.RethinkDB()


RDB_HOST = 'localhost'
RDB_PORT = 28015
DB = 'climb'

rdb_conn = r.connect(host=RDB_HOST, port=RDB_PORT, db=DB)

latitude = float(input('Enter latitude: ')) # 39.32
longitude = float(input('Enter longitude: ')) # -111.09
maxDistance = int(input('Enter mile radius (max 500): ')) # 50
maxResults = int(input('Enter how many routes you want (max 500): ')) # 500

url = 'https://www.mountainproject.com/data/get-routes-for-lat-lon?lat={}&lon={}&maxDistance={}&maxResults={}&key=200628419-0e57df72e449af2cbcb4064bc6e65531'.format(latitude, longitude, maxDistance, maxResults)
# url = requests.get('https://www.mountainproject.com/data/get-routes-for-lat-lon?lat=39.32&lon=-111.09&maxDistance=50&maxResults=500&key=200628419-0e57df72e449af2cbcb4064bc6e65531')

data = requests.get(url)
# print(data)

display = pprint.PrettyPrinter(indent=4)
print(display.pprint(data.json()))

r.table('routes').insert(data.json()['routes']).run(rdb_conn)
# r.db('climb').table('routes')