# 📚 Library ETL Project

This project demonstrates a simple but complete **ETL pipeline** using **Python, MySQL, and Docker**.

We simulate a library system that tracks book lending transactions, then use **ETL (Extract-Transform-Load)** to create a city-level summary in a new analytics database.
Run an ETL script that:
  - **Extracts** data from `library.transactions` and `users`
  - **Transforms** it by aggregating books lent per city
  - **Loads** it into a new `analytics` database as `city_loan_summary` table

---

## 📦 Tech Stack

- 🐍 Python 3
- 🐬 MySQL 8 (via Docker)
- 🐳 Docker & Docker Compose
- 💡 DBeaver (optional GUI)
- `mysql-connector-python`

---

## 📁 Project Structure

library-etl-project/
├── docker-compose.yml # MySQL setup
├── create_tables.py # Creates users & transactions tables
├── insert_data.py # Populates users & transactions
├── etl.py # ETL pipeline to analytics DB
├── requirements.txt # Python dependencies
├── .gitignore
└── README.md

---

## 🛠️ Setup & Run

### 1. Clone & set up environment

```bash
git clone https://github.com/your-username/library-etl-project.git
cd library-etl-project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

---

### 2. Set Up Python Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate

### 3. Install Dependencies
```bash
pip install -r requirements.txt

### 4. Start MySQL Container
```bash
docker-compose up -d
This starts MySQL in a Docker container with:

Username: root

Password: root

Port: 3306

### 🛠️ Execute Project Scripts
### 5. Create Tables
```bash
python3 tables.py

### 6. Insert Sample Data
```bash
python3 insert_data.py

### 7. Run ETL Script
```bash
python3 etl.py

✅ This script will:

Read from library.users and library.transactions

Aggregate book count per city

Store result in analytics.city_loan_summary

### 8. 🧹 Clean Up
Stop the Docker container:
```bash
docker-compose down
