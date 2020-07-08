# IRONHACK Data Analysis - Project I

This repository is related to the pipeline project performed at IRONHACK Data Analysis Bootcamp.


![Image](https://images.unsplash.com/photo-1527474305487-b87b222841cc?ixlib=rb-1.2.1&auto=format&fit=crop&w=1867&q=80)


## Challenge 1

The aim of the project is to analyzed how gender is reprensented in data jobs per country. For this project, we will analyze the percentage of male and female by country and job, in order to know more about the percentage which represent each job. For this challenge you will need the following libraries:

## Bonus 1

For the Bonus 1, we will analyzed the intention of vote based on a poll. For this poll, we have analyzed the intention of vote in order to know who is for or againts the question provided. 

## Bonus 2

For the Bonus 2, we have analyzed the main skills of the related job that were asked in the data poll. For those ones, we have pointed out the top 10 skills that are more relevant. 

---

## **Structure:**

###  **Configuration**
Please, install all the libraries in requirements.txt before run the script.
Furthemore, there is a config.ini file where you have to specify all parameters that you need for run the script. Please, fill out all the variables in order to run the script. You will need the database, api url, and webscraping url. 

The following python libraries are requested:

- Python
- pandas
- request
- sqlalchemy
- beautifulsoup4
- configparser
- pysftp

In order to send an email and upload the outcome csv, you will need to provide the mail, reciever, pass, sftp and sftp password. 
Don't worry about privacity, this file doesn't be uploaded to github.


### How to use the pipeline
First things first, you will need to set up the config.ini file in order to run the script. Here is an example of the variables that you have to set up: 
```
[email]
user = your user email
password = your password email
receiver = person who recieved the email

[data]
db = database path
url = url for scrapping country codes

[website]
myHostname = xxxxxxx
myUsername = xxxxxxx
myPassword = xxxxxxx 
```

Pipeline is launched through main_script.py giving as paramenters:
- `-c / --country` - an European country.

Example:
`python main_script.py -c Spain`


### **Inputs**

- Raw database containing poll data.
- API calls to retrieve job titles and skills related to proviedd ID
- Web scraping to get country names and country codes.



### :file_folder: **Folder structure**

└── ih_datamadpt0420_project_m1
    ├── __trash__
    ├── .gitignore
    ├── .env
    ├── requeriments.txt
    ├── README.md
    ├── main_script.py
    ├── config.ini
    ├── notebooks
    │   ├── notebook1.ipynb
    │   └── notebook2.ipynb
    ├── p_acquisition
    │   ├── __init__.py
    │   └── m_acquisition.py
    ├── p_analysis
    │   ├── __init__.py
    │   └── m_analysis.py
    ├── p_reporting
    │   ├── __init__.py
    │   └── m_reporting.py
    ├── p_wrangling
    │   ├── __init__.py
    │   └── m_wrangling.py
    └── data
        ├── html
        ├── raw
        └── results
```

---
### **Processing stages**

#### **Acquisition**

- [Data base](/data/raw/raw_data_project_m1.db ) SQLAlchemy.
- Data base procesed with Pandas
- Job titles  [API](http://dataatwork.org/data/) with request.
- Country codes [EuroStat](https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes) with request and beautifulsoup

#### **Wrangling**
- Functions that clean the dataframes in order to have better data to analyzed data. 
  
#### **Analysis**
 Given a country, we will provided data with 3 csv: 
- Country, gender, job and Quantity and Percentage of total.
- Vote intention(positive and negative), mean of arguments group by country
- Skills by education level

  
#### **Reporting**
With the previous analysis we will provided with the next reports: 
- CSV of each report that will be find in data/results folder
- An email with the csv attached. 
- The table will be able to consult on the website provided.

  
---
### ** Next stages**
- Improve api connection