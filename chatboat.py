from nltk.tokenize import word_tokenize

# Simple responses dictionary
responses = {
    "hello": "Hi there! How can I help you today?",
    "how are you": "I'm a chatbot, I don't have feelings, but thanks for asking!",
    "bye": "Goodbye! Have a great day!"
}

def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        tokens = word_tokenize(user_input)
        found = False
        for key in responses:
            if key in user_input:
                print("Chatbot:", responses[key])
                found = True
                break
        if not found:
            print("Chatbot: Sorry, I don't understand that.")
        if "bye" in user_input:
            break

chatbot()