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
