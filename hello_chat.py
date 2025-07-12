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
    
    # # 🛡️ Guardrail added here (before any logic)
    # # guardrail_result = await guard_health_input.run(user_input)
    # guardrail_result = await guard_health_input.run(context=None, agent=wellness_agent ,input=user_input, )

    
    # if not isinstance(guardrail_result, GuardrailFunctionOutput):
    #     # 🛑 Tripwire triggered — show message and skip further processing
    #     await cl.Message(f"{guardrail_result.message}").send()
    #     return
    
    # # ✅ Use clean/safe user input from guardrail
    # user_input = guardrail_result.output.lower()


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
    

# import chainlit as cl
# from agents import Runner
# from core_agent import wellness_agent
# from context import UserSessionContext
# from runconfig import config
# from utils.guardrails import guard_health_input

# # Store context per user
# user_contexts = {}

# @cl.on_chat_start
# async def on_chat_start():
#     await cl.Message("👋 Welcome to the Health & Wellness Planner Agent!").send()
#     await cl.Message("Please enter your name:").send()

# @cl.on_message
# async def on_message(message: cl.Message):
#     user_id = message.author  
#     user_input = message.content.strip()

#     # Setup session if user is new
#     if user_id not in user_contexts:
#         name = user_input.capitalize()
#         uid = hash(user_id) % 10000
#         user_contexts[user_id] = UserSessionContext(name=name, uid=uid)
#         await cl.Message(f"✅ Hello {name}! Now enter your goal like 'Nutrition', 'Fitness', 'Meal plan' or 'Exit'").send()
#         return

#     # Exit condition
#     if user_input.lower() in ["exit", "quit", "bye"]:
#         await cl.Message("👋 Session ended. Take care and stay healthy!").send()
#         user_contexts.pop(user_id, None)
#         await cl.Message("👋 Welcome to the Health & Wellness Planner Agent!").send()
#         await cl.Message("Please enter your name:").send()
#         return

#     context = user_contexts[user_id]

#     # ✅ Run guardrail on input
#     guardrail_result = await guard_health_input.run(
#         input=user_input,
#         context=context,
#         agent=wellness_agent
#     )

#     # 🛑 If tripwire triggered, show block message
#     if guardrail_result.tripwire_triggered:
#         await cl.Message(guardrail_result.result.message).send()
#         return

#     # ✅ Extract clean input from result
#     safe_input = guardrail_result.result.output_info

#     # Run the main wellness agent
#     result = await Runner.run(
#         starting_agent=wellness_agent,
#         input=safe_input,
#         context=context,
#         run_config=config
#     )

#     prefix = f"**Dear {context.name} (UID: {context.uid})**,\n\n"
#     await cl.Message(prefix + result.final_output).send()
