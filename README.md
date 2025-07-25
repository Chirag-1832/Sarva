#  KPA Forms API (Wheel Specifications)

A FastAPI backend to submit and retrieve wheel specification forms, connected to a PostgreSQL database and documented using Swagger UI.

---

##  Tech Stack

- **FastAPI** – High-performance Python web framework  
- **SQLAlchemy** – ORM for database interaction  
- **PostgreSQL** – Relational database  
- **Pydantic** – Data validation  
- **Uvicorn** – ASGI server  

---

##  Features

- Submit new wheel specification forms  
- Retrieve forms filtered by:
  - `formNumber`
  - `submittedBy`
  - `submittedDate`  
- Swagger UI for API testing  
- PostgreSQL integration using SQLAlchemy ORM  

---

## ⚙️ Getting Started

###  Prerequisites

Make sure the following are installed:

- Python 3.9 or higher  
- PostgreSQL  

To install PostgreSQL:

- [Download for Windows/Linux/macOS](https://www.postgresql.org/download/)  
- For macOS using Homebrew: brew install postgresql

### Clone the Repository

git clone https://github.com/Chirag-1832/Sarva.git
cd Sarva/kpa_backend

### Install the Dependencies
 - pip install -r requirements.txt

### Set Up PostgreSQL

### Create a .env File

### Run the Server
- uvicorn app.main:app --reload

### API Documentation
- http://127.0.0.1:8000/docs

### Author

Master Oogway






