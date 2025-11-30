# Cycle_Wellness_Agent
AI-powered cycle wellness coach using multi-agent architecture to support mental health through reproductive health awareness

## Table of Contents
1. [Project Overview](#project-overview)
2. [Problem Statement](#problem-statement)
3. [Solution](#solution)
4. [Architecture](#architecture)
5. [Core Features](#core-features)
6. [Folder Structure](#folder-structure)
7. [Setup Instructions](#setup-instructions)
8. [Technologies Used](#technologies-used)
9. [License](#license)

## Project Overview
Cycle Wellness Agent is an AI-powered sequential multi-agent system whose users are women of reproductive age, basically women who've started menstruating, and have not reached menopause yet. The agent does the following: 
- Track menstrual cycles and user's symptoms
- Take note of user's mood and energy levels
- Detect patterns across cycles
- Deliver phase-specific wellness guidance
- Provide alerts for concerning emotional symptoms/patterns

This project was built for the capstone project of the **5-Day AI Agents Intensive Course with Google** run by Kaggle and Google. It falls in the *Agents for Good* track.

## Problem Statement
Many women of reproductive age find it challenging to understand how their menstrual cycle affects mood, energy, and overall wellbeing. Manual tracking can be time-consuming, and insights from symptoms are often overlooked and not always readily available. Therefore, there is a need for an AI-powered system that combines cycle tracking with personalized wellness guidance.

## Solution
Cycle Wellness Agent provides an intelligent, supportive assistant that:
- Collects cycle and symptom data
- Identifies patterns in mood and physical symptoms
- Offers personalized, phase-based recommendations
- Detects concerning emotional trends and suggests supportive resources

The solution offered by this agent is modular, sequential, and scalable. Each of the agents specializes in a task to provide an accurate and empathetic user experience.

## Architecture
Cycle Wellness Agent uses a **Sequential Multi-Agent System**, with 3 agents as below:

1. **Intake Agent** – Welcomes the user and collects initial cycle info (last period date, average cycle length, symptoms)
2. **Analysis Agent** – Processes data and identifies patterns, analyzes trends, and generates insights.
3. **Wellness Coach Agent** – Provides phase-based wellness recommendations, fetches evidence-based tips using Google Search, and stores insights in memory.

**Custom Tools**:  
- **Cycle Calculator** calculates phase, predicts next period
- **Pattern Analyzer** analyzes mood trends from stored data  
- **Recommendation Generator**: matches phase + mood to wellness tips 

**Built-In Tools**
**Google Search** fetch evidence-based mental health strategies

**Memory Bank** Uses an in-memory memory system to manage user sessions, cycle data, mood logs, and insights. This enables the agent to provide personalized, context-aware recommendations and track patterns over time.

**Observability and Logging** Comprehensive logging system to track agent behavior, tool usage, memory operations, session events, and key interactions. This ensures full observability of the system, making debugging, evaluation, and monitoring easier.

**Agent Flow Diagram:**  

User Input → Agent 1 (Intake) → Agent 2 (Analysis) → Agent 3 (Wellness Coach) → Response to User
                                                              ↓
                                                        Memory Bank
                                                    (stores everything)

## Core Features
1. **Cycle Tracking & Phase Awareness** User inputs cycle start date, length, symptoms; Calculates menstrual, follicular, ovulation, and luteal phases; Stores the info in Memory Bank.
2. **Mood & Symptom Logging** – Daily check-ins to capture mood, energy, and physical symptoms; track mood, energy, anxiety levels, and physical symptoms; link symptoms to cycle phase.
3. **Pattern Recognition & Insights** – Identifies recurring patterns, triggers, and trends  
4. **Personalized Wellness Recommendations** – Suggests coping strategies based on cycle phase and mood trends  
5. **Crisis Pattern Detection** – Detects concerning emotional patterns and provides supportive resources immediately

## Folder Structure

- `agents/` 
  - Intake Agent
  - Analysis Agent
  - Wellness Agent
- `tools/` 
  - Cycle Calculator
  - Pattern Analyzer
  - Recommendation Generator
- `utils/` 
  - Logger
  - Memory Manager
- `.gitignore`
- `LICENSE`
- `README.md` – Project documentation
- `config.py` – Configuration settings
- `main.py` – Entry point to test the agent system
- `requirements.txt` – Python dependencies
- `setup.py` – Install ADK components
- `test_intake_agent.py`


## Setup Instructions
### Clone the repository
git clone https://github.com/Nindium1/Cycle_Wellness_Agent.git
cd Cycle_Wellness_Agent

### Create Virtual Environment
 [Use either of the following depending on your system:]
python -m venv venv
or
py -m venv venv

### Activate the virtual environment
venv\Scripts\activate [Windows]
source venv/bin/activate [MacOS/ Linux]

### Install dependencies
pip install -r requirements.txt

### Run the agent system
py main.py


## Technologies Used
Python 3.10+
Gemini / LLM Agents
Google Search API
Custom multi-agent architecture
Memory Bank for state & session management

## License
MIT License.
