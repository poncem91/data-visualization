import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------   
# Data Visualization
# Mariafe Ponce                   
# ---------------------------------------------
""" Program creates three data visualizations.
    1)  Is a bar graph that shows the average review
        score for each video game publisher.
    2)  Shows a line graph of number of games released
        each year by different consoles.
    3)  Shows a pie chart of the distribution of video
        game sales by rating category.
"""
# ---------------------------------------------
def main(file_name):
    
    # loads csv file into pandas dataframe
    data = pd.read_csv(file_name)

    # calls each visualization function
    rating_publisher_score(data)
    games_per_year(data)
    sales_by_rating(data)
    
# ---------------------------------------------
# Function creates a bar graph of average
# review scores based on rating category
# ---------------------------------------------

def rating_publisher_score(df):
    
    # calculates mean of data grouped by publisher
    rating_review = df.groupby('Metadata.Publishers').mean()

    # plots mean score by publisher sorted in ascending order
    ax = rating_review['Metrics.Review Score'].sort_values().plot.bar(title="Average Review Score per Publisher",
                                                   color=["maroon","navy","orange"],figsize=(13,7), ylim=(55,95),
                                                   yticks=(np.arange(55, 95.1, 5)), fontsize=8)
    #labels each bar with its score
    for p in ax.patches:
        ax.annotate("{:.1f}".format((p.get_height())), xy=(p.get_x(), p.get_height()+0.5), fontsize=7)

    #labels graph's axis
    plt.xlabel("Publisher")
    plt.ylabel("Average Review Score")
    
    # improves layout
    plt.tight_layout()
    plt.show()

# ---------------------------------------------
# Function creates a line graph of number of 
# games released per year by console
# ---------------------------------------------

def games_per_year(df):

    # calculates number of games released each year by console and sorts by year
    game_count = df.groupby('Release.Year')['Release.Console'].value_counts().sort_index().unstack()

    # plots number of games released by year by console
    game_count.plot(kind='line', title="Games Released per Year per Console",
                    xticks=(np.arange(2004,2009,1)),
                    yticks=(np.arange(0,130,10)), grid=True, fontsize=8,
                    color=["red","blue","orange","purple","green"],
                    figsize=(13,7))

    # label appropriately
    plt.xlabel("Year")
    plt.ylabel("Number of Games Released")
    plt.legend()

    # improves layout
    plt.tight_layout()
    plt.show()
    
# ---------------------------------------------
# Function creates a pie graph of percent
# of sales by each game rating category
# ---------------------------------------------

def sales_by_rating(df):

    # groups data by Rating and calculates sum of each variable
    by_rating = df.groupby('Release.Rating').sum()

    # plots a pie chart showing the proportions of total sales for each Rating
    by_rating['Metrics.Sales'].plot(kind='pie', fontsize=10, autopct='%1.1f%%',
                                    colors=["crimson","gold","gray"],
                                    title="Percent of Total Sales by\nVideo Game Rating Category",
                                    labels=["Everyone","Mature","Teen"],figsize=(6,6),
                                    labeldistance=1.05, explode=[0.08,0,0])

    # gets rid of out of place label
    plt.ylabel("")

    # improves layout
    plt.tight_layout()
    plt.show()

# ---------------------------------------------

main("video_games.csv")
