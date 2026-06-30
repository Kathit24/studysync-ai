import pandas as pd
import numpy as np

np.random.seed(42)

n = 5000

study_hours = np.random.uniform(1, 10, n)
attendance = np.random.randint(50, 101, n)
assignment_completion = np.random.randint(40, 101, n)
previous_gpa = np.random.uniform(4.5, 9.8, n)
mock_test_score = np.random.randint(35, 101, n)
sleep_hours = np.random.uniform(4, 9, n)
screen_time = np.random.uniform(1, 8, n)
stress_level = np.random.randint(1, 11, n)
programming_practice_hours = np.random.uniform(0, 6, n)
class_participation = np.random.randint(1, 11, n)

learning_style = np.random.choice(
    ["Visual", "Auditory", "Reading", "Kinesthetic"], n
)

gender = np.random.choice(
    ["Male", "Female"], n
)

semester = np.random.randint(1, 9, n)
age = np.random.randint(17, 25, n)

# Generate realistic GPA
final_gpa = (
    previous_gpa * 0.45
    + study_hours * 0.18
    + attendance * 0.015
    + assignment_completion * 0.01
    + mock_test_score * 0.012
    + programming_practice_hours * 0.08
    + sleep_hours * 0.05
    - stress_level * 0.07
    - screen_time * 0.04
)

final_gpa = np.clip(final_gpa, 4.0, 10.0)

df = pd.DataFrame({
    "age": age,
    "gender": gender,
    "semester": semester,
    "study_hours": study_hours.round(2),
    "attendance": attendance,
    "assignment_completion": assignment_completion,
    "previous_gpa": previous_gpa.round(2),
    "mock_test_score": mock_test_score,
    "sleep_hours": sleep_hours.round(2),
    "screen_time": screen_time.round(2),
    "stress_level": stress_level,
    "programming_practice_hours": programming_practice_hours.round(2),
    "class_participation": class_participation,
    "learning_style": learning_style,
    "final_gpa": final_gpa.round(2)
})

df.to_csv("notebook/data/students.csv", index=False)

print(df.head())
print("\nDataset Created Successfully!")