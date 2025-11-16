# Products API (FastAPI + SQLModel)

Simple, complete Products CRUD API built with FastAPI and SQLModel (SQLite by default).
This project is ready to run locally and to be pushed to GitHub as a portfolio project.

## Features
- Create, Read, Update, Delete products
- Filtering, pagination (skip/limit) and search by name
- Uses SQLite by default (file `products.db`) — easy to run without extra DB setup
- Auto-generated OpenAPI docs: `/docs` (Swagger UI)

## Quick Start

1. Create virtual env and install:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the server:
```bash
uvicorn app.main:app --reload --port 4000
```

3. Open docs:
```
http://127.0.0.1:4000/docs
```

## Notes
- To use MySQL instead of SQLite, set the environment variable `DATABASE_URL`, e.g.:
  `export DATABASE_URL="mysql+pymysql://user:pass@localhost/dbname"`
- The database file `products.db` is included in `.gitignore` so it won't be pushed to GitHub.

## Project structure
```
products_project/
├─ app/
│  ├─ main.py
│  ├─ database.py
│  ├─ models.py
│  └─ routers/
│     └─ products.py
├─ requirements.txt
├─ README.md
└─ .gitignore
```
