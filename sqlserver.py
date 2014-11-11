import os
import logging
from salt.utils.decorators import depends

log = logging.getLogger(__name__)

try:
	import pymssql
	HAS_PYMSSQL = True
except ImportError:
	HAS_PYMSSQL= False

__virtualname__= 'sqlServer'

def __virtual__():
	'''
	Load module only if pymssql installed
	'''
	return __virtualname__ if HAS_PYMSSQL else False
	
def _connect(host,uid,passw,db):
	'''
	=== windowsdb.sls ===
	sqlserver:
		db_name:
			host: set de ip to connect to the server (192.168.0.0:port) 
			uid: user for the database
			passw: password from the user
			db: database name
	=== end of pillar ===
	
	Returne pymssql.connect instance (host, user_db, password_db, database)
	'''
	return pymssql.connect(host,uid,passw,db)

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
	return conn.cursor().execute(query).fetchall()
