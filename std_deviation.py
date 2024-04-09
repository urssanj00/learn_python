

import numpy as np


def mean(dataset_n):
    sc_data = dataset_n
    mean = sc_data.sum()/len(sc_data)
    return mean


def std_deviation_interim(dataset_n):
    mean_val = mean(dataset_n)
    # Calculate the difference between each element in dataset and mean_val
    diff = dataset_n - mean_val
    diff_sqr = diff**2
    diff_sqr_sum = diff_sqr.sum()
    print('diff_sqr_sum', diff_sqr_sum)
    return diff_sqr_sum


def std_deviation_sample(dataset):
    dataset_n = np.array(dataset)  # numpy dataset
    std_dev_interim_val = std_deviation_interim(dataset_n)
    std_dev_sample_val = std_dev_interim_val / (len(dataset_n)-1)
    return std_dev_sample_val


def std_deviation_population(dataset):
    dataset_n = np.array(dataset)  # numpy dataset
    std_dev_interim_val = std_deviation_interim(dataset_n)
    std_dev_population_val = std_dev_interim_val / (len(dataset_n))
    return std_dev_population_val


data = [10, 9, 8, 7, 9.5, 9, 4]
sc_data = np.array(data)
print(1)
std_dev_samp_val = std_deviation_sample(data)
print(2)
print('Standard Deviation Sample:', std_dev_samp_val)
print(3)
std_dev_pop_val = std_deviation_population(data)
print('Standard Deviation Population:', std_dev_pop_val)
