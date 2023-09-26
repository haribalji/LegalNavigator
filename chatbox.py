import random

responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm just a computer program,I'm here to help!", "I'm doing well, thanks for asking!"],
    "what is your name?":["My name is Rin"],
    "bye": ["Goodbye!", "See you later!", "Have a great day!"],
    "default": ["I'm not sure what you mean.", "Could you please rephrase that?", "I didn't understand."]
}

def response(userinput):
    userinput = userinput.lower()
    
    
    for key in responses:
        if key in userinput:
            return random.choice(responses[key])
    
    
    return random.choice(responses["default"])

print("Chatbox: Hello!")
while True:
    userinput = input("You: ")
    if userinput.lower() == "bye":
        print("Chatbox: Goodbye!")
        break
    respond=response(userinput)
    print("Chatbox:", respond)
