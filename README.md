# 🧠 Life Admin Assistant

## Overview
The **Life Admin Assistant** is a Python-based productivity system designed to help users manage tasks, make better decisions, and monitor mental workload using a stress-driven adaptive model.

The system simulates real-life decision-making by adjusting recommendations based on the user’s stress level.

---

## 🚀 Features

### 1. Decision Helper
- Evaluates multiple options
- Uses weighted scoring system:
  - importance
  - urgency
  - effort
  - long-term benefit
- Adjusts weights based on system mode
  
---

### 2. Task Prioritiser
- Takes multiple tasks as input
- Assigns priority based on:
  - importance
  - urgency (derived from deadline)
  - stress factor
- Sorts tasks in order of priority

---

### 3. Mental Load Checker
- Calculates stress score based on:
  - stress level
  - sleep hours
  - workload
- Dynamically assigns system mode:
  - SURVIVAL
  - BALANCED
  - OPTIMISED
    
---

### 4. Logging System
- Stores all user interactions in a log file
- Tracks:
  - decisions made
  - task prioritisation results
  - mental load evaluations

---

## ⚙️ Core Concept

The system is **state-driven**, meaning all decisions depend on the current stress level:

- 🔴 **SURVIVAL MODE** → prioritises urgency and short-term survival tasks  
- 🟡 **BALANCED MODE** → balanced decision-making  
- 🟢 **OPTIMISED MODE** → focuses on long-term productivity

This creates a dynamic and adaptive assistant that mimics human decision fatigue.

---

## ▶️ How to Run

```bash
python main.py
