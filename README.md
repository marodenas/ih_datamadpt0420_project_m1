# IRONHACK 
## Data Analysis Bootcamp - Project I - Data Pipeline  
  
![Image](https://images.unsplash.com/photo-1543674892-7d64d45df18b?ixlib=rb-1.2.1&auto=format&fit=crop&w=1920&h=500&q=80)  
## Table of Contents  

* [About the Project](#about-the-project)  
  * [Challenge 1](#pushpin-challenge-1)  
  * [Challenge 3](#pushpin-challenge-2)  
  * [Challenge 2](#pushpin-challenge-3)      
  * [Built With](#hammer-built-with)  
* [How to use the pipeline](#how-to-use-the-pipeline)  
  * [Prerequisites](#page_with_curl-prerequisites)  
  * [Inputs](#computer-inputs)  
  * [Folder Structure](#file_folder-folder-structure)  
 * [Procesing Stages](#procesing-stages)
	  * [Acquistion](#electric_plug-acquisition)  
	  * [Wrangling](#wrench-wrangling)  
	  * [Analysis](#rocket-analysis)  
	  * [Reporting](#mailbox-reporting)  
* [Next Stages](#next-stages) 
  
## About the project  
  
The aim of this repository is to show the adquire skills throught Module 1 of Data Analytics in IronHack's Bootcamp [PT2020]  
  
We construct a Data Pipeline where we respond to certain challenge, showcasing the programming skills and tools that have been learned.  

If you want to see more about the project, you can visit https://www.marodenas.es/ironhackm1
  
###  :pushpin: Challenge 1  
  
The objetive of this challenge is to analyzed how gender is reprensented in data jobs per country. We have analyzed the percentage of male and female by country and job, in order to know more about the percentage which represent each job.  

At the end we will obtain a table like this:   
  
| Country | Job Title      | Gender     | Quantity | Percentage |  
|---------|----------------|------------|----------|------------|  
| Spain   | Data Scientist | Male       | 25       | 5%         |  
| Spain   | Data Scientist | Female     | 25       | 5%         |  
| ...     | ...            | ...        | ...      | ...        |  
** Percentages are in proportion to each gender in each job category for each country  
  
###  :pushpin: Challenge 2  
  
For Challenge 2, we have analyzed the intention of vote based on a poll where people show their intention of vote in a scale of 5 points from against to for. The data have been grouped by country and by intention of vote, where positive intention were grouped and negative intention were grouped too.  

At the end we will obtain a table like this:   
  
| Country | Vote      | Number of Pro Arguments  | Number of Pro Arguments |  
|---------|-----------|--------------------------|-------------------------|  
| Italy   | Against   |                          | 25                      |  
| Italy   | In favor  |                          | 25                      |  
  
  
###  :pushpin: Challenge 3  
  
For Challenge 3, we have analyzed the top ten skills per a given education scale by country.   

At the end we will obtain a table like this:   
  
| Country | Education Level | Skill 1  | Skill 2 | ... |  
|---------|-----------------|----------|---------|-----|  
| France  | high            | computers and electronics | ... | ... |  
| France  | medium          | deductive reasoning | ... | ... |  
| France  | low             | english language | ... | ... |  
| France  | no              |      critical thinking | ... | ... |  
  ###  :hammer: Built With   
The core of the project is Python 3.7.3, but you have to install those libraries for run the script.   
Native packages:  
- [Argparse](https://docs.python.org/3.7/library/argparse.html)  
- [Configparser](https://docs.python.org/3/library/configparser.html)  
- [Datetime](https://docs.python.org/2/library/datetime.html)  
- [Re](https://docs.python.org/3/library/re.html)  
- [Smtplib](https://docs.python.org/3/library/smtplib.html)  
- [Email](https://docs.python.org/3/library/email.examples.html)  
  
Furthermore, it is has to be installed the following libraries:  
- [SQL Alchemy (v.1.3.17)](https://docs.sqlalchemy.org/en/13/intro.html)  
- [Pandas (v.0.24.2)](https://pandas.pydata.org/pandas-docs/stable/reference/index.html)  
- [Numpy (v.1.18.1)](https://numpy.org/doc/stable/)  
- [Requests (v.2.23.0)](https://requests.readthedocs.io/)  
- [Beautiful Soup (v.4.9.1)](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)  
- [Pysftp (0.2.9) ](https://pypi.org/project/pysftp/)  

  
## **How to use the pipeline**
###  **:page_with_curl:Prerequisites**  
Please, install all the libraries mentinoned in [Built With](#built-with) in your enviroment in order to run the script.  
   
Furthemore, there is a config.ini file where you have to specify all parameters that you need to run the script. Please, fill out all the variables in order to run the script. You will need the database, api url, and webscraping url.   
  
In order to send an email and upload the outcome csv, you will need to provide a gmail email, reciever, pass.
For uploading the html version of the results, you will need to provide the sftp user and password of your hosting. 

Don't worry about privacity, this config file will not be uploaded to github.  

Example of config.ini file: 

```  
[email]  
user = your user email  
password = your password email  
receiver = people who will recieve the email  
  
[data]  
db = database path  
url = url for scrapping country codes  
  
[website]  
myHostname = xxxxxxx  
myUsername = xxxxxxx  
myPassword = xxxxxxx ```  
```
  
Pipeline is launched through main_script.py giving as paramenters. If you leave it blank, all European's contries will be retrieved:  
- `-c / --country` - an European country.  
  
Example:  
`python main_script.py -c Spain`  
  
  
### **:computer: Inputs**  

It is mandatory to connect those sources with the pipeline in order to get the expected results. 

- [Data base](/data/raw/raw_data_project_m1.db ) SQLAlchemy.  
- Data base procesed with Pandas  
- Job titles  [API](http://dataatwork.org/data/) with request.  
- Country codes [EuroStat](https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes) with request and beautifulsoup  
  
  
  
### :file_folder: **Folder structure**  
```
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
  

## **Processing stages**  
  
### **:electric_plug: Acquisition**  
  
- Functions that get all the info from the sources mentioned before. 
  
### **:wrench: Wrangling**  
- Functions that clean the dataframes in order to have better Dataframes for analyzing them
 ### **:rocket: Analysis**  

- Function that merge the data in order to answer each challenge.
  
 ### **:mailbox: Reporting**  
With the previous analysis we will provided with the next reports: 
- CSV of each report that will be find in data/results folder  
- An email with the csv attached. - The table will be able to consult on the website provided.  
- Html tables. You could see
  
 ---  
### ** Next stages**  
- Multiprocessing connection. 
- Object Oriented Programing data pipeline.
