
# coding: utf-8


import pandas as pd


def clean(x):
    try:
        return x["face"][0]["attribute"]["gender"]
    except:
        return {} 


def get_gender(x):
    if x == {}:
        return "Unknown"
    else:
        return str(x['value'])

def asign_score(dic,thres):
    if dic == {}:
        return 0
    elif dic['confidence'] < thres:
        return 0
    elif dic["value"] == "Male":
        return 1
    elif dic['value'] == "Female":
        return -1

def name_gender_lsit(df,names):
    lst = []
    for name in names:
        sub_list = []
        x = df[df["name"] == name]
        dic = dict(x.gender.value_counts())
        sub_list.append(name)
        gend_score = x["gend_score"].sum()
        if gend_score == 0:
            sub_list.append("Unknown")
        elif gend_score <0:
            sub_list.append("Female")
        elif gend_score >0:
            sub_list.append("Male")
        lst.append(sub_list)
    rdf = pd.DataFrame(lst)
    rdf.columns = ['name','gender']
    return rdf

def stats(d,total):
    for key, value in d.items():
        d[key] = value / total
    return d

def gender_df(path, path_save,thres=70):
    df = pd.read_json(path,lines=True)
    df.columns = ["name","props"]
    df["props"] = df["props"].apply(clean)
    df["gender"] = df["props"].apply(lambda x: get_gender(x))
    df["gend_score"] = df.props.apply(lambda x: asign_score(x,thres))
    names = df.name.unique()
    print("Total names:",len(names))
    print("Saving: "+path_save)
    df = name_gender_lsit(df,names)
    df.to_csv(path_save,index=False)
    dic = df.gender.value_counts().to_dict()
    print(dic)
    print(stats(dic,len(names)))
    return df

# formal = gender_df("google_img/formal.json","google_img/formal.csv",70)

# health = gender_df("google_img/health.json","google_img/health.csv")

def main():
    pass

if __name__ == "__main__":
   main()