import argparse
from p_acquisition import m_acquisition as mac
from p_analysis import m_analysis as man
from p_reporting import m_reporting as mre


def argument_parser():
    parser = argparse.ArgumentParser(description='Set chart type')
    parser.add_argument("-c", "--country", type=str, help="Country filter. Please, include country name capitalized. ")
    args = parser.parse_args()
    return args


def main(args):
    print('==== Starting Pipeline ====')
    ## Challenge 1
    # getting data
    data_raw = mac.get_data_from_sql()
    data_no_job = mac.get_country_name(data_raw)
    data = mac.get_normalized_job_title(data_no_job)
    # analizing data
    final_df = man.analyze(data, args.country)
    # saving csv
    locationcsv = [mre.save_csv(final_df, args.country)]


    ##Bonus 1 - poll info
    #getting data
    data_poll = mac.get_poll_info()
    # analizing data
    data_b1 = man.get_poll_resume(data_poll, args.country)
    # saving csv
    locationcsv.append(mre.save_csv(data_b1, f'Poll{args.country}'))

    ##Bonus 2 -
    # getting data
    data_skills = mac.get_skills(args.country)
    # analizing data
    data_skills_by_education = man.get_skills_by_education(data_skills)
    # saving csv
    locationcsv.append(mre.save_csv(data_skills_by_education, f'Skills{args.country}'))

    # sending email with attached reports
    mre.send_email(locationcsv)
    #uploading to website
    mre.upload_to_website(locationcsv)

    print(
        '==== Pipeline is complete. You may find the results in the folder ./data/results ====')


if __name__ == '__main__':
    arguments = argument_parser()
    main(arguments)
