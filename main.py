# import asyncio
# from utils.streaming import stream_user_input
# from context import UserSessionContext
# async def main():
#     context = UserSessionContext(name="Ali", uid=123)

#     print("🧠 Health & Wellness Planner Agent\n")
#     print("💬 Type your goal or question (type 'exit' to quit):\n")


#     user_input = input("You: ")
#     await stream_user_input(user_input, context)

# if __name__ == "__main__":
#     asyncio.run(main())

import asyncio
from utils.streaming import run_user_input
from context import UserSessionContext

async def main():
    user_context = UserSessionContext(name="Zain", uid=1)
    user_input = input("How can I help you with your health goals?\n> ")
    await run_user_input(user_input, user_context)

if __name__ == "__main__":
    asyncio.run(main())
