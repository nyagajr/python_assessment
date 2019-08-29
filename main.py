from parse import month_data
import sqlite3

conn = sqlite3.connect('data.db')

conn.set_trace_callback(print)

cursor = conn.cursor()

CREATE_QUERY = '''CREATE TABLE IF NOT EXISTS data (start_date date UNIQUE, end_date date UNIQUE, value float)'''

INSERT_QUERY = '''REPLACE INTO data VALUES (?, ?, ?);'''

cursor.execute(CREATE_QUERY)

cursor.executemany(INSERT_QUERY, month_data)

conn.commit()

conn.close()
