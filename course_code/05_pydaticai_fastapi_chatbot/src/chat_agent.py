from pydantic_ai import Agent
from model import nividia_model
from data_models import ChatRequest, ChatResponse

chat_agent = Agent(
    model=nividia_model(),
    system_prompt="Be a joking programming nerd, always answer with programming joke. Also add in som emojis to make it funnier"
    )

chat_agent

async def chat(request: ChatRequest):
    result = await chat_agent.run(
        request.question, message_history=request.message_history
    )

    return ChatResponse(
        response = result.output, message_history = result.all_messages()
    )