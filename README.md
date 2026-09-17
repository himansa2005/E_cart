# Flask E-Commerce Shopping Cart Application

A lightweight, interactive web application featuring an object-oriented shopping cart system built with Python and Flask. This project showcases core object-oriented programming (OOP) principles integrated into a full-stack web application structure.

---

## 📌 Project Overview

This application manages e-commerce cart operations including adding items, applying discount codes, dynamic subtotal calculations, and tax computations. 

* **Backend Engine**: Built on custom Python OOP logic (`ShoppingCart` class) handling validation, discounting, and total calculations.
* **Web Interface**: Rendered through a responsive Flask application (`app.py`) with dynamic HTML templates and CSS styling.

---

## 🛠️ Tech Stack & Concepts

* **Language**: Python 3
* **Framework**: Flask
* **Core Concepts**: Object-Oriented Programming (OOP), Static Methods, Encapsulation, REST API Routes
* **Frontend**: HTML5, CSS3, JavaScript / Jinja2 Templates
* **Tooling**: VS Code AI Agents (for Web App scaffolding and UI generation)

---

## 💡 AI Assistance & Transparency

In alignment with modern AI-assisted development workflows:
* **Core Logic (`E CART.py`)**: Designed and implemented independently using custom OOP Python principles.
* **Web App Architecture (`app.py`, `templates/`, `static/`)**: Scaffolding, Flask route configurations, UI templates, and frontend styling were built using **VS Code AI Agents**.
* **Integration**: Custom backend logic was integrated into the AI-generated web interface to form a complete full-stack web application.

---

## 📂 Project Structure

```text
.
├── static/              # Static assets (CSS styles, JS, images)
├── templates/           # Flask HTML templates (Jinja2)
├── app.py               # Flask application entry point & routes
├── E CART.py            # Core ShoppingCart OOP Python class logic
├── README.md            # Project documentation
└── requirements.txt     # Python dependency list
```

---

## 🚀 Key Features

* **Dynamic Price & Quantity Validation**: Ensures non-zero inputs and minimum quantities.
* **Automatic Item Grouping**: Incrementally merges duplicate items added to the cart.
* **Discount Code System**: Supports promotional coupon calculation during checkout.
* **Tax Rate Calculation**: Computes configurable tax rates automatically on discounted subtotals.

---

## ⚙️ Setup & Local Execution

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
   cd YOUR_REPOSITORY_NAME
   ```

2. **Create & activate a virtual environment (optional):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application:**
   ```bash
   python app.py
   ```

5. **Access in browser:**
   Open `http://127.0.0.1:5000` in your web browser.
