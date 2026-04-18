from flask import Flask, render_template, jsonify
from database import get_packets, init_db
from sniffer import start_sniffing
import threading
