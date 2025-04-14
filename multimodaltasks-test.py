from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv
import os
load_dotenv()

llm = LLM(model="gpt-4o", api_key=os.environ["OPENAI_API_KEY"])
# Create a multimodal agent
image_analyst = Agent(
    role="IMAGE Analyst",
    goal="Analyze images and provide detailed descriptions",
    backstory="Expert in visual analysis with deep knowledge of subject matter",
    multimodal=True, verbose=True
)

# Create a task for image analysis
task = Task(
    description="Analyze the image at https://assets.bundesliga.com/contender/2023/11/GettyImages-1268071225.jpg and provide a detailed description",
    expected_output="A detailed description of the  image",
    agent=image_analyst, verbose=True
)
# Create a task for image analysis
task1 = Task(
    description="Analyze the image at https://p.imgci.com/db/PICTURES/CMS/305300/305349.jpg and provide a detailed description",
    expected_output="A detailed description of the  image",
    agent=image_analyst,verbose=True
)
# Create a task for image analysis
task2 = Task(
    description="Analyze the image at https://upload.wikimedia.org/wikipedia/commons/4/4a/Depart4x100.jpg and provide a detailed description",
    expected_output="A detailed description of the  image",
    agent=image_analyst,
    verbose=True
)

# Create and run the crew
crew = Crew(
    agents=[image_analyst],
    tasks=[task,task1,task2]
)

result = crew.kickoff()