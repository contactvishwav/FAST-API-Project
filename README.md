# FAST-API-Project

A **FastAPI**-based user management system that allows for creating, reading, updating, and deleting users. The project uses **UUIDs** to identify users and provides role-based user attributes. This API is a lightweight solution to manage a simple in-memory user database with structured models and error handling.

## Features

- **GET** all users  
- **POST** to register a new user  
- **DELETE** a user by ID  
- **PUT** to update user information  
- Supports **role-based** user management  
- **In-memory** storage for simplicity (data is lost on restart)

## Requirements

- **Python 3.8+**
- **FastAPI**  
- **Pydantic**

Install the dependencies using:
pip install fastapi pydantic uvicorn

1. Clone the repository and navigate into the project folder
2. Run the FastAPI server using the following command: uvicorn main:app --reload
3. Access the API Documentation: http://127.0.0.1:8000/docs or http://127.0.0.1:8000/redoc
