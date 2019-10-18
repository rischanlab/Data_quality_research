import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.stats
def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h

input_file = 'summary/cost.csv'

output_plot_ideal_vs_standard = 'impact_missing_on_cost'

# ===============================================================
# IDEAL VS STANDARD

df = pd.read_csv(input_file, names=['db','cost'])

#Jaccard

df10 = df[df['db'].str.contains("db_10mdiab")]
#
df20 = df[df['db'].str.contains("db_20mdiab")]

df30 = df[df['db'].str.contains("db_30mdiab")]

df40 = df[df['db'].str.contains("db_40mdiab")]

df50 = df[df['db'].str.contains("db_50mdiab")]

df60 = df[df['db'].str.contains("db_60mdiab")]

df70 = df[df['db'].str.contains("db_70mdiab")]

df80 = df[df['db'].str.contains("db_80mdiab")]

df90 = df[df['db'].str.contains("db_90mdiab")]


df10 = list(mean_confidence_interval(df10['cost']))
df10.insert(0,10)

df20 = list(mean_confidence_interval(df20['cost']))
df20.insert(0,20)

df30 = list(mean_confidence_interval(df30['cost']))
df30.insert(0,30)

df40 = list(mean_confidence_interval(df40['cost']))
df40.insert(0,40)

df50 = list(mean_confidence_interval(df50['cost']))
df50.insert(0,50)

df60 = list(mean_confidence_interval(df60['cost']))
df60.insert(0,60)

df70 = list(mean_confidence_interval(df70['cost']))
df70.insert(0,70)

df80 = list(mean_confidence_interval(df80['cost']))
df80.insert(0,80)

df90 = list(mean_confidence_interval(df90['cost']))
df90.insert(0,90)


df = pd.DataFrame([df10, df20, df30, df40, df50, df60, df70, df80, df90])
df.columns = ['percentage','mean','lb','ub']
print(df)
mean0 = df['mean']
ub0 = df['ub']
lb0 = df['lb']


# Set some parameters to apply to all plots. These can be overridden
# in each plot if desired
import matplotlib
# Plot size to 14" x 7"
matplotlib.rc('figure', figsize = (14, 7))
# Font size to 14
matplotlib.rc('font', size = 14)
# Do not display top and right frame lines
matplotlib.rc('axes.spines', top = False, right = False)
# Remove grid lines
matplotlib.rc('axes', grid = False)
# Set backgound color to white
matplotlib.rc('axes', facecolor = 'white')


t = np.arange(len(mean0))

_, ax = plt.subplots()
# Plot the data, set the linewidth, color and transparency of the
# line, provide a label for the legend
ax.plot(mean0, lw = 1, color = '#539caf', alpha = 1, label = 'generate insight cost - dynamic imputation', marker='x', linewidth=2, markersize=12)

# Shade the confidence interval
ax.fill_between(t, lb0, ub0, color = '#539caf', alpha = 0.4)

# Label the axes and provide a title
ax.set_title("Impact of percentage missing on cost to generate insights - 95% CI")
ax.set_xlabel("percentage of missing")
ax.set_ylabel("Time (s)")
x = [10, 20, 30, 40, 50, 60, 70, 80, 90]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
ax.set_ylim(ymin=0.0)
ax.set_ylim(ymax=50.0)

ax.legend(loc='lower left')

plt.savefig('plot/' + output_plot_ideal_vs_standard, format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot_ideal_vs_standard + '.png')
plt.show()
