import datetime

def get_time_based_greeting() -> str:
    """Return a more natural greeting depending on the current time of day."""
    hour = datetime.datetime.now().hour

    if 5 <= hour < 12:
        return "🌅 Good morning!"
    elif 12 <= hour < 15:
        return "☀️ Good afternoon!"
    elif 15 <= hour < 18:
        return "🌤️ Good evening!"
    elif 18 <= hour < 22:
        return "🌙 Good night!"
    else:
        return "🛌 It's late, hope you're doing well!"
