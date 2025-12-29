# AI Student Productivity Agent

This project was built as part of an online hackathon.

## Problem
Students often use simple to-do lists that do not understand task priority, urgency, or workload.  
Such tools also do not help in deciding what task should be done next.

## Solution
This project implements an AI-based productivity agent that:
- Understands tasks written in natural language
- Automatically prioritizes student-related tasks
- Schedules tasks using a calendar tool
- Maintains memory to suggest the next best task

## How It Works
The agent follows an agentic workflow:
1. Interprets the user’s task
2. Extracts task details and assigns priority
3. Schedules the task using a calendar tool
4. Stores tasks in memory
5. Suggests the next task when asked

## Features
- Student-focused priority logic
- Memory-based task recommendation
- Explainable decision-making
- Minimal Streamlit user interface

## Tech Stack
- Python
- Streamlit
- Rule-based agent logic

## Limitations
- Lightweight language understanding
- Session-based memory only
- No real calendar API integration

## Future Improvements
- Integration with real language models
- Persistent memory across sessions
- Real calendar service integration

## How to Run
```bash
pip install streamlit
streamlit run ui.py
