import mysql.connector
from mysql.connector import Error

def run_etl():
    try:
        # Step 1: Connect to source database (library)
        src = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="library"
        )
        src_cursor = src.cursor()

        # Extract & Transform: Aggregate books lent per city
        src_cursor.execute("""
            SELECT u.city, COUNT(t.id) AS books_lent
            FROM users u
            JOIN transactions t ON u.id = t.user_id
            GROUP BY u.city
        """)
        results = src_cursor.fetchall()

        # Step 2: Connect to destination database (analytics)
        dest = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root"
        )
        dest_cursor = dest.cursor()

        # Create destination DB and table if not exists
        dest_cursor.execute("CREATE DATABASE IF NOT EXISTS analytics")
        dest_cursor.execute("USE analytics")
        dest_cursor.execute("""
            CREATE TABLE IF NOT EXISTS city_loan_summary (
                city VARCHAR(50),
                books_lent INT
            )
        """)

        # Optional: clear old data before insert (for fresh ETL)
        dest_cursor.execute("DELETE FROM city_loan_summary")

        # Load: Insert aggregated data
        dest_cursor.executemany(
            "INSERT INTO city_loan_summary (city, books_lent) VALUES (%s, %s)",
            results
        )
        dest.commit()

        print("✅ ETL complete: Data loaded into analytics.city_loan_summary")

    except Error as e:
        print(f"❌ ETL failed: {e}")

    finally:
        # Close resources
        if src_cursor:
            src_cursor.close()
        if src:
            src.close()
        if dest_cursor:
            dest_cursor.close()
        if dest:
            dest.close()

if __name__ == "__main__":
    run_etl()
