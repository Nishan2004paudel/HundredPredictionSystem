import sqlite3

def create_connection():
    conn = sqlite3.connect('users.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_user(username, password, email):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (username, password, email)
        VALUES (?, ?, ?)
    ''', (username, password, email))
    conn.commit()
    conn.close()

def get_user(username):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM users WHERE username = ?
    ''', (username,))
    user = cursor.fetchone()
    conn.close()
    return user

# Create the users table if it doesn't exist
create_table()