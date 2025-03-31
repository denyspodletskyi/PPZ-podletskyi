import sqlite3


def main():
    # 1. Підключення до бази даних
    conn = sqlite3.connect("trains.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS train_cars (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT NOT NULL,
        capacity INTEGER NOT NULL
    )''')

    # 3. Додаємо тестові дані
    cursor.executemany("INSERT INTO train_cars (type, capacity) VALUES (?, ?)", [
        ("Пасажирський", 50),
        ("Вантажний", 100),
        ("Швидкісний", 200)
    ])

    # 2. Отримання списку таблиць
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    print("Таблиці в базі даних:")
    for table in tables:
        print(table[0])

    # 3. Виведення вмісту кожної таблиці
    for table in tables:
        table_name = table[0]
        print(f"\nВміст таблиці {table_name}:")
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    # 4. Закриття з'єднання
    conn.close()


if __name__ == "__main__":
    main()
