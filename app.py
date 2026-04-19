from flask import Flask, render_template, jsonify
from database import get_packets, init_db
from sniffer import start_sniffing
import threading

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
