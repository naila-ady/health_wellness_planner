# # import asyncio
# # from utils.streaming import stream_user_input
# # from context import UserSessionContext
# # async def main():
# #     context = UserSessionContext(name="Ali", uid=123)

# #     print("🧠 Health & Wellness Planner Agent\n")
# #     print("💬 Type your goal or question (type 'exit' to quit):\n")


# #     user_input = input("You: ")
# #     await stream_user_input(user_input, context)

# # if __name__ == "__main__":
# #     asyncio.run(main())

# import asyncio
# from utils.streaming import run_user_input
# from context import UserSessionContext
# from agents import RunContextWrapper

# async def main():
#     user_context = UserSessionContext(name="Zain", uid=1)
#     user_input = input("How can I help you with your health goals?\n> ")
#     await run_user_input(user_input, user_context)

# if __name__ == "__main__":
#     asyncio.run(main())

# main.py
import asyncio
from context import UserSessionContext
from core_agent import wellness_agent
from runconfig import config
from agents import Runner

async def main():
    user_context = UserSessionContext(name="TestUser", uid=1 , goal= None)

    print("🤖 How can I help you with your health goals?")

    while True:
        user_input = input("> ")

        if user_input.lower() in {"exit", "quit"}:
            print("👋 Take care! Ending session.")
            break


        result = await Runner.run(
            starting_agent=wellness_agent,
            input=user_input,
            context=user_context,
            run_config=config
        )

        print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
