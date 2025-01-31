# FastAPI API Development with JSON Handling and Versioning

## Overview

This repository contains an API developed using FastAPI. The API provides endpoints for managing a To-Do List, including versioning, authentication, and HTTP exception handling. The implementation follows best practices in API development, including environment variable management.

## Features

- Developed using FastAPI.
- Implements API versioning (`apiv1` and `apiv2`).
- Parses JSON strings and traverses nested data.
- Implements authentication via API key stored in an `.env` file.
- Implements proper HTTP exception handling.
- Provides Swagger UI for API testing.

## Installation

To set up and run this FastAPI application, follow these steps:

### Prerequisites

- Python 3.8 or later
- pip (Python package installer)

### Steps

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository/lab4
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   .venv\Scripts\activate     # On Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the project root (DO NOT COMMIT THIS FILE) and add:
   ```sh
   LAB4_API_KEY=my_api_key
   ```
5. Add `.env` to `.gitignore` to prevent committing sensitive information.

## Running the Application

1. Start the FastAPI server:
   ```sh
   uvicorn main:app --reload
   ```
2. Open your browser or use a tool like Postman to test the API at:
   ```
   http://127.0.0.1:8000
   ```

## API Endpoints

### Version 1 (`apiv1`)

- `GET /tasks/{task_id}` - Retrieve a specific task.
- `POST /tasks` - Add a new task.
- `PATCH /tasks/{task_id}` - Update a task.
- `DELETE /tasks/{task_id}` - Delete a task.

### Version 2 (`apiv2`)

- Includes all `apiv1` functionalities with enhanced HTTP exception handling and authentication.

#### HTTP Status Codes

- `201` - Task successfully added.
- `204` - Task updated, deleted, or no tasks available.
- `404` - Task not found.
- `200` - Default status for other cases.

## Dependencies

This project requires the following dependencies, listed in `requirements.txt`:

- FastAPI
- Uvicorn
- Python-dotenv

## Testing

You can test the API using the built-in Swagger UI provided by FastAPI:

- Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.
- Try the endpoints under `apiv1` and `apiv2`.

## Required Output

- Updated `main.py` file containing the API code.
- `requirements.txt` file listing dependencies.
- `.gitignore` file excluding `.env`.
- Screenshot of Swagger UI.

## Author

[Guiller Neri] - [Y](https://github.com/yourusername)[our GitHub Profile](https://github.com/yourusername)

## Repository Link

[GitHub Repository](https://github.com/yourusername/your-repository)

[https://github.com/neri-Guiller09/lab4](https://github.com/neri-Guiller09/lab4)
