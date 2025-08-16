
print("🤖 Bot: Hi there! I'm SmartBot. What's your name?")

# Memory feature: store user name
user_name = input("👤 You: ").strip().capitalize()
print(f"🤖 Bot: Nice to meet you, {user_name}! Type 'exit' to quit anytime.\n")

while True:
    user_input = input(f"👤 {user_name}: ").lower().strip()

    # Exit condition
    if "exit" in user_input or "bye" in user_input:
        print(f"🤖 Bot: Goodbye {user_name}! Stay positive ✨")
        break

    # Greetings
    elif any(word in user_input for word in ["hello", "hi", "hey"]):
        print(f"🤖 Bot: Hey {user_name}! How’s your day going?")

    # Asking about mood
    elif "how are you" in user_input:
        print("🤖 Bot: I’m running on electricity ⚡ and good vibes! How about you?")
    elif "good" in user_input or "fine" in user_input or "great" in user_input:
        print(f"🤖 Bot: Awesome, {user_name}! Keep it up! 😃")
    elif "sad" in user_input or "bad" in user_input or "not good" in user_input:
        print(f"🤖 Bot: Oh no {user_name}, remember: tough times don’t last, tough people do 💪")

    # Asking bot's identity
    elif "who are you" in user_input or "your name" in user_input:
        print("🤖 Bot: I’m SmartBot, a rule-based chatbot built with Python 🐍")

    # Joke feature
    elif "joke" in user_input:
        print("🤖 Bot: Why did the computer go to the doctor? Because it caught a virus 🤒😂")

    # Fake weather feature
    elif "weather" in user_input:
        print("🤖 Bot: I can’t check real weather yet, but I bet it’s a good day to smile ☀️")

    # Time-related response
    elif "time" in user_input:
        print("🤖 Bot: I don’t have a clock yet ⏰, but it’s always the right time to learn something new!")

    # Help menu
    elif "help" in user_input:
        print("🤖 Bot: You can ask me about jokes, weather, time, how I’m doing, or just say hi!")

    # Catch-all fallback
    else:
        print("🤖 Bot: Interesting... tell me more! 🤔")
