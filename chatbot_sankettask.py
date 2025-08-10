import random
def quirky_chatbot(): """A quirky chatbot with personality."""
greetings = ["Hey there!", "Yo, what’s up?", "Salutations, human!"] 
farewells = ["Ciao!", "Stay cool!", "May your code compile on the first try!"] 
compliments = ["That's a nice name!", "I dig your vibe already.", "You're giving 'cool' a whole new dimension."]



print(random.choice(greetings))

name = input("What's your name? ")
print(f"{random.choice(compliments)} 😎")
print(f"Nice to meet you, {name}!")

mood = input("How are you feeling today? ")
if "good" in mood.lower() or "great" in mood.lower():
    print("Awesome! Keep riding that wave 🌊")
elif "bad" in mood.lower() or "sad" in mood.lower():
    print("Ah, digital hugs incoming 🤖❤️")
else:
    print("Mysterious mood detected. Intriguing...")

print(random.choice(farewells))