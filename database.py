import sqlite3

def get_connection():
    return sqlite3.connect("packets.db", check_same_thread=False)


def save_packet(data, alert=None):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO packets (src, dst, protocol, port, alert) VALUES (?, ?, ?, ?, ?)",
        (data["src"], data["dst"], data["protocol"], data["port"], alert)
    )

    conn.commit()
    conn.close()

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS packets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        src TEXT,
        dst TEXT,
        protocol TEXT,
        port INTEGER,
        alert TEXT
    )
    """)

    conn.commit()
    conn.close()

def get_packets():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM packets ORDER BY id DESC LIMIT 50")
    data = cursor.fetchall()

    conn.close()
    return data
