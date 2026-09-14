# 🌱 TerraLoop

## Measure Waste. Close the Loop.

TerraLoop is a Python-based smart household waste and recycling management system designed to help households track, analyze, and improve their waste-management habits.

The application allows users to record daily waste, monitor recycling performance, identify high-waste categories, receive actionable sustainability recommendations, and experiment with **What-If scenarios** to understand the potential impact of waste reduction.

---

## 🎯 Problem Statement

Households generate different types of waste every day, but waste is often discarded without being properly measured or analyzed.

This creates several challenges:

- It is difficult to identify which category produces the most waste.
- Recycling habits are difficult to measure.
- Households may not recognize their major waste-management problems.
- General sustainability advice may not address a household's specific waste patterns.
- Users have limited ways to understand how changing their habits could affect their waste profile.

TerraLoop addresses these problems by turning household waste records into understandable statistics, insights, recommendations, and simulations.

---

## 💡 Our Solution

TerraLoop follows a simple workflow:

**Record → Analyze → Understand → Improve**

Users can:

1. Record waste by category.
2. Enter the weight of each waste record.
3. Mark whether the waste was recycled.
4. Search, update, and delete records.
5. Analyze waste by category.
6. Calculate the household recycling rate.
7. Identify the highest-waste category.
8. Receive rule-based sustainability recommendations.
9. View a custom sustainability score.
10. Experiment with waste-reduction scenarios.
11. Generate a summary report for a selected period.

---

# ✨ Key Features

## 🗑️ Waste Management

- Add waste records
- Update existing records
- Delete waste records
- Search records
- Filter records by category
- Record waste weight
- Record recycling status
- Add notes to individual records
- Prevent invalid waste entries

---

## 📊 Waste Analysis

TerraLoop calculates and displays:

- Total waste generated
- Total recycled waste
- Recycling rate
- Category-wise waste distribution
- Category-wise percentages
- Highest-waste category
- E-waste contribution
- Waste-management statistics for selected periods

---

## 🔥 Waste Hotspot Analyzer

The Waste Hotspot Analyzer identifies the category contributing the largest amount of waste.

For example:

> If plastic represents the largest share of recorded waste, TerraLoop identifies plastic as the current waste hotspot.

This helps users focus their efforts on the areas where improvement could have the greatest impact.

---

## 🌱 Sustainability Score

TerraLoop provides a custom Sustainability Score based on the household's recorded waste-management performance.

The score is designed to provide a simple way for users to understand their current performance and identify areas for improvement.

### Important Note

The Sustainability Score is a **custom scoring model created for this prototype**. It is not an officially standardized or scientifically validated environmental index.

Future versions can improve the scoring model using real-world datasets, expert-defined environmental indicators, and validated sustainability benchmarks.

---

## 💡 Recommendation Engine

TerraLoop analyzes recorded waste patterns and generates actionable recommendations.

Examples include:

- Reducing excessive plastic waste
- Improving paper recycling
- Composting suitable organic waste
- Improving glass recycling
- Increasing metal recycling
- Handling e-waste responsibly
- Improving overall recycling performance

### Recommendation Approach

The current Recommendation Engine is **rule-based**.

It uses predefined conditions based on the user's recorded waste data rather than machine-learning models.

Therefore, TerraLoop does **not** claim that its recommendation system is artificial intelligence.

---

## 🔬 What-If Simulator

The What-If Simulator allows users to explore hypothetical waste-reduction scenarios.

For example:

> What happens if plastic waste is reduced by 30%?

TerraLoop creates a hypothetical version of the household's waste data and compares the scenario with the current data.

This allows users to understand how changing waste-generation patterns could affect their overall waste profile.

---

# 🌍 Sustainable Development Goals

TerraLoop supports multiple United Nations Sustainable Development Goals.

## 🏙️ SDG 11 — Sustainable Cities and Communities

TerraLoop encourages responsible household waste management, which contributes to cleaner and more sustainable communities.

## ♻️ SDG 12 — Responsible Consumption and Production

The project helps users understand their consumption-related waste and encourages better recycling and waste-management practices.

## 🌎 SDG 13 — Climate Action

Better waste management and increased recycling can contribute to more sustainable resource use and support climate-conscious behavior.

---

# 🧠 Object-Oriented Programming

TerraLoop is developed using Python and follows an Object-Oriented Programming structure.

The main classes include:

### `Household`

Stores household information such as:

- Household name
- Number of members

### `WasteRecord`

Represents an individual waste entry.

It stores:

- Record ID
- Date
- Waste category
- Weight
- Recycling status
- Notes

### `WasteManager`

Responsible for managing waste records.

It handles operations such as:

- Adding records
- Updating records
- Deleting records
- Searching records
- Filtering records

### `WasteAnalyzer`

Responsible for calculating:

- Total waste
- Recycled waste
- Recycling rate
- Category breakdown
- Category percentages
- Waste hotspot
- Sustainability score

### `RecommendationEngine`

Analyzes waste-management patterns and generates rule-based recommendations.

### `SustainabilitySimulator`

Creates hypothetical waste scenarios and compares them with the current household data.

### `TerraLoopApp`

Controls the graphical user interface and connects the different components of the application.

---

# 🏗️ Project Architecture

TerraLoop follows a modular structure:

```text
User
  │
  ▼
TerraLoopApp
  │
  ├── Household
  │
  ├── WasteManager
  │      │
  │      └── WasteRecord
  │
  ├── WasteAnalyzer
  │
  ├── RecommendationEngine
  │
  └── SustainabilitySimulator
