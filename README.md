# anujpythonAssessment

# FastAPI Project for Vodex.ai Assignment

## Overview
This project implements a FastAPI application that performs CRUD (Create, Read, Update, Delete) operations for two entities: **Items** and **User Clock-In Records**. The application uses MongoDB Atlas for data storage and provides a RESTful API to manage these entities.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Testing the APIs](#testing-the-apis)
- [Hosted Documentation](#hosted-documentation)
- [Contributing](#contributing)
- [License](#license)

## Features
- CRUD operations for Items:
  - Create, read, update, and delete items.
  - Filter items based on various criteria (Email, Expiry Date, Insert Date, Quantity).
  - MongoDB aggregation to count items grouped by email.
- CRUD operations for User Clock-In Records:
  - Create, read, update, and delete clock-in records.
  - Filter clock-in records based on Email, Location, and Insert DateTime.
- Automatic Swagger documentation generation for the API.

## Requirements
- Python 3.7 or higher
- MongoDB Atlas account
- Dependencies:
  - FastAPI
  - Uvicorn
  - Pydantic
  - pymongo
  - python-dotenv (for environment variable management)

## Setup

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/anujmehta29/fastapi-assignment.git
cd fastapi-assignment


### 2. Create a Virtual Environment
    Create a virtual environment to manage dependencies:
    python3 -m venv venv
    Activate the virtual environment:

    For Windows:
    venv\Scripts\activate

    For Linux/Mac:
    source venv/bin/activate


3. Install Dependencies
    Install the required dependencies using pip:

      pip install -r requirements.txt
      If the requirements.txt file is not created yet, you can generate it using:

      pip freeze > requirements.txt


4. Set Up Environment Variables
    Create a .env file in the project root directory to store your environment variables:

    MONGODB_URI=mongodb+srv://anuj2903:Itsanuj2903@fastapi-assignment.albn8.mongodb.net/FastAPI-Assignment?retryWrites=true&w=majority&appName=FastAPI-Assignment


5. MongoDB Atlas Configuration
    Ensure that your IP address is whitelisted in the MongoDB Atlas dashboard under the Network Access section. You can also allow access from anywhere by adding 0.0.0.0/0, but this is not recommended for production due to security risks.


## Running the Application
    Run the application using Uvicorn:
    uvicorn main:app --reload
    Replace main with the name of your main application file if different.



API Endpoints
    GET /api/items: Retrieve all items
    POST /api/items: Create a new item
    PUT /api/items/{item_id}: Update an existing item
    DELETE /api/items/{item_id}: Delete an item

Testing the APIs
You can test the APIs using tools like Postman or through the automatically generated Swagger documentation available at http://127.0.0.1:8000/docs.

Hosted Documentation
Swagger UI is automatically available at /docs for API documentation.

License:
  No license specified.
