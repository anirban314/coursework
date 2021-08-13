# Coursera, Applied Data Science with Python, University of Michigan
# Course 2, Applied Plotting, Charting & Data Representation in Python
# Week 2: Peer-graded Assignment


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
    df = pd.read_csv('files/noaa-dataset.csv')
    df = split_dates(df)
    df = cleanup_data(df)

    df_10yr = get_record(df[df['YYYY'] != '2015'])
    df_2015 = get_record(df[df['YYYY'] == '2015'])

    max_2015 = df_2015[df_2015['Max'] > df_10yr['Max']]    #days in 2015 breaking 10yr HIGH
    min_2015 = df_2015[df_2015['Min'] < df_10yr['Min']]    #days in 2015 breaking 10yr LOW

    # Plotting the Graph
    plt.figure(figsize=(16,9), dpi=80)
    
    plt.plot(df_10yr.index, df_10yr['Max'], alpha=0.5, lw=1.5, ls=':', c='tab:blue', label='10-Year High')
    plt.plot(df_10yr.index, df_10yr['Min'], alpha=0.3, lw=1.2, ls='-', c='tab:blue', label='10-Year Low')
    plt.fill_between(df_10yr.index, df_10yr['Max'], df_10yr['Min'], alpha=0.1, color='tab:blue')

    plt.scatter(max_2015.index, max_2015['Max'], s=20, c='tab:red', label='2015 High')
    plt.scatter(min_2015.index, min_2015['Min'], s=20, c='darkslateblue', label='2015 Low')
    
    # Improving Data-Ink Ratio
    pretty_x = prettify_x(df_2015)
    plt.xticks(ticks=pretty_x.index, labels=pretty_x)
    
    pretty_y = prettify_y(-30, 40)
    plt.yticks(ticks=pretty_y.index, labels=pretty_y)

    plt.title('Daily Record High and Low Temperatures for the Period 2005-2014\nvs. New Daily Record Temperatures in 2015 near Ann Arbor, MI',
        fontsize='x-large',
        color='slategrey',
        pad=10
    )
    plt.tick_params(axis='both', right=True, labelright=True, labelsize='medium', colors='slategrey')
    plt.legend(frameon=False, loc='lower center', markerscale=1.25, fontsize='large', labelcolor='slategrey', labelspacing=0.75)
    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    plt.show()


def split_dates(df):
    # Date Format in CSV: YYYY-MM-DD
    df['YYYY'] = df['Date'].apply(lambda x: x[:4])
    df['MMDD'] = df['Date'].apply(lambda x: x[5:])
    return df


def cleanup_data(df):
    df = df[df['MMDD'] != '02-29']              #dropping all records for leap days
    df['Data_Value'] = df['Data_Value'] / 10    #converting 'tenths of degrees C' back to 'degrees C'
    return df


def get_record(df):
    df_max = (
        df[df['Element']=='TMAX']
        .groupby('MMDD', as_index=False)
        .agg({'Data_Value':np.max})
        .rename(columns={'Data_Value':'Max'})
    )
    df_min = (
        df[df['Element']=='TMIN']
        .groupby('MMDD', as_index=False)
        .agg({'Data_Value':np.min})
        .rename(columns={'Data_Value':'Min'})
    )
    return pd.merge(df_max, df_min, how='outer', on='MMDD')


def prettify_x(df):
    tick_loc = df[df['MMDD'].str.endswith('-01')].index
    tick_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return pd.Series(tick_labels, index=tick_loc)


def prettify_y(low, high):
    tick_loc = [*range(low, high+1, 10)]
    tick_labels = []
    for num in tick_loc:
        if num%20 == 0:
            tick_labels.append(f'{num}\u2103')      #\u2103=℃
        else:
            tick_labels.append('')
    return pd.Series(tick_labels, index=tick_loc)


if __name__ == '__main__':
    main()