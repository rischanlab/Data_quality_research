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

input_file1 = 'results/dropnan_measures_vs_ideal.csv'
input_file2 = 'results/nodrop_measures_vs_ideal.csv'

output_plot1 = 'all_percentage_dropnan_measures_vs_ideal'
output_plot2 = 'all_percentage_nodrop_measures_vs_ideal'

# ===============================================================
# IDEAL VS STANDARD

df = pd.read_csv(input_file1, names=['percentage','k','RBO','Jaccard'])
k = 5
#Jaccard
dfj0 = df[(df['k'] == k) & (df['percentage'] == 0)]
dfj0 = dfj0['Jaccard']

dfj5 = df[(df['k'] == k) & (df['percentage'] == 5)]
dfj5 = dfj5['Jaccard']

dfj10 = df[(df['k'] == k) & (df['percentage'] == 10)]
dfj10 = dfj10['Jaccard']

dfj15 = df[(df['k'] == k) & (df['percentage'] == 15)]
dfj15 = dfj15['Jaccard']

dfj0 = list(mean_confidence_interval(dfj0))
dfj0.insert(0,0)
dfj0.insert(1,'Jaccard')

dfj5 = list(mean_confidence_interval(dfj5))
dfj5.insert(0,5)
dfj5.insert(1,'Jaccard')

dfj10 = list(mean_confidence_interval(dfj10))
dfj10.insert(0,10)
dfj10.insert(1,'Jaccard')

dfj15 = list(mean_confidence_interval(dfj15))
dfj15.insert(0,15)
dfj15.insert(1,'Jaccard')



#RBO
dfr0 = df[(df['k'] == k) & (df['percentage'] == 0)]
dfr0 = dfr0['RBO']

dfr5 = df[(df['k'] == k) & (df['percentage'] == 5)]
dfr5 = dfr5['RBO']

dfr10 = df[(df['k'] == k) & (df['percentage'] == 10)]
dfr10 = dfr10['RBO']

dfr15 = df[(df['k'] == k) & (df['percentage'] == 15)]
dfr15 = dfr15['RBO']

dfr0 = list(mean_confidence_interval(dfr0))
dfr0.insert(0,0)
dfr0.insert(1,'RBO')

dfr5 = list(mean_confidence_interval(dfr5))
dfr5.insert(0,5)
dfr5.insert(1,'RBO')

dfr10 = list(mean_confidence_interval(dfr10))
dfr10.insert(0,10)
dfr10.insert(1,'RBO')

dfr15 = list(mean_confidence_interval(dfr15))
dfr15.insert(0,15)
dfr15.insert(1,'RBO')


df = pd.DataFrame([dfj0, dfj5, dfj10, dfj15,
                   dfr0, dfr5, dfr10, dfr15])
df.columns = ['k','measurement','mean','lb','ub']

mean0 = df[df['measurement'] == 'Jaccard'].reset_index()
mean0 = mean0['mean']
ub0 = df[df['measurement'] == 'Jaccard'].reset_index()
ub0 = ub0['ub']
lb0 = df[df['measurement'] == 'Jaccard'].reset_index()
lb0 = lb0['lb']

mean1 = df[df['measurement'] == 'RBO'].reset_index()
mean1 = mean1['mean']
ub1 = df[df['measurement'] == 'RBO'].reset_index()
ub1 = ub1['ub']
lb1 = df[df['measurement'] == 'RBO'].reset_index()
lb1 = lb1['lb']

df = pd.read_csv(input_file1, names=['percentage','k','RBO','Jaccard'])
k = 5
#Jaccard
dfj0 = df[(df['k'] == k) & (df['percentage'] == 0)]
dfj0 = dfj0['Jaccard']

dfj5 = df[(df['k'] == k) & (df['percentage'] == 5)]
dfj5 = dfj5['Jaccard']

dfj10 = df[(df['k'] == k) & (df['percentage'] == 10)]
dfj10 = dfj10['Jaccard']

dfj15 = df[(df['k'] == k) & (df['percentage'] == 15)]
dfj15 = dfj15['Jaccard']

dfj0 = list(mean_confidence_interval(dfj0))
dfj0.insert(0,0)
dfj0.insert(1,'Jaccard')

dfj5 = list(mean_confidence_interval(dfj5))
dfj5.insert(0,5)
dfj5.insert(1,'Jaccard')

dfj10 = list(mean_confidence_interval(dfj10))
dfj10.insert(0,10)
dfj10.insert(1,'Jaccard')

dfj15 = list(mean_confidence_interval(dfj15))
dfj15.insert(0,15)
dfj15.insert(1,'Jaccard')



#RBO
dfr0 = df[(df['k'] == k) & (df['percentage'] == 0)]
dfr0 = dfr0['RBO']

dfr5 = df[(df['k'] == k) & (df['percentage'] == 5)]
dfr5 = dfr5['RBO']

dfr10 = df[(df['k'] == k) & (df['percentage'] == 10)]
dfr10 = dfr10['RBO']

dfr15 = df[(df['k'] == k) & (df['percentage'] == 15)]
dfr15 = dfr15['RBO']

dfr0 = list(mean_confidence_interval(dfr0))
dfr0.insert(0,0)
dfr0.insert(1,'RBO')

dfr5 = list(mean_confidence_interval(dfr5))
dfr5.insert(0,5)
dfr5.insert(1,'RBO')

dfr10 = list(mean_confidence_interval(dfr10))
dfr10.insert(0,10)
dfr10.insert(1,'RBO')

dfr15 = list(mean_confidence_interval(dfr15))
dfr15.insert(0,15)
dfr15.insert(1,'RBO')


df = pd.DataFrame([dfj0, dfj5, dfj10, dfj15,
                   dfr0, dfr5, dfr10, dfr15])
df.columns = ['k','measurement','mean','lb','ub']

mean0 = df[df['measurement'] == 'Jaccard'].reset_index()
mean0 = mean0['mean']
ub0 = df[df['measurement'] == 'Jaccard'].reset_index()
ub0 = ub0['ub']
lb0 = df[df['measurement'] == 'Jaccard'].reset_index()
lb0 = lb0['lb']

mean1 = df[df['measurement'] == 'RBO'].reset_index()
mean1 = mean1['mean']
ub1 = df[df['measurement'] == 'RBO'].reset_index()
ub1 = ub1['ub']
lb1 = df[df['measurement'] == 'RBO'].reset_index()
lb1 = lb1['lb']

# Set some parameters to apply to all plots. These can be overridden
# in each plot if desired
import matplotlib
# Plot size to 14" x 7"
matplotlib.rc('figure', figsize = (14, 14))
# Font size to 14
matplotlib.rc('font', size = 25)
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
ax.plot(mean0, lw = 1, color = '#539caf', alpha = 1, label = 'Jaccard', marker='x', linestyle='-.', linewidth=2, markersize=12)
ax.plot(mean1, lw = 1, color = '#b65332', alpha = 1, label = 'RBO 0.95', marker='<', linestyle='-', linewidth=2, markersize=12)

# Shade the confidence interval
ax.fill_between(t, lb0, ub0, color = '#539caf', alpha = 0.4)
ax.fill_between(t, lb1, ub1, color = '#b65332', alpha = 0.4)

# Label the axes and provide a title
ax.set_title("Impact of percentage of missing on Effectiveness, k = 5")
ax.set_xlabel("percentage of missing")
ax.set_ylabel("Effectiveness - Missing Measures to Ideal - drop nan rows")
x = [0, 5, 10, 15]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
ax.set_ylim(ymin=0.0)
ax.set_ylim(ymax=1.01)

ax.legend(loc='lower left')

plt.savefig('plot/' + output_plot1, format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot1 + '.png')
plt.show()



df = pd.read_csv(input_file2, names=['percentage','k','RBO','Jaccard'])
k = 5
#Jaccard
dfj0 = df[(df['k'] == k) & (df['percentage'] == 0)]
dfj0 = dfj0['Jaccard']

dfj5 = df[(df['k'] == k) & (df['percentage'] == 5)]
dfj5 = dfj5['Jaccard']

dfj10 = df[(df['k'] == k) & (df['percentage'] == 10)]
dfj10 = dfj10['Jaccard']

dfj15 = df[(df['k'] == k) & (df['percentage'] == 15)]
dfj15 = dfj15['Jaccard']

dfj0 = list(mean_confidence_interval(dfj0))
dfj0.insert(0,0)
dfj0.insert(1,'Jaccard')

dfj5 = list(mean_confidence_interval(dfj5))
dfj5.insert(0,5)
dfj5.insert(1,'Jaccard')

dfj10 = list(mean_confidence_interval(dfj10))
dfj10.insert(0,10)
dfj10.insert(1,'Jaccard')

dfj15 = list(mean_confidence_interval(dfj15))
dfj15.insert(0,15)
dfj15.insert(1,'Jaccard')



#RBO
dfr0 = df[(df['k'] == k) & (df['percentage'] == 0)]
dfr0 = dfr0['RBO']

dfr5 = df[(df['k'] == k) & (df['percentage'] == 5)]
dfr5 = dfr5['RBO']

dfr10 = df[(df['k'] == k) & (df['percentage'] == 10)]
dfr10 = dfr10['RBO']

dfr15 = df[(df['k'] == k) & (df['percentage'] == 15)]
dfr15 = dfr15['RBO']

dfr0 = list(mean_confidence_interval(dfr0))
dfr0.insert(0,0)
dfr0.insert(1,'RBO')

dfr5 = list(mean_confidence_interval(dfr5))
dfr5.insert(0,5)
dfr5.insert(1,'RBO')

dfr10 = list(mean_confidence_interval(dfr10))
dfr10.insert(0,10)
dfr10.insert(1,'RBO')

dfr15 = list(mean_confidence_interval(dfr15))
dfr15.insert(0,15)
dfr15.insert(1,'RBO')


df = pd.DataFrame([dfj0, dfj5, dfj10, dfj15,
                   dfr0, dfr5, dfr10, dfr15])
df.columns = ['k','measurement','mean','lb','ub']

mean0 = df[df['measurement'] == 'Jaccard'].reset_index()
mean0 = mean0['mean']
ub0 = df[df['measurement'] == 'Jaccard'].reset_index()
ub0 = ub0['ub']
lb0 = df[df['measurement'] == 'Jaccard'].reset_index()
lb0 = lb0['lb']

mean1 = df[df['measurement'] == 'RBO'].reset_index()
mean1 = mean1['mean']
ub1 = df[df['measurement'] == 'RBO'].reset_index()
ub1 = ub1['ub']
lb1 = df[df['measurement'] == 'RBO'].reset_index()
lb1 = lb1['lb']

df = pd.read_csv(input_file2, names=['percentage','k','RBO','Jaccard'])
k = 5
#Jaccard
dfj0 = df[(df['k'] == k) & (df['percentage'] == 0)]
dfj0 = dfj0['Jaccard']

dfj5 = df[(df['k'] == k) & (df['percentage'] == 5)]
dfj5 = dfj5['Jaccard']

dfj10 = df[(df['k'] == k) & (df['percentage'] == 10)]
dfj10 = dfj10['Jaccard']

dfj15 = df[(df['k'] == k) & (df['percentage'] == 15)]
dfj15 = dfj15['Jaccard']

dfj0 = list(mean_confidence_interval(dfj0))
dfj0.insert(0,0)
dfj0.insert(1,'Jaccard')

dfj5 = list(mean_confidence_interval(dfj5))
dfj5.insert(0,5)
dfj5.insert(1,'Jaccard')

dfj10 = list(mean_confidence_interval(dfj10))
dfj10.insert(0,10)
dfj10.insert(1,'Jaccard')

dfj15 = list(mean_confidence_interval(dfj15))
dfj15.insert(0,15)
dfj15.insert(1,'Jaccard')



#RBO
dfr0 = df[(df['k'] == k) & (df['percentage'] == 0)]
dfr0 = dfr0['RBO']

dfr5 = df[(df['k'] == k) & (df['percentage'] == 5)]
dfr5 = dfr5['RBO']

dfr10 = df[(df['k'] == k) & (df['percentage'] == 10)]
dfr10 = dfr10['RBO']

dfr15 = df[(df['k'] == k) & (df['percentage'] == 15)]
dfr15 = dfr15['RBO']

dfr0 = list(mean_confidence_interval(dfr0))
dfr0.insert(0,0)
dfr0.insert(1,'RBO')

dfr5 = list(mean_confidence_interval(dfr5))
dfr5.insert(0,5)
dfr5.insert(1,'RBO')

dfr10 = list(mean_confidence_interval(dfr10))
dfr10.insert(0,10)
dfr10.insert(1,'RBO')

dfr15 = list(mean_confidence_interval(dfr15))
dfr15.insert(0,15)
dfr15.insert(1,'RBO')


df = pd.DataFrame([dfj0, dfj5, dfj10, dfj15,
                   dfr0, dfr5, dfr10, dfr15])
df.columns = ['k','measurement','mean','lb','ub']

mean0 = df[df['measurement'] == 'Jaccard'].reset_index()
mean0 = mean0['mean']
ub0 = df[df['measurement'] == 'Jaccard'].reset_index()
ub0 = ub0['ub']
lb0 = df[df['measurement'] == 'Jaccard'].reset_index()
lb0 = lb0['lb']

mean1 = df[df['measurement'] == 'RBO'].reset_index()
mean1 = mean1['mean']
ub1 = df[df['measurement'] == 'RBO'].reset_index()
ub1 = ub1['ub']
lb1 = df[df['measurement'] == 'RBO'].reset_index()
lb1 = lb1['lb']

# Set some parameters to apply to all plots. These can be overridden
# in each plot if desired
import matplotlib
# Plot size to 14" x 7"
matplotlib.rc('figure', figsize = (14, 14))
# Font size to 14
matplotlib.rc('font', size = 25)
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
ax.plot(mean0, lw = 1, color = '#539caf', alpha = 1, label = 'Jaccard', marker='x', linestyle='-.', linewidth=2, markersize=12)
ax.plot(mean1, lw = 1, color = '#b65332', alpha = 1, label = 'RBO 0.95', marker='<', linestyle='-', linewidth=2, markersize=12)

# Shade the confidence interval
ax.fill_between(t, lb0, ub0, color = '#539caf', alpha = 0.4)
ax.fill_between(t, lb1, ub1, color = '#b65332', alpha = 0.4)

# Label the axes and provide a title
ax.set_title("Impact of percentage of missing on Effectiveness, k = 5")
ax.set_xlabel("percentage of missing")
ax.set_ylabel("Effectiveness - Missing Measures to Ideal")
x = [0, 5, 10, 15]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
ax.set_ylim(ymin=0.0)
ax.set_ylim(ymax=1.01)

ax.legend(loc='lower left')

plt.savefig('plot/' + output_plot2, format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot2 + '.png')
plt.show()