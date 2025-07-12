from agents import Agent 
from tools.goal_analyzer import goal_analyzer
from tools.meal_planner import meal_planner
from tools.scheduler import schedule
from tools.tracker import progress_tracker
from tools.workout_recommender import workout_plan
# from tools.wellness_conversational_tool  import wellness_flow
from all_agents.escalation_agent import escalation_agent
from all_agents.injurysupport_agent import injury_support_agent
from all_agents.nutrition_agent import nutrition_agent

wellness_agent= Agent(
    name ="wellness Planner Agent",
    instructions="""
    You are a helpful and supportive Wellness Planner Agent""",

    tools=[
        goal_analyzer,
        meal_planner,
        schedule,
        progress_tracker,
        workout_plan
    ],
    handoffs=[
        escalation_agent,
        nutrition_agent,
        injury_support_agent
    ]
)





