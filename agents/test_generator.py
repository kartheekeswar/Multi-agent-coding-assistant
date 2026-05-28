"""
Test Generator Agent - Creates comprehensive unit tests for code
"""

import sys
import os

# Add parent directory AND current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
sys.path.append(current_dir)

from langchain_groq import ChatGroq
from prompts.agent_prompts import TEST_GENERATOR_PROMPT
from dotenv import load_dotenv

load_dotenv()


class TestGeneratorAgent:
    """Agent that generates comprehensive unit tests"""
    
    def __init__(self, model="llama-3.3-70b-versatile"):
        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model=model,
            temperature=0.2
        )
        self.name = "Test Generator"
    
    def generate_tests(self, code: str, user_input: str) -> str:
        """Generate unit tests for the code
        
        Args:
            code: The code to test
            user_input: The original user request
            
        Returns:
            Generated test code
        """
        prompt = TEST_GENERATOR_PROMPT.format(
            code=code,
            user_input=user_input
        )
        
        try:
            response = self.llm.invoke(prompt)
            return response.content
        except Exception as e:
            return f"Error in Test Generator: {str(e)}"


# Test the agent
if __name__ == "__main__":
    from code_reader import CodeReaderAgent
    from code_writer import CodeWriterAgent
    
    user_request = "Build a Python function that validates email addresses"
    
    # Step 1: Analyze
    print("=" * 60)
    print("STEP 1: Code Reader")
    print("=" * 60)
    reader = CodeReaderAgent()
    analysis = reader.analyze(user_request)
    print(analysis)
    
    # Step 2: Write Code
    print("\n" + "=" * 60)
    print("STEP 2: Code Writer")
    print("=" * 60)
    writer = CodeWriterAgent()
    code = writer.write_code(analysis, user_request)
    print(code)
    
    # Step 3: Generate Tests
    print("\n" + "=" * 60)
    print("STEP 3: Test Generator")
    print("=" * 60)
    test_gen = TestGeneratorAgent()
    tests = test_gen.generate_tests(code, user_request)
    print(tests)