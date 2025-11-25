from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()

@tool
def calculator(a: float, b: float, operation: str) -> float:
    """Useful for performing basic arithmetic calculations."""
    """Performs basic arithmetic operations."""
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    else:
        raise ValueError(f"Unsupported operation: {operation}")
    
@tool
def greet(name: str) -> str:
    """Greets the user by name."""
    return f"Hello, {name}! How can I assist you today?"


def main():
    model = ChatOpenAI(temperature=0)
    tools = [calculator, greet]
    agent_executor = create_agent(model, tools)
    print("Welcome! I'm your AI assistant. Type 'quit' to exit.")
    print("You can ask me to perform calculations or chat with me.")


    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == 'quit':
            break

        print("\nAssistant: ", end="")
        for chunk in agent_executor.stream(
            {"messages":[HumanMessage(content=user_input)]}):
            
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()

if __name__ == "__main__":
    main()