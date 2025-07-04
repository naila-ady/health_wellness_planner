

from agents import function_tool, RunContextWrapper
from context import UserSessionContext

@function_tool
async def goal_analyzer(
    context: RunContextWrapper[UserSessionContext],
    user_input: str
) -> str:
    """the goal decided by user in the input asked by the agent u will further work according to your code
    """

    user_input = user_input.lower().strip()

    # Step 1: If goal is not yet set → show menu
    # if not context.goal:
    #     context.goal = {}  # Mark that menu has been shown
    #     return (
    #         "Please choose your goal category:\n"
    #         "- 🍽️ Nutrition\n"
    #         "- 🏥 Injury Support\n"
    #         "- 🧠 Mental Support\n"
    #         "Just type one of the above."
    #     )

    # Step 2: Set goal type if not already set
    if "type" not in context.goal:
        if "nutrition" in user_input:
            context.goal["type"] = "nutrition"
            return "✅ Goal set: Nutrition."
        elif "injury" in user_input or "treatment" in user_input:
            context.goal["type"] = "injury_support"
            return "✅ Goal set: Injury Support."
        elif "mental" in user_input or "stress" in user_input:
            context.goal["type"] = "mental_support"
            return "✅ Goal set: Mental Support."
        else:
            return (
                "❌ Sorry, I didn't understand.\n"
                "Please choose: Nutrition, Injury Support, or Mental Support."
            )

    return "Handled"
