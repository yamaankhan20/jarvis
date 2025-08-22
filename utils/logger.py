def log(message: str):
    """Log Jarvis events for debugging."""
    with open("jarvis.log", "a") as f:
        f.write(message + "\n")
