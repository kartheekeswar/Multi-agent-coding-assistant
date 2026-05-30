---
title: Multi Agent Coding Assistant
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: "1.39.0"
app_file: app.py
pinned: false
python_version: "3.11"
---

# Multi-Agent Coding Assistant

A production-ready AI application where 5 specialized agents collaborate to deliver complete coding solutions.

## Live Demo

https://huggingface.co/spaces/Kartheek321/multi-agent-coding-assistant

## Overview

Enter any coding request and watch 5 AI agents work together to deliver analysis, code, review, tests, and documentation.

## Agents

- Code Reader - Analyzes your request and identifies requirements
- Code Writer - Generates clean, production-ready code
- Code Reviewer - Reviews code quality and suggests improvements
- Test Generator - Creates comprehensive pytest test suites
- Documentation Writer - Writes professional markdown documentation

## Tech Stack

Frontend: Streamlit
LLM API: Groq (Llama-3.3-70B, Llama-3.1-8B)
AI Framework: LangChain
Deployment: HuggingFace Spaces, GitHub CI/CD
Language: Python 3.11

## Local Setup

Clone repository:
git clone https://github.com/Kartheek321/multi-agent-coding-assistant.git
cd multi-agent-coding-assistant

Install dependencies:
pip install -r requirements.txt

Add API key:
echo "GROQ_API_KEY=your_key" > .env

Run app:
streamlit run app.py

## Project Structure

```
multi-agent-coding-assistant/
├── app.py                    Main Streamlit application
├── orchestrator.py           Agent orchestration logic
├── agents/
│   ├── code_reader.py        Analyzes coding requests
│   ├── code_writer.py        Generates code
│   ├── code_reviewer.py      Reviews code quality
│   ├── test_generator.py     Creates unit tests
│   └── doc_writer.py         Writes documentation
├── prompts/
│   └── agent_prompts.py      Prompt templates for all agents
├── requirements.txt          Python dependencies
└── packages.txt              System packages
```

## Technical Skills Demonstrated

- Multi-agent AI system design and implementation
- LangChain integration with multiple LLM models
- Production-ready Streamlit application development
- Prompt engineering for specialized AI agents
- End-to-end deployment with CI/CD pipeline
- Agent orchestration and workflow management

## Connect

Live App: https://huggingface.co/spaces/Kartheek321/multi-agent-coding-assistant
