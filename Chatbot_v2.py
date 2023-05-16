from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chatbot
bot = ChatBot('My Chatbot')

# Create a list of responses that the chatbot can use
responses = [
    "Hello, how are you?",
    "I'm doing well, thank you.",
    "That's good to hear.",
    "Thank you.",
    "You're welcome."
]

# Create a new trainer for the chatbot
trainer = ListTrainer(bot)

# Train the chatbot using the list of responses
trainer.train(responses)

# Get a response to the input text 'How are you?'
response = bot.get_response('How are you?')
print(response)

# Get a response to the input text 'What is your name?'
response = bot.get_response('What is your name?')
print(response)

# Get a response to the input text 'Thank you'
response = bot.get_response('Thank you')
print(response)