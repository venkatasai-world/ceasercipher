🔐 Caesar Cipher Web App

This is a simple Caesar Cipher encoder/decoder web application built with Python Flask for the backend and HTML/CSS for the frontend. The app allows users to enter a message, choose a shift value, and either encode or decode the message. It also features a clean, responsive design with a background image.

How to Run Locally:

1. Clone the repository:
   git clone https://github.com/your-username/caesar-cipher-web.git
   cd caesar-cipher-web

2. Install dependencies:
   pip install -r requirements.txt

3. Run the app locally (development):
   python app.py

4. Or run in production using Gunicorn:
   gunicorn app:app

Features:

- Caesar cipher encoding and decoding
- Shift selection
- Preserves symbols, numbers, and spaces
- Responsive mobile-friendly layout
- Background image styling
- Works with Flask and Gunicorn

Files Included:

- app.py - Python Flask backend
- templates/index.html - Frontend with embedded HTML and CSS
- requirements.txt - Python package dependencies

Requirements:

- Python 3.x
- Flask
- Gunicorn

Deploy this on platforms like Render, Replit, or locally on your system.

Enjoy using the Caesar Cipher Web App! 🔐
