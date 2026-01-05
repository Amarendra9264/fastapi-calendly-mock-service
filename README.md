# fastapi-calendly-mock-service
Mock Calendly-style scheduling API for a medical clinic, built using FastAPI. Supports availability lookup, slot booking, appointment-type durations, and no-availability handling.
 
# FastAPI Calendly Mock Service

This project is a mock implementation of Calendly API endpoints using FastAPI. It is designed for testing and development purposes, simulating the behavior of the real Calendly API.

## Project Structure

```
app/
  main.py                # FastAPI application entry point
  api/
	 endpoints/
		calendly_intgration_api.py  # Calendly API mock endpoints
```

## Features
- Mock endpoints for Calendly integration
- Easy to extend and customize
- FastAPI-based for high performance and easy testing

## Getting Started


## Prerequisites
- Python 3.8 or higher
- Poetry (Python package manager)

## Installation Steps

1. Install Poetry (if not already installed)
	```bash
	curl -sSL https://install.python-poetry.org | python3 -
	```

2. Clone the repository
	```bash
	git clone <repo-url>
	cd fastapi-calendly-mock-service
	```

3. Install dependencies using Poetry
	```bash
	poetry install
	```

4. (Optional) Create a `.env` file in the root directory with any required environment variables.

## Running the Application

1. Activate the Poetry virtual environment
	```bash
	poetry shell
	```

2. Run the FastAPI application using Uvicorn
	```bash
	# For development
	poetry run uvicorn app.main:app --reload --port 8000

	# For production
	poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --loop asyncio
	```

3. Access the API documentation
	- Swagger UI: http://localhost:8000/api/docs


## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements.

## License

This project is licensed under the MIT License.
