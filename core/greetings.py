import datetime

def get_time_based_greeting():
    """Return greeting depending on current time."""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        return "Good morning!"
    elif 12 <= hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"