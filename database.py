import sqlite3

def get_connection():
    return sqlite3.connect("packets.db", check_same_thread=False)


def save_packet(data, alert=None):
    conn = get_connection()
    cursor = conn.cursor()
