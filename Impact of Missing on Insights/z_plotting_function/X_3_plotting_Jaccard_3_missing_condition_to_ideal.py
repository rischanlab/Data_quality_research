import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.stats
def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h

input_file_missing_attr_vs_ideal = 'results/missing_attributes_vs_ideal_10_executions.csv'
input_file_missing_measure_vs_ideal = 'results/missing_measures_vs_ideal_10_executions.csv'
input_file_missing_a_m_vs_ideal = 'results/missing_combine_a_m_vs_ideal_10_executions.csv'



output_plot = 'Jaccard_three_missing_condition_vs_ideal'


# ===============================================================
# STANDARD DYNAMIC VS IDEAL

df = pd.read_csv(input_file_missing_attr_vs_ideal, names=['percentage','k','RBO','Jaccard'])

percent = 10
#Jaccard
k5j = df[(df['k'] == 5) & (df['percentage'] == percent)]
k5j = k5j['Jaccard']
k10j = df[(df['k'] == 10) & (df['percentage'] == percent)]
k10j = k10j['Jaccard']
k15j = df[(df['k'] == 15) & (df['percentage'] == percent)]
k15j = k15j['Jaccard']
k20j = df[(df['k'] == 20) & (df['percentage'] == percent)]
k20j = k20j['Jaccard']

#RBO
k5r = df[(df['k'] == 5) & (df['percentage'] == percent)]
k5r = k5r['RBO']
k10r = df[(df['k'] == 10) & (df['percentage'] == percent)]
k10r = k10r['RBO']
k15r = df[(df['k'] == 15) & (df['percentage'] == percent)]
k15r = k15r['RBO']
k20r = df[(df['k'] == 20) & (df['percentage'] == percent)]
k20r = k20r['RBO']

k5j = list(mean_confidence_interval(k5j))
k5j.insert(0,5)
k5j.insert(1,'Jaccard')
k10j = list(mean_confidence_interval(k10j))
k10j.insert(0,10)
k10j.insert(1,'Jaccard')
k15j = list(mean_confidence_interval(k15j))
k15j.insert(0,15)
k15j.insert(1,'Jaccard')
k20j = list(mean_confidence_interval(k20j))
k20j.insert(0,20)
k20j.insert(1,'Jaccard')

k5r = list(mean_confidence_interval(k5r))
k5r.insert(0,5)
k5r.insert(1,'RBO 0.95')
k10r = list(mean_confidence_interval(k10r))
k10r.insert(0,10)
k10r.insert(1,'RBO 0.95')
k15r = list(mean_confidence_interval(k15r))
k15r.insert(0,15)
k15r.insert(1,'RBO 0.95')
k20r = list(mean_confidence_interval(k20r))
k20r.insert(0,20)
k20r.insert(1,'RBO 0.95')

df = pd.DataFrame([k5j, k10j, k15j,k20j, k5r, k10r, k15r,k20r])
df.columns = ['k','measurement','mean','lb','ub']

mean0 = df[df['measurement'] == 'Jaccard'].reset_index()
mean0 = mean0['mean']
ub0 = df[df['measurement'] == 'Jaccard'].reset_index()
ub0 = ub0['ub']
lb0 = df[df['measurement'] == 'Jaccard'].reset_index()
lb0 = lb0['lb']

mean1 = df[df['measurement'] == 'RBO 0.95'].reset_index()
mean1 = mean1['mean']
ub1 = df[df['measurement'] == 'RBO 0.95'].reset_index()
ub1 = ub1['ub']
lb1 = df[df['measurement'] == 'RBO 0.95'].reset_index()
lb1 = lb1['lb']

df1 = pd.read_csv(input_file_missing_measure_vs_ideal, names=['percentage','k','RBO','Jaccard'])

percent = 10
#Jaccard
k5j = df1[(df1['k'] == 5) & (df1['percentage'] == percent)]
k5j = k5j['Jaccard']
k10j = df1[(df1['k'] == 10) & (df1['percentage'] == percent)]
k10j = k10j['Jaccard']
k15j = df1[(df1['k'] == 15) & (df1['percentage'] == percent)]
k15j = k15j['Jaccard']
k20j = df1[(df1['k'] == 20) & (df1['percentage'] == percent)]
k20j = k20j['Jaccard']

#RBO
k5r = df1[(df1['k'] == 5) & (df1['percentage'] == percent)]
k5r = k5r['RBO']
k10r = df1[(df1['k'] == 10) & (df1['percentage'] == percent)]
k10r = k10r['RBO']
k15r = df1[(df1['k'] == 15) & (df1['percentage'] == percent)]
k15r = k15r['RBO']
k20r = df1[(df1['k'] == 20) & (df1['percentage'] == percent)]
k20r = k20r['RBO']

k5j = list(mean_confidence_interval(k5j))
k5j.insert(0,5)
k5j.insert(1,'Jaccard')
k10j = list(mean_confidence_interval(k10j))
k10j.insert(0,10)
k10j.insert(1,'Jaccard')
k15j = list(mean_confidence_interval(k15j))
k15j.insert(0,15)
k15j.insert(1,'Jaccard')
k20j = list(mean_confidence_interval(k20j))
k20j.insert(0,20)
k20j.insert(1,'Jaccard')

k5r = list(mean_confidence_interval(k5r))
k5r.insert(0,5)
k5r.insert(1,'RBO 0.95')
k10r = list(mean_confidence_interval(k10r))
k10r.insert(0,10)
k10r.insert(1,'RBO 0.95')
k15r = list(mean_confidence_interval(k15r))
k15r.insert(0,15)
k15r.insert(1,'RBO 0.95')
k20r = list(mean_confidence_interval(k20r))
k20r.insert(0,20)
k20r.insert(1,'RBO 0.95')

df1 = pd.DataFrame([k5j, k10j, k15j,k20j, k5r, k10r, k15r,k20r])
df1.columns = ['k','measurement','mean','lb','ub']

mean2 = df1[df1['measurement'] == 'Jaccard'].reset_index()
mean2 = mean2['mean']
ub2 = df1[df1['measurement'] == 'Jaccard'].reset_index()
ub2 = ub2['ub']
lb2 = df1[df1['measurement'] == 'Jaccard'].reset_index()
lb2 = lb2['lb']

mean3 = df1[df1['measurement'] == 'RBO 0.95'].reset_index()
mean3 = mean3['mean']
ub3 = df1[df1['measurement'] == 'RBO 0.95'].reset_index()
ub3 = ub3['ub']
lb3 = df1[df1['measurement'] == 'RBO 0.95'].reset_index()
lb3 = lb3['lb']

df2 = pd.read_csv(input_file_missing_a_m_vs_ideal, names=['percentage','k','RBO','Jaccard'])

percent = 10
#Jaccard
k5j = df2[(df2['k'] == 5) & (df2['percentage'] == percent)]
k5j = k5j['Jaccard']
k10j = df2[(df2['k'] == 10) & (df2['percentage'] == percent)]
k10j = k10j['Jaccard']
k15j = df2[(df2['k'] == 15) & (df2['percentage'] == percent)]
k15j = k15j['Jaccard']
k20j = df2[(df2['k'] == 20) & (df2['percentage'] == percent)]
k20j = k20j['Jaccard']

#RBO
k5r = df2[(df2['k'] == 5) & (df2['percentage'] == percent)]
k5r = k5r['RBO']
k10r = df2[(df2['k'] == 10) & (df2['percentage'] == percent)]
k10r = k10r['RBO']
k15r = df2[(df2['k'] == 15) & (df2['percentage'] == percent)]
k15r = k15r['RBO']
k20r = df2[(df2['k'] == 20) & (df2['percentage'] == percent)]
k20r = k20r['RBO']

k5j = list(mean_confidence_interval(k5j))
k5j.insert(0,5)
k5j.insert(1,'Jaccard')
k10j = list(mean_confidence_interval(k10j))
k10j.insert(0,10)
k10j.insert(1,'Jaccard')
k15j = list(mean_confidence_interval(k15j))
k15j.insert(0,15)
k15j.insert(1,'Jaccard')
k20j = list(mean_confidence_interval(k20j))
k20j.insert(0,20)
k20j.insert(1,'Jaccard')

k5r = list(mean_confidence_interval(k5r))
k5r.insert(0,5)
k5r.insert(1,'RBO 0.95')
k10r = list(mean_confidence_interval(k10r))
k10r.insert(0,10)
k10r.insert(1,'RBO 0.95')
k15r = list(mean_confidence_interval(k15r))
k15r.insert(0,15)
k15r.insert(1,'RBO 0.95')
k20r = list(mean_confidence_interval(k20r))
k20r.insert(0,20)
k20r.insert(1,'RBO 0.95')

df2 = pd.DataFrame([k5j, k10j, k15j,k20j, k5r, k10r, k15r,k20r])
df2.columns = ['k','measurement','mean','lb','ub']

mean7 = df2[df2['measurement'] == 'Jaccard'].reset_index()
mean7 = mean7['mean']
ub7 = df2[df2['measurement'] == 'Jaccard'].reset_index()
ub7 = ub7['ub']
lb7 = df2[df2['measurement'] == 'Jaccard'].reset_index()
lb7 = lb7['lb']

mean8 = df2[df2['measurement'] == 'RBO 0.95'].reset_index()
mean8 = mean8['mean']
ub8 = df2[df2['measurement'] == 'RBO 0.95'].reset_index()
ub8 = ub8['ub']
lb8 = df2[df2['measurement'] == 'RBO 0.95'].reset_index()
lb8 = lb8['lb']

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
#markers = ['s','x','*','+','<','o']
#linestyles = [':','-.','-','--','-.','-']

ax.plot(mean0, lw = 1, color = '#539caf', alpha = 1, label = 'Jaccard Missing Attributes (A) to Ideal', marker='o', linestyle='dashed', linewidth=2, markersize=12)
#ax.plot(mean1, lw = 1, color = '#b65332', alpha = 1, label = 'RBO 0.95 Dynamic to Ideal', marker='s', linestyle=':', linewidth=2, markersize=12)

ax.plot(mean2, lw = 1, color = '#5be19a', alpha = 1, label = 'Jaccard Missing Measure (M) to Ideal', marker='x', linestyle='-.', linewidth=2, markersize=12)
#ax.plot(mean3, lw = 1, color = '#ece554', alpha = 1, label = 'RBO 0.95 Standard to Ideal', marker='<', linestyle='-', linewidth=2, markersize=12)

ax.plot(mean7, lw = 1, color = '#b65332', alpha = 1, label = 'Jaccard Missing A and M to Ideal', marker='<', linestyle='-', linewidth=2, markersize=12)


# Shade the confidence interval
ax.fill_between(t, lb0, ub0, color = '#539caf', alpha = 0.4)
#ax.fill_between(t, lb1, ub1, color = '#b65332', alpha = 0.4)

ax.fill_between(t, lb2, ub2, color = '#5be19a', alpha = 0.4)
#ax.fill_between(t, lb3, ub3, color = '#ece554', alpha = 0.4)

ax.fill_between(t, lb7, ub7, color = '#b65332', alpha = 0.4)


# Label the axes and provide a title
ax.set_title("Impact of k on Effectiveness - 95% CI, 10 % missing")
ax.set_xlabel("k")
ax.set_ylabel("Effectiveness - Jaccard missing with 3 conditions to Ideal")
x = [5, 10, 15, 20]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
ax.set_ylim(ymin=0.0)
ax.set_ylim(ymax=1.01)

ax.legend(loc='lower left')

plt.savefig('plot/' + output_plot, format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()