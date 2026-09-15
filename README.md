# 🌱 TerraLoop

## Measure Waste. Close the Loop.

TerraLoop is a Python-based **Smart Household Waste & Recycling Manager** designed to help households record, analyze, and improve their waste-management habits.

The project combines **Object-Oriented Programming, data analysis, graphical user interfaces, and sustainability concepts** to turn everyday waste data into useful insights and actionable recommendations.

---

# 📸 Application Preview

## Dashboard

![TerraLoop Dashboard](images/Screenshot%202026-09-14%20192722.png)

## Add Waste

![TerraLoop Add Waste](images/Screenshot%202026-09-14%20192743.png)

## Records

![TerraLoop Records](images/Screenshot%202026-09-14%20192803.png)

## Analysis

![TerraLoop Analysis](images/Screenshot%202026-09-14%20192820.png)

## Recommendations

![TerraLoop Recommendations](images/Screenshot%202026-09-14%20192833.png)

## What-If Simulator

![TerraLoop What-If Simulator](images/Screenshot%202026-09-14%20192844.png)

---

# 📖 Project Overview

Household waste is often produced every day but rarely measured or analyzed.

TerraLoop provides a simple way to:

- Record daily household waste
- Categorize different types of waste
- Track recycling
- Analyze waste patterns
- Identify high-waste categories
- Calculate a sustainability score
- Receive rule-based recommendations
- Simulate possible waste-reduction scenarios
- Generate summary reports

The goal is to transform waste management from a passive activity into a **data-driven and interactive process**.

---

# 🎯 Problem Statement

Many households know that waste management is important, but they do not have an easy way to understand:

- How much waste they produce
- Which category produces the most waste
- How much of their waste is recycled
- Where their biggest waste-management problems are
- What improvements they should make

TerraLoop addresses this problem by converting recorded waste data into understandable statistics, insights, and recommendations.

---

# 💡 Our Solution

TerraLoop provides a desktop application where users can record household waste and receive meaningful analysis.

The application follows the process:

**Record → Analyze → Identify → Improve → Simulate**

This allows users to understand their current waste patterns and explore what could happen if they reduce waste in specific categories.

---

# ✨ Key Features

### 📝 Waste Recording
Add waste records containing:

- Date
- Category
- Weight
- Recycling status
- Notes

### 📋 Record Management
Users can:

- Add records
- Search records
- Filter records
- Edit records
- Delete records

### 📊 Waste Analysis
TerraLoop calculates:

- Total waste
- Recycled waste
- Recycling rate
- Category-wise distribution
- Category percentages
- Waste hotspot
- E-waste percentage

### 🌱 Sustainability Score
A project-defined score summarizes the recorded waste-management performance.

### 💡 Recommendation Engine
The application provides rule-based suggestions based on waste patterns.

### 🔬 What-If Simulator
Users can simulate a reduction in a selected waste category without changing their original data.

### 📄 Reports
Users can generate a summary report for a selected period.

---

# 🧠 Object-Oriented Programming

Object-Oriented Programming is a major part of TerraLoop's architecture.

The project divides different responsibilities into separate classes.

## `Household`

Represents the household using TerraLoop.

Stores:

- Household name
- Number of members

## `WasteRecord`

Represents an individual waste entry.

Stores:

- Record ID
- Date
- Waste category
- Weight
- Recycling status
- Notes

## `WasteManager`

Manages the collection of waste records.

Responsibilities include:

- Adding records
- Updating records
- Deleting records
- Searching records
- Filtering records

## `WasteAnalyzer`

Performs calculations and analysis.

Responsibilities include:

- Total waste
- Recycled waste
- Recycling rate
- Category breakdown
- Category percentages
- Waste hotspot detection
- E-waste analysis
- Sustainability score

## `RecommendationEngine`

Analyzes waste patterns and generates **rule-based sustainability recommendations**.

## `SustainabilitySimulator`

Creates hypothetical versions of the waste dataset and allows users to explore possible waste-reduction scenarios.

## `TerraLoopApp`

Controls the Tkinter graphical interface and connects the major components of the application.

---

# 🏗️ System Architecture

TerraLoop follows a modular architecture where different classes handle different responsibilities.

```text
                         ┌──────────────────┐
                         │       USER       │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │  TerraLoopApp    │
                         │    Tkinter GUI   │
                         └────────┬─────────┘
                                  │
             ┌────────────────────┼────────────────────┐
             │                    │                    │
             ▼                    ▼                    ▼
     ┌────────────────┐  ┌────────────────┐  ┌─────────────────────┐
     │ WasteManager   │  │ WasteAnalyzer  │  │ RecommendationEngine│
     └───────┬────────┘  └────────────────┘  └─────────────────────┘
             │
             ▼
     ┌────────────────┐
     │  WasteRecord   │
     └────────────────┘
                                  │
                                  ▼
                     ┌────────────────────────┐
                     │ SustainabilitySimulator│
                     └────────────────────────┘
```

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Tkinter | Graphical User Interface |
| Pillow | Image generation and image handling |
| `datetime` | Date and time handling |
| Object-Oriented Programming | Application architecture |
| Git / GitHub | Version control and source-code hosting |

---

---

# ⚙️ Installation

## Prerequisites

- Python 3.x
- pip

Check Python:

```bash
python --version
```

Install Pillow:

```bash
pip install pillow
```

Tkinter is included with most standard Python installations on Windows.

---

# ▶️ How to Run

Open a terminal inside the TerraLoop project directory and run:

```bash
python First.py
```

The TerraLoop graphical interface should launch.

---

# 📖 How to Use

### 1. Launch TerraLoop

Run:

```bash
python First.py
```

The dashboard will open.

### 2. Add Waste

Open **Add Waste** and enter:

- Date
- Waste category
- Weight
- Recycling status
- Optional notes

### 3. Manage Records

Open **Records** to:

- View records
- Search records
- Filter records
- Edit records
- Delete records

### 4. Analyze Waste

Open **Hotspot & Analysis** to view:

- Total waste
- Recycled waste
- Recycling rate
- Category distribution
- Waste hotspot
- Sustainability score

### 5. View Recommendations

Open **Recommendations** to receive suggestions based on the recorded waste data.

### 6. Try What-If Mode

Open **What-If Simulator**, select a category and reduction percentage, and compare the hypothetical results.

The original records are not modified.

### 7. Generate a Report

Open **Report**, select the required period, and generate a summary.

---

# 🧪 Testing

TerraLoop was tested using sample data and different types of user input.

| Test Case | Expected Result |
|---|---|
| Add valid waste record | Record is added successfully |
| Enter negative weight | Input is rejected |
| Enter zero weight | Input is rejected |
| Enter invalid date | Input is rejected |
| Edit an existing record | Record is updated |
| Delete a record | Record is removed |
| Search by category | Matching records are displayed |
| Filter by category | Selected category is displayed |
| Calculate total waste | Correct total is calculated |
| Calculate recycling rate | Correct percentage is calculated |
| Identify hotspot | Highest-waste category is identified |
| Generate recommendations | Relevant recommendations are displayed |
| Run What-If simulation | Hypothetical results are generated |
| Generate report | Selected-period summary is generated |

---

# 📊 Sustainability Score

TerraLoop includes a **custom Sustainability Score** designed specifically for this prototype.

The score is intended to:

- Summarize waste-management performance
- Encourage better waste-management habits
- Highlight areas for improvement
- Make waste analysis easier to understand

## ⚠️ Important Limitation

The TerraLoop Sustainability Score is **not an officially standardized or scientifically validated environmental index**.

It is a **project-defined metric created for this prototype**.

Future versions could refine the score using:

- Validated environmental indicators
- Real-world waste-management datasets
- Expert-defined sustainability benchmarks
- Region-specific standards

---

# 💡 Recommendation Engine

The Recommendation Engine currently uses predefined rules based on the user's waste data.

For example:

```text
IF plastic waste is high
        ↓
Recommend reducing unnecessary plastic use
```

Another example:

```text
IF recycling rate is low
        ↓
Recommend improving recycling practices
```

This approach makes the system:

- Predictable
- Explainable
- Easy to understand

> The Recommendation Engine is currently **rule-based, not machine-learning based**.

---

# 🔬 What-If Simulator

The What-If Simulator allows users to explore possible waste-reduction scenarios.

```text
Current Waste
     ↓
Select Category
     ↓
Select Reduction %
     ↓
Create Hypothetical Dataset
     ↓
Analyze New Scenario
     ↓
Compare Results
```

The original records remain unchanged during the simulation.

---

# 🌍 SDG Alignment

TerraLoop supports the following United Nations Sustainable Development Goals.

## 🏙️ SDG 11 — Sustainable Cities and Communities

TerraLoop encourages responsible household waste management and helps users understand their waste-generation patterns.

## ♻️ SDG 12 — Responsible Consumption and Production

TerraLoop supports responsible consumption by helping users:

- Track waste
- Understand waste categories
- Monitor recycling
- Identify waste hotspots
- Improve waste-management practices

## 🌎 SDG 13 — Climate Action

Improved resource use and responsible waste-management practices can contribute to broader environmental sustainability.

TerraLoop provides information that can encourage more environmentally responsible decisions.

---

# ⚠️ Limitations

### 1. Custom Sustainability Score

The score is project-defined and is not an officially standardized environmental index.

### 2. User-Entered Data

Analysis depends on the accuracy of the information entered by users.

### 3. Rule-Based Recommendations

Recommendations currently use predefined rules instead of machine-learning models.

### 4. No Automatic Waste Recognition

The prototype does not currently identify waste automatically using computer vision.

### 5. No Smart-Bin Integration

The application does not directly connect to smart bins, weighing sensors, or IoT hardware.

### 6. Limited Dataset

The prototype primarily works with household-level recorded data.

### 7. Further Validation Required

The sustainability model would require additional testing and expert validation before being used as a real-world benchmark.

---

# 🚀 Future Scope

TerraLoop can be expanded into a larger waste-management platform.

### 📱 Mobile Application
Develop Android and iOS applications for easier waste recording.

### 🌐 Web Application
Convert the desktop application into a web-based platform.

### ☁️ Cloud Synchronization
Allow users to securely synchronize their data across devices.

### 📡 IoT Smart-Bin Integration
Connect TerraLoop with smart bins and sensors for automated measurements.

### ⚖️ Automatic Waste Weighing
Integrate digital weighing systems to reduce manual data entry.

### 📷 Computer Vision
Use image classification to automatically identify waste categories.

### 🤖 Machine Learning
Use machine-learning models for personalized recommendations and pattern detection.

### 📈 Advanced Analytics
Add long-term trends, comparisons, charts, and predictive analytics.

### 🏙️ Community-Level Analysis
Allow anonymized household data to contribute to community-level insights.

### 🏆 Gamification
Introduce achievements, streaks, challenges, goals, and household milestones.

### 🌍 Regional Benchmarks
Compare waste-management performance with appropriate regional benchmarks.

### 📄 Advanced Reporting
Future versions could generate professionally formatted PDF reports.

---

# 🎯 Project Impact

TerraLoop aims to make household waste management:

**Measurable → Understandable → Actionable**

Instead of simply asking:

> "How much waste do we produce?"

TerraLoop encourages users to ask:

- What type of waste are we producing?
- How much are we recycling?
- Where is our biggest waste problem?
- What should we improve?
- What could happen if we changed our habits?

This makes waste management a more **data-driven and interactive activity**.

---

# 🌱 Why TerraLoop?

The name **TerraLoop** combines two ideas.

### Terra

Represents the Earth and our environment.

### Loop

Represents the idea of keeping materials in productive use through reuse and recycling instead of treating them as unnecessary waste.

Therefore:

> **TerraLoop = Creating a better loop between people, resources, and the planet.**

---

# 🏆 Hackathon Information

| Information | Details |
|---|---|
| Competition | Myra's Global Tech HACK-AI-THON 2026 |
| Project | TerraLoop |
| Project Type | Smart Household Waste & Recycling Manager |
| Language | Python |
| GUI | Tkinter |
| Programming Approach | Object-Oriented Programming |
| SDGs | SDG 11, SDG 12, SDG 13 |
| Tagline | Measure Waste. Close the Loop. |

---

# 🔗 Source Code

The main application source code is:

```text
First.py
```

The repository also contains the screenshots used in this README.

---

# 👥 Team Contributions

This project was developed collaboratively by four team members, with each member responsible for a specific part of the project.

| **Team Member** | **Role** | **Contribution** |
|---|---|---|
| **Satvik** | Documentation & GitHub | Prepared the project documentation, organized the GitHub repository, maintained the README, and documented the project's features and technical details. |
| **Kanav** | Python Development | Developed the main Python application, including the OOP structure, waste-management logic, analysis features, recommendation engine, simulator, and Tkinter interface. |
| **Nipun** | Presentation | Prepared the project presentation and organized the key points used to explain TerraLoop, its features, technical approach, and impact. |
| **Tanvi** | Video & Demonstration | Created the project demonstration video and explained the project, including its features and working. |

# 🏁 Conclusion

TerraLoop demonstrates how **Python, Object-Oriented Programming, data analysis, graphical interfaces, and sustainability concepts** can be combined to create a practical technology solution.

The core concept is:

**Measure → Understand → Identify → Improve → Close the Loop**

Although TerraLoop is currently a prototype, its modular architecture provides a foundation for future development involving:

- IoT
- Machine Learning
- Computer Vision
- Cloud Platforms
- Mobile Applications
- Advanced Analytics
- Community-Level Data

---

# 🌱 TerraLoop

## Measure Waste. Close the Loop.

**Built with Python ♻️ | Designed for Sustainability 🌍 | Powered by Data 📊**
