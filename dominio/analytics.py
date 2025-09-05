import numpy as np
import pandas as pd
from .models import HarvestBatch, Plot



modelo1 = HarvestBatch.objects.all()
modelo2 = Plot.objects.all()

data1 = list(modelo1.values())
data2 = list(modelo2.values())


df_Harvest = pd.DataFrame(data1)
df_Plot = pd.DataFrame(data2)

df_filtrado= pd.merge(df_Harvest, df_Plot, left_on="Plot_id_id", right_on="id", how="left")

df_filtrado["kg_x_m2"] = df_filtrado["quantity_kg"] / df_filtrado["area"]