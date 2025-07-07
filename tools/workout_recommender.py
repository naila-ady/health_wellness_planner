# from agents import function_tool
# @function_tool
# async def workout_plan(plan:str) ->str:
#     """
#     when user want workplan ask him the level you want 
#     1: Beginner Fitness plan ,
#     2: Advance fitness plan,
    
#     """
    
#     work_plan = plan.lower()
#     if "Beginner" in work_plan and ("weightloss" in work_plan   or "obesity" in work_plan):
#         return f""" Here is your beginner plan
#                     1: Take a brisk 30-minute walk outdoors or on treadmill.
#                     2: Add 10 min stretching.
#                     3: Jumping jacks (30s), 
#                     4:  squats (30s)"""
#     elif "Advance" in work_plan and  ("weightloss" in work_plan or "obesity" in work_plan):
#         return f""" 1: Take a brisk 30-minute walk outdoors or on treadmill.
#                   2: Add 10 min stretching.
#                   3: sets of push-ups, 
#                   4: dumbbell rows, and wall sits (30s hold)"""
#     else:
#         return f" Take a brisk 20-minute walk outdoors or on treadmill. Add 10 min more on daily basis."
#     # return f"❌ Please describe your goal and experience level (e.g. 'I'm a beginner or intermediate')."


                  
    
from agents import function_tool

@function_tool
async def workout_plan(plan: str) -> str:
    """
    Suggest a fitness workout plan based on the user's fitness level beginner or advance.
    """

    work_plan = plan.lower()

    if "beginner" in work_plan or "weightloss"  in work_plan:
    
        return (
            "🏋️ Beginner Weight Loss Plan:\n"
            "1. Brisk 30-minute walk (outdoors or treadmill)\n"
            "2. 10 minutes of stretching\n"
            "3. Jumping jacks (30 seconds)\n"
            "4. Squats (30 seconds)"
        )

    elif "advance" in work_plan or "Obesity" in work_plan :
        return (
            "💪 Advanced Weight Loss Plan:\n"
            "1. Brisk 30-minute walk (outdoors or treadmill)\n"
            "2. 10 minutes of stretching\n"
            "3. Sets of push-ups\n"
            "4. Dumbbell rows\n"
            "5. Wall sits (30-second hold)"
        )

    else:
        return (
            "🚶‍♂️ General Fitness Tip:\n"
            "Start with a brisk 20-minute walk daily, and gradually add 10 more minutes every week."
        )
