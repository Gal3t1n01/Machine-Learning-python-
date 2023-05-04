import pandas as pd
import  numpy as np

mtcars = pd.read_csv('mtcars.csv')

print(mtcars.sort_values(by=['mpg'], ascending=False).head(5))

cyl_8 = mtcars[mtcars["cyl"] == 8]
najmanji = cyl_8.sort_values(by=["mpg"]).head(3)
print("Najmanja potrošnja kod 8 cilindara:")
print(najmanji[["car", "mpg"]])

cyl_6 = mtcars[mtcars["cyl"] == 6]
srednja6 = cyl_6.sort_values(by=["mpg"])
print("Srednja potrošnja kod 6 cilindara:")
print(srednja6[["car","mpg"]])

cyl_4 = mtcars[mtcars["cyl"] == 4]
odabrani = cyl_4[(mtcars["wt"] >= 2) & (mtcars["wt"] <= 2.2)]
srednja_potrosnja_4 = odabrani["mpg"].mean()
print("Srednja potrošnja automobila s 4 cilindra i masom između 2000 i 2200 lbs: {:.2f}".format(srednja_potrosnja_4))

manual = mtcars[mtcars["am"] == 1]
auto = mtcars[mtcars["am"] == 0]
print("Broj automobila s ručnim mjenjačem: {}".format(manual.shape[0]))
print("Broj automobila s automatskim mjenjačem: {}".format(auto.shape[0]))

snaga = mtcars[ (mtcars["hp"] > 100) & (mtcars["am"] == 1)] 
print("Broj automobila s automatskim mjenjacem sa snagon preko 100 hp: {}".format(snaga.shape[0]))

print(mtcars.wt * 1000 * 0.45359237)