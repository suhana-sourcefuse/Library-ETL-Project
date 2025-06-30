import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="library"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    city ENUM('New Delhi', 'Mumbai', 'Bangalore')
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    book_title VARCHAR(100),
    date_lent DATE,
    date_returned DATE,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
""")

print("✅ Tables created.")
conn.close()
