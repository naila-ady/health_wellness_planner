# chainlit_app.py

import chainlit as cl
from agents import Runner
from core_agent import wellness_agent
from context import UserSessionContext
from runconfig import config

# Store context per user
user_contexts = {}

@cl.on_chat_start
async def on_chat_start():
    await cl.Message("👋 Welcome to the Health & Wellness Planner Agent!").send()
    await cl.Message("Please enter your name:").send()

@cl.on_message
async def on_message(message: cl.Message):
    user_id = message.author  
    user_input = message.content.strip().lower()

    # Check if user context is created
    if user_id not in user_contexts:
        name = user_input.capitalize()
        user_contexts[user_id] = UserSessionContext(name=name, uid=hash(user_id) % 10000)
        await cl.Message(f"✅ Hello {name}! Now enter your goal like 'Nutrition', 'Fitness', 'Meal plan' or 'Exit'").send()
        
        return
    # Handle "exit" to end chat gracefully
    if user_input.lower() in ["exit", "quit", "bye"]:
        await cl.Message("👋 Session ended. Take care and stay healthy!").send()
        user_contexts.pop(user_id, None)
        
        await cl.Message("👋 Welcome to the Health & Wellness Planner Agent!").send()
        await cl.Message("Please enter your name:").send()
        return



    # Get the user context
    context = user_contexts[user_id]

    # Run the agent
    result = await Runner.run(
        starting_agent=wellness_agent,
        input=user_input,
        context=context,
        run_config=config
    )

    # Add name and UID
    prefix = f"**Dear {context.name} (UID: {context.uid})**,\n\n"
    await cl.Message(prefix + result.final_output).send()
    
