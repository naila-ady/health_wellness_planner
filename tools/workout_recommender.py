from agents import function_tool
@function_tool
async def workout_plan(plan:str) ->str:
    """
    Recommends a short, single workout based on user's goal and experience.
    Recognizes terms like 'weight loss', 'muscle gain', 'beginner', etc. 📈
    """
    
    work_plan = plan.lower()
    if "beginner" in work_plan and ("weightloss" in work_plan   or "obesity" in work_plan):
        return f"""\ 1: Take a brisk 30-minute walk outdoors or on treadmill.
                  2: Add 10 min stretching.
                  3: Jumping jacks (30s), 
                  4 :squats (30s)"""
    elif "intermediate" in work_plan and  ("weightloss" in work_plan or "obesity" in work_plan):
        return f"""\ 1: Take a brisk 30-minute walk outdoors or on treadmill.
                  2: Add 10 min stretching.
                  3: sets of push-ups, 
                  4: dumbbell rows, and wall sits (30s hold)"""
    elif "walk" in work_plan:
        return f" Take a brisk 20-minute walk outdoors or on treadmill. Add 10 min more on daily basis."
    return f"❌ Please describe your goal and experience level (e.g. 'I'm a beginner or intermediate')."


                  
    
    