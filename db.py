import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname='sovs_db',
        user='your_user',
        password='your_password',
        host='localhost',
        port='5432'
    )