from statistics import mean, median


def get_age_stat(data, lastname, stat):
    age_list = []

    stat_result = None
    for row in data:
        if row['LastName'] == lastname:
            age_list.append(row['Age'])

            
    if age_list:   
        if stat.lower() == 'mean':
            stat_result = mean(age_list)
        if stat.lower() == 'median':
            stat_result = median(age_list)
        
    return {'LastName':lastname,
            stat:stat_result}
