"""
Documentation Writer Agent - Generates professional documentation
"""

import sys
import os

# Add parent directory AND current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
sys.path.append(current_dir)

from langchain_groq import ChatGroq
from prompts.agent_prompts import DOC_WRITER_PROMPT
from dotenv import load_dotenv

load_dotenv()


class DocWriterAgent:
    """Agent that generates professional documentation"""
    
    def __init__(self, model="llama-3.3-70b-versatile"):
        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model=model,
            temperature=0.3
        )
        self.name = "Documentation Writer"
    
    def generate_docs(self, code: str) -> str:
        """Generate documentation for the code
        
        Args:
            code: The code to document
            
        Returns:
            Markdown documentation
        """
        prompt = DOC_WRITER_PROMPT.format(code=code)
        
        try:
            response = self.llm.invoke(prompt)
            return response.content
        except Exception as e:
            return f"Error in Doc Writer: {str(e)}"


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
    
    # Step 3: Generate Docs
    print("\n" + "=" * 60)
    print("STEP 3: Documentation Writer")
    print("=" * 60)
    doc_writer = DocWriterAgent()
    docs = doc_writer.generate_docs(code)
    print(docs)