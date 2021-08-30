import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def detailed_scatter(subplot, x, y, title):
    x_mean, x_std = x.mean(), x.std()
    y_mean, y_std = y.mean(), y.std()
    temp_corr = x.corr(y)
    # I prefer titles of my plots to be descriptive
    complete_title = "{}\n".format(title) + \
                 "x mean = {:.2f}, x std = {:.2f}\n".format(x_mean, x_std) + \
                 "y mean = {:.2f}, y std = {:.2f}\n".format(y_mean, y_std) + \
                 "correlation = {:.2f}\n".format(temp_corr)
    subplot.scatter(x, y, c='black') 
    subplot.set_title(complete_title, pad=-990)
    subplot.set_xlabel('x')
    subplot.set_ylabel('y')
    return

def scatter_with_trendline(subplot, x, y, title):
    detailed_scatter(subplot, x, y, title)
    fitted_reg = np.poly1d(np.polyfit(x, y, 1))
    subplot.plot(x, fitted_reg(x), 'r', label='{}'.format(fitted_reg))
    subplot.legend(loc='lower right')
    return

if __name__ == '__main__':
    quartet = pd.read_csv('data/anscombe_quartet.csv', sep=',')
    quartet_means = quartet.groupby(['dataset']).mean()
    quartet_standard_dev = quartet.groupby(['dataset']).std()

    # Plot & Save the Anscombe Quartet Dataset
    cat = pd.unique(quartet['dataset'])
    fig, axs = plt.subplots(2,2, figsize=(10,10))
    fig.subplots_adjust(wspace=0.5, hspace=0.5)
    for x in range(2):
        for y in range(2):
            temp_category = cat[(x * 2) + y]
            temp_x = quartet[quartet['dataset'] == temp_category]['x']
            temp_y = quartet[quartet['dataset'] == temp_category]['y']
            scatter_with_trendline(axs[x, y],temp_x, temp_y, temp_category)
    plt.tight_layout()
    plt.savefig('generated_figures/quartet3.png')

    datasaurus = pd.read_csv('data/DatasaurusDozen.tsv', sep='\t')
    datasaurus_means = datasaurus.groupby(['dataset']).mean()
    datasaurus_standard_dev = datasaurus.groupby(['dataset']).std()

    # Plot & Save the Datasaurus Dataset
    categories = pd.unique(datasaurus['dataset'])
    fig, axs = plt.subplots(4,4, figsize=(15,15))
    fig.subplots_adjust(wspace=0.9, hspace=0.9)
    for x in range(4):
        for y in range(4):
            if((x * 4) + y >= len(categories)):
                fig.delaxes(axs[x, y])
            else:
                temp_category = categories[(x * 4) + y]
                temp_x = datasaurus[datasaurus['dataset'] == temp_category]['x']
                temp_y = datasaurus[datasaurus['dataset'] == temp_category]['y']
                detailed_scatter(axs[x,y], temp_x, temp_y, temp_category)
    fig.tight_layout()
    plt.savefig('generated_figures/datasaurus_dozen2.png')