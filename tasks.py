import pandas as pd 

# some usefull functions for repetative data processing tasks before and after using the scripts

def get_gender_dictionaty(df):
    """ Returns a dictionary where KEY is FIRST NAME and VALUE is GENDER. 
    	Dictionary is generated from a dataframe with a 'gender' column and 'name' column
    """
    df = df[df['gender'] != 'unknown']
    gender_dict = df[['name','gender']].set_index('name')['gender'].to_dict()
    return gender_dict

def save_lst_as_df(lst,col_name,path,header=True, index=False, encoding = "utf-8"):
	""" Returns a dataframe generated from the passed list, saves it as csv at specified path
	"""
    df = pd.DataFrame({
    col_name: lst  
    })
    df.to_csv(path,header=header,index=index,encoding = encoding)
    print("Dataframe saved at: "+path)
    return df 

def print_stats(df, col):
    """ Prints the number of instances in the data set, number of instances with a known value,
        absolute and relative frequencies.
    """
    dic = df[col].value_counts().to_dict()
    total = sum(dic.values())
    print("Total in dataset: ", len(df))
    print("Total gender determined: ", total)
    print("Ratio known/total: ", total / len(df))
#     print(sum(dic.values()))
    print(dic)
#     print 
#     print(df[col].value_counts())
    dic.update((k, v / total ) for k,v in dic.items())
    print(dic)

def concat_dataframes(df_list = []):
	""" Verticaly concats given data frames 
	"""
    return pd.concat(df_list)

# add filter unknown or nan