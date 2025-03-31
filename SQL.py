import sqlite3


# Підключення до БД або створення нової, якщо її не існує
def connect_db():
    conn = sqlite3.connect('articles.db')
    return conn


# Створення таблиці Articles, якщо вона не існує
def create_table():
    conn = connect_db()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Articles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL,
                    author TEXT UNIQUE NOT NULL)''')
    conn.commit()
    conn.close()


# Створення нової статті
def create_article(title, content, author):
    conn = connect_db()
    c = conn.cursor()
    c.execute('''INSERT INTO Articles (title, content, author) 
                 VALUES (?, ?, ?)''', (title, content, author))
    conn.commit()
    conn.close()


# Видалення статті за id
def delete_article(article_id):
    conn = connect_db()
    c = conn.cursor()
    c.execute('''DELETE FROM Articles WHERE id = ?''', (article_id,))
    conn.commit()
    conn.close()


# Перегляд вмісту статті за id
def view_article(article_id):
    conn = connect_db()
    c = conn.cursor()
    c.execute('''SELECT * FROM Articles WHERE id = ?''', (article_id,))
    article = c.fetchone()
    conn.close()

    if article:
        print(f"ID: {article[0]}")
        print(f"Title: {article[1]}")
        print(f"Content: {article[2]}")
        print(f"Author: {article[3]}")
    else:
        print("Article not found.")


# Приклад використання функцій
create_table()  # Створення таблиці

# Створення нової статті
create_article('Перша стаття', 'Python — один з найпопулярніших мов програмування, завдяки своїй простоті та потужності.', 'Богдан Пилипів')

# Перегляд статті
view_article(1)

# Видалення статті
delete_article(1)
