
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def init_db():
    connection = sqlite3.connect("sparo.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_user(email, password):
    connection = sqlite3.connect("sparo.db")
    cursor = connection.cursor()

    password_hash = generate_password_hash(password)

    cursor.execute(
        "INSERT INTO users (email, password_hash) VALUES (?, ?)",
        (email, password_hash)
    )

    connection.commit()
    connection.close()

def check_login(email,password):
    connection = sqlite3.connect("sparo.db")
    cursor = connection.cursor()
    cursor.execute(
        "SELECT password_hash FROM users WHERE email = ?", (email,)
    )
    user = cursor.fetchone()
    connection.close()

    if user is None:
        return False

    return check_password_hash(user[0], password)

if __name__ == "__main__":
    init_db()
    print("Database succesvol aangemaakt!")
