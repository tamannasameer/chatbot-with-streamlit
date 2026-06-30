from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from langchain_community.chat_message_histories import ChatMessageHistory
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.1)

system_prompt = SystemMessage(content="You are a very humble and sweet AI assistant.")
memory = ChatMessageHistory()

def get_response(user_input):
    memory.add_user_message(user_input)

    messages = [system_prompt] + memory.messages

    response = llm.invoke(messages)

    memory.add_ai_message(response.content)

    return response.content