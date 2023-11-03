import random

def tell_a_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't some fish play piano? Because you can't tuna fish!",
        "Why did the bicycle fall over? Because it was two-tired!"
    ]
    return random.choice(jokes)

print(tell_a_joke());