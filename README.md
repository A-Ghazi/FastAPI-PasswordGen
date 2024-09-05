# Password Generator API

This is a simple Password Generator API built with FastAPI. It allows you to generate a random password of a specified length containing letters, digits, and special characters.

## Features

- Generates a random password of a specified length.
- The password includes uppercase and lowercase letters, digits, and special characters.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/password-generator-api.git
    cd password-generator-api
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install fastapi uvicorn
    ```

## Usage

1. Run the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

    This will start the server at `http://127.0.0.1:8000`.

2. To generate a password, make a GET request to:

    ```
    http://127.0.0.1:8000/generate/{item_length}
    ```

    Replace `{item_length}` with the desired length of the password. For example:

    ```
    http://127.0.0.1:8000/generate/12
    ```

    This will return a JSON response with a randomly generated password of length 12.

## Example

```bash
curl -X 'GET' 'http://127.0.0.1:8000/generate/12' -H 'accept: application/json'

Respone:
{
  "Generated Password": "aB3$dE5&hJ9#"
}
