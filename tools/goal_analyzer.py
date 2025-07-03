from agents import function_tool
@function_tool()
async def goal_analyzer(goal_text:str) -> str:
    """
    Very simple tool that checks if the user's goal is health-related.
    Returns the detected category as a string.

    """
    goal = goal_text.lower()

    if "diet" in goal or "meal" in goal:
        return "Nutrition"
    elif "exercise" in goal or "gym" in goal:
        return "Fitness"
    elif "sleep" in goal:
        return "Sleep"
    elif "mental" in goal or "stress" in goal:
        return "Mental Health"
    else:
        return "Not a health-related goal"

