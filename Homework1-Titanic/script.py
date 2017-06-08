import math
import pandas
import numpy as np


def print_to_file(filename, data):
    file = open(filename, 'w')
    res = ''
    for x in data:
        if len(res) != 0:
            res = res + ' '
        res += str(x)
    file.write(res)
    file.close()

def print_to_file_without_spaces(filename, data):
    file = open(filename, 'w')
    res = ''
    for x in data:
        res += str(x)
    file.write(res)
    file.close()

data = pandas.read_csv('Data/titanic.csv', index_col='PassengerId')

# Calculating the number of male and female passengers
sex_data = data['Sex']
male = sum(1 if x == 'male' else 0 for x in sex_data)
female = sum(1 if x == 'female' else 0 for x in sex_data)
print_to_file('1', [male, female])

# Calculating the percent of survived passengers
survived_data = data['Survived']
survived = sum(survived_data)
overall_amount = len(data)
result = round(100 * survived / overall_amount, 2)
print_to_file('2', [result])

# Calculating the percent of first class passengers
p_class = data['Pclass']
first_class_passengers = sum(1 if x == 1 else 0 for x in p_class)
result = round(100 * first_class_passengers / overall_amount, 2)
print_to_file('3', [result])

# Calculating mean and average passengers age
age = np.array(data['Age'])
age_mean = round(np.nanmean(age), 2)
age_median = round(np.nanmedian(age), 2)
print_to_file('4', [age_mean, age_median])

# Calculating Pirson's correlation
sib_sp = data['SibSp']
parch = data['Parch']
X = np.array(sib_sp)
Y = np.array(parch)
x_mean = np.mean(X)
y_mean = np.mean(Y)

XX = X - x_mean
YY = Y - y_mean

frac_numerator = np.sum(XX * YY)

sqrt_x = sum((x - x_mean) ** 2 for x in X)
sqrt_y = sum((y - y_mean) ** 2 for y in Y)

frac_denumerator = math.sqrt(sqrt_x * sqrt_y)

pirson_correlation = round(frac_numerator / frac_denumerator, 2)
print_to_file('5', [pirson_correlation])

# The most popular female's name
names = data['Name']
female_names = []
for i in range(0, len(names)):
    if sex_data.get(i) == 'female':
        female_names.append(names.get(i))

count = {}
cur_oc = 0
popular_name = ''
for x in female_names:
    cur_name = x.split('. ')[-1]
    if count.get(cur_name) is None:
        count[cur_name] = 1
    else:
        count[cur_name] += 1
    occur = count[cur_name]
    if occur > cur_oc:
        cur_oc = occur
        popular_name = cur_name

print_to_file_without_spaces('6', popular_name)



