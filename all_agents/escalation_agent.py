from agents import Agent
escalation_agent = Agent(
    name="Escalation Agent",
    handoff_description = "Handles user requests to speak with a human trainer, coach, or real person.",
    instructions="You are a handoff agent. When a user wants to speak to a human trainer or coach, you acknowledge their request and inform them that a real person will follow up shortly."
)
