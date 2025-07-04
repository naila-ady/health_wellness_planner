from agents import Agent
injury_support_agent=Agent(
    name = "Injury Support Agent",
    instructions = " You are handoff agent.If user concerns about bones injury , jointPain, or any physical limitation ,you provide them with guidence and traetment",
    handoff_description="Handles user request to examine physical issues"
)