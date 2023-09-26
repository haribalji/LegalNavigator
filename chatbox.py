import random

responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm just a computer program,I'm here to help!", "I'm doing well, thanks for asking!"],
    "what is your name?":["My name is Rin"],
    "what is legal rights?":["A legal right is an interest accepted and protected by law. Also, any debasement of any legal right is punishable by law. Legal rights affect every citizen. Legal rights are equally available to all the citizens without the discrimination of caste, creed & sex"],
    "what is the main objective of this legal navigation website?":["To guide the ignorant people to know about the legal rights"],
    "what are my rights as a citizen?":["Right to freedom of speech and expression, assembly, association or union, movement, residence, and right to practice any profession or occupation"],
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
