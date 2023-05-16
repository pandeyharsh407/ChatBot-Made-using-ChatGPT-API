import openai

# Set the OpenAI API key
openai.api_key = "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"

# Set the model to use
model_engine = "text-davinci-002"

def generate_response(prompt):
  completions = openai.Completion.create(
      engine=model_engine,
      prompt=prompt,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.5,
  )

  message = completions.choices[0].text
  return message.strip()

# Create a dictionary to store previous conversations
conversations = {}

# Test the chatbot
while True:
  prompt = input("You: ")
  # Check if the prompt has been said before
  if prompt in conversations:
    response = conversations[prompt]
  else:
    # Generate a new response
    response = generate_response(prompt)
    # Add the prompt and response to the dictionary
    conversations[prompt] = response
  print("Ava:", response)