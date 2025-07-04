# from agents import function_tool ,RunContextWrapper
# from datetime import datetime
# from context import UserSessionContext



# @function_tool
# async def progress_tracker(update: str ,context:RunContextWrapper[UserSessionContext]) -> str:
#     """
#     Logs the user's progress updates (e.g., 'I worked out 4 times and lost 1kg').
#     Appends the update and timestamp to the context's progress_logs.
#     Returns a confirmation with a motivational message.
#     """
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    
#     context.progress_logs.append({
#         "entry": update,
#         "timestamp": timestamp
#     })

#     return f"✅ Progress update logged: '{update}' at {timestamp}. Keep up the great work! 💪"


from agents import function_tool, RunContextWrapper
from datetime import datetime
from context import UserSessionContext  # adjust path if needed

@function_tool
async def progress_tracker( context: RunContextWrapper[UserSessionContext] ,update: str) -> str:
    """
    Logs the user's progress updates (e.g., 'I worked out 4 times and lost 1kg').
    Appends the update and timestamp to the context's progress_logs.
    Returns a confirmation with a motivational message.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    context.progress_logs.append({
        "entry": update,
        "timestamp": timestamp
    })

    return f"✅ Progress update logged: '{update}' at {timestamp}. Keep up the great work! 💪"
