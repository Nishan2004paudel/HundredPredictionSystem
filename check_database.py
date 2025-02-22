import sqlite3

def create_connection():
    conn = sqlite3.connect('users.db')
    return conn

def check_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return users

if __name__ == "__main__":
    users = check_users()
    for user in users:
        print(user)