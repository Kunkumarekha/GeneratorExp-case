# 🔄 Generator Expression Case – FastAPI

A simple **FastAPI project** created to understand and practice **Generator Expressions** in Python.

This project uses a supermarket inventory example to demonstrate how a generator expression can be used inside a FastAPI endpoint to generate inventory records.


## 📌 Project Overview

The application manages supermarket inventory using three Python lists:

* 🛒 Item names
* 💰 Item prices
* 📦 Item stock quantities

The `/items` endpoint uses a **Generator Expression** to create inventory dictionaries one at a time.

## 🛠️ Technologies Used

* Python
* FastAPI
* Uvicorn
* Generator Expressions
* Python Lists
* `range()`
* REST API

## 📂 Project Structure

```text
GeneratorExp-case/
│
├── main.py
└── README.md

## 📋 Sample Data

The application starts with the following inventory:

```python
items = ["Rice", "Toor Dal", "Sugar", "Cooking Oil", "Biscuits"]

prices = [60.0, 120.0, 55.0, 150.0, 30.0]

stock = [50, 30, 40, 25, 60]

# 🔄 Generator Expression

The main purpose of this project is to practice a **Generator Expression**.

### Code

```python
result = (
    {
        "item": items[i],
        "price": prices[i],
        "stock": stock[i]
    }
    for i in range(len(items))
)
```

The general syntax of a generator expression is:

```python
(expression for item in iterable)
```

In this project:

```text
Expression → Dictionary containing item, price and stock

Variable → i

Iterable → range(len(items))

## 💡 Why Use a Generator Expression?

A generator expression produces values **one at a time** instead of creating all values immediately.

For example:

```python
result = (
    {
        "item": items[i],
        "price": prices[i],
        "stock": stock[i]
    }
    for i in range(len(items))
)

The generator produces:

```text
1 → Rice
2 → Toor Dal
3 → Sugar
4 → Cooking Oil
5 → Biscuits
```

Only when the values are requested.

## 🔢 Converting Generator to List

FastAPI needs to return the inventory data as JSON.

Therefore, the generator is converted into a list:

```python
return list(result)
```

The complete endpoint is:

```python
@app.get("/items")
def display_items():

    result = (
        {
            "item": items[i],
            "price": prices[i],
            "stock": stock[i]
        }
        for i in range(len(items))
    )

    return list(result)


# 🔍 API Endpoint

### Get All Items

```http
GET /items
```

### Example URL

```text
http://127.0.0.1:8000/items
```

### Example Response

```json
[
    {
        "item": "Rice",
        "price": 60.0,
        "stock": 50
    },
    {
        "item": "Toor Dal",
        "price": 120.0,
        "stock": 30
    },
    {
        "item": "Sugar",
        "price": 55.0,
        "stock": 40
    },
    {
        "item": "Cooking Oil",
        "price": 150.0,
        "stock": 25
    },
    {
        "item": "Biscuits",
        "price": 30.0,
        "stock": 60
    }
]


# ⚙️ How to Run

### 1. Install FastAPI

```bash
pip install fastapi
```

### 2. Install Uvicorn

```bash
pip install uvicorn
```

Or:

```bash
pip install fastapi uvicorn
```

### 3. Run the application

From the `GeneratorExp-case` directory:

```bash
uvicorn main:app --reload
```

The API will start at:

```text
http://127.0.0.1:8000
```

# 📖 Swagger API Documentation

FastAPI automatically provides interactive documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You can test the `/items` endpoint directly from Swagger UI.

# 🧠 Generator Expression vs List

### List Comprehension

```python
result = [
    {
        "item": items[i],
        "price": prices[i],
        "stock": stock[i]
    }
    for i in range(len(items))
]
```

Creates the complete list immediately.

### Generator Expression

```python
result = (
    {
        "item": items[i],
        "price": prices[i],
        "stock": stock[i]
    }
    for i in range(len(items))
)
```

Produces values one at a time.

### Main Difference

| List Comprehension                | Generator Expression             |
| --------------------------------- | -------------------------------- |
| Uses `[]`                         | Uses `()`                        |
| Creates a list immediately        | Produces values lazily           |
| Stores all results in memory      | Produces one value at a time     |
| Can be accessed multiple times    | Generator is consumed once       |
| Useful when all values are needed | Useful for sequential processing |

---

# 📚 Concepts Practiced

This project helped me practice:

* Python Generator Expressions
* Lazy evaluation
* Python lists
* List indexing
* `range()`
* `len()`
* Dictionary creation
* Functions
* FastAPI
* REST API basics
* GET requests
* JSON responses
* Swagger UI
* Uvicorn

---

# 🎯 Learning Objective

The objective of this project is to understand how **Generator Expressions work in Python** and how they can be used in a practical **FastAPI application**.

This is a learning project focused on understanding the difference between **normal loops, list comprehensions, and generator expressions**.



## 👩‍💻 Author

**Udayana Kunkuma Rekha**

Learning and practicing:

**Python → FastAPI → SQL → Backend Development**

---

⭐ If you found this project useful, consider giving the repository a star!
