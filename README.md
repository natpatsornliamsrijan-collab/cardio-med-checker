# cvs-med-interaction

## Overview
This is a command-line interface (CLI) application designed to identify potential interactions between cardiovascular medications (Heart Medications) and various dietary supplements or food items. The program leverages structured clinical data to provide reliable safety insights for healthcare providers and patients.

## Purpose
Managing heart health often involves multiple medications. Some supplements can interfere with these drugs, causing risks such as bleeding, low blood pressure, or reduced treatment effect.

Cardiovascular diseases are the most common type of noncommunicable diseases (NCDs). According to the World Health Organization (WHO), they are the leading cause of death worldwide.

Because many patients require long-term treatment and often use supplements, this tool helps identify potential interactions and support safer medication use.

For this reason, this project focuses on cardiovascular drugs to support safer medication use.
---

## Core Features

### 1. Drug Group Coverage
The system categorizes medications into major cardiovascular groups, including:
* **Anticoagulants** (e.g., Warfarin)
* **Antiplatelets** (e.g., Aspirin, Clopidogrel)
* **ACE Inhibitors** (e.g., Lisinopril)
* **Beta Blockers** (e.g., Metoprolol)
* **Calcium Channel Blockers** (e.g., Amlodipine)
* **Statins** (e.g., Atorvastatin)
* **Diuretics** (e.g., Furosemide)

### 2. Interaction Classification
Interactions are analyzed based on their physiological impact:
* **Increase Effect:** Higher drug concentration/effect (Risk of toxicity).
* **Decrease Effect:** Lower drug concentration/effect (Risk of treatment failure).
* **Unclear:** Inconclusive data from current clinical studies.

### 3. Severity Scale
| Level | Description |
| :--- | :--- |
| **Major** | High risk of serious outcomes (e.g., bleeding, hospitalization). |
| **Moderate** | Requires clinical monitoring or dose adjustment. |
| **Minor** | Small clinical impact; unlikely to require significant changes. |

---

## Data Sources
The logic and interaction database are based on the following clinical references:

* **World Health Organization (WHO) (2025):** Noncommunicable diseases – global data and statistics on prevalence and mortality.  
* **World Health Organization (WHO) (2025):** Cardiovascular diseases (CVDs) – leading cause of death globally (~19–20 million deaths per year).  
* **Kanji et al. (2012):** Systematic review on supplement–cardiovascular drug interactions.  
* **Tan et al. (2020):** Systematic review on Warfarin and food/herbal interactions.  
* **American Heart Association (AHA):** Standards for drug classification.

## Limitations
* **Prototype Status:** This is a simplified prototype and does not contain a complete database of all known drugs or supplements.
* **Data Gaps:** If an item is not found in the system, the program will trigger a warning—**absence of data does not imply safety.**

---

> [!CAUTION]
> **Medical Disclaimer:** This program is for educational purposes only and does not replace professional medical advice. Always consult with a doctor or pharmacist before making any changes to your medication or diet.

---

## How to Run
Ensure you have Python installed on your system, then run:

```bash
python CVS.py
