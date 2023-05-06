from datetime import datetime


def current_timestamp() -> int:
    return int(datetime.now().timestamp())