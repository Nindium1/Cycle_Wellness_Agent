# Cycle Wellness Agent: AI-Powered Menstrual Health Companion

## Project Overview

**Cycle Wellness Agent** is an intelligent multi-agent system designed to help individuals track their menstrual cycles, log moods and symptoms, identify patterns, and receive personalized wellness recommendations. Built using Google's Agent Development Kit (ADK), this project demonstrates advanced agentic AI capabilities including sequential agent orchestration, custom tool development, memory management, and comprehensive observability.


## The Problem

Menstrual health tracking is crucial for understanding hormonal patterns and their impact on physical and mental wellbeing. However, existing solutions often fall short in several ways:

1. **Lack of Pattern Recognition**: Most cycle tracking apps simply record data without intelligently analyzing correlations between cycle phases and mood/symptom patterns.

2. **Generic Recommendations**: Users receive one-size-fits-all wellness advice that doesn't account for their unique cycle patterns or current phase.

3. **Mental Health Gap**: The connection between hormonal fluctuations and mental health (anxiety, depression, mood swings) is often overlooked or inadequately addressed.

4. **Data Overload**: Users are overwhelmed with data points but lack actionable insights about what their patterns mean and how to respond.

The Cycle Wellness Agent addresses these gaps by providing an empathetic, intelligent companion that learns individual patterns over time and delivers personalized, phase-appropriate wellness guidance.


## The Solution

### Core Capabilities

The Cycle Wellness Agent offers five integrated features:

1. **Cycle Tracking & Phase Awareness**: Automatically calculates current menstrual cycle phase (menstrual, follicular, ovulation, luteal) based on user-provided period dates and cycle length.

2. **Mood & Symptom Logging**: Enables users to log daily moods (anxious, tired, energetic, etc.) and physical symptoms (cramps, headaches, fatigue).

3. **Pattern Recognition**: Analyzes historical data to identify correlations such as "anxiety tends to spike 5 days before period" or "energy peaks during follicular phase."

4. **Personalized Wellness Recommendations**: Generates phase-appropriate, evidence-based wellness tips tailored to the user's current cycle phase, mood state, and symptoms.

5. **Crisis Detection**: Monitors for concerning mental health indicators and provides immediate crisis resources when needed.


## Architecture

### Multi-Agent Sequential Pipeline

The system employs a **three-agent sequential architecture** where each agent has a specialized role:

#### **Agent 1: Intake Agent** ("Getting to Know You")
- **Role**: Friendly onboarding and data collection
- **Responsibilities**:
  - Welcomes users with warm, supportive language
  - Collects cycle information (last period date, cycle length)
  - Gathers current mood and symptom data
  - **Uses Tool**: Cycle Calculator to determine current phase
- **Output**: Structured intake data passed to Agent 2

#### **Agent 2: Analysis Agent** ("The Pattern Detective")
- **Role**: Data processing and pattern identification
- **Responsibilities**:
  - Receives intake data from Agent 1
  - Analyzes mood/symptom patterns from historical logs
  - Identifies phase-mood correlations
  - Detects crisis signals (severe depression, self-harm mentions)
  - **Uses Tool**: Pattern Analyzer to identify trends
- **Output**: Comprehensive analysis report passed to Agent 3

#### **Agent 3: Wellness Coach Agent** ("Your Supportive Guide")
- **Role**: Personalized wellness recommendations
- **Responsibilities**:
  - Receives analysis from Agent 2
  - Generates phase-appropriate wellness tips
  - Provides crisis resources if signals detected
  - Delivers encouragement and validation
  - **Uses Tools**: Recommendation Generator for personalized tips
- **Output**: Final wellness guidance to user

### Custom Tools

Three custom FunctionTools power the agent capabilities:

1. **Cycle Calculator Tool**
   - Calculates current cycle phase based on last period date
   - Predicts next period date
   - Provides phase-specific descriptions
   - Returns structured data including days in cycle and days until next period

2. **Pattern Analyzer Tool**
   - Processes historical mood logs (JSON format)
   - Identifies phase-mood correlations
   - Tracks symptom frequency
   - Detects overall mood trends (predominantly positive/negative)
   - Returns actionable insights

3. **Recommendation Generator Tool**
   - Takes cycle phase, mood, and symptoms as input
   - Matches user state to curated wellness recommendations
   - Provides phase-appropriate activities and self-care tips
   - Includes mood-specific coping strategies
   - Returns structured recommendation categories

### Memory & State Management

The system implements a **dual-layer memory architecture**:

- **Session Memory** (InMemorySessionService): Maintains conversation context within a single session, enabling agents to reference previous exchanges
- **Long-term Storage** (Custom cycle_data_store): Structured storage for:
  - Cycle information (dates, lengths, phases)
  - Mood logs with timestamps
  - Identified patterns and insights
  - User preferences

This separation allows for both conversational continuity and persistent pattern tracking across multiple sessions.

### Observability

Comprehensive logging tracks all system activities:

- **Agent Transitions**: Start/complete events for each agent
- **Tool Calls**: Arguments and results for all tool invocations
- **Memory Operations**: Data storage and retrieval events
- **Key Events**: Cycle data logged, patterns identified, recommendations generated
- **Pipeline Status**: Overall system success/failure tracking

Logs are output both to console and to `cycle_wellness_agent.log` for audit trails and debugging.


## Technical Implementation

### Technology Stack

- **Framework**: Google Agent Development Kit (ADK)
- **LLM**: Gemini 2.5 Flash Lite
- **Language**: Python 3.11
- **Key Libraries**:
  - `google-genai`: Gemini API integration
  - `google-adk`: Agent orchestration framework
  - `python-dotenv`: Environment configuration
  - `logging`: Observability implementation

### Project Structure

```
Cycle_Wellness_Agent/
├── agents/
│   ├── intake_agent.py          # Agent 1: Data collection
│   ├── analysis_agent.py        # Agent 2: Pattern detection
│   └── wellness_agent.py        # Agent 3: Recommendations
├── tools/
│   ├── cycle_calculator.py      # Phase calculation tool
│   ├── pattern_analyzer.py      # Pattern identification tool
│   └── recommendation_generator.py  # Wellness tips tool
├── utils/
│   ├── logger.py                # Observability system
│   └── memory_manager.py        # Memory & session management
├── config.py                    # Configuration settings
├── setup.py                     # ADK component imports
├── main.py                      # Pipeline orchestration
├── requirements.txt             # Dependencies
└── .env                         # API credentials
```

### ADK Concepts Demonstrated

This project fulfills the capstone requirements by implementing:

1. **Multi-agent System** (Sequential Agents)
   - Three specialized agents working in coordinated pipeline
   - Each agent receives output from previous agent via `output_key` mechanism

2. **Tools** (3 Custom + Built-in potential)
   - Custom FunctionTools: cycle_calculator, pattern_analyzer, recommendation_generator
   - All tools follow proper ADK patterns with type hints and docstrings

3. **Sessions & Memory**
   - InMemorySessionService for conversation state
   - InMemoryMemoryService for potential long-term storage
   - Custom structured storage for cycle-specific data

4. **Observability** (Logging & Tracing)
   - Comprehensive logging system tracking all agent actions
   - Pipeline status monitoring
   - File-based audit trail


## Project Journey

### Development Process

The development followed an iterative approach focused on functionality first, polish second:

**Phase 1: Foundation** (Setup & Structure)
- Created project repository and file structure
- Installed and configured ADK
- Set up API authentication with environment variables
- Established core configuration patterns

**Phase 2: Agent Development**
- Built three agents with distinct personalities and roles
- Defined agent instructions for sequential data flow
- Implemented proper `output_key` connections between agents
- Iterated on agent tone to be warm and supportive

**Phase 3: Tool Creation**
- Developed cycle calculator with date math logic
- Built pattern analyzer for trend identification
- Created recommendation generator with curated wellness database
- Added comprehensive testing for each tool

**Phase 4: Integration & Testing**
- Connected agents in sequential pipeline
- Debugged tool invocation and data passing
- Resolved API key authentication issues
- Fixed parameter type conflicts (List[Dict] → str)

**Phase 5: Memory & Observability**
- Implemented session management
- Built structured cycle data storage
- Created comprehensive logging system
- Added pipeline status tracking

### Key Challenges & Solutions

**Challenge 1: API Authentication**
- *Issue*: Gemini API couldn't access hardcoded API key in config
- *Solution*: Implemented `.env` file with `python-dotenv` for proper environment variable loading

**Challenge 2: Tool Parameter Complexity**
- *Issue*: Pattern analyzer using `List[Dict]` parameter caused API rejection
- *Solution*: Simplified to JSON string parameter, parsed internally

**Challenge 3: Agent Data Flow**
- *Issue*: Agents responding independently rather than sequentially
- *Solution*: Clarified agent instructions to explicitly reference previous agent outputs via `output_key`

**Challenge 4: Conversation vs Pipeline**
- *Issue*: Initial design expected multi-turn conversation, but sequential agents run all at once
- *Solution*: Adjusted input format to provide complete data upfront for demonstration purposes


## Future Enhancements

While the current implementation successfully demonstrates core ADK concepts, several enhancements would improve real-world usability:

1. **Interactive Conversation Loop**: Implement true multi-turn conversations where users respond to agent questions iteratively

2. **Persistent Database**: Replace in-memory storage with actual database (PostgreSQL/Firebase) for data persistence across sessions

3. **Historical Pattern Analysis**: Build machine learning models to predict future symptoms based on accumulated cycle data

4. **Web Interface**: Deploy as web application with user-friendly UI for easier interaction

5. **Google Search Integration**: Re-enable google_search tool once tool compatibility issues resolved for evidence-based research

6. **Export Functionality**: Allow users to export their cycle data and insights as PDF reports

7. **Reminder System**: Implement proactive notifications for upcoming cycle phases or symptom predictions



## Conclusion

The Cycle Wellness Agent demonstrates the power of multi-agent AI systems to address real human needs with empathy and intelligence. By combining sequential agent orchestration, custom tool development, memory management, and comprehensive observability, this project creates a foundation for personalized menstrual health support.

The journey from concept to implementation highlighted both the capabilities and constraints of the ADK framework while reinforcing the importance of user-centered design in AI applications. Most importantly, it showcases how AI can serve as a supportive companion in navigating the complex intersection of hormonal health and mental wellbeing.

**Target Users**: Women of reproductive age seeking to understand their cycle patterns and improve wellbeing

**Project Significance**: Addresses the mental health gap in cycle tracking by providing intelligent, personalized support that goes beyond simple data logging
