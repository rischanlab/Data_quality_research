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

input_file1 = 'results/variance_readmitted_no_vs_whole_nodrop_attr.csv'
input_file2 = 'results/variance_insulin_steady_vs_no_steady_nodrop_attr.csv'

output_plot = 'variance_nodrop_attr_readmitted_vs_insulin'

# ===============================================================
# IDEAL VS STANDARD

df = pd.read_csv(input_file1, names=['percentage','k','variance'])

percent = 10

#Jaccard
k5j = df[(df['k'] == 5) & (df['percentage'] == percent)]
k5j = k5j['variance']
k10j = df[(df['k'] == 10) & (df['percentage'] == percent)]
k10j = k10j['variance']
k15j = df[(df['k'] == 15) & (df['percentage'] == percent)]
k15j = k15j['variance']
k20j = df[(df['k'] == 20) & (df['percentage'] == percent)]
k20j = k20j['variance']
#print(k5j)

k5j = list(mean_confidence_interval(k5j))
k5j.insert(0,5)
#print(k5j)
#k5j.insert(1,'Jaccard')
k10j = list(mean_confidence_interval(k10j))
k10j.insert(0,10)
#k10j.insert(1,'Jaccard')
k15j = list(mean_confidence_interval(k15j))
k15j.insert(0,15)
#k15j.insert(1,'Jaccard')
k20j = list(mean_confidence_interval(k20j))
k20j.insert(0,20)
#k20j.insert(1,'Jaccard')


percent_0 = 0
k5j0 = df[(df['k'] == 5) & (df['percentage'] ==percent_0)]
k5j0 = k5j0['variance']
k10j0 = df[(df['k'] == 10) & (df['percentage'] ==percent_0)]
k10j0 = k10j0['variance']
k15j0 = df[(df['k'] == 15) & (df['percentage'] ==percent_0)]
k15j0 = k15j0['variance']
k20j0 = df[(df['k'] == 20) & (df['percentage'] ==percent_0)]
k20j0 = k20j0['variance']
#print(k5j)

k5j0 = list(mean_confidence_interval(k5j0))
k5j0.insert(0,5)
#print(k5j)
#k5j.insert(1,'Jaccard')
k10j0 = list(mean_confidence_interval(k10j0))
k10j0.insert(0,10)
#k10j.insert(1,'Jaccard')
k15j0 = list(mean_confidence_interval(k15j0))
k15j0.insert(0,15)
#k15j.insert(1,'Jaccard')
k20j0 = list(mean_confidence_interval(k20j0))
k20j0.insert(0,20)
#k20j.insert(1,'Jaccard')


df = pd.DataFrame([k5j, k10j, k15j,k20j])
df.columns = ['k','mean','lb','ub']

mean0 = df['mean']
ub0 = df['ub']
lb0 = df['lb']
#print(ub0)


dfx = pd.DataFrame([k5j0, k10j0, k15j0,k20j0])
dfx.columns = ['k','mean','lb','ub']

mean00 = dfx['mean']
ub00 = dfx['ub']
lb00 = dfx['lb']
#print(ub0)


df1 = pd.read_csv(input_file2, names=['percentage','k','variance'])

k5r = df1[(df1['k'] == 5) & (df1['percentage'] == percent)]
k5r = k5r['variance']
k10r = df1[(df1['k'] == 10) & (df1['percentage'] == percent)]
k10r = k10r['variance']
k15r = df1[(df1['k'] == 15) & (df1['percentage'] == percent)]
k15r = k15r['variance']
k20r = df1[(df1['k'] == 20) & (df1['percentage'] == percent)]
k20r = k20r['variance']


k5r = list(mean_confidence_interval(k5r))
k5r.insert(0,5)
#k5r.insert(1,'RBO 0.95')
k10r = list(mean_confidence_interval(k10r))
k10r.insert(0,10)
#k10r.insert(1,'RBO 0.95')
k15r = list(mean_confidence_interval(k15r))
k15r.insert(0,15)
#k15r.insert(1,'RBO 0.95')
k20r = list(mean_confidence_interval(k20r))
k20r.insert(0,20)
#k20r.insert(1,'RBO 0.95')


k5r0 = df1[(df1['k'] == 5) & (df1['percentage'] ==percent_0)]
k5r0 = k5r0['variance']
k10r0 = df1[(df1['k'] == 10) & (df1['percentage'] ==percent_0)]
k10r0 = k10r0['variance']
k15r0 = df1[(df1['k'] == 15) & (df1['percentage'] ==percent_0)]
k15r0 = k15r0['variance']
k20r0 = df1[(df1['k'] == 20) & (df1['percentage'] ==percent_0)]
k20r0 = k20r0['variance']


k5r0 = list(mean_confidence_interval(k5r0))
k5r0.insert(0,5)
#k5r.insert(1,'RBO 0.95')
k10r0 = list(mean_confidence_interval(k10r0))
k10r0.insert(0,10)
#k10r.insert(1,'RBO 0.95')
k15r0 = list(mean_confidence_interval(k15r0))
k15r0.insert(0,15)
#k15r.insert(1,'RBO 0.95')
k20r0 = list(mean_confidence_interval(k20r0))
k20r0.insert(0,20)
#k20r.insert(1,'RBO 0.95')

df1 = pd.DataFrame([k5r, k10r, k15r,k20r])
df1.columns = ['k','mean','lb','ub']

mean1 = df1['mean']
ub1 = df1['ub']
lb1 = df1['lb']

df1x = pd.DataFrame([k5r0, k10r0, k15r0,k20r0])
df1x.columns = ['k','mean','lb','ub']

mean10 = df1x['mean']
ub10 = df1x['ub']
lb10 = df1x['lb']


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
ax.plot(mean0, lw = 1, color = '#539caf', alpha = 1, label = 'q1: readmitted = NO vs whole 10 % missing', marker='x', linestyle='-.', linewidth=2, markersize=12)
ax.plot(mean1, lw = 1, color = '#b65332', alpha = 1, label = 'q2: insulin = Steady vs !Steady 10 % missing', marker='<', linestyle='-', linewidth=2, markersize=12)

ax.plot(mean00, lw = 1, color = '#5be19a', alpha = 1, label = 'q1: readmitted = NO vs whole 0 % missing', marker='o', linestyle='-', linewidth=2, markersize=12)
ax.plot(mean10, lw = 1, color = '#ece554', alpha = 1, label = 'q2: insulin = Steady vs !Steady 0 % missing', marker='s', linestyle='--', linewidth=2, markersize=12)

# Shade the confidence interval
ax.fill_between(t, lb0, ub0, color = '#539caf', alpha = 0.4)
ax.fill_between(t, lb1, ub1, color = '#b65332', alpha = 0.4)
ax.fill_between(t, lb00, ub00, color = '#5be19a', alpha = 0.4)
ax.fill_between(t, lb10, ub10, color = '#e6a3ba', alpha = 0.4)

# Label the axes and provide a title
ax.set_title("Impact of k and missing attributes, 95% CI")
ax.set_xlabel("k")
ax.set_ylabel("variance topk set")
x = [5, 10, 15, 20]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
ax.set_ylim(ymin=0.0)
ax.set_ylim(ymax=0.02)

ax.legend(loc='best')

plt.savefig('plot/' + output_plot, format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()



