from statistics import mean, median


def get_age_stat(data, age, stat):
    age_list = []

    stat_result = None
    for row in data:
        if row['Age'] == age:
            age_list.append(row['Age'])
    if stat.lower() == 'mean':
        stat_result = mean(stat_result)
    if stat.lower() == 'median':
        stat_result = median(stat_result)
    
    return {'age':age,
            stat:stat_result}
