import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np
import calplot
import plotly.express as px



def plot_correlation(df, title = 'Matrice de corrélation'):
    """
    df: dataframe

    return: heatmap of correlation
    """
    corr = df.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    f, ax = plt.subplots(figsize=(8, 7))
    cmap = sns.diverging_palette(230, 20, as_cmap=True)
    ax.set_title(title)
    sns.heatmap(corr,annot=True, fmt='.2f', mask=mask, cmap=cmap, vmax=.3, center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5})

def plot_mean_corr(df):
    """
    df: dataframe
    
    return: moyenne des matrices de corrélation des 12 mois
    """
    df_ = df[df.index.month == 1 ]
    corr_ = df_.corr()
    corr_ = corr_.fillna(0)
    for m in range(2,13): 
        df_ = df[df.index.month == m ]
        new_corr = df_.corr()
        new_corr = new_corr.fillna(0)
        corr_ += new_corr
    corr_/=12
    mask = np.triu(np.ones_like(corr_, dtype=bool))
    f, ax = plt.subplots(figsize=(11, 9))
    cmap = sns.diverging_palette(230, 20, as_cmap=True)
    title= 'Moyenne des corrélations par mois sur 2012 '
    ax.set_title(title)
    sns.heatmap(corr_,annot=True, fmt='.2f', mask=mask, cmap=cmap, vmax=.3, center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5})
    
    
def plot_ts(df, title="", x_label="", y_label=""):
    """
    df: dataframe
    title: titre du plot
    x_label: nom de l'axe x
    y_label: nom de l'axe y

    return: plot de la série temporelle
    """
    fig = px.line(df, title = title)
    fig.update_xaxes(title_text = x_label)
    fig.update_yaxes(title_text = y_label)
    fig.show()
def plot_list_ts(df, ts_columns): 
    """
    df: dataframe
    list: list de colonnes à plot

    return: plot de la série temporelle
    """
    for col in ts_columns:
        titre= "Serie temporelle: "+col
        plot_ts(df[col], titre, "Date", col)

def plot_calendar(df, column):
    """
    df: dataframe
    column: colonne à plot

    return: plot du calendrier
    """
    pl = calplot.calplot(data = df[column],how = 'sum', cmap = 'Reds', figsize = (12, 12), suptitle = column)
    
