from agent import function_tool
@function_tool
async def workout_plan(plan:str) ->str:
    """
    Recommends a short, single workout based on user's goal and experience.
    Recognizes terms like 'weight loss', 'muscle gain', 'beginner', etc.
    """
    
    work_plan = plan.lower()
    if "beginner" in plan and "weightloss" in plan or "obesity" in plan:
        return f" 1: Take a brisk 30-minute walk outdoors or on treadmill.
                  2: Add 10 min stretching.
                  3: Jumping jacks (30s), 
                  4 :squats (30s)"
    if "intermediate" in plan and  "weightloss" in plan or "obesity" in plan:
        return f" 1: Take a brisk 30-minute walk outdoors or on treadmill.
                  2: Add 10 min stretching.
                  3: Jumping jacks (30s), 
                  4 :squats (30s)"
    
    