# AI Agent for Advertisement Auditing

## Overview

This project implements a rule-based AI agent that audits advertisements against a product catalogue and advertising policy.

The agent classifies each advertisement into one of the following decisions:

- **Pass** – Advertisement is valid.
- **Auto Fix** – Advertisement price is corrected using the catalogue price.
- **Escalate** – Advertisement requires human review due to policy violations.

---

## Project Workflow

```text
Advertisement
      │
      ▼
Retrieve Product by SKU
      │
      ▼
Check Product Status
      │
      ▼
Check Prohibited Claims
      │
      ▼
Check Attribute-backed Claims
      │
      ▼
Check Price
      │
      ▼
Generate Decision
```

---

## Decision Logic

The agent follows the decision precedence below:

1. **Escalate**
   - Product is discontinued
   - Prohibited claim detected
   - Unsupported attribute-backed claim

2. **Auto Fix**
   - Advertised price differs from catalogue price

3. **Pass**
   - Product is active
   - Price matches
   - No policy violations

---

## Technologies Used

- Python
- Pandas
- Google Colab

---

## Project Files

| File | Description |
|------|-------------|
| ADA assessment (agent)_Nuradilla.ipynb | Main notebook |
| results.csv | Generated audit results |
| README.md | Project documentation |

---

## Output Schema

The generated CSV contains the following columns:

| Column | Description |
|--------|-------------|
| ad_id | Advertisement ID |
| decision | pass / auto_fix / escalate |
| corrected_value | Corrected catalogue price (auto_fix only) |
| reason | Explanation for the decision |

---

## Future Improvements

Future versions of the agent could integrate a Large Language Model (LLM) to interpret paraphrased advertising claims while keeping deterministic rule validation for business-critical checks.
