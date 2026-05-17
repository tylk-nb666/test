"""Small greeting utilities for the test project."""

from datetime import datetime, timezone


def build_greeting(name: str = "world") -> str:
    """Return a friendly greeting for the provided name."""
    clean_name = name.strip() or "world"
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return f"Hello, {clean_name}! Generated at {timestamp}."


if __name__ == "__main__":
    print(build_greeting())
