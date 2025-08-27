import datetime

def get_time_based_greeting() -> str:
    """Return a warm and natural greeting depending on the current time of day."""
    hour = datetime.datetime.now().hour

    if 5 <= hour < 8:
        return "🌄 Good early morning! Wishing you a fresh and energetic start."
    elif 8 <= hour < 12:
        return "☀️ Good morning! Hope your day is going well."
    elif 12 <= hour < 15:
        return "🍽️ Good afternoon! Don’t forget to take a lunch break."
    elif 15 <= hour < 18:
        return "🌤️ Good evening! Keep up the great work."
    else:
        return "🌌 It's late night! Take care and get some rest."
