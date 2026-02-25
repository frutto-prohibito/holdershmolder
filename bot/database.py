import sqlite3

# подключаемся к файлу базы (создастся если нет)
conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

# создаём таблицу заказов если нет
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()


# функция для добавления заказа
def add_order(name: str, address: str):
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO orders (name, address) VALUES (?, ?)",
        (name, address)
    )
    conn.commit()
    conn.close()
