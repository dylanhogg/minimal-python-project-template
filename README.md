# minimal-python-project-template

A minimal quick-start Python project template, using [uv](https://github.com/astral-sh/uv) package manager.

Uses the following 3rd party libraries:

- APP - https://github.com/tiangolo/typer - For building CLI applications
- APP - https://github.com/Delgan/loguru - Python logging made (stupidly) simple
- APP - https://github.com/theskumar/python-dotenv - Reads key-value pairs from a .env file and can set them as environment variables.
- APP - https://github.com/pydantic/pydantic - Data validation and settings management using Python type annotations
- DEV - https://github.com/astral-sh/uv - An extremely fast Python package and project manager
- DEV - https://github.com/psf/black - The uncompromising Python code formatter
- DEV - https://github.com/pytest-dev/pytest - makes it easy to write small tests, yet scales to support complex functional testing

See Makefile for quick utility commands for creation of venv, running the app, running tests etc.

Includes mdc cursorrule files in `.cursor/rules`as per https://docs.cursor.com/context/rules
