


from agents import function_tool, RunContextWrapper
from context import UserSessionContext

@function_tool
async def goal_analyzer(
    context: RunContextWrapper[UserSessionContext],
    user_input: str
) -> str:
    """
    Analyze the user's input and set their goal category (only once).
    """

    user_input = user_input.lower().strip()

    # Step 1: If no goal dict, show menu once and initialize
    if not context.goal:
        context.goal = {"menu_shown": True}
        return (
            "Please choose your goal category:\n"
            "- 🍽️ Nutrition Diet / Meal Planner\n"
            "- 🏥 Fitness Training / Gym / Workout\n"
            "- 🧠 Mental Health\n"
            "- 🤕 Injury Support\n"
            "- 👋 exit"
        )

    # Step 2: If goal type not yet set → handle input
    if "type" not in context.goal:
        if "nutrition" in user_input or "meal" in user_input or "diet" in user_input:
            context.goal["type"] = "nutrition"
            return "✅ Goal set: Nutrition."
        elif "fitness" in user_input or "gym" in user_input or "workout" in user_input:
            context.goal["type"] = "fitness"
            return "✅ Goal set: Fitness."
        elif "injury" in user_input or "treatment" in user_input:
            context.goal["type"] = "injury_support"
            return "✅ Goal set: Injury Support."
        elif "mental" in user_input or "stress" in user_input:
            context.goal["type"] = "mental_support"
            return "✅ Goal set: Mental Health."
        else:
            return (
                "❌ Sorry, I didn't understand.\n"
                "Please choose: Nutrition, Fitness, Mental Health, or Injury Support."
            )

    # Step 3: Goal already set → don't ask again
    return f"🎯 Your goal is already set to: {context.goal['type'].replace('_', ' ').title()}.\n(You can now continue or type 'exit' to quit.)"
