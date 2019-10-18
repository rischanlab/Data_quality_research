import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

input_file_ideal_standard_rbo = 'results/ideal_vs_standard_rbo.csv'
input_file_ideal_dynamic_rbo = 'results/ideal_vs_dynamic_rbo.csv'
input_file_standard_dynamic_rbo = 'results/standard_vs_dynamic_rbo.csv'

input_file_ideal_standard_jc = 'results/ideal_vs_standard_jaccard.csv'
input_file_ideal_dynamic_jc = 'results/ideal_vs_dynamic_jaccard.csv'
input_file_standard_dynamic_jc = 'results/standard_vs_dynamic_jaccard.csv'

output_plot_ideal_vs_standard = 'ideal_vs_standard'
output_plot_ideal_vs_dynamic = 'ideal_vs_dynamic'
output_plot_standard_vs_dynamic = 'standard_vs_dynamic'

# ===============================================================
# IDEAL VS STANDARD

df = pd.read_csv(input_file_ideal_standard_rbo, names=['k','p','rbo'])
dfj = pd.read_csv(input_file_ideal_standard_jc, names=['k','Jaccard'])
df = pd.pivot_table(df, values='rbo', index=['k'], columns=['p'])
df['Jaccard'] = pd.Series(dfj['Jaccard'].values, index=df.index)

df = df.rename(columns={0.8:'RBO p 0.8',0.85:'RBO p 0.85',0.9:'RBO p 0.9',0.95:'RBO p 0.95',0.99:'RBO p 0.99'})

my_color = ['purple', 'blue', 'green', 'brown', 'black', 'red']
print(df)

markers = ['s','x','*','+','<','o']
linestyles = [':','-.','-','--','-.','-']
ax = df.plot(kind='line', markersize=7, linewidth=1, color=my_color)
for i, line in enumerate(ax.get_lines()):
    line.set_marker(markers[i])

for i, line in enumerate(ax.get_lines()):
    line.set_linestyle(linestyles[i])

# for adding legend
ax.legend(ax.get_lines(), df.columns, loc='best')
plt.xlabel('$k$', fontsize=10)
plt.ylabel('$effectiveness\ score$ standard to ideal', fontsize=10)
plt.xticks([5,10,15,20])
plt.legend(frameon=False)
ax.set_ylim(ymin=0.10)

plt.savefig('plot/' + output_plot_ideal_vs_standard, format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot_ideal_vs_standard + '.png')
plt.show()

# ===============================================================
# IDEAL VS DYNAMIC

df = pd.read_csv(input_file_ideal_dynamic_rbo, names=['k','p','rbo'])
dfj = pd.read_csv(input_file_ideal_dynamic_jc, names=['k','Jaccard'])
df = pd.pivot_table(df, values='rbo', index=['k'], columns=['p'])
df['Jaccard'] = pd.Series(dfj['Jaccard'].values, index=df.index)

df = df.rename(columns={0.8:'RBO p 0.8',0.85:'RBO p 0.85',0.9:'RBO p 0.9',0.95:'RBO p 0.95',0.99:'RBO p 0.99'})

my_color = ['purple', 'blue', 'green', 'brown', 'black', 'red']
print(df)

markers = ['s','x','*','+','<','o']
linestyles = [':','-.','-','--','-.','-']
ax = df.plot(kind='line', markersize=7, linewidth=1, color=my_color)
for i, line in enumerate(ax.get_lines()):
    line.set_marker(markers[i])

for i, line in enumerate(ax.get_lines()):
    line.set_linestyle(linestyles[i])

# for adding legend
ax.legend(ax.get_lines(), df.columns, loc='best')
plt.xlabel('$k$', fontsize=10)
plt.ylabel('$effectiveness\ score$ dynamic to ideal', fontsize=10)
plt.xticks([5,10,15,20])
plt.legend(frameon=False)
ax.set_ylim(ymin=0.10)

plt.savefig('plot/' + output_plot_ideal_vs_dynamic, format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot_ideal_vs_dynamic + '.png')
plt.show()

# ===============================================================
# STANDARD VS DYNAMIC

df = pd.read_csv(input_file_standard_dynamic_rbo, names=['k','p','rbo'])
dfj = pd.read_csv(input_file_standard_dynamic_jc, names=['k','Jaccard'])
df = pd.pivot_table(df, values='rbo', index=['k'], columns=['p'])
df['Jaccard'] = pd.Series(dfj['Jaccard'].values, index=df.index)

df = df.rename(columns={0.8:'RBO p 0.8',0.85:'RBO p 0.85',0.9:'RBO p 0.9',0.95:'RBO p 0.95',0.99:'RBO p 0.99'})

my_color = ['purple', 'blue', 'green', 'brown', 'black', 'red']
print(df)

markers = ['s','x','*','+','<','o']
linestyles = [':','-.','-','--','-.','-']
ax = df.plot(kind='line', markersize=7, linewidth=1, color=my_color)
for i, line in enumerate(ax.get_lines()):
    line.set_marker(markers[i])

for i, line in enumerate(ax.get_lines()):
    line.set_linestyle(linestyles[i])

# for adding legend
ax.legend(ax.get_lines(), df.columns, loc='best')
plt.xlabel('$k$', fontsize=10)
plt.ylabel('$effectiveness\ score$ dynamic to standard', fontsize=10)
plt.xticks([5,10,15,20])
plt.legend(frameon=False)
ax.set_ylim(ymin=0.10)

plt.savefig('plot/' + output_plot_standard_vs_dynamic, format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot_standard_vs_dynamic + '.png')
plt.show()


# IMPACT OF M ON EFFECIENCY
#
# df = pd.read_csv("results/impact_m_efficiency.csv")
#
# my_color = ['purple', 'blue', 'green', 'brown', 'black', 'red']
#
# markers = ['s','x','*','+','<','o']
# linestyles = [':','-.','-','--','-.','-']
# ax = df.plot(kind='line', markersize=7, linewidth=1, color=my_color)
# for i, line in enumerate(ax.get_lines()):
#     line.set_marker(markers[i])
#
# for i, line in enumerate(ax.get_lines()):
#     line.set_linestyle(linestyles[i])
#
# # for adding legend
# ax.legend(ax.get_lines(), df.columns, loc='best')
# plt.xlabel('$k$', fontsize=10)
# plt.ylabel('$effectiveness\ score$ dynamic to standard', fontsize=10)
# plt.xticks([5,10,15,20])
# plt.legend(frameon=False)
# ax.set_ylim(ymin=0.10)
#
# plt.savefig('plot/' + output_plot_standard_vs_dynamic, format="svg", dpi = 1000)
# plt.savefig('plot/' + output_plot_standard_vs_dynamic + '.png')
# plt.show()
