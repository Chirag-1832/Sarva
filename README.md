#  KPA Forms API (Wheel Specifications)

A FastAPI backend to submit and retrieve wheel specification forms, connected to PostgreSQL and documented with Swagger.

---

##  Tech Stack

- **FastAPI** – Web framework  
- **SQLAlchemy** – ORM  
- **PostgreSQL** – Database  
- **Pydantic** – Data validation  
- **Uvicorn** – ASGI server  

---

## ⚙️ Setup Instructions

### 1. Install dependencies  
Install Python packages using  
pip install -r requirements.txt

### 2. Install PostgreSQL  
Download and install PostgreSQL from the official website:  
https://www.postgresql.org/download/  
(Mac users can also use: brew install postgresql)

### 3. Create PostgreSQL Database and User  
Login to psql and run the following:

- CREATE DATABASE kpa_db;
- CREATE USER kpa_user WITH PASSWORD 'your_password';
- GRANT ALL PRIVILEGES ON DATABASE kpa_db TO kpa_user;

### 4. Create a .env file  
In the project root directory, create a `.env` file with:

DATABASE_URL=postgresql://kpa_user:your_password@localhost/kpa_db

### 5. Run the application  
Start the FastAPI app using:  
uvicorn app.main:app --reload

Swagger UI will be available at:  
http://127.0.0.1:8000/docs

---

##  API Endpoints

###  POST /api/forms/wheel-specifications  
Submit a new wheel specification form.

- **Request Body:**
  - formNumber (string)
  - submittedBy (string)
  - submittedDate (string, format YYYY-MM-DD)
  - fields (object containing all wheel specification fields)

- **Response:**  
  - success: true  
  - message: "Wheel specification submitted successfully"  
  - data: Form summary

- **Error:**  
  - 400 Bad Request if formNumber already exists

---

###  GET /api/forms/wheel-specifications  
Retrieve a list of submitted forms.

- **Optional Query Parameters:**
  - formNumber
  - submittedBy
  - submittedDate

- **Response:**  
  - success: true  
  - message: "Filtered wheel specification forms fetched successfully"  
  - data: List of form summaries

---

##  Postman Collection

A Postman collection is included in the repo as `KPA_form_data.postman_collection.json`.  
You can import it into Postman and test all the API routes easily.

---

##  Limitations & Assumptions

- No authentication or user validation implemented  
- PostgreSQL must be pre-installed and running locally  
- Assumes .env is configured properly with DB credentials  
- Swagger UI available only in development (--reload mode)

---

##  Author

Built by **Master Oogway** 🐢  
GitHub: [https://github.com/Chirag-1832](https://github.com/Chirag-1832)
