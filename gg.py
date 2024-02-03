import sqlite3
conn = sqlite3.connect('chat_history.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS chat_history
            (user_message TEXT, bot_message TEXT)''')
c.execute('SELECT * FROM chat_history')
a=c.fetchall()
for i in a:
    print(i)
conn.close()
