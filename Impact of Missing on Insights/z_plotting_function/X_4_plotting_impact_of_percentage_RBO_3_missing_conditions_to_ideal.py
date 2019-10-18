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

input_file_missing_attr_vs_ideal = 'results/missing_attributes_vs_ideal_10_executions.csv'
input_file_missing_measure_vs_ideal = 'results/missing_measures_vs_ideal_10_executions.csv'
input_file_missing_a_m_vs_ideal = 'results/missing_combine_a_m_vs_ideal_10_executions.csv'


output_plot = 'all_percentage_RBO_compare_three_missing_to_ideal'

# ===============================================================
# IDEAL VS STANDARD

df1 = pd.read_csv(input_file_missing_attr_vs_ideal, names=['percentage','k','RBO','Jaccard'])
df2 = pd.read_csv(input_file_missing_measure_vs_ideal, names=['percentage','k','RBO','Jaccard'])
df3 = pd.read_csv(input_file_missing_a_m_vs_ideal, names=['percentage','k','RBO','Jaccard'])


#Jaccard

df1j10 = df1[(df1['k'] == 5) & (df1['percentage'] == 10)]
df1j10 = df1j10['Jaccard']

df1j20 = df1[(df1['k'] == 5) & (df1['percentage'] == 20)]
df1j20 = df1j20['Jaccard']

df1j30 = df1[(df1['k'] == 5) & (df1['percentage'] == 30)]
df1j30 = df1j30['Jaccard']

df1j40 = df1[(df1['k'] == 5) & (df1['percentage'] == 40)]
df1j40 = df1j40['Jaccard']

df1j50 = df1[(df1['k'] == 5) & (df1['percentage'] == 50)]
df1j50 = df1j50['Jaccard']

df1j60 = df1[(df1['k'] == 5) & (df1['percentage'] == 60)]
df1j60 = df1j60['Jaccard']

df1j70 = df1[(df1['k'] == 5) & (df1['percentage'] == 70)]
df1j70 = df1j70['Jaccard']

df1j80 = df1[(df1['k'] == 5) & (df1['percentage'] == 80)]
df1j80 = df1j80['Jaccard']

df1j90 = df1[(df1['k'] == 5) & (df1['percentage'] == 90)]
df1j90 = df1j90['Jaccard']

df1j10 = list(mean_confidence_interval(df1j10))
df1j10.insert(0,10)
df1j10.insert(1,'Jaccard')

df1j20 = list(mean_confidence_interval(df1j20))
df1j20.insert(0,20)
df1j20.insert(1,'Jaccard')

df1j30 = list(mean_confidence_interval(df1j30))
df1j30.insert(0,30)
df1j30.insert(1,'Jaccard')

df1j40 = list(mean_confidence_interval(df1j40))
df1j40.insert(0,40)
df1j40.insert(1,'Jaccard')

df1j50 = list(mean_confidence_interval(df1j50))
df1j50.insert(0,50)
df1j50.insert(1,'Jaccard')

df1j60 = list(mean_confidence_interval(df1j60))
df1j60.insert(0,60)
df1j60.insert(1,'Jaccard')

df1j70 = list(mean_confidence_interval(df1j70))
df1j70.insert(0,70)
df1j70.insert(1,'Jaccard')

df1j80 = list(mean_confidence_interval(df1j80))
df1j80.insert(0,80)
df1j80.insert(1,'Jaccard')

df1j90 = list(mean_confidence_interval(df1j90))
df1j90.insert(0,90)
df1j90.insert(1,'Jaccard')

#RBO
df1r10 = df1[(df1['k'] == 5) & (df1['percentage'] == 10)]
df1r10 = df1r10['RBO']

df1r20 = df1[(df1['k'] == 5) & (df1['percentage'] == 20)]
df1r20 = df1r20['RBO']

df1r30 = df1[(df1['k'] == 5) & (df1['percentage'] == 30)]
df1r30 = df1r30['RBO']

df1r40 = df1[(df1['k'] == 5) & (df1['percentage'] == 40)]
df1r40 = df1r40['RBO']

df1r50 = df1[(df1['k'] == 5) & (df1['percentage'] == 50)]
df1r50 = df1r50['RBO']

df1r60 = df1[(df1['k'] == 5) & (df1['percentage'] == 60)]
df1r60 = df1r60['RBO']

df1r70 = df1[(df1['k'] == 5) & (df1['percentage'] == 70)]
df1r70 = df1r70['RBO']

df1r80 = df1[(df1['k'] == 5) & (df1['percentage'] == 80)]
df1r80 = df1r80['RBO']

df1r90 = df1[(df1['k'] == 5) & (df1['percentage'] == 90)]
df1r90 = df1r90['RBO']

df1r10 = list(mean_confidence_interval(df1r10))
df1r10.insert(0,10)
df1r10.insert(1,'RBO')

df1r20 = list(mean_confidence_interval(df1r20))
df1r20.insert(0,20)
df1r20.insert(1,'RBO')

df1r30 = list(mean_confidence_interval(df1r30))
df1r30.insert(0,30)
df1r30.insert(1,'RBO')

df1r40 = list(mean_confidence_interval(df1r40))
df1r40.insert(0,40)
df1r40.insert(1,'RBO')

df1r50 = list(mean_confidence_interval(df1r50))
df1r50.insert(0,50)
df1r50.insert(1,'RBO')

df1r60 = list(mean_confidence_interval(df1r60))
df1r60.insert(0,60)
df1r60.insert(1,'RBO')

df1r70 = list(mean_confidence_interval(df1r70))
df1r70.insert(0,70)
df1r70.insert(1,'RBO')

df1r80 = list(mean_confidence_interval(df1r80))
df1r80.insert(0,80)
df1r80.insert(1,'RBO')

df1r90 = list(mean_confidence_interval(df1r90))
df1r90.insert(0,90)
df1r90.insert(1,'RBO')


df2j10 = df2[(df2['k'] == 5) & (df2['percentage'] == 10)]
df2j10 = df2j10['Jaccard']

df2j20 = df2[(df2['k'] == 5) & (df2['percentage'] == 20)]
df2j20 = df2j20['Jaccard']

df2j30 = df2[(df2['k'] == 5) & (df2['percentage'] == 30)]
df2j30 = df2j30['Jaccard']

df2j40 = df2[(df2['k'] == 5) & (df2['percentage'] == 40)]
df2j40 = df2j40['Jaccard']

df2j50 = df2[(df2['k'] == 5) & (df2['percentage'] == 50)]
df2j50 = df2j50['Jaccard']

df2j60 = df2[(df2['k'] == 5) & (df2['percentage'] == 60)]
df2j60 = df2j60['Jaccard']

df2j70 = df2[(df2['k'] == 5) & (df2['percentage'] == 70)]
df2j70 = df2j70['Jaccard']

df2j80 = df2[(df2['k'] == 5) & (df2['percentage'] == 80)]
df2j80 = df2j80['Jaccard']

df2j90 = df2[(df2['k'] == 5) & (df2['percentage'] == 90)]
df2j90 = df2j90['Jaccard']

df2j10 = list(mean_confidence_interval(df2j10))
df2j10.insert(0,10)
df2j10.insert(1,'Jaccard')

df2j20 = list(mean_confidence_interval(df2j20))
df2j20.insert(0,20)
df2j20.insert(1,'Jaccard')

df2j30 = list(mean_confidence_interval(df2j30))
df2j30.insert(0,30)
df2j30.insert(1,'Jaccard')

df2j40 = list(mean_confidence_interval(df2j40))
df2j40.insert(0,40)
df2j40.insert(1,'Jaccard')

df2j50 = list(mean_confidence_interval(df2j50))
df2j50.insert(0,50)
df2j50.insert(1,'Jaccard')

df2j60 = list(mean_confidence_interval(df2j60))
df2j60.insert(0,60)
df2j60.insert(1,'Jaccard')

df2j70 = list(mean_confidence_interval(df2j70))
df2j70.insert(0,70)
df2j70.insert(1,'Jaccard')

df2j80 = list(mean_confidence_interval(df2j80))
df2j80.insert(0,80)
df2j80.insert(1,'Jaccard')

df2j90 = list(mean_confidence_interval(df2j90))
df2j90.insert(0,90)
df2j90.insert(1,'Jaccard')

#RBO
df2r10 = df2[(df2['k'] == 5) & (df2['percentage'] == 10)]
df2r10 = df2r10['RBO']

df2r20 = df2[(df2['k'] == 5) & (df2['percentage'] == 20)]
df2r20 = df2r20['RBO']

df2r30 = df2[(df2['k'] == 5) & (df2['percentage'] == 30)]
df2r30 = df2r30['RBO']

df2r40 = df2[(df2['k'] == 5) & (df2['percentage'] == 40)]
df2r40 = df2r40['RBO']

df2r50 = df2[(df2['k'] == 5) & (df2['percentage'] == 50)]
df2r50 = df2r50['RBO']

df2r60 = df2[(df2['k'] == 5) & (df2['percentage'] == 60)]
df2r60 = df2r60['RBO']

df2r70 = df2[(df2['k'] == 5) & (df2['percentage'] == 70)]
df2r70 = df2r70['RBO']

df2r80 = df2[(df2['k'] == 5) & (df2['percentage'] == 80)]
df2r80 = df2r80['RBO']

df2r90 = df2[(df2['k'] == 5) & (df2['percentage'] == 90)]
df2r90 = df2r90['RBO']

df2r10 = list(mean_confidence_interval(df2r10))
df2r10.insert(0,10)
df2r10.insert(1,'RBO')

df2r20 = list(mean_confidence_interval(df2r20))
df2r20.insert(0,20)
df2r20.insert(1,'RBO')

df2r30 = list(mean_confidence_interval(df2r30))
df2r30.insert(0,30)
df2r30.insert(1,'RBO')

df2r40 = list(mean_confidence_interval(df2r40))
df2r40.insert(0,40)
df2r40.insert(1,'RBO')

df2r50 = list(mean_confidence_interval(df2r50))
df2r50.insert(0,50)
df2r50.insert(1,'RBO')

df2r60 = list(mean_confidence_interval(df2r60))
df2r60.insert(0,60)
df2r60.insert(1,'RBO')

df2r70 = list(mean_confidence_interval(df2r70))
df2r70.insert(0,70)
df2r70.insert(1,'RBO')

df2r80 = list(mean_confidence_interval(df2r80))
df2r80.insert(0,80)
df2r80.insert(1,'RBO')

df2r90 = list(mean_confidence_interval(df2r90))
df2r90.insert(0,90)
df2r90.insert(1,'RBO')

df3j10 = df3[(df3['k'] == 5) & (df3['percentage'] == 10)]
df3j10 = df3j10['Jaccard']

df3j20 = df3[(df3['k'] == 5) & (df3['percentage'] == 20)]
df3j20 = df3j20['Jaccard']

df3j30 = df3[(df3['k'] == 5) & (df3['percentage'] == 30)]
df3j30 = df3j30['Jaccard']

df3j40 = df3[(df3['k'] == 5) & (df3['percentage'] == 40)]
df3j40 = df3j40['Jaccard']

df3j50 = df3[(df3['k'] == 5) & (df3['percentage'] == 50)]
df3j50 = df3j50['Jaccard']

df3j60 = df3[(df3['k'] == 5) & (df3['percentage'] == 60)]
df3j60 = df3j60['Jaccard']

df3j70 = df3[(df3['k'] == 5) & (df3['percentage'] == 70)]
df3j70 = df3j70['Jaccard']

df3j80 = df3[(df3['k'] == 5) & (df3['percentage'] == 80)]
df3j80 = df3j80['Jaccard']

df3j90 = df3[(df3['k'] == 5) & (df3['percentage'] == 90)]
df3j90 = df3j90['Jaccard']

df3j10 = list(mean_confidence_interval(df3j10))
df3j10.insert(0,10)
df3j10.insert(1,'Jaccard')

df3j20 = list(mean_confidence_interval(df3j20))
df3j20.insert(0,20)
df3j20.insert(1,'Jaccard')

df3j30 = list(mean_confidence_interval(df3j30))
df3j30.insert(0,30)
df3j30.insert(1,'Jaccard')

df3j40 = list(mean_confidence_interval(df3j40))
df3j40.insert(0,40)
df3j40.insert(1,'Jaccard')

df3j50 = list(mean_confidence_interval(df3j50))
df3j50.insert(0,50)
df3j50.insert(1,'Jaccard')

df3j60 = list(mean_confidence_interval(df3j60))
df3j60.insert(0,60)
df3j60.insert(1,'Jaccard')

df3j70 = list(mean_confidence_interval(df3j70))
df3j70.insert(0,70)
df3j70.insert(1,'Jaccard')

df3j80 = list(mean_confidence_interval(df3j80))
df3j80.insert(0,80)
df3j80.insert(1,'Jaccard')

df3j90 = list(mean_confidence_interval(df3j90))
df3j90.insert(0,90)
df3j90.insert(1,'Jaccard')

#RBO
df3r10 = df3[(df3['k'] == 5) & (df3['percentage'] == 10)]
df3r10 = df3r10['RBO']

df3r20 = df3[(df3['k'] == 5) & (df3['percentage'] == 20)]
df3r20 = df3r20['RBO']

df3r30 = df3[(df3['k'] == 5) & (df3['percentage'] == 30)]
df3r30 = df3r30['RBO']

df3r40 = df3[(df3['k'] == 5) & (df3['percentage'] == 40)]
df3r40 = df3r40['RBO']

df3r50 = df3[(df3['k'] == 5) & (df3['percentage'] == 50)]
df3r50 = df3r50['RBO']

df3r60 = df3[(df3['k'] == 5) & (df3['percentage'] == 60)]
df3r60 = df3r60['RBO']

df3r70 = df3[(df3['k'] == 5) & (df3['percentage'] == 70)]
df3r70 = df3r70['RBO']

df3r80 = df3[(df3['k'] == 5) & (df3['percentage'] == 80)]
df3r80 = df3r80['RBO']

df3r90 = df3[(df3['k'] == 5) & (df3['percentage'] == 90)]
df3r90 = df3r90['RBO']

df3r10 = list(mean_confidence_interval(df3r10))
df3r10.insert(0,10)
df3r10.insert(1,'RBO')

df3r20 = list(mean_confidence_interval(df3r20))
df3r20.insert(0,20)
df3r20.insert(1,'RBO')

df3r30 = list(mean_confidence_interval(df3r30))
df3r30.insert(0,30)
df3r30.insert(1,'RBO')

df3r40 = list(mean_confidence_interval(df3r40))
df3r40.insert(0,40)
df3r40.insert(1,'RBO')

df3r50 = list(mean_confidence_interval(df3r50))
df3r50.insert(0,50)
df3r50.insert(1,'RBO')

df3r60 = list(mean_confidence_interval(df3r60))
df3r60.insert(0,60)
df3r60.insert(1,'RBO')

df3r70 = list(mean_confidence_interval(df3r70))
df3r70.insert(0,70)
df3r70.insert(1,'RBO')

df3r80 = list(mean_confidence_interval(df3r80))
df3r80.insert(0,80)
df3r80.insert(1,'RBO')

df3r90 = list(mean_confidence_interval(df3r90))
df3r90.insert(0,90)
df3r90.insert(1,'RBO')

df1 = pd.DataFrame([df1j10, df1j20, df1j30, df1j40, df1j50, df1j60, df1j70, df1j80, df1j90,
                   df1r10, df1r20, df1r30, df1r40,df1r50, df1r60,df1r70, df1r80,df1r90])
df1.columns = ['k','measurement','mean','lb','ub']

mean0 = df1[df1['measurement'] == 'Jaccard'].reset_index()
mean0 = mean0['mean']
ub0 = df1[df1['measurement'] == 'Jaccard'].reset_index()
ub0 = ub0['ub']
lb0 = df1[df1['measurement'] == 'Jaccard'].reset_index()
lb0 = lb0['lb']

mean1 = df1[df1['measurement'] == 'RBO'].reset_index()
mean1 = mean1['mean']
ub1 = df1[df1['measurement'] == 'RBO'].reset_index()
ub1 = ub1['ub']
lb1 = df1[df1['measurement'] == 'RBO'].reset_index()
lb1 = lb1['lb']

df2 = pd.DataFrame([df2j10, df2j20, df2j30, df2j40, df2j50, df2j60, df2j70, df2j80, df2j90,
                   df2r10, df2r20, df2r30, df2r40,df2r50, df2r60,df2r70, df2r80,df2r90])
df2.columns = ['k','measurement','mean','lb','ub']

mean2 = df2[df2['measurement'] == 'Jaccard'].reset_index()
mean2 = mean2['mean']
ub2 = df2[df2['measurement'] == 'Jaccard'].reset_index()
ub2 = ub2['ub']
lb2 = df2[df2['measurement'] == 'Jaccard'].reset_index()
lb2 = lb2['lb']

mean3 = df2[df2['measurement'] == 'RBO'].reset_index()
mean3 = mean3['mean']
ub3 = df2[df2['measurement'] == 'RBO'].reset_index()
ub3 = ub3['ub']
lb3 = df2[df2['measurement'] == 'RBO'].reset_index()
lb3 = lb3['lb']


df3 = pd.DataFrame([df3j10, df3j20, df3j30, df3j40, df3j50, df3j60, df3j70, df3j80, df3j90,
                   df3r10, df3r20, df3r30, df3r40,df3r50, df3r60,df3r70, df3r80,df3r90])
df3.columns = ['k','measurement','mean','lb','ub']

mean4 = df3[df3['measurement'] == 'Jaccard'].reset_index()
mean4 = mean4['mean']
ub4 = df3[df3['measurement'] == 'Jaccard'].reset_index()
ub4 = ub4['ub']
lb4 = df3[df3['measurement'] == 'Jaccard'].reset_index()
lb4 = lb4['lb']

mean5 = df3[df3['measurement'] == 'RBO'].reset_index()
mean5 = mean5['mean']
ub5 = df3[df3['measurement'] == 'RBO'].reset_index()
ub5 = ub5['ub']
lb5 = df3[df3['measurement'] == 'RBO'].reset_index()
lb5 = lb5['lb']

# Set some parameters to apply to all plots. These can be overridden
# in each plot if desired
import matplotlib
# Plot size to 14" x 7"
matplotlib.rc('figure', figsize = (14, 14))
# Font size to 14
matplotlib.rc('font', size = 20)
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
#ax.plot(mean0, lw = 1, color = '#539caf', alpha = 1, label = 'Jaccard Missing Attributes (A) to Ideal', marker='o', linestyle='dashed', linewidth=2, markersize=12)
ax.plot(mean1, lw = 1, color = '#b65332', alpha = 1, label = 'RBO 0.95 Missing Attributes (A) to Ideal', marker='s', linestyle=':', linewidth=2, markersize=12)

#ax.plot(mean2, lw = 1, color = '#5be19a', alpha = 1, label = 'Jaccard Missing Measure (M) to Ideal', marker='x', linestyle='-.', linewidth=2, markersize=12)
ax.plot(mean3, lw = 1, color = '#ece554', alpha = 1, label = 'RBO 0.95 Missing Measures (M) to Ideal', marker='<', linestyle='-', linewidth=2, markersize=12)

#ax.plot(mean4, lw = 1, color = '#b65332', alpha = 1, label = 'Jaccard Missing A and M to Ideal', marker='s', linestyle=':', linewidth=2, markersize=12)
ax.plot(mean5, lw = 1, color = '#5be19a', alpha = 1, label = 'RBO 0.95 Missing A and M to Ideal', marker='x', linestyle='-.', linewidth=2, markersize=12)

# Shade the confidence interval
#ax.fill_between(t, lb0, ub0, color = '#539caf', alpha = 0.4)
ax.fill_between(t, lb1, ub1, color = '#b65332', alpha = 0.4)

#ax.fill_between(t, lb2, ub2, color = '#5be19a', alpha = 0.4)
ax.fill_between(t, lb3, ub3, color = '#ece554', alpha = 0.4)

#ax.fill_between(t, lb4, ub4, color = '#b65332', alpha = 0.4)
ax.fill_between(t, lb5, ub5, color = '#539caf', alpha = 0.4)

# Label the axes and provide a title
ax.set_title("Impact of missing percentage on Effectiveness - 95% CI, k = 5")
ax.set_xlabel("percentage of missing (%)")
ax.set_ylabel("Effectiveness RBO 0.95")
x = [10, 20, 30, 40, 50, 60, 70, 80, 90]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
ax.set_ylim(ymin=0.0)
ax.set_ylim(ymax=1.0)

ax.legend(loc='upper right')

plt.savefig('plot/' + output_plot, format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()
