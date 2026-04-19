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
