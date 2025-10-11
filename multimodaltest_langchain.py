from crewai import Agent, Task, Crew
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
#from langchain_core.schema import HumanMessage
from langchain_core.messages.human import HumanMessage
from langchain_core.messages import AIMessage

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.environ["GEMINI_API_KEY"]
)

# Test the model directly first
messages = [
    HumanMessage(
        content=[
            {
                "type": "text",
                "text": "What do you see in this image?"
            },
            {
                "type": "image_url",
                "image_url": "https://assets.bundesliga.com/contender/2023/11/GettyImages-1268071225.jpg"
            }
        ]
    )
]

response = llm.invoke(messages)
print(response.content)