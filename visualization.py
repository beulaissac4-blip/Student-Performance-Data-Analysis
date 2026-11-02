import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("cleaned_students.csv")

# Subject-wise average
subjects = ["Maths", "Science", "English"]
average_marks = df[subjects].mean()

# Bar Chart
plt.figure(figsize=(8, 5))
average_marks.plot(kind="bar")

plt.title("Subject-wise Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.savefig("subject_average.png")
plt.show()

# Student Performance Graph
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="Name", y="Maths")

plt.title("Student Maths Performance")
plt.xlabel("Students")
plt.ylabel("Maths Marks")
plt.savefig("student_performance.png")
plt.show()

print("Graphs Generated Successfully!")