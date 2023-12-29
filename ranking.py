import pandas as pd
import openpyxl


def create_ranking():
    # Base DataFrame
    ranking_df = pd.DataFrame({
        "ID": [],
        "Name": [],
        "Record Stage": []
    })

    ranking_df2 = ranking_df.copy()

    # Transforming in Excel
    with pd.ExcelWriter("ranking.xlsx", engine='openpyxl') as writer:
        ranking_df.to_excel(writer, sheet_name="Sheet1", index=False)
        ranking_df2.to_excel(writer, sheet_name="Sheet2", index=False)


def load_ranking(sheet_name):
    with pd.ExcelFile("ranking.xlsx") as xls:
        ranking_df = pd.read_excel(xls, sheet_name=sheet_name)
    
    return ranking_df


def set_ranking(ranking_df, player) :
    # Defining data about the current player
    new_row = {
        "ID": player.get_cpf(),
        "Name": player.get_name(),
        "Record Stage": player.get_stage()
    }

    # DataFrame to dict 'cause of ease of handling
    ranking_dict_list = ranking_df.to_dict(orient='records')

    # First filter (Name, ID and better score, in other words, there will be replacement)
    filtered_ranking_dict_list = [registered_name for registered_name in ranking_dict_list if not (player.get_name() == registered_name["Name"] and player.get_cpf() == registered_name["ID"] and player.get_stage() > registered_name["Record Stage"])]

    # If the length is equal, the first filter don't filtered nothing
    if(len(ranking_dict_list) == len(filtered_ranking_dict_list)):

        # Checking if the Name and/or ID are unique OR if we already have this Name and ID but score isn't better than that one defined in Excel
        filtered_ranking_dict_list_2 = [registered_name for registered_name in filtered_ranking_dict_list if not (player.get_name() == registered_name["Name"] and player.get_cpf() == registered_name["ID"])]
        
        # If the legth is different, so the we already have the Name and ID but the score is worst than that one in Excel, so we only sort the existing list
        if(len(filtered_ranking_dict_list_2) != len(filtered_ranking_dict_list)):
            sorted_ranking = sorted(ranking_dict_list, key=lambda x: x['Record Stage'], reverse=True)

        # If the length is equal, so we don't have this Name and ID in Excel, so we need to add
        else:
            filtered_ranking_dict_list_2.append(new_row)
            sorted_ranking = sorted(filtered_ranking_dict_list_2, key=lambda x: x['Record Stage'], reverse=True)

    # If the first filter isn't equal of the Excel ranking, it's a sign we need to replace some row in Excel so we're gonna add the new row
    else:
        filtered_ranking_dict_list.append(new_row)
        sorted_ranking = sorted(filtered_ranking_dict_list, key=lambda x: x['Record Stage'], reverse=True)

    return pd.DataFrame(sorted_ranking)


def update_ranking(new_ranking_df, main_sheet_name, supporting_sheet_name):

    # We need to overwrite Excel, so we also need the sheet that isn't being used
    supporting_ranking_df = load_ranking(supporting_sheet_name)

    with pd.ExcelWriter("ranking.xlsx", engine="openpyxl") as writer:
        new_ranking_df.to_excel(writer, sheet_name=main_sheet_name, index=False)
        supporting_ranking_df.to_excel(writer, sheet_name=supporting_sheet_name, index=False)