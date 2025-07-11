# 📁 app.py
import chainlit as cl 
from core_agent import wellness_agent
from agents import Runner
from context import UserSessionContext
from requests import session
from runconfig import config

# Ask for user name + UID on chat start
@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="👋 Welcome to Wellness Agent!\nPlease enter your **name and UID** (e.g. `Ali, 123`)").send()

@cl.on_message
async def on_message(message: cl.Message):
    # session = cl.user_session
    
    await cl.Message(content=f"👋 Hello! You said: {message.content}").send()

    # Step 1: If context not set → expect name, uid input
    if "context" not in session:
        try:
            name, uid = map(str.strip, message.content.split(","))
            session["context"] = UserSessionContext(name=name, uid=int(uid))
            await cl.Message(content=f"✅ Thanks {name} (UID: {uid})! Now share your goal like 'Nutrition' or 'Fitness'.").send()
        except:
            await cl.Message(content="❌ Invalid format. Please enter like `Ali, 123`").send()
        return

    # Step 2: Run main agent
    context = session["context"]
    result = await Runner.run(
        starting_agent=wellness_agent,
        input=message.content,
        context=context,
        run_config=config
    )

    await cl.Message(content=f"👤 {context.name} (UID: {context.uid})\n\n🧠 {result.final_output}").send()
