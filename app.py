from flask import Flask, render_template, jsonify
from database import get_packets, init_db
from sniffer import start_sniffing
import threading

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/packets")
def packets():
    data = get_packets()
    return jsonify(data)


def run_sniffer():
    start_sniffing()

if __name__ == "__main__":
    init_db()  # create table

    thread = threading.Thread(target=run_sniffer)
    thread.daemon = True
    thread.start()

    app.run(debug=False)
