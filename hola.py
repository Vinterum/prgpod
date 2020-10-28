# %%
import numpy as np
import pandas as pd

# %%
lista = [1,2,4,6]
nplista = np.array(lista)
pdlista = pd.Series(lista)

print(lista*10)
print(nplista*2)
print(pdlista*2)

# %%
df = pd.read_csv("insurance.csv")
print(df)

# %%
df.head(10)

# %%
df.tail()

# %%
df.sample()

# %%
df.describe()

# %%
df.info

# %%
df[['age']]

# %%
df[['age','bmi']]

# %%
df[-3:]

# %%
df[:2,['age','bmi']]

# %%
