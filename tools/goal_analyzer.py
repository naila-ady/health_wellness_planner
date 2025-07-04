
# from agents import function_tool
# from agents import RunContextWrapper
# from context import UserSessionContext

# @function_tool
# async def goal_analyzer(
#     context: RunContextWrapper[UserSessionContext],   # ← must be first
#     user_input: str                                  # user's free text
# ) -> str:
#     """
#     Ask the user to pick a goal category (treatment, nutrition, fitness, mental support, sleep).
#     Save the choice in context.goal and prompt the next required detail.
#     """

#     # -------------------------------------------------
#     # 1) If no goal chosen yet → show menu
#     # -------------------------------------------------
#     if not context.goal:
#         # Initialize an empty dict so we know menu was shown
#         context.goal = {}
#         return (
#             "Please select the category you'd like help with:\n"
#             "- 🏥 Treatment\n"
#             "- 🍽️ Nutrition\n"
#             "- 🧠 Mental Support\n"
#             "- 💪 Exercise & Fitness\n"
#             "- 🛌 Sleep Issues\n"
#             "Type your choice."
#         )

#     choice = user_input.lower().strip()

#     # -------------------------------------------------
#     # 2) Match the choice and save context.goal["type"]
#     # -------------------------------------------------
#     if "treatment" in choice or "injury" in choice:
#         context.goal["type"] = "treatment"
#         return (
#             "✅ Goal set: Treatment.\n"
#             "Please describe the injury or issue you're facing."
#         )

#     if "nutrition" in choice or "diet" in choice or "meal" in choice:
#         context.goal["type"] = "nutrition"
#         return (
#             "✅ Goal set: Nutrition.\n"
#             "Do you have any dietary preference (vegetarian, vegan, gluten free, etc.)?"
#         )

#     if "mental" in choice or "stress" in choice or "depression" in choice:
#         context.goal["type"] = "mental_support"
#         return (
#             "✅ Goal set: Mental Support.\n"
#             "How would you describe your current mood or stress levels?"
#         )

#     if "exercise" in choice or "fitness" in choice or "workout" in choice:
#         context.goal["type"] = "fitness"
#         return (
#             "✅ Goal set: Exercise & Fitness.\n"
#             "Are you a beginner, intermediate, or advanced exerciser?"
#         )

#     if "sleep" in choice:
#         context.goal["type"] = "sleep"
#         return (
#             "✅ Goal set: Sleep Issues.\n"
#             "What time do you usually go to bed and wake up?"
#         )

#     # -------------------------------------------------
#     # 3) Fallback when input isn't understood
#     # -------------------------------------------------
#     return (
#         "❌ I didn't catch that.\n"
#         "Please type one of: Treatment, Nutrition, Mental Support, Exercise & Fitness, Sleep Issues."
#     )


# tools/goal_analyzer.py
from agents import function_tool
from agents import RunContextWrapper
from context import UserSessionContext

@function_tool
async def goal_analyzer(
    context: RunContextWrapper[UserSessionContext],
    user_input: str
) -> str:
    """
    1. Show menu if no goal yet.
    2. Store goal type.
    3. For Nutrition → ask diet preference, store in context.diet_preferences.
       When both are set, signal to call meal_planner next.
    """

    user_input = user_input.lower().strip()

    # ------------------------------------------------------------------
    # 1) FIRST TURN -> show menu
    # ------------------------------------------------------------------
    if context.goal is None:
        context.goal = {}                       # mark that menu shown
        return (
            "Please select the category you'd like help with:\n"
            "- 🏥 Treatment\n"
            "- 🍽️ Nutrition\n"
            "- 🧠 Mental Support\n"
            "- 💪 Exercise & Fitness\n"
            "- 🛌 Sleep Issues\n"
            "Type your choice."
        )

    # ------------------------------------------------------------------
    # 2) IF GOAL TYPE NOT SET YET -> set it
    # ------------------------------------------------------------------
    if "type" not in context.goal:
        if "treatment" in user_input or "injury" in user_input:
            context.goal["type"] = "treatment"
            return (
                "✅ Goal set: Treatment.\n"
                "Please briefly describe the injury or issue you're facing."
            )
        if "nutrition" in user_input or "diet" in user_input or "meal" in user_input:
            context.goal["type"] = "nutrition"
            return (
                "✅ Goal set: Nutrition.\n"
                "Which diet preference suits you? (vegetarian, vegan, nonveg, gluten_free, high_protein)"
            )
        if "fitness" in user_input or "exercise" in user_input or "workout" in user_input:
            context.goal["type"] = "fitness"
            return (
                "✅ Goal set: Exercise & Fitness.\n"
                "Are you a beginner, intermediate, or advanced exerciser?"
            )
        if "mental" in user_input or "stress" in user_input or "depression" in user_input:
            context.goal["type"] = "mental_support"
            return (
                "✅ Goal set: Mental Support.\n"
                "How would you describe your current mood or stress levels?"
            )
        if "sleep" in user_input:
            context.goal["type"] = "sleep"
            return (
                "✅ Goal set: Sleep Issues.\n"
                "What time do you usually go to bed and wake up?"
            )
        # fallback
        return (
            "❌ I didn't catch that.\n"
            "Please choose one of: Treatment, Nutrition, Mental Support, Fitness, Sleep."
        )

    # ------------------------------------------------------------------
    # 3) ADDITIONAL QUESTIONS PER GOAL TYPE
    # ------------------------------------------------------------------
    goal_type = context.goal["type"]

    # --- Nutrition branch ---
    if goal_type == "nutrition":
        if context.diet_preferences is None:
            if user_input in {"vegetarian", "vegan", "nonveg", "gluten_free", "high_protein"}:
                context.diet_preferences = user_input    # store preference
                # signal to agent that meal_planner is ready to be called
                return "next_tool: meal_planner"
            else:
                return (
                    "❌ Please choose one diet preference:\n"
                    "- vegetarian\n- vegan\n- nonveg\n- gluten_free\n- high_protein"
                )
        # If preference already set, we should never be here
        return "next_tool: meal_planner"

    # --- Fitness branch (example) ---
    if goal_type == "fitness":
        # Here you might store context.workout_level, then signal workout_plan
        # (implement similarly to nutrition if needed)
        return "next_tool: workout_plan"

    # --- Treatment, mental_support, sleep: let agent hand‑off or use LLM
    return "Handled"

