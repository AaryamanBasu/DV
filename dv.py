import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)
iris = pd.read_csv("../input/Iris.csv")
iris.head()


iris["Species"].value_counts()


iris.plot(kind="scatter", x="SepalLengthCm", y="SepalWidthCm")


OR


sns.jointplot(x="SepalLengthCm", y="SepalWidthCm", data=iris, size=5)


OR

sns.boxplot(x="Species", y="PetalLengthCm", data=iris)
