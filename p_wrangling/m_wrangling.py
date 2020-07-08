import pandas as pd


# wrangling functions

def get_country_name(df, cc):
    # df['Country'] = df['Country'].apply(lambda x: cc[x])
    df['Country'] = df['Country'].map(cc)
    return df


def normalize_gender(df):
    df['Gender'] = df['Gender'].apply(lambda x: 'Female' if x == "Fem" else x.lower().capitalize())
    return df


def normalize_age(x):
    x = re.sub(r'\D', '', x)
    if int(x) > 1000:
        return 2016 - int(x)
    else:
        return int(x)


def clean_skills(df,country=None):
    # drop null education
    df_sk = df.dropna(subset=['Education Level'])
    # most repeated job
    if not country:
        country = "All"
        # most repeated job
        df_sk = df_sk.groupby(['Job Code','Education Level']).size()
        df_new = pd.DataFrame(df_sk).reset_index()
        idx = df_new.groupby(['Education Level'])[0].transform(max) == df_new[0]
        df_new = df_new[idx]
        return df_new
    else:
        #most repeated job per education level
        df_sk = df_sk.groupby(['Country','Job Code','Education Level']).size()
        df_new = pd.DataFrame(df_sk).reset_index()
        df_new = df_new[df_new['Country']==country]
        df_new = df_new.groupby(['Education Level','Country','Job Code'])[0].max().sort_values(ascending=False).reset_index()
        df_new = df_new.groupby(['Country','Education Level']).head(1)
        return df_new


def csv_to_html(x):
    i = 0
    new_location = []
    for y in x:
        df = pd.read_csv(y)
        df.to_html(f'data/html/table-{i}.html')
        new_location.append(f'data/html/table-{i}.html')
        i += 1
    return new_location
