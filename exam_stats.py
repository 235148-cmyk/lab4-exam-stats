import pandas as pd
import numpy as np
from scipy import stats

# Exam scores with 2 missing values
scores = pd.Series(
    [72, 65, 88, np.nan, 54, 91, 76, np.nan, 83, 69]
)

# Descriptive statistics
print("Descriptive Statistics:")
print(scores.describe())

# Remove missing values before calculating skewness and kurtosis
valid_scores = scores.dropna()

print("\nSkewness:", stats.skew(valid_scores))
print("Kurtosis:", stats.kurtosis(valid_scores))

# Count missing values
print("\nMissing values:", scores.isnull().sum())

# Fill missing values with the mean
scores_filled = scores.fillna(scores.mean())

print("\nFilled scores:")
print(scores_filled)
