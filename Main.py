import matplotlib.pyplot as plt
import pandas as pd
import re

df = pd.read_csv('climate_change_indicators.csv', index_col=0)

fig, ax = plt.subplots()
x = df.columns[63:].tolist()

for i, valor in enumerate(x):
    x[i] = re.sub(r'F', '', x[i])


mx = df['Country'].iloc[128]
us = df['Country'].iloc[211]
arg = df['Country'].iloc[8]
bra = df['Country'].iloc[26]
wld = df['Country'].iloc[221]

r_mx = df.loc[df['Country'] == mx, df.columns[63:]].values.tolist()[0]
r_us = df.loc[df['Country'] == us, df.columns[63:]].values.tolist()[0]
r_arg = df.loc[df['Country'] == arg, df.columns[63:]].values.tolist()[0]
r_bra = df.loc[df['Country'] == bra, df.columns[63:]].values.tolist()[0]
r_wld = df.loc[df['Country'] == wld, df.columns[63:]].values.tolist()[0]

y = {mx: r_mx, us: r_us, arg: r_arg, bra: r_bra, wld: r_wld}

ax.errorbar(x, y[mx], yerr=0.1, label=f'Error bar from {mx}')

ax.plot(x, y[mx], marker='^', label=mx)
ax.plot(x, y[us], marker='o', label=us)
ax.plot(x, y[arg], marker='>', label=arg)
ax.plot(x, y[bra], marker='*', label=bra)
ax.plot(x, y[wld], marker='p', label=wld)

ax.set_title('Climate change indicators')
ax.legend(loc = 'upper right')
ax.set_xlabel('Time (years)')
ax.set_ylabel('Temperature variation (°C)')

plt.show()