import os
import typer
from library import log
from dotenv import load_dotenv
from loguru import logger

load_dotenv()


def main(required_arg: str, optional_arg: str = None):
    token = os.getenv("EXAMPLE_TOKEN")
    logger.debug(f"Hello! required_arg = {required_arg}, optional_arg = {optional_arg}")
    logger.debug(f"PYTHONPATH = {os.getenv('PYTHONPATH', 'Not set')}")
    logger.info(f"LOG_STDERR_LEVEL = {os.getenv('LOG_STDERR_LEVEL', 'Not set. Copy `.env_template` to `.env`')}")
    logger.info(f"LOG_FILE_LEVEL = {os.getenv('LOG_FILE_LEVEL', 'Not set. Copy `.env_template` to `.env`')}")


if __name__ == "__main__":
    log.configure()
    typer.run(main)
