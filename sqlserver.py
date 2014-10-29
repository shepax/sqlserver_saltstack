import os
import logging
from salt.utils.decorators import depends

log = loggin.getLogger(__name__)

try:
	import pymssql
	HAS_PYMSSQL = True
except ImportError:
	HAS_PYMSSQL= False

__virtualname__= 'SqlServer'

def __virtual__():
	'''
	Load module only if pyodbc installed
	'''
	return __virtualname__ if HAS_PYMSSQL else False
	
def _connect(server,uid,passw)
	'''
	=== windowsdb.sls ===
	sqlserver:
		db_name:
			server: set de ip to connect to the server (192.168.0.0:port) 
			uid: user for the database
			passw: password from the user
	=== end of pillar ===
	
	Returne pymssql.connect instance (server, user_db, password_db)
	'''
	return conn = pymssql.connect(server,uid,passw)

def run_query(db, query):
	'''
	Get the pillar variables for the connection
	server
	uid
	passw
	=======================================================
    Run SQL query and return result

    CLI Example:

        salt '*' sqlserver.run_query db_name "select * from my_table"
    '''
	server = __salt__['pillar.get']('sqlserver:'+ db + ':server')
	uid =  __salt__['pillar.get']('sqlserver:'+ db + ':uid')
	passw = __salt__['pillar.get']('sqlserver:'+ db + ':passw')
	
	'''
	Making the connection to the server
	'''
	conn= _connect(server,uid,passw)
		
	#executing the query 
	return conn.cursor().execute(query).fetchall()
