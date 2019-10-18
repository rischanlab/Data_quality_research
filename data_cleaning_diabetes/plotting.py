import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#input_file_ideal_standard_rbo = 'results/ideal_vs_standard_rbo.csv'
#input_file_ideal_dynamic_rbo = 'results/ideal_vs_dynamic_rbo.csv'
#input_file_standard_dynamic_rbo = 'results/standard_vs_dynamic_rbo.csv'

input_file_ideal_standard = 'results/ideal_vs_standard_plot.csv'
input_file_ideal_dynamic = 'results/ideal_vs_dynamic_plot.csv'
input_file_standard_dynamic = 'results/standard_vs_dynamic_plot.csv'

output_plot_ideal_vs_standard = 'ideal_vs_standard'
output_plot_ideal_vs_dynamic = 'ideal_vs_dynamic'
output_plot_standard_vs_dynamic = 'standard_vs_dynamic'

# ===============================================================
# IDEAL VS STANDARD

df = pd.read_csv(input_file_ideal_standard, index_col=0)

my_color = ['blue', 'blue', 'black', 'black', 'red', 'red']
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
plt.xlabel('Percentage of missing and impute', fontsize=10)
plt.ylabel('$effectiveness\ score$ standard to ideal', fontsize=10)
#plt.yticks([0.001,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
#plt.xticks([0,10,20,30,40,50,60,70,80,90,100])
plt.legend(frameon=False)
ax.set_ylim(ymin=0.0)

plt.savefig('plot/' + output_plot_ideal_vs_standard, format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot_ideal_vs_standard +'.png')
plt.show()

# ===============================================================
# IDEAL VS DYNAMIC

df = pd.read_csv(input_file_ideal_dynamic, index_col=0)

my_color = ['blue', 'blue', 'black', 'black', 'red', 'red']
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
plt.xlabel('Percentage of missing and impute', fontsize=10)
plt.ylabel('$effectiveness\ score$ dynamic to ideal', fontsize=10)
#plt.yticks([0.001,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
#plt.xticks([0,10,20,30,40,50,60,70,80,90,100])
plt.legend(frameon=False)
ax.set_ylim(ymin=0.0)

plt.savefig('plot/' + output_plot_ideal_vs_dynamic, format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot_ideal_vs_dynamic +'.png')
plt.show()


# ===============================================================
# STANDARD VS DYNAMIC

df = pd.read_csv(input_file_standard_dynamic, index_col=0)

my_color = ['blue', 'blue', 'black', 'black', 'red', 'red']
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
plt.xlabel('Percentage of missing and impute', fontsize=10)
plt.ylabel('$effectiveness\ score$ dynamic to standard', fontsize=10)
#plt.yticks([0.001,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
#plt.xticks([0,10,20,30,40,50,60,70,80,90,100])
plt.legend(frameon=False)
ax.set_ylim(ymin=0.0)

plt.savefig('plot/' + output_plot_standard_vs_dynamic, format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot_standard_vs_dynamic +'.png')
plt.show()