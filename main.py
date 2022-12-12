# Install packages
# Installation des paquets
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import dates

# Load data
# Chargement des données
df = pd.read_csv("commodity_prices.csv")

# Clean data
# Nettoyage des données
df["Year"] = df['Year'].astype(str) + '-01-01'
df["Year"] = pd.to_datetime(df["Year"])

# Get 2000's prices for creating index
# Prendre les prices des années 2000 pour créer un index
df2000s = df.loc[(df['Year'] > "1999-12-01") & (df['Year'] <= "2010-01-01")]

# Let's calculate index for Rice.
# Calculons l'index du riz.
ricebase = df2000s['Rice'].mean()
df['Rice index'] = df['Rice'] * 100 / ricebase

# Let's calculate index for Gold.
# Calculons l'index de l'or.
goldbase = df2000s['Gold'].mean()
df['Gold index'] = df['Gold'] * 100 / goldbase

# Our goal on this program will be to know if there is a correlation between some specific product and some others.
# Notre but dans ce programme sera de savoir si il y a une corrélation entre des produits spécifiques (riz, or) et d'autres (platine, argent ou encore blé, maïs, orge).

# Let's calculate index for Wheat, Maize and Barley to compare with Rice.
# Calculons l'index pour le blé, le maïs et l'orge pour le comparer avec le riz.

df["Wheat index"] = df["Wheat"]*100/(df2000s["Wheat"].mean())
df["Maize index"] = df["Maize"]*100/(df2000s["Maize"].mean())
df["Barley index"] = df["Barley"]*100/(df2000s["Barley"].mean())

# Let's calculate index for Silver and Platinum to compare with Gold.
# Calculons l'index pour l'argent et le platine pour le comparer avec l'or.

df["Silver index"] = df["Silver"]*100/(df2000s["Silver"].mean())
df["Platinum index"] = df["Platinum"]*100/(df2000s["Platinum"].mean())

# Let's look at graphs to see how it looks.
# Calculons l'index pour le blé, le maïs et l'orge pour le comparer avec le riz.

fig, ax = plt.subplots(figsize=(10, 6))
plt.plot(df["Year"], df["Rice index"], label = "Rice index")
plt.plot(df["Year"], df["Wheat index"], label = "Wheat Index")
plt.plot(df["Year"], df["Maize index"], label = "Maize Index")
plt.plot(df["Year"], df["Barley index"], label = "Barley Index")
plt.legend()
plt.show()

# Most correlation is probably between rice and wheat.
# La plus grande corrélation est probablement entre le riz et le blé.

print(df["Gold index"])
fig, ax = plt.subplots(figsize=(10, 6))
plt.plot(df["Year"], df["Gold index"], label = "Gold Index")
plt.plot(df["Year"], df["Silver index"], label = "Silver Index")
plt.plot(df["Year"], df["Platinum index"], label = "Platinum Index")
plt.legend()
plt.show()

# Most correlation is between gold and silver.
# La plus grande corrélation est probablement entre l'or et l'argent.

# Here the goal would be to explain the problem and the results with a credible explanation.
# Ici le but aurait été d'expliquer le problème et les résultats avec une explication crédible.

# With the following code, we can find out the cheapest and the most expensive commodity.
# Avec le code suivant, nous pouvons trouver la commodité la moins cher et la plus chère.

tsum = df.sum(numeric_only=True).sort_values()[:3]
lsum = df.sum(numeric_only=True).sort_values(ascending=False)[:3]

tsum = {"Name":list(tsum.index), "Sum":list(tsum)}
tsum = pd.DataFrame(tsum)

lsum = {"Name":list(lsum.index), "Sum":list(lsum)}
lsum = pd.DataFrame(lsum)

plt.bar(tsum["Name"], tsum["Sum"])
plt.show()

plt.bar(lsum["Name"], lsum["Sum"])
plt.ticklabel_format(style='plain', axis='y')
plt.show()

# We can see with the graphics that tobacco is from far the most expensive commodity since 1960.
# Obviously it's a small project so we can not really find any conclusion because we miss some datas (quantities for example) but also because comparaisons are not really relevant.

# Nous pouvons voir avec les graphiques que le tabac est de loin la plus chère commidité depuis 1960.
# Évidemment c'est un court projet donc nous ne pouvons pas faire de conclusion car il nous manque des données (les quantités par exemple) mais aussi car les comparaisons ne sont pas assez pertinentes.