

# Importing BaseModel from Pydantic for data validation and structure
from pydantic import BaseModel

# Importing typing tools to define optional and list-based fields
from typing import Optional, List, Dict

# Defining the session-wide context model
class UserSessionContext(BaseModel):
    # User's display name (used for personalization)
    name: str

    # Unique user/session ID
    uid: int
    

    # Parsed goal (structured) extracted by GoalAnalyzerTool
    # Example: {"type": "weight_loss", "amount": 5, "duration": "2 months"}
    goal: dict= {}

    # User's dietary preference, e.g., "vegetarian", "keto", etc.
    diet_preferences: Optional[str] = None

    # Custom workout plan generated for the user
    # Could be a string or a structured dict depending on your tool
    workout_plan: Optional[dict] = None

    # Meal plan (list of meals for 7 days or more)
    meal_plan: Optional[List[str]] = None

    # Any injury or limitation user mentioned, e.g., "knee pain"
    injury_notes: Optional[str] = None

    # Keeps track of which agents were handed off to and why
    # Example: ["Handed off to InjurySupportAgent due to knee pain"]
    handoff_logs: List[str] = []

    # Logs user's weekly progress updates
    # Example: [{"entry": "Lost 1kg", "timestamp": "2025-07-03 10:30"}]
    progress_logs: List[Dict[str, str]] = []
