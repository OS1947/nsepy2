from pony.orm import *
from sshtunnel import SSHTunnelForwarder

REMOTE_HOST = '152.67.7.9'
REMOTE_SSH_PORT = 22
REMOTE_USERNAME = 'ubuntu'
KEY_FILE = "/home/praty/Documents/Project/Demand-Plan/openssh_format"
server = SSHTunnelForwarder((REMOTE_HOST, REMOTE_SSH_PORT),
        ssh_username=REMOTE_USERNAME,
        ssh_pkey=KEY_FILE,
        remote_bind_address=('localhost', 5432),
        local_bind_address=('localhost', 5432))
server.start()

db = Database()

#db.bind(provider='sqlite', filename='praty_test.sqlite', create_db=True)

db.bind(provider='postgres', user='pkpgsql', password='pk@pgsql2018', host='localhost', port='5432', database='nse')

@db_session
q = select(r.symbol for r in test)
