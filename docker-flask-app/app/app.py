from flask import Flask, render_template
import psycopg2
import redis
import time

app = Flask(__name__)

# Redis Connection
redis_client = redis.Redis(host='redis', port=6379)

# PostgreSQL Connection Function
def get_db_connection():
    while True:
        try:
            connection = psycopg2.connect(
                host="db",
                database="flaskdb",
                user="postgres",
                password="postgres"
            )
            return connection
        except Exception as e:
            print("Database not ready, retrying...")
            time.sleep(5)

# Initialize Database
def initialize_database():
    conn = get_db_connection()
    cur = conn.cursor()

    with open("init.sql", "r") as file:
        cur.execute(file.read())

    conn.commit()
    cur.close()
    conn.close()

initialize_database()

@app.route("/")
def home():

    # Redis Counter
    redis_client.incr('hits')
    visitor_count = redis_client.get('hits').decode('utf-8')

    # PostgreSQL Insert
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("INSERT INTO visitors DEFAULT VALUES;")
    conn.commit()

    # Fetch Visit Count
    cur.execute("SELECT COUNT(*) FROM visitors;")
    db_visits = cur.fetchone()[0]

    cur.close()
    conn.close()

    return render_template(
        "index.html",
        redis_visits=visitor_count,
        db_visits=db_visits
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
