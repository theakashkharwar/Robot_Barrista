# ☕ Robot Barista (Python CLI Project)

A simple command-line based **Robot Barista** program built in Python that simulates a coffee shop experience.
The program interacts with the user, evaluates their "character", prioritizes customers, and processes drink orders.

---

## 🚀 Features

### 👤 Customer Interaction

* Takes user's name as input
* Special checks for certain users (Ben, Patricia, Loki)
* Evaluates:

  * Whether the user is "evil"
  * Number of good deeds performed

### 🧔 Priority System

* Asks if the user has a beard
* Gives **priority access** if beard length > 1 inch

### ☕ Menu System

Available drinks:

* Coffee
* Latte (with optional whipped cream)
* Chai
* Venti
* Frappuccino

### 💰 Pricing Logic

* Dynamic pricing based on:

  * Selected drink
  * Add-ons (e.g., whipped cream)
  * Number of cups ordered

---

## 🧠 Concepts Used

This project demonstrates basic Python programming concepts:

* Variables
* Conditional statements (`if`, `elif`, `else`)
* Nested conditions
* User input handling (`input()`)
* Type casting (`int()`)
* String concatenation
* Basic program flow control (`exit()`)

---

## ▶️ How to Run

1. Make sure Python is installed (Python 3.x recommended)
2. Save the file as `robot_barista.py`
3. Run the program:

```bash
python robot_barista.py
```

---

## 💡 Example Flow

1. User enters name
2. System checks if user is special (Ben, Patricia, Loki)
3. Evaluates morality (evil + good deeds)
4. Checks beard priority
5. Displays menu
6. Takes order and quantity
7. Calculates total bill

---

## ⚠️ Known Issues / Limitations

* Case-sensitive inputs (e.g., "Yes" vs "yes")
* Typo in menu vs condition:

  * `"Frappuccino"` vs `"Frappacino"` (will cause mismatch)
* No input validation for incorrect values
* Currency symbol printed incorrectly (`q` instead of ₹ or $)
* No loop (program runs only once per execution)

---

## 🔧 Possible Improvements

* Make input case-insensitive
* Fix spelling inconsistencies
* Add loops for multiple customers
* Improve UI formatting
* Add error handling for invalid inputs
* Use functions for modular design
* Store menu in a dictionary for scalability

---

## 🎯 Learning Purpose

This project is ideal for beginners who want to:

* Practice Python basics
* Understand decision-making logic
* Build interactive CLI programs

---

## 📌 Final Thought

This is a **foundation-level project** — simple, but important.
If you’re serious about becoming a strong developer (or even a hacker), mastering this level of logic control is non-negotiable.

Build small → understand deeply → then scale.

---
