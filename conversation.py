from datetime import datetime

from database_functions import *
from tools import get_tools
from openai_functions import chat_completion

tools = get_tools(get_database_schema_string(),
                  get_database_definitions())


def format_chat_history(chat_history: list[list], query: str) -> list[list]:
    formatted_chat_history = []
    for ch in chat_history:
        formatted_chat_history.append({
            'role': 'user',
            'content': ch[0]
        })
        formatted_chat_history.append({
            'role': 'assistant',
            'content': ch[1]
        })
    formatted_chat_history.append({
        "role": "user",
        "content": query
    })
    return formatted_chat_history


def handle_chat_completion(chat_history: list[list]) -> list[list]:
    try:
        query = chat_history[-1][0]
        print(f'User query -> {query}')
        formatted_chat_history = format_chat_history(chat_history[:-1], query)
        response = chat_completion(formatted_chat_history)
        print(f'Chatbot response -> {response}')
        chat_history[-1][1] = response
        return chat_history
    except:
        chat_history[-1][1] = config.ERROR_MESSAGE
        return chat_history


def handle_user_query(message: str, chat_history: list[tuple]) -> tuple:
    chat_history += [[message, None]]
    return '', chat_history
