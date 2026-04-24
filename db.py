import mysql.connector
from mysql.connector import Error, pooling

DB_PARAMS = {
<<<<<<< HEAD
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'bd_imc',
    'charset': 'utf8mb4',
    'timezone': '-03:00',
    'use_pure': True,
    'connect_timeout': 10
}

_pool = pooling.MySQLConnectionPool(
    pool_name='imc_pool',
    pool_size=5,
    **DB_PARAMS
=======
    'host' : 'localhost',
    'user' : 'root',
    'password' : '',
    'database' : 'imc_python',
    'charset' : 'utf8mb4',
    'time_zone' : '-03:00',
    'use_pure' : True,
    'connect_timeout' : 10

}

_pool= pooling.MySQLConnectionPool(
    pool_name='imc_pool',
    pool_size = 5,
    **DB_PARAMS 
>>>>>>> 426b602 (primeiro commit)
)

def get_connection():
    try:
        return _pool.get_connection()
    except Error as e:
<<<<<<< HEAD
        raise Exception(f'Erro ao obter conexão do pool: {e}')


def execute_query(sql, params=None, fetch=False):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute(sql, params or ())

        if fetch:
            return cursor.fetchall()
        else:
            conn.commit()
            return cursor.rowcount

    except Error as e:
        conn.rollback()
        raise Exception(f'Erro ao executar a query: {e}')

    finally:
        cursor.close()
        conn.close()
=======
        raise Exception(f'Erro ao obter conexão do pool; {e}')
    
def execute_query(sql, params=None, fetch=False):
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql, params or ())

        if fetch:
            return cursor.fetchall()
        else:
            conn.commit()
            return cursor.rowcount


    except Error as e:
        conn.rollback()
        raise Exception(f'Erro ao executar query {e}' )
    finally:
        cursor.close()
        conn.close()
>>>>>>> 426b602 (primeiro commit)
