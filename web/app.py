import os
import psycopg2
from flask import Flask, render_template_string

app = Flask(__name__)

DB_NAME = os.environ["POSTGRES_DB"]
DB_USER = os.environ["POSTGRES_USER"]
DB_PASSWORD = os.environ["POSTGRES_PASSWORD"]
DB_HOST = "db"        # имя сервиса БД из docker-compose.yml
DB_PORT = 5432


def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
    )


@app.route("/")
def index():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email FROM users ORDER BY id;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    html = """
    <h1>Пользователи из БД</h1>
    <table border="1" cellpadding="5">
      <tr><th>ID</th><th>Name</th><th>Email</th></tr>
      {% for r in rows %}
      <tr>
        <td>{{ r[0] }}</td>
        <td>{{ r[1] }}</td>
        <td>{{ r[2] }}</td>
      </tr>
      {% endfor %}
    </table>
    """
    return render_template_string(html, rows=rows)


@app.route("/health")
def health():
    return "OK", 200


@app.route("/api/users/count")
def users_count():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM users;")
    count = cur.fetchone()[0]
    cur.close()
    conn.close()
    return str(count)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
