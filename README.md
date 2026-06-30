# mini-dns-lookup

A simple Python network application that acts as a local DNS resolver. It uses a background UDP server to resolve domain names to IP addresses and features a Flask web interface.

## Features

- UDP background server powered by Python's `socket` library.
- Flask web interface for querying domain names from a browser.
- Client-server architecture split between the frontend and resolver backend.

## Project Structure

```text
mini-dns-lookup/
├── project01/
│   ├── app.py
│   ├── server.py
│   ├── .gitignore
│   └── templates/
│       └── index.html
└── README.md
```
