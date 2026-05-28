# Python FastAPI CRUD API

A raw CRUD API project built using Python FastAPI focusing on backend API development and real API communication.

## Features

* GET API
* POST API
* PUT API
* DELETE API
* Dynamic JSON response handling
* Backend API development using FastAPI

## Tech Stack

* Python
* FastAPI
* Uvicorn
* REST API

## API Endpoints

### Get All Users

```text
http://127.0.0.1:8000/hi
```

### Hello Route

```text
http://127.0.0.1:8000/hello
```

### Create User (POST)

```text
http://127.0.0.1:8000/postlist
```

### Get User By ID

```text
http://127.0.0.1:8000/users/{user_id}
```

### Update User (PUT)

```text
http://127.0.0.1:8000/users/{user_id}
```

### Delete User (DELETE)

```text
http://127.0.0.1:8000/users/{user_id}
```

## Learning Outcome

This project helped me understand:

* CRUD operations
* FastAPI fundamentals
* API requests and responses
* Real backend communication
* REST API development using Python

## Author

Hruthik Vardhan

## How to Download this Repository

Clone the repository using:

```bash
git clone https://github.com/Hruthikvardhan/python-fastapi-crud-api.git
```

Or click **Code → Download ZIP** on GitHub.

## How to Run Locally

1. Open project in VS Code or any Python IDE.

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run FastAPI server:

```bash
uvicorn Main:app --reload
```

4. Open browser:

```text
http://127.0.0.1:8000/docs
```

Swagger UI will open automatically for API testing.
