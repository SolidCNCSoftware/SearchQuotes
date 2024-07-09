import sqlite3

def create_table():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS lines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            line TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_lines(file_path):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            c.execute('INSERT INTO lines (line) VALUES (?)', (line.strip(),))
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    insert_lines('translate.txt')
