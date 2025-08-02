# 📚 Bookstore Test Automation Framework

A clean and modular test automation framework built in Python, designed for validating core functionality of a sample bookstore system. This project showcases best practices in SDET work — from API testing to custom utilities and HTML reporting.

---

## 🔧 Technologies Used
- Python 3.12
- PyTest
- `requests` (API testing)
- PyTest Fixtures & Parametrize
- JSON File I/O
- HTML Reporting (`pytest-html`)

---

## ✅ Features
- Unit tests for utility functions (e.g., discount calculation, price filtering)
- API tests using live endpoints and status code validation
- Parameterized test cases
- Test fixtures for reusable book data
- Custom test report: `report.html`
- Organized directory structure

---

## 📁 Project Structure

```
bookstore_sdet_framework/
├── book.py
├── book_utils.py
├── conftest.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   └── books.json
└── tests/
    ├── __init__.py
    ├── test_book_utils.py
    └── test_api_sample.py
```

---

## 🚀 How to Run Tests

1️⃣ Create a virtual environment:
```bash
python -m venv .venv
.\.venv\Scripts ctivate
```

2️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

3️⃣ Run the test suite:
```bash
pytest
```

4️⃣ Generate an HTML test report:
```bash
$env:PYTHONPATH="." ; pytest --html=report.html
```

The report will be saved as `report.html`.

---

## 👩‍💻 Author

**Fara Khalili**  
Experienced developer/SDET, real-world test automation projects.

---

✅ _This project is part of my professional SDET portfolio._