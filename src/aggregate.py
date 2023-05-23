from statistics import mean, median


def get_age_stat(data, lastname, stat):
    age_list = []

    stat_result = None
    for row in data:
        if row['LastName'] == lastname:
            age_list.append(row['Age'])
    if stat.lower() == 'mean':
        stat_result = mean(stat_result)
    if stat.lower() == 'median':
        stat_result = median(stat_result)
    
    return {'LastName':lastname,
            stat:stat_result}
