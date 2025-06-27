# Simple Task Management API

This project is an implementation of a simple RESTful API for managing tasks, built with Python and FastAPI. It serves as a practical demonstration of core backend principles including RESTful design, input validation, error handling, and basic security.

## Features

- Create a new task.
- Retrieve a list of all tasks.
- Retrieve a specific task by its ID.
- Basic Authentication (HTTP Basic Auth).
- CORS enabled for easy development.
- Automatic API documentation via Swagger UI

### Instructions

**Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
**Create a .env file**
    USERNAME = "your preferred username"
    PASSWORD = "your preferred password"

**Run the application:**
    ```bash
    uvicorn main:app --reload
    ```
    The API will be available at `http://127.0.0.1:8000`

## API Documentation & Usage

The API is protected by Basic Authentication. Use the following credentials:
- **Username:** `[hardcode yours in your .env file]`
- **Password:** `[hardcode yours in your .env file]`

You can explore and test the API endpoints interactively using the auto-generated documentation:
- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)


### Example `curl` Commands

#### 1. Create a New Task (POST /tasks)
```bash
curl -X POST "http://127.0.0.1:8000/tasks" \
-u "username:password" \
-H "Content-Type: application/json" \
-d '{
  "title": "Learn FastAPI",
  "description": "Read the official documentation and build a project."
}'
```

#### 2. Get All Tasks (GET /tasks)
```bash
curl -X GET "http://127.0.0.1:8000/tasks" \
-u "username:password"
```

#### 3. Get a Specific Task (GET /tasks/{id})
*First, create a task and copy its `id` from the response.*
```bash
# Replace {your_task_id} with an actual ID
curl -X GET "http://127.0.0.1:8000/tasks/{your_task_id}" \
-u "username:password"
```

## Design Choices
- **Framework**: **FastAPI** was chosen for its high performance, built-in data validation with Pydantic, and automatic OpenAPI documentation, which perfectly align with the task requirements.

- **Unique ID Generation**: **`uuid.uuid4()`** is used to generate unique, random IDs on the server-side, ensuring that clients don't need to provide them