import sqlite3

def findfibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return findfibonacci(n-1) + findfibonacci(n-2)


def get_user_data(user_id):
            conn = sqlite3.connect('example.db')
            cursor = conn.cursor()
            query = f"SELECT * FROM users WHERE id = {user_id}"
            cursor.execute(query)
            result = cursor.fetchall()
            conn.close()
            return result