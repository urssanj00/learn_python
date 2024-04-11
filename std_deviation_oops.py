import numpy as np
import math as mt

class StasLibs:

    def __init__(self, dataset):
        self.dataset_n = np.array(dataset)  # numpy dataset


    def mean(self):
        mean = self.dataset_n.sum()/len(self.dataset_n)
        return mean

    def variance_interim(self):
        mean_val = self.mean()
        # Calculate the difference between each element in dataset and mean_val
        diff = self.dataset_n - mean_val
        diff_sqr = diff**2
        diff_sqr_sum = diff_sqr.sum()
        print('diff_sqr_sum', diff_sqr_sum)
        return diff_sqr_sum

    def variance_sample(self):
        variance_interim_val = self.variance_interim()
        variance_sample_val = variance_interim_val / (len(self.dataset_n)-1)
        return variance_sample_val

    def variance_population(self):
        variance_interim_val = self.variance_interim()
        variance_population_val = variance_interim_val / (len(self.dataset_n))
        return variance_population_val

    def std_deviation_sample(self):
        variance_val = self.variance_sample()
        return mt.sqrt(variance_val)

    def std_deviation_population(self):
        variance_val = self.variance_population()
        return mt.sqrt(variance_val)
    
data = [10, 9, 8, 7, 9.5, 9, 4]


stas_libs_obj = StasLibs(data)

print(1)
std_dev_samp_val = stas_libs_obj.std_deviation_sample()
print(2)
print('Standard Deviation Sample:', std_dev_samp_val)
print(3)
std_dev_pop_val = stas_libs_obj.std_deviation_population()
print('Standard Deviation Population:', std_dev_pop_val)

print ('4. numpy std dev : ', np.std(data))
print (np.mean(data), stas_libs_obj.mean())
print (np.var(data), stas_libs_obj.variance_population())