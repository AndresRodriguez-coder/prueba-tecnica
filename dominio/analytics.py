import numpy as np
import pandas as pd
from .models import HarvestBatch, Plot



modelo1 = HarvestBatch.objects.all()
data1 = list(modelo1.values())
df_Harvest = pd.DataFrame(data1)


modelo2 = Plot.objects.all()
data2 = list(modelo2.values())
df_Plot = pd.DataFrame(data2)


df_results = pd.DataFrame()

df_results["kg_x_m2"] = df_Harvest["quantity_kg"]/ df_Plot["area"]

