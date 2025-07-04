from agents import function_tool
@function_tool()
async def goal_analyzer(collect_goals:str) -> str:
    """
    Very simple tool that checks if the user's goal is health-related.
    Returns the detected category as a string.

    """
    goal = collect_goals.lower()

    if "diet_plan" in goal or "meal_plan" in goal or "diet/meal" in goal:
        return "Nutrition :you have a dietary goal. Do you follow any specific diet like vegetarian or gluten_free?"
    elif "exercise" in goal or "gym" in goal:
        return "Fitness :you have a fitness goal. How many days per week do you want to work out?"
    elif "sleep" in goal:
        return "Sleep: Got it ! Sleep issue,explain your sleeping pattern"
    elif "mental" in goal or "stress" in goal or "depression "in goal:
        return "Mental Health :your mental heallth is to be considered ,whats ur age? ,"
    else:
        return "Not a health-related goal"

