import mysql.connector
from datetime import date

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="library"
)

cursor = conn.cursor()

users = [
    ("Ankit", "Sharma", 30, "New Delhi"),
    ("Meera", "Kapoor", 28, "Bangalore"),
    ("Rohan", "Verma", 26, "Mumbai"),
    ("Neha", "Singh", 32, "New Delhi"),
    ("Vikas", "Mehta", 29, "Bangalore"),
    ("Priya", "Desai", 27, "Mumbai"),
    ("Amit", "Jain", 35, "New Delhi"),
    ("Sneha", "Patel", 31, "Bangalore"),
    ("Rahul", "Nair", 24, "Mumbai"),
    ("Isha", "Khanna", 22, "New Delhi"),
    ("Karan", "Malhotra", 33, "Bangalore"),
    ("Tanya", "Reddy", 25, "Mumbai"),
    ("Arjun", "Gupta", 30, "New Delhi"),
    ("Divya", "Menon", 28, "Bangalore"),
    ("Nikhil", "Chopra", 34, "Mumbai"),
    ("Pooja", "Joshi", 29, "New Delhi"),
    ("Siddharth", "Pillai", 31, "Bangalore"),
    ("Alok", "Mishra", 27, "Mumbai"),
    ("Kritika", "Agarwal", 26, "New Delhi"),
    ("Harsh", "Saxena", 32, "Bangalore"),
    ("Ritu", "Kohli", 24, "Mumbai"),
    ("Yash", "Tiwari", 28, "New Delhi"),
    ("Ananya", "Rao", 30, "Bangalore"),
    ("Deepak", "Das", 29, "Mumbai"),
    ("Simran", "Yadav", 25, "New Delhi")
]


cursor.executemany("INSERT INTO users (first_name, last_name, age, city) VALUES (%s, %s, %s, %s)", users)

transactions = [
    (1, "Atomic Habits", date(2024, 5, 20), date(2024, 6, 1)),
    (2, "1984", date(2024, 5, 25), None),
    (1, "Ikigai", date(2024, 6, 10), None)
]

cursor.executemany("INSERT INTO transactions (user_id, book_title, date_lent, date_returned) VALUES (%s, %s, %s, %s)", transactions)

conn.commit()
print("✅ Users and transactions inserted.")
conn.close()
