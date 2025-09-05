import numpy as np
import pandas as pd
from .models import HarvestBatch, Plot



modelo1 = HarvestBatch.objects.all()
data1 = list(modelo1.values())
df1 = pd.DataFrame(data1)

print(df1)

modelo2 = Plot.objects.all()
data2 = list(modelo2.values())
df2 = pd.DataFrame(data2)

print(df2)

print(df1)
df_results = pd.DataFrame()

df_results["kg_x_m2"] = df1["quantity_kg"]/ df2["area"]



print (df_results)