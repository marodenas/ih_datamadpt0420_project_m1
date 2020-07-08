import pandas as pd
import numpy as np
import requests
from sqlalchemy import create_engine
import re
from bs4 import BeautifulSoup
from p_wrangling import m_wrangling as mwr
import configparser


# acquisition functions
def get_data_from_sql():
    cfg = configparser.RawConfigParser()
    cfg.read('config.ini')
    sqlitedb_path = cfg['data']['db']
    print('Getting data from Database...')
    engine = create_engine(f'sqlite:///{sqlitedb_path}')
    data = pd.read_sql_query("SELECT career_info.normalized_job_code as 'Job Title', \
                                personal_info.gender as 'Gender', \
                                country_info.country_code as 'Country' \
                                FROM personal_info \
                                JOIN country_info on personal_info.uuid = country_info.uuid \
                                JOIN career_info on personal_info.uuid = career_info.uuid", engine)
    df_sql = mwr.normalize_gender(data)
    return df_sql


# get country name from webscraping
def get_country_name(df):
    cfg = configparser.RawConfigParser()
    cfg.read('config.ini')
    url = cfg['data']['url']
    print('Getting Countries from webscraping..')
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'lxml')
    td = soup.find_all('td')
    rows = [row.text for row in td if row != ""]
    rows_parsed = [re.sub(r'\W', '', x) for x in rows if x != "\n"]
    countries = {rows_parsed[x + 1]: rows_parsed[x] for x in range(0, len(rows_parsed) - 1, 2) if rows_parsed[x] != ""}
    countries['GR'] = 'Greece'
    countries['GB'] = 'Great Britain'
    data = mwr.get_country_name(df, countries)
    return data


# get title name from api
def get_job_title(x):
    if x == None:
        return "Unknown"
    else:
        x = str(x)
        response = requests.get(f'http://api.dataatwork.org/v1/jobs/{x}')
        return response.json()['title']


def get_normalized_job_title(df):
    print('Getting Job Title from Api...')
    jobs = df['Job Title'].unique()
    unique_jobs = {x: get_job_title(x) for x in jobs}
    # df['Job Title'] = df['Job Title'].apply(lambda x: unique_jobs[x] if x != 'Unknown' else x)
    df['Job Title'] = df['Job Title'].map(unique_jobs)
    return df


def get_poll_info():
    print('Getting Poll info...')
    cfg = configparser.RawConfigParser()
    cfg.read('config.ini')
    sqlitedb_path = cfg['data']['db']
    engine = create_engine(f'sqlite:///{sqlitedb_path}')
    data = pd.read_sql_query("SELECT poll_info.question_bbi_2016wave4_basicincome_vote as 'Vote', \
                                poll_info.question_bbi_2016wave4_basicincome_argumentsfor as 'For', \
                                poll_info.question_bbi_2016wave4_basicincome_argumentsagainst as 'Against', \
                                country_info.country_code as 'Country' \
                                FROM poll_info\
                                JOIN country_info on poll_info.uuid = country_info.uuid", engine)
    data['n_args_for'] = data['For'].apply(lambda x: len(x.split("|")))
    data['n_args_against'] = data['Against'].apply(lambda x: len(x.split("|")))
    data = get_country_name(data)
    return data


def get_skills(country=None):
    print('Getting Skillss...')
    cfg = configparser.RawConfigParser()
    cfg.read('config.ini')
    sqlitedb_path = cfg['data']['db']
    engine = create_engine(f'sqlite:///{sqlitedb_path}')
    df_sql = pd.read_sql_query("SELECT career_info.dem_education_level as 'Education Level', \
                                career_info.normalized_job_code as 'Job Code', \
                                country_info.country_code as 'Country'\
                                FROM career_info \
                                JOIN country_info on career_info.uuid = country_info.uuid", engine)
    data = get_country_name(df_sql)
    df = mwr.clean_skills(data,country)
    return df
