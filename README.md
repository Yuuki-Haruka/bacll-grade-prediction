# Cambodia Grade 12 National Exam Predictor

This project is a **Streamlit web application** that predicts:

- Final exam grade (A–F)
- Grade for each subject

based on the **Cambodia Grade 12 (Bac II) national exam system**.

---

## Features

- Select exam track:
  - Science
  - Social Science
- Input scores for each subject
- Automatically:
  - Calculates total score
  - Applies English bonus deduction (-25)
  - Assigns grade for each subject
  - Predicts final exam grade (A–F)
- Displays results in a table
- Shows score visualization (bar chart)
- Download results as CSV file

---

## Grading System

### Final Grade (Total Score)

| Grade | Score Range |
|------|------------|
| A | 427 – 500 |
| B | 380 – 426 |
| C | 332 – 379 |
| D | 285 – 331 |
| E | 237 – 284 |
| F | 0 – 236 |

---

### Subject Grade

#### 125 Marks Subject

| Grade | Range |
|------|------|
| A | 113 – 125 |
| B | 100 – 112 |
| C | 88 – 99 |
| D | 75 – 87 |
| E | 63 – 74 |
| F | 0 – 62 |

---

#### 75 Marks Subject

| Grade | Range |
|------|------|
| A | 68 – 75 |
| B | 60 – 67 |
| C | 53 – 60 |
| D | 45 – 52 |
| E | 38 – 44 |
| F | 0 – 37 |

---

#### 50 Marks Subject

| Grade | Range |
|------|------|
| A | 45 – 50 |
| B | 40 – 44 |
| C | 35 – 39 |
| D | 30 – 34 |
| E | 25 – 29 |
| F | 0 – 24 |

---

## Exam Formula

Final Score = Total Score - 25

**Note:**
- English is treated as a **bonus subject**
- 25 points are deducted from the total score

---

## Project Structure
# Cambodia Grade 12 National Exam Predictor

This project is a **Streamlit web application** that predicts:

- Final exam grade (A–F)
- Grade for each subject

based on the **Cambodia Grade 12 (Bac II) national exam system**.

---

## Features

- Select exam track:
  - Science
  - Social Science
- Input scores for each subject
- Automatically:
  - Calculates total score
  - Applies English bonus deduction (-25)
  - Assigns grade for each subject
  - Predicts final exam grade (A–F)
- Displays results in a table
- Shows score visualization (bar chart)
- Download results as CSV file

---

## Grading System

### Final Grade (Total Score)

| Grade | Score Range |
|------|------------|
| A | 427 – 500 |
| B | 380 – 426 |
| C | 332 – 379 |
| D | 285 – 331 |
| E | 237 – 284 |
| F | 0 – 236 |

---

### Subject Grade

#### 125 Marks Subject

| Grade | Range |
|------|------|
| A | 113 – 125 |
| B | 100 – 112 |
| C | 88 – 99 |
| D | 75 – 87 |
| E | 63 – 74 |
| F | 0 – 62 |

---

#### 75 Marks Subject

| Grade | Range |
|------|------|
| A | 68 – 75 |
| B | 60 – 67 |
| C | 53 – 60 |
| D | 45 – 52 |
| E | 38 – 44 |
| F | 0 – 37 |

---

#### 50 Marks Subject

| Grade | Range |
|------|------|
| A | 45 – 50 |
| B | 40 – 44 |
| C | 35 – 39 |
| D | 30 – 34 |
| E | 25 – 29 |
| F | 0 – 24 |

---

## Exam Formula

Final Score = Total Score - 25

**Note:**
- English is treated as a **bonus subject**
- 25 points are deducted from the total score

---

## Project Structure
bacll-grade-prediction/
│
├── app.py # Streamlit application
├── train_model.py # Save grading rules using pickle
├── gpa_model.pkl # Generated configuration file
├── myenv/ # Virtual environment (optional)
└── README.md

---

## Installation

### 1. Create virtual environment

```bash
python3 -m venv myenv
source myenv/bin/activate