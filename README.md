# Mini DNS Resolver

A simple, full-stack network application built with Python that acts as a local DNS resolver. It uses a background UDP server to resolve domain names to IP addresses and features a clean web interface powered by Flask.

## 🚀 Features
* **UDP Background Server:** Uses Python's native `socket` library to handle UDP network requests and resolve domain names.
* **Web Interface:** A Flask-based frontend that allows users to easily query domain names from their browser.
* **Client-Server Architecture:** Demonstrates core networking concepts by separating the backend service from the frontend client.

## 📂 Project Structure
```text
mini-dns-resolver/
├── server.py              # The background UDP server that resolves IPs
├── app.py                 # The Flask web server acting as the client
├── templates/
│   └── index.html         # The HTML interface for the web app
└── .gitignore             # Git ignore file (excludes env/)
