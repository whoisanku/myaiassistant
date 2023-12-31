import os
import constants
from langchain_google_genai import ChatGoogleGenerativeAI

# Set your Google API Key
os.environ['GOOGLE_API_KEY'] = constants.APIKEY

# Initialize the model
llm = ChatGoogleGenerativeAI(model="gemini-pro")

# Invoke the model
query = input("Enter your question: ")
response = llm.invoke(query)

# Handle the response
print(response.content)