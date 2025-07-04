import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

#1. generate random data with numpy
np.random.seed(0)
student_ids = np.arange(1, 21)
ee_scores = np.random.randint(25, 100, size=20)
entc_scores = np.random.randint(25, 100, size=20)
cse_scores = np.random.randint(25, 100, size=20)


#2.create dataframe with pandas
df = pd.DataFrame({
    'StudentID': student_ids,
    'EE':ee_scores,
    'ENTC': entc_scores,
    'CSE': cse_scores
})


print("First 5 rows of the DataFrame:")
print(df.head())

#3. basic analysis with pandas
print("\nAverage scores:")
print(df[['EE', 'ENTC', 'CSE']].mean())
print("\nStudent with highest EE score:")



#4.visualization with matplotlib
plt.figure(figsize=(8, 5))
plt.plot(df['StudentID'], df['EE'], marker='o', label='EE')
plt.plot(df['StudentID'], df['ENTC'], marker='s', label='ENTC')
plt.plot(df['StudentID'], df['CSE'], marker='^', label='CSE')
plt.xlabel('StudentID')
plt.ylabel('Score')
plt.title('Student Scores by branch')
plt.legend()
plt.show()

#5.visualization with seaborn
plt.figure(figsize=(8, 5))
sns.boxplot(data=df[['EE', 'ENTC', 'CSE']])
plt.title('Score Distribution by branch')
plt.ylabel('Score')
plt.show()