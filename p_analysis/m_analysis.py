import pandas as pd
import numpy as np
import requests


# analysis functions

def filtering(df, country):
    filter = df['Country'] == country
    return df[filter]


def analyze(df, country=None):
    if country:
        filtered_df = df[df['Country'] == country]
        test = filtered_df.groupby(['Country', 'Job Title', 'Gender']).agg(Quantity=('Job Title', 'count'))
        test['Percentage'] = round(test['Quantity'] / sum(test['Quantity']) * 100, 2)
        return test.reset_index()
    else:
        print("no country")
        test = df.groupby(['Country', 'Job Title', 'Gender']).agg(Quantity=('Job Title', 'count'))
        test['Percentage'] = round(test['Quantity'] / sum(test['Quantity']) * 100, 2)
        return test.reset_index()


def get_poll_resume(df,country=None):
    # data agrupation
    df_sql = df
    filteryes = (df_sql['Vote'] == 'I would vote for it') | (df_sql['Vote'] == 'I would probably vote for it')
    filterno = (df_sql['Vote'] == 'I would vote against it') | (df_sql['Vote'] == 'I would probably vote against it')
    df_sql.loc[filteryes, 'Vote'] = 'In Favor'
    df_sql.loc[filterno, 'Vote'] = 'Against'

    # data manipulation
    df_agg = df_sql.groupby(['Country','Vote']).agg(yes=('n_args_for', 'mean'),no=('n_args_against', 'mean')).reset_index()
    df = df_agg[df_agg['Vote']!='I would not vote']
    df = df.rename(columns={'yes':'Number of Pro Arguments','no':'Number of Cons Arguments'})
    if country:
        df = df[df['Country']==country]
        return df
    else:
        return df


def get_skills_names(x):
    x = str(x)
    response = requests.get(f'http://api.dataatwork.org/v1/jobs/{x}/related_skills')
    if response.status_code != 404:
        skill_raw = response.json()['skills']
        results = [x['skill_name'] for x in skill_raw[0:10]]
        return results
    else:
        skill_raw = ['No related skills']
        return skill_raw


def get_skills_by_education(df):
    df['Skills'] = df['Job Code'].apply(get_skills_names)
    df_skills = pd.DataFrame(df['Skills'].values.tolist(), columns=['Skill-' + str(x) for x in range(1, 11)])
    final = pd.concat([df['Education Level'].reset_index(drop=True), df_skills.reset_index(drop=True)], axis=1)
    return final
