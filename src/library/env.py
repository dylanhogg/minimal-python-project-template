import os
from dotenv import load_dotenv

load_dotenv()


def get(name, default=None) -> str:
    if os.getenv(name) is None and default is None:
        raise ValueError(f"{name} environment variable is not set.")
    elif os.getenv(name) is None:
        return default
    else:
        return os.environ[name]
