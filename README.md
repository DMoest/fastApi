# FastAPI application backend

This is a FastAPI application backend that serves as a backend for a simple web
application. The application is a simple CRUD application that allows users to
create, read, update, and delete items.

## Cloning the repository

First, clone the repository:

1. Open a terminal
2. Navigate to the directory where you want to clone the repository
3. Clone the repository by running the following command:

```bash
$ git clone https://github.com/DMoest/fastApi.git
$ cd fastApi
```

### Environment & Dependencies

This project uses [Poetry](https://python-poetry.org/) for dependency
management originally but its possible to use other ways to manage your
dependencies if you rather prefer a specific way. However those ways are not
covered in this README. To use a different way you are required to do
some extra work on your own and I recommend you to check the `pyproject.
toml` for the dependencies required by the project.

1. Make sure you have Poetry dependency manager installed on your system. If
   you don't have it installed, you can check how to install it here:
   `https://python-poetry.org/`
2. Create a virtual environment for the project and activate it:
   ```bash
   $ poetry shell
   ```
3. Install the project dependencies into your virtual environment
   ```bash 
   $ poetry install
   ```
4. Create a `.env` file in the root of the project. Be sure to check out
   the `.env.example` file for the required environment variables. Among
   these variables are the database configuration credentials and more that
   the application requires and you need to configure these separately.
5. Now, if you configured your `.env` file correctly, you can run the
   application with the following command:
   ```bash
   $ poetry run uvicorn main:app --reload --port 
   <PORT_OF_YOUR_CHOICE>
   ```

### Working with the API

FastAPI provides a built-in interactive API documentation that you can use to
test the API endpoints. To access the API documentation, open your browser and
navigate to `http://localhost:<PORT_OF_YOUR_CHOICE>/docs`. You can use the
interactive API documentation to test the API endpoints.

### Running the tests
