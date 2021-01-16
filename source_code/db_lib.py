import pymysql,json

"""This file is used for connecting to database.

Point 1: Connection:
    Step 1: add your connection info in 'connection.py' eg. I saved as mysql_zgc
    Step 2: import connections \n import db_lib as LIB
    Step 3: mysql_config_file = connections.mysql_zgc
            sqlconn = LIB.mySQLconnect_from_connection(mysql_config_file)

Connection done!


Point 2: Run SQL
    Step 1: sql = "select * from user where user_id = '{}'".format(input_userid)
    Step 2: dataset = LIB.runMysqlQuery(mysql_conn, sql)

Dataset got!"""



def mySQLconnect_from_connection(mysql_config):
    hostname = mysql_config['host']
    portnum = mysql_config['port']
    username = mysql_config['user']
    password = mysql_config['password']
    dbname = mysql_config['database']
    charset = mysql_config['charset']
    print(hostname,username,dbname)

    return pymysql.connect(host=hostname, port=int(portnum), user=username, 
        passwd=password, db=dbname, charset=charset,autocommit=True)

def runMysqlQuery(conn, query_str,fw=None):
    cursor = conn.cursor()
    cursor._defer_warnings = True
    try:
        cursor.execute(query_str)

    except Exception as e:
        if fw!=None:
            fw.writelines("query_str {} Error {}\n".format(query_str,e.args))
        else:
            print("query_str {}  Error {}".format(query_str, e.args))
        cursor.close()
        return []
    result = cursor.fetchall()
    cursor.close()
    return result
