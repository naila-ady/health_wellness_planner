
# import asyncio
# from utils.streaming import stream_user_input
# from context import UserSessionContext

# async def main():
#     context = UserSessionContext(name="Ali", uid=123)
#     print("""
# 🧠 Health & Wellness Planner Agent
#     Please choose your goal category:
#     - 🍽️ Nutrition Diet /Meal Planner
#     - 🏥 Fitness Training /Gym /Workout
#     - 🧠 Mental Health
#     - 🤕 Injury Support
#     - 👋   exit
# """)

      
#     while True:
#         user_input = input("You: ").strip()
        
#         if user_input.lower() == "exit":
#             print("👋 Goodbye! Stay healthy.")
#             break

#         await stream_user_input(user_input, context)

# if __name__ == "__main__":
#     asyncio.run(main())


import asyncio
from utils.streaming import stream_user_input
from context import UserSessionContext

async def main():
    context = UserSessionContext(name="Ali", uid=123)
    print("🧠 Health & Wellness Planner Agent")
    print("💬 Type your goal category (e.g., 'Nutrition', 'Fitness', 'Mental Health', 'Injury Support') or type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == "exit":
            print("👋 Goodbye! Stay healthy.")
            break

        await stream_user_input(user_input, context)

if __name__ == "__main__":
    asyncio.run(main())
