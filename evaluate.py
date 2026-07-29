import pandas as pd

# Load the audit results
results = pd.read_csv("results.csv")

print("=== Audit Summary ===")
print(f"Total advertisements: {len(results)}")

print("\nDecision counts:")
print(results["decision"].value_counts())

print("\nDecision percentages:")
print((results["decision"].value_counts(normalize=True) * 100).round(2))

print("\nEvaluation script completed.")

# ---------------------------------------------------------
# If a ground truth file is provided later, you can extend
# this script to calculate:
# - Accuracy
# - Precision
# - Recall
# - F1-score
# ---------------------------------------------------------
