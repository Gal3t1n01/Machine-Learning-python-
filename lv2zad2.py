import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6),
delimiter=",", skiprows=1)

mpg = data[:,0]
hp = data[:,3]
wt = data[:,5]

plt.scatter(mpg,hp,s = wt*100)
plt.xlabel('Konjska snaga (hp)')
plt.xlabel('Potrosnja (mpg)')

mpg_min = np.min(mpg)
mpg_max = np.max(mpg)
mpg_sr = np.mean(mpg)
print(f"Min potrosnja : {mpg_min}")
print(f"Max potrosnja : {mpg_max}")
print(f"Avg potrosnja : {mpg_sr}")

plt.show()

datasix = data[data[:,4] == 6]
cy1_mpg = data[:,0]
cy1_hp = data[:,3]


plt.scatter(cy1_mpg,cy1_hp)
plt.xlabel('Konjska snaga')
plt.xlabel('Potrosnja')

mpg_min_auto = np.min(cy1_mpg)
mpg_max_auto = np.max(cy1_mpg)
mpg_sr_auto = np.mean(cy1_mpg)

print(f"Min potrosnja : {mpg_min_auto}")
print(f"Max potrosnja : {mpg_max_auto}")
print(f"Avg potrosnja : {mpg_sr_auto}")
plt.show()