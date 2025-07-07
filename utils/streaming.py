from agents import Runner
from core_agent import wellness_agent
from context import UserSessionContext
from runconfig import config


async def stream_user_input(user_input:str ,ctx:UserSessionContext):
    result= await Runner.run(
        starting_agent=wellness_agent,
        input=user_input,               
        context=ctx,                
        run_config=config           
    )
    print(result.final_output)       


