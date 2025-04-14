from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv
import os
load_dotenv()

llm = LLM(model="gpt-4o", api_key=os.environ["OPENAI_API_KEY"])

# Create a multimodal agent for detailed analysis
expert_analyst = Agent(
    role="Visual Quality Inspector",
    goal="Perform detailed quality analysis of product images",
    backstory="Senior quality control expert with expertise in visual inspection",
    multimodal=True,
    llm=llm 
)

# Create a task with specific analysis requirements
inspection_task = Task(
    description="""
    Analyze the product image at https://static1.xdaimages.com/wordpress/wp-content/uploads/2022/09/IMG_20220916_164330-1024x832.jpg with focus on:
    1. Quality of materials
    2. Manufacturing defects
    3. Compliance with standards
    Provide a detailed report highlighting any issues found.
    """,
    expected_output="A detailed report highlighting any issues found",
    agent=expert_analyst
)

# Create and run the crew
crew = Crew(
    agents=[expert_analyst],
    tasks=[inspection_task]
)

result = crew.kickoff()
print(result.raw)