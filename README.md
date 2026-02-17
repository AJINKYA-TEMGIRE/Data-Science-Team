# Agentic Multi-Agent Data Science Automation Platform

## Overview

This project implements an **agentic AI system that automates the end-to-end data science workflow** using a collaborative team of specialized AI agents.
Instead of relying on a single LLM, the platform simulates a real data science team structure where agents coordinate, delegate tasks, and execute tools to complete complex objectives.

The system can assist with:

* Data discovery and loading
* Exploratory data analysis
* Visualization generation
* Machine learning code development
* File and environment management
* Pipeline orchestration

This project demonstrates applied concepts in:

* Agentic AI
* Multi-agent orchestration
* Tool-grounded reasoning
* Autonomous workflow execution
* Modular ML system design

---

## Architecture

### Team Leader

A central **Data Science Team Agent** coordinates workflow execution by assigning tasks to specialized agents based on capability and context.

### Specialized Agents

| Agent              | Responsibility                          |
| ------------------ | --------------------------------------- |
| Data Loader        | CSV discovery and ingestion             |
| File Manager       | Filesystem navigation and manipulation  |
| Data Understanding | Pandas-based exploration and statistics |
| Visualization      | Chart creation and plotting             |
| Coding Agent       | Machine learning and Python development |
| Shell Agent        | Controlled environment execution        |

Each agent has:

* Tool-restricted permissions
* Task-specific instructions
* Shared contextual memory
* Controlled execution boundaries

---

## Key Features

* Multi-agent collaborative reasoning
* Modular architecture for easy extension
* Tool-based execution instead of pure prompting
* Session memory and contextual awareness
* Safe shell execution constraints
* ML pipeline automation support
* Designed for experimentation and scalability

---

## Tech Stack

* Python
* Agentic AI Framework (Agno)
* Groq LLM Integration
* Pandas
* Matplotlib
* DuckDuckGo Search Tools
* SQLite Session Memory
* Modular Tool Interfaces

---

## Project Structure

```
project-root/
│
├── data/
│   └── Pune_property_data.csv
│
├── agents/
│   └── agent_definitions.py
│
├── memory.db
├── main.py
└── README.md
```

---

## Installation

### 1️⃣ Clone Repository

```
git clone https://github.com/AJINKYA-TEMGIRE/Data-Science-Team.git
cd Data-Science-Team
```

### 2️⃣ Install Dependencies

Using uv (recommended)

```
uv sync
```

Or pip

```
pip install -r requirements.txt
```

---

## Environment Setup

Create a `.env` file:

```
GROQ_API_KEY=your_key_here
```

---

## Running the System

```
python app.py
```

This launches the CLI interface where you can interact with the agent team.

---

## Example Use Cases

* Load and explore new datasets
* Generate statistical summaries
* Produce visual insights
* Build ML model scripts
* Assist with feature engineering
* Rapid experimentation workflows

---

## Design Philosophy

This project explores the shift from:

Single LLM Prompting
➡️ Autonomous Agent Collaboration

The architecture focuses on:

* Task decomposition
* Capability specialization
* Safe tool grounding
* Human-in-the-loop validation
* Extendable intelligent systems

---

## Future Improvements

* UI Dashboard Interface
* Vector memory integration
* Automated model evaluation loops
* Dataset version tracking
* Experiment logging
* Cloud execution support
* Autonomous hyperparameter tuning agents

---

## Author

Ajinkya Temgire
ML Engineer | AI Systems Builder
