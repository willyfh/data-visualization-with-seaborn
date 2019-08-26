import pandas as pd
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns

# read dataset
df = pd.read_csv('Pokemon.csv', index_col=0, encoding='latin1')

# display first 5 data
df.head()

# display scatter plot
sns.lmplot(x='Attack', y='Defense', data=df,
           fit_reg=False, 
           hue='Stage')

plt.ylim(0, None)
plt.xlim(0, None)

# display box plot for combat stats
stats_df = df.drop(['Total', 'Stage', 'Legendary'], axis=1)

sns.boxplot(data=stats_df)

# display violin plot with whitegrid theme for attack distribution by type
sns.set_style('whitegrid')

sns.violinplot(x='Type 1', y='Attack', data=df)

# display swarm plot
sns.swarmplot(x='Type 1', y='Attack', data=df)

# overlaying violin and swarm plot
plt.figure(figsize=(10,6))

sns.violinplot(x='Type 1',
               y='Attack', 
               data=df, 
               inner=None) # Remove the bars inside the violins

sns.swarmplot(x='Type 1', 
              y='Attack', 
              data=df, 
              color='k', # Make points black
              alpha=0.7) # and slightly transparent

plt.title('Attack by Type')