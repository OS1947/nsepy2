# login to remote server pgsql, hosted on Oracle cloud
def dbconnect():
    import psycopg2
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

    conn = psycopg2.connect(dbname='nse', user='pkpgsql', password='pk@pgsql2018', host='localhost', port='5432')
    cur = conn.cursor()