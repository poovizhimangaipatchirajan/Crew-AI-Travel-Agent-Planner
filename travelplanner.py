import os
from dotenv import load_dotenv

load_dotenv()

# Turn off the execution trace share prompt
os.environ["CREWAI_TELEMETRY_OPT_OUT"] = "true"

from crewai import Agent, Crew, Task

# Loop until non-empty input is received
city = ""
while not city.strip():
    city = input("Which city you want to explore? ").strip()

planner = Agent(
    role="Expert Travel Guide & Planner",
    goal="Recommend the top 3 must-visit attractions in {city} tailored for a memorable experience.",
    backstory=(
        "You are a seasoned world traveler and professional travel curator with years "
        "of experience exploring hidden gems and famous cultural landmarks."
    ),
    memory=False
)

task = Task(
    description=(
        "Identify and describe the top 3 must-visit places in {city}. "
        "For each location, provide its name, a short description of why it is special, "
        "and a practical tip for visitors."
    ),
    expected_output=(
        "A well-structured list containing exactly 3 recommended attractions in {city}, "
        "each with a name, brief description, and a helpful visitor tip."
    ),
    agent=planner,
)

crew = Crew(agents=[planner], tasks=[task])

result = crew.kickoff(inputs={"city": city})

print("\n" + "=" * 50)
print(f"TRAVEL SUGGESTIONS FOR {city.upper()}:")
print("=" * 50)
print(result)