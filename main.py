import asyncio
from utils.streaming import stream_user_input
from context import UserSessionContext

async def main():
    # Ask for user input at the start
    name = input("👤 Enter your name: ").strip()
    uid_input = input("🆔 Enter your User ID (just a number): ").strip()

    try:
        uid = int(uid_input)
    except ValueError:
        print("❌ Invalid UID. Please enter a numeric value.")
        return

    context = UserSessionContext(name=name, uid=uid)

    print("\n🧠 Health & Wellness Planner Agent")
    print("💬 Type your goal category (e.g., 'Nutrition', 'Fitness', 'Mental Health', 'Injury Support') or type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("👋 Goodbye! Stay healthy.")
            break

        response = await stream_user_input(user_input, context)

        # 🔍 Debug context log (you can comment this out if no longer needed)
        print(f"DEBUG: context.name = {context.name}, uid = {context.uid}, goal = {context.goal}")

        # 🟢 Add personalization unless it's a system/menu message
        skip_prefixes = (
            "Please choose your goal category",
            "❌",
            "👋",
            "Sorry, I",
            "I didn't understand",
            "How can I help"
        )
        if response and not any(response.strip().startswith(prefix) for prefix in skip_prefixes):
            response = f"Dear {context.name} (UID: {context.uid}),\n\n{response}"

        # 🩺 Show the final agent response
        print(f"\n🩺 Wellness Agent: {response}\n")

if __name__ == "__main__":
    asyncio.run(main())
