import pandas as pd
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