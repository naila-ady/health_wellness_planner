from agents import function_tool

@function_tool
async def schedule(followup_time:str) ->str:
    """
    A preferred time schedule that suits you the best for weekly health and progress check
    Accept input like :Monday 7pm friday 11am
    """
    timeSlot = followup_time.lower()
    valid_days={"Monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"}
    # check kar rahe hain ke user ke input mein koi valid din hai ya nahi
    if any(day in timeSlot for day in valid_days.split()):  
        # agar valid din mila, to confirm message bhej rahe hain (title() se format set krengay)
        return f"Weekly scheduled checkup time slot preferred for you is {followup_time.title()}"
    else:
        # agar koi valid din nahi mila, to user ko error message dikhate hain
        return "❌ Please provide a valid day like 'Monday 7am' or 'Friday evening'."
