import pandas as pd
import sys
from genderize import Genderize
# Genderize client can be downloaded from:
# https://pypi.python.org/pypi/Genderize

genderize = Genderize(
    user_agent='GenderizeDocs/0.0',
    api_key='ebebc52f3b62785a2736f670eba79cad')  # API key


def fetch_gender(name_list, genderize_obj):
    """Return a list of dictionaries, a dictionary for each name in the passed list
    name_list.
    """
    # name_list = df.cleaned_name.unique()
    gender_list = []
    for i in range(0, len(name_list), 10):
        gender_list.append(genderize_obj.get(name_list[i:i + 10]))
    gender_list[0]
    gender_list_flat = [item for sublist in gender_list for item in sublist]
    return gender_list_flat

def get_dataframe(flat_list):
    """ Returns pandas dataframe, where every row is a dictionary from the flat list
    """
    return pd.DataFrame(flat_list)

def get_stats(df,col):
    """ Returns a dictionary with number absolute and relative frequency
    """
    total =len(df)
    dic =  df[col].value_counts().to_dict()
    for k,v in dic.items():
        dic[k] = [v,round(v/total,2)]
    return dic

def load_file(path,col,typ="json"):
    """ Returns list of unique names from a specified file, and column
    """
    if typ == "csv":
        df = pd.read_csv(path)
    else:
        df = pd.read_json(path)
    name_list = df[col].unique()
    return name_list

def save_file(df,path,typ="json"):
    """Saves dataframe as file in specified format:
       JSON or CSV
    """
    if typ == "csv":
        df.to_csv(path)
    else:
        df.to_json(path)
    print("File saved at: "+path)

if __name__ == "__main__":

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # example

    name_list = load_file(input_path,"name")

    print("Fetching gender...")

    flat_list = fetch_gender(name_list,genderize)

    df = get_dataframe(flat_list)

    print("Stats: {}".format(get_stats(df,"gender")))

    save_file(df,output_path,"csv")