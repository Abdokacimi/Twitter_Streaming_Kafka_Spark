import psycopg2
from requests.models import CONTENT_CHUNK_SIZE
# ================= PostgresSql Credentials===============
hostname = 'localhost'
database = 'twitter_users'
username = 'postgres'
pwd = '365pass'
port_id = 5434
# ================= Loading stage !=======================


def load_to_db(CSV_FILE):
    conn = None
    try:
        with psycopg2.connect(
                host=hostname,
                dbname=database,
                user=username,
                password=pwd,
                port=port_id) as conn:
            with conn.cursor() as cur:
                cur.execute('drop table if exists tweets')
                CREATE_Script = '''
            create table if not exists tweets(
                user_id varchar(90) primary key,
                username varchar(90)not null,
                tweet varchar(300) not null,
                created_at varchar(90) not null
            )
            '''
                cur.execute(CREATE_Script)
                with open(CSV_FILE) as my_file:
                    COPY_Script = 'COPY tweets FROM STDIN WITH CSV HEADER DELIMITER AS \',\''
                    cur.copy_expert(sql=COPY_Script, file=my_file)
                    print("file copied to db !")

    except Exception as e:
        print(e)

    finally:
        if conn != None:
            conn.close()
