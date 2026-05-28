"""
Code Reviewer Agent - Reviews code quality and provides feedback
"""

import sys
import os

# Add parent directory AND current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
sys.path.append(current_dir)

from langchain_groq import ChatGroq
from prompts.agent_prompts import CODE_REVIEWER_PROMPT
from dotenv import load_dotenv

load_dotenv()


class CodeReviewerAgent:
    """Agent that reviews code and provides constructive feedback"""
    
    def __init__(self, model="llama-3.3-70b-versatile"):
        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model=model,
            temperature=0.3
        )
        self.name = "Code Reviewer"
    
    def review_code(self, code: str, user_input: str) -> str:
        prompt = CODE_REVIEWER_PROMPT.format(
            code=code,
            user_input=user_input
        )
        
        try:
            response = self.llm.invoke(prompt)
            return response.content
        except Exception as e:
            return f"Error in Code Reviewer: {str(e)}"


# Test the agent
if __name__ == "__main__":
    from code_reader import CodeReaderAgent
    from code_writer import CodeWriterAgent
    
    user_request = "Build a Python function that validates email addresses"
    
    # Step 1: Reader analyzes
    print("=" * 60)
    print("STEP 1: Code Reader")
    print("=" * 60)
    reader = CodeReaderAgent()
    analysis = reader.analyze(user_request)
    print(analysis)
    
    # Step 2: Writer generates code
    print("\n" + "=" * 60)
    print("STEP 2: Code Writer")
    print("=" * 60)
    writer = CodeWriterAgent()
    code = writer.write_code(analysis, user_request)
    print(code)
    
    # Step 3: Reviewer reviews code
    print("\n" + "=" * 60)
    print("STEP 3: Code Reviewer")
    print("=" * 60)
    reviewer = CodeReviewerAgent()
    review = reviewer.review_code(code, user_request)
    print(review)