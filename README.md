# FastAPI Backend System - Item & User Management

A scalable backend REST API built using FastAPI and MongoDB Atlas to manage items and user clock-in records with support for filtering, aggregation, and real-time data operations.

## 🚀 Features
- Full CRUD operations for Items and User Clock-In Records  
- Advanced filtering based on Email, Date, Quantity, and Location  
- MongoDB aggregation for analytics (grouping and counting data)  
- RESTful API design following best practices  
- Automatic API documentation using Swagger (FastAPI)  

## 🛠 Tech Stack
- Python  
- FastAPI  
- MongoDB Atlas  
- Pydantic  
- Uvicorn  

## 📂 Project Structure
- Routes → API endpoints  
- Models → Data validation schemas  
- Database → MongoDB connection and queries  

## ⚙️ Setup Instructions

### Clone the Repository
git clone https://github.com/anujmehta29/fastapi-assignment.git  
cd fastapi-assignment  

### Create Virtual Environment
python -m venv venv  

### Activate Environment
Windows:
venv\Scripts\activate  

Linux / Mac:
source venv/bin/activate  

### Install Dependencies
pip install -r requirements.txt  

### Configure Environment Variables
Create a `.env` file and add:
MONGODB_URI=<your-mongodb-connection-string>  

## ▶️ Run the Application
uvicorn main:app --reload  

## 📌 API Endpoints

### Items APIs
- GET /api/items → Retrieve all items  
- POST /api/items → Create a new item  
- PUT /api/items/{id} → Update an item  
- DELETE /api/items/{id} → Delete an item  

### User Clock-In APIs
- GET /api/clockins → Retrieve all records  
- POST /api/clockins → Create a record  
- PUT /api/clockins/{id} → Update a record  
- DELETE /api/clockins/{id} → Delete a record  

## 📸 API Documentation
Swagger UI available at:
http://127.0.0.1:8000/docs  

## 🔧 Future Improvements
- Add authentication (JWT-based security)  
- Dockerize the application  
- Deploy on cloud (AWS / GCP)  

## 📎 Repository Link
https://github.com/anujmehta29/fastapi-assignment
