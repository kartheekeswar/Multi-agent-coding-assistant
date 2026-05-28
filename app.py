"""
Multi-Agent Coding Assistant - Streamlit UI
"""

import streamlit as st
import sys
import os
from datetime import datetime

# Add paths
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
sys.path.append(os.path.join(current_dir, "agents"))

from agents.code_reader import CodeReaderAgent
from agents.code_writer import CodeWriterAgent
from agents.code_reviewer import CodeReviewerAgent
from agents.test_generator import TestGeneratorAgent
from agents.doc_writer import DocWriterAgent


# Page config
st.set_page_config(
    page_title="Multi-Agent Coding Assistant",
    page_icon="🤖",
    layout="wide"
)

# Initialize session state
if 'results' not in st.session_state:
    st.session_state.results = None
if 'agents_initialized' not in st.session_state:
    st.session_state.agents_initialized = False


# Initialize agents (cached)
@st.cache_resource
def initialize_agents():
    """Initialize all agents once"""
    return {
        'reader': CodeReaderAgent(),
        'writer': CodeWriterAgent(),
        'reviewer': CodeReviewerAgent(),
        'test_gen': TestGeneratorAgent(),
        'doc_writer': DocWriterAgent()
    }


# Title and description
st.title("🤖 Multi-Agent Coding Assistant")
st.markdown("**5 specialized AI agents collaborate to deliver complete coding solutions**")

# Sidebar with agent info
with st.sidebar:
    st.header("🎯 Meet Your Agents")
    
    agents_info = [
        ("📖", "Code Reader", "Analyzes your request"),
        ("✍️", "Code Writer", "Generates clean code"),
        ("🔍", "Code Reviewer", "Reviews for quality"),
        ("🧪", "Test Generator", "Creates pytest tests"),
        ("📝", "Documentation Writer", "Writes docs")
    ]
    
    for emoji, name, desc in agents_info:
        st.markdown(f"**{emoji} {name}**")
        st.caption(desc)
        st.divider()
    
    st.markdown("### 💡 Tips")
    st.info("Be specific in your request for better results!")
    
    st.markdown("### 📊 Example Requests")
    st.code("""• Build a Python function to validate emails
- Create a binary search algorithm
- Write a REST API with FastAPI
- Implement a sorting algorithm
- Build a class for managing tasks""", language="text")


# Main content
col1, col2 = st.columns([3, 1])

with col1:
    user_input = st.text_area(
        "**What would you like to build?**",
        height=120,
        placeholder="Example: Build a Python function that validates email addresses..."
    )

with col2:
    st.markdown("###")  # Spacer
    st.markdown("###")  # Spacer
    process_button = st.button("🚀 Start Agents", type="primary", use_container_width=True)


# Process request
if process_button and user_input:
    # Initialize agents
    agents = initialize_agents()
    
    # Create tabs for results
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📖 Analysis", 
        "✍️ Code", 
        "🔍 Review", 
        "🧪 Tests", 
        "📝 Docs"
    ])
    
    results = {}
    
    # Agent 1: Code Reader
    with tab1:
        with st.spinner("📖 Code Reader analyzing..."):
            results['analysis'] = agents['reader'].analyze(user_input)
        st.success("✅ Analysis complete!")
        st.markdown("### 📖 Code Analysis")
        st.markdown(results['analysis'])
    
    # Agent 2: Code Writer
    with tab2:
        with st.spinner("✍️ Code Writer generating code..."):
            results['code'] = agents['writer'].write_code(results['analysis'], user_input)
        st.success("✅ Code generated!")
        st.markdown("### ✍️ Generated Code")
        st.markdown(results['code'])
    
    # Agent 3: Code Reviewer
    with tab3:
        with st.spinner("🔍 Code Reviewer reviewing..."):
            results['review'] = agents['reviewer'].review_code(results['code'], user_input)
        st.success("✅ Review complete!")
        st.markdown("### 🔍 Code Review")
        st.markdown(results['review'])
    
    # Agent 4: Test Generator
    with tab4:
        with st.spinner("🧪 Test Generator creating tests..."):
            results['tests'] = agents['test_gen'].generate_tests(results['code'], user_input)
        st.success("✅ Tests generated!")
        st.markdown("### 🧪 Unit Tests")
        st.markdown(results['tests'])
    
    # Agent 5: Doc Writer
    with tab5:
        with st.spinner("📝 Documentation Writer writing docs..."):
            results['documentation'] = agents['doc_writer'].generate_docs(results['code'])
        st.success("✅ Documentation complete!")
        st.markdown("### 📝 Documentation")
        st.markdown(results['documentation'])
    
    # Save results
    st.session_state.results = results
    
    # Success message
    st.success("🎉 All 5 agents completed successfully! Check each tab above.")
    
    # Download section
    st.divider()
    st.subheader("📥 Download Results")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Combined report
        full_report = f"""# Multi-Agent Coding Assistant Report
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## User Request
{user_input}

## 📖 Analysis
{results['analysis']}

## ✍️ Generated Code
{results['code']}

## 🔍 Code Review
{results['review']}

## 🧪 Unit Tests
{results['tests']}

## 📝 Documentation
{results['documentation']}
"""
        st.download_button(
            label="📄 Download Full Report",
            data=full_report,
            file_name=f"coding_assistant_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
            mime="text/markdown"
        )
    
    with col2:
        # Code only
        st.download_button(
            label="💻 Download Code",
            data=results['code'],
            file_name=f"generated_code_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py",
            mime="text/plain"
        )
    
    with col3:
        # Tests only
        st.download_button(
            label="🧪 Download Tests",
            data=results['tests'],
            file_name=f"test_code_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py",
            mime="text/plain"
        )

elif process_button and not user_input:
    st.error("⚠️ Please enter your coding request first!")

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: gray;'>
    Built with ❤️ using LangChain, Groq, and Streamlit | Multi-Agent AI System
</div>
""", unsafe_allow_html=True)