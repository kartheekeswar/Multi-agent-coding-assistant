"""
Code Writer Agent - Generates production-quality code based on analysis
"""

import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_groq import ChatGroq
from prompts.agent_prompts import CODE_WRITER_PROMPT
from dotenv import load_dotenv

load_dotenv()


class CodeWriterAgent:
    """Agent that writes production-quality code based on analysis"""
    
    def __init__(self, model="llama-3.3-70b-versatile"):
        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model=model,
            temperature=0.2
        )
        self.name = "Code Writer"
    
    def write_code(self, analysis: str, user_input: str) -> str:
        prompt = CODE_WRITER_PROMPT.format(
            analysis=analysis,
            user_input=user_input
        )
        
        try:
            response = self.llm.invoke(prompt)
            return response.content
        except Exception as e:
            return f"Error in Code Writer: {str(e)}"


# Test the agent
if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(current_dir)
    
    from code_reader import CodeReaderAgent
    
    reader = CodeReaderAgent()
    user_request = "Build a Python function that validates email addresses"
    
    print("Code Reader analyzing...\n")
    analysis = reader.analyze(user_request)
    print(analysis)
    print("\n" + "="*60 + "\n")
    
    writer = CodeWriterAgent()
    print("Code Writer generating code...\n")
    code = writer.write_code(analysis, user_request)
    print(code)