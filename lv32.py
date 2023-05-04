import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

mtcars = pd.read_csv('mtcars.csv')
print(mtcars)

mtcars.groupby('cyl')['mpg'].mean().plot.bar()


mtcars.boxplot(by='cyl', column='wt')


mtcars.boxplot(by='am', column='mpg')



mtcars.plot.scatter(x = 'qsec', y='hp', c='am', colormap='plasma')
plt.show()