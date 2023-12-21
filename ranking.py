import pandas as pd
import openpyxl


def set_ranking(ranking_df, player):
    pass


def load_ranking():
    try:
        print(type(pd.read_excel("ranking.xlsx", engine="openpyxl")))
        return pd.read_excel("ranking.xls", engine="openpyxl")
    except:
        open("ranking.xls", engine="openpyxl")
        print("\nThere was no ranking, so I created one!")
        return
            