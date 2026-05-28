"""
Code Reader Agent - Analyzes user requests and understands the task
"""

import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_groq import ChatGroq
from prompts.agent_prompts import CODE_READER_PROMPT
from dotenv import load_dotenv

load_dotenv()


class CodeReaderAgent:
    """Agent that analyzes user requests and understands coding tasks"""
    
    def __init__(self, model="llama-3.1-8b-instant"):
        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model=model,
            temperature=0.3
        )
        self.name = "Code Reader"
    
    def analyze(self, user_input: str) -> str:
        prompt = CODE_READER_PROMPT.format(user_input=user_input)
        
        try:
            response = self.llm.invoke(prompt)
            return response.content
        except Exception as e:
            return f"Error in Code Reader: {str(e)}"


# Test the agent
if __name__ == "__main__":
    reader = CodeReaderAgent()
    
    user_request = "Build a Python function that validates email addresses"
    
    print(f"Code Reader analyzing...\n")
    analysis = reader.analyze(user_request)
    print(analysis)