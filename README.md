# 📡 Network Packet Sniffer & Intrusion Detection System (IDS)

A real-time network monitoring tool that captures packets, analyzes traffic, and detects suspicious activities like port scanning using Python.

---

## 🚀 Features

- 📡 Live packet capture using Scapy  
- 🌐 Extracts:
  - Source IP
  - Destination IP
  - Protocol (TCP / UDP / ICMP)
  - Port numbers  
- 🚨 Intrusion Detection:
  - Detects Port Scanning attacks  
- 📊 Real-time web dashboard using Flask  
- 🗄️ Stores packets in SQLite database  
- 🔴 Highlights suspicious traffic in UI  

---

## 🧠 How It Works

1. Captures live network packets  
2. Extracts key information (IP, protocol, port)  
3. Tracks ports accessed per IP  
4. If multiple ports are accessed → triggers alert  
5. Displays everything in a live dashboard  

---

## 🎥 Demo Video

Demo video of the project is uploaded in  [YouTube](https://youtu.be/wfUmvEzUr0U?si=vdICvPUkhPAgQ_g3)



---

## 🛠️ Tech Stack

- Python  
- Scapy  
- Flask  
- SQLite  
- HTML, CSS, JavaScript  

---

## 📁 Project Structure

```

network-sniffer/
│
├── app.py
├── sniffer.py
├── analyzer.py
├── database.py
│
├── templates/
│ └── index.html
│
├── static/
│ └── script.js
│
├── requirements.txt
└── README.md

```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/vrxayush/network-packet-sniffer-ids.git
cd network-sniffer
```

### 2️⃣ Install Dependencies
```
pip install -r requirements.txt
```
### 3️⃣ Install Packet Capture Driver (Windows)
``` 
Install Npcap (required for Scapy)
```
### 4️⃣ Run the Application
```
python app.py
```
### 5️⃣ Open in Browser
```
http://127.0.0.1:5000
```
---
## ⚠️ Important Notes
1. Requires Administrator privileges to capture packets
2. Works best on local machine (cannot be deployed on cloud)
3.  Demo uses simulated traffic for detection

### 📌 Example Detection
```
⚠️ Port Scan Detected: 10.x.x.x
```
---
## 📈 Future Improvements

- 🌍 IP Geolocation mapping
- 📊 Traffic visualization charts
- 🚨 Multiple attack detection (DoS, brute force)
- 🔐 Authentication system
- 🐳 Docker deployment

## 🎯 Use Case

This project demonstrates:

- Network Monitoring
- Packet Analysis
- Intrusion Detection Systems (IDS)
- Cybersecurity fundamentals
---
## 👨‍💻 Author

Ayush Shah  
Computer Science Engineering Student  
Specialization: IoT, Cyber Security, Blockchain
