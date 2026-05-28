"""
Multi-Agent Orchestrator
Coordinates all agents to provide complete coding assistance
"""

import sys
import os

# Add paths
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
sys.path.append(os.path.join(current_dir, "agents"))

from agents.code_reader import CodeReaderAgent
from agents.code_writer import CodeWriterAgent
from agents.code_reviewer import CodeReviewerAgent
from agents.test_generator import TestGeneratorAgent
from agents.doc_writer import DocWriterAgent


class CodingAssistantOrchestrator:
    """Orchestrates all coding assistant agents"""
    
    def __init__(self):
        """Initialize all agents"""
        print("Initializing agents...")
        self.reader = CodeReaderAgent()
        self.writer = CodeWriterAgent()
        self.reviewer = CodeReviewerAgent()
        self.test_gen = TestGeneratorAgent()
        self.doc_writer = DocWriterAgent()
        print("All agents ready!\n")
    
    def process_request(self, user_input: str) -> dict:
        """Process user request through all agents
        
        Args:
            user_input: The user's coding request
            
        Returns:
            Dictionary with results from all agents
        """
        results = {
            'user_input': user_input,
            'analysis': '',
            'code': '',
            'review': '',
            'tests': '',
            'documentation': ''
        }
        
        # Step 1: Analyze request
        print("=" * 60)
        print("AGENT 1: Code Reader - Analyzing request...")
        print("=" * 60)
        results['analysis'] = self.reader.analyze(user_input)
        print(results['analysis'])
        
        # Step 2: Generate code
        print("\n" + "=" * 60)
        print("AGENT 2: Code Writer - Generating code...")
        print("=" * 60)
        results['code'] = self.writer.write_code(results['analysis'], user_input)
        print(results['code'])
        
        # Step 3: Review code
        print("\n" + "=" * 60)
        print("AGENT 3: Code Reviewer - Reviewing code...")
        print("=" * 60)
        results['review'] = self.reviewer.review_code(results['code'], user_input)
        print(results['review'])
        
        # Step 4: Generate tests
        print("\n" + "=" * 60)
        print("AGENT 4: Test Generator - Creating tests...")
        print("=" * 60)
        results['tests'] = self.test_gen.generate_tests(results['code'], user_input)
        print(results['tests'])
        
        # Step 5: Generate documentation
        print("\n" + "=" * 60)
        print("AGENT 5: Documentation Writer - Writing docs...")
        print("=" * 60)
        results['documentation'] = self.doc_writer.generate_docs(results['code'])
        print(results['documentation'])
        
        print("\n" + "=" * 60)
        print("ALL AGENTS COMPLETED SUCCESSFULLY!")
        print("=" * 60)
        
        return results


# Test the orchestrator
if __name__ == "__main__":
    orchestrator = CodingAssistantOrchestrator()
    
    # User request
    user_request = "Build a Python function that validates email addresses"
    
    print(f"\nUSER REQUEST: {user_request}\n")
    
    # Process through all agents
    results = orchestrator.process_request(user_request)
    
    print("\n" + "=" * 60)
    print("FINAL SUMMARY")
    print("=" * 60)
    print(f"✅ Analysis: {len(results['analysis'])} chars")
    print(f"✅ Code: {len(results['code'])} chars")
    print(f"✅ Review: {len(results['review'])} chars")
    print(f"✅ Tests: {len(results['tests'])} chars")
    print(f"✅ Documentation: {len(results['documentation'])} chars")