import nltk
from nltk.chat.util import Chat, reflections

# Download required NLTK data
nltk.download('punkt')

# Define chatbot pairs (pattern, response)
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you today?", "Hi there! What can I do for you?"]
    ],
    [
        r"what is your name?",
        ["I'm a chatbot created using Python and NLTK."]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you!", "Feeling awesome. You?"]
    ],
    [
        r"(.*) your name?",
        ["My name is CodTechBot."]
    ],
    [
        r"(.) help (.)",
        ["Sure, I'm here to help. What do you need assistance with?"]
    ],
    [
        r"quit|exit|bye",
        ["Bye! Have a nice day!", "Goodbye! Take care!"]
    ],
    [
        r"(.*)",
        ["Sorry, I didn’t understand that. Can you please rephrase?"]
    ]
]

# Create chatbot
def codtech_chatbot():
    print("Hi! I'm CodTechBot. Type 'quit' or 'bye' to exit.")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

# Run chatbot
if _name_ == "_main_":
    codtech_chatbot()