import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col=0, parse_dates=True)

# Clean data
df = df[(df["value"] > df["value"].quantile(0.025)) & (df["value"] < df["value"].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=[12,4])
    plt.plot(df.index, df["value"], linewidth=1, color="red")
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
  
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby([df.index.year.rename('Year'), df.index.month_name().rename('Month')])['value'].mean().reset_index()
  
    # Draw bar plot
    fig = plt.figure(figsize=[4,6])
    sns.barplot(data=df_bar, y="value", x="Year", hue="Month", errorbar=None)
    df_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title="Months", labels=df_order)
  
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axs = plt.subplots(ncols=2, width_ratios=[1,2], sharex=False, sharey=True, figsize=(12,6))
    fig.tight_layout(w_pad=5)
    sns.boxplot(data=df_box, y="value", x="year", ax=axs[0], fliersize=2)
    sns.boxplot(data=df_box, y="value", x="month", ax=axs[1], fliersize=2, order=['Jan','Feb','Mar','Apr','May','Jun', 'Jul','Aug','Sep','Oct','Nov','Dec'])
    axs[0].set(xlabel="Year", ylabel="Page Views", title="Year-wise Box Plot (Trend)")
    axs[1].set(xlabel="Month", ylabel="Page Views", title="Month-wise Box Plot (Seasonality)")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
