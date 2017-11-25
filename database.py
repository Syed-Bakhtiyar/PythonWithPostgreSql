import psycopg2
import json

connection = psycopg2.connect(user='Bakhtiyar', password='pakistan', database='learning', host='localhost')

with connection.cursor() as cursor:
    cursor.execute('CREATE TABLE IF NOT EXISTS users(id serial primary key,'
                   'email character varying(255) not null unique, '
                   'first_name character varying(255), '
                   'last_name character varying(255) )')
    cursor.execute('CREATE TABLE IF NOT EXISTS post(id serial primary key,'
                   ' user_id integer not null, '
                   'post text not null)')

    connection.commit();
