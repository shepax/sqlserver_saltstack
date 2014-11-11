import os
import logging
from salt.utils.decorators import depends

log = logging.getLogger(__name__)

try:
	import pyodbc
	HAS_PYODBC = True
except ImportError:
	HAS_PYODBC= False

__virtualname__= 'sqlodbc'

def __virtual__():
	'''
	Load module only if pymssql installed
	'''
	return __virtualname__ if HAS_PYODBC else False
	
def _connect(host,uid,passw,db):
	'''
	=== windowsdb.sls ===
	sqlodbc:
		db_name:
			host: set de ip to connect to the server (192.168.0.0:port) 
			uid: user for the database
			passw: password from the user
			db: database name
	=== end of pillar ===
	
	Returne pymssql.connect instance (host, user_db, password_db, database)
	'''
	connStr = (
    r'DRIVER={SQL Server};' +
    r'SERVER='+ host +';'+
    r'DATABASE='+ db +';'
    r'UID='+ uid +';'
    r'PWD='+ passw +';'
    )
	
	return pyodbc.connect(connStr)

def run_query(db, query):
	'''
	Get the pillar variables for the connection
	host
	uid
	passw
	=======================================================
    Run SQL query and return result
    CLI Example:
        salt '*' sqlserver.run_query db_name "select * from my_table"
    '''
	host = __salt__['pillar.get']('sqlserver:'+ db + ':host')
	uid =  __salt__['pillar.get']('sqlserver:'+ db + ':uid')
	passw = __salt__['pillar.get']('sqlserver:'+ db + ':passw')
	
	'''
	Making the connection to the server
	'''
	conn = _connect(host,uid,passw,db)
		
	#executing the query 
	rows = conn.cursor().execute(query).fetchall()
	for row in rows:
		print row
