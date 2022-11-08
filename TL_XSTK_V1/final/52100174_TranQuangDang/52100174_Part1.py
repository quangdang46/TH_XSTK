from statistics import *
from math import *


# 1.mean()
# Dữ liệu đầu vào đúng định dạng
data_1 = [1, 2, 3, 4, 5]
data_2 =[-1,-2,3,4,5]
data_3={1:"a", 2:"b", 3:"c", 4:"d", 5:"e"}

print("Mean of data_1: ", mean(data_1))
print("Mean of data_2: ", mean(data_2))
print("Mean of data_3: ", mean(data_3))

# Đầu ra:
'''
Mean of data_1:  3
Mean of data_2:  1.8
Mean of data_3:  3
'''
# Dữ liệu không đúng định dạng
# data_1 = []
# data_2={"a":1,"b":2,"c":3,"d":4,"e":5}
# print("Mean of empty parameter",mean(data_1))
# print("Mean of data_1 is", mean(data_1))
# print("Mean of data_2 is", mean(data_2))

# Đầu ra

# '''
# Traceback (most recent call last):
#   File "c:\Users\Admin\Desktop\TL_GK\52100174_Part1.py", line 5, in <module>
#     print("Mean of empty parameter",mean(data_1))
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2288.0_x64__qbz5n2kfra8p0\lib\statistics.py", line 328, in mean
#     raise StatisticsError('mean requires at least one data point')
# statistics.StatisticsError: mean requires at least one data point
# '''

# 2.fmean()
# Dữ liệu đầu vào đúng định dạng
data_1 = [1, 2, 3, 4, 5]
data_2 =[-1,-2,3,4,5]
data_3={1:"a", 2:"b", 3:"c", 4:"d", 5:"e"}

print("Mean of data_1: ", fmean(data_1))
print("Mean of data_2: ", fmean(data_2))
print("Mean of data_3: ", fmean(data_3))

# Đầu ra:
'''
Mean of data_1:  3.0
Mean of data_2:  1.8
Mean of data_3:  3.0
'''

# # Dữ liệu không đúng định dạng
# data_1 = []
# data_2={"a":1,"b":2,"c":3,"d":4,"e":5}
# print("Mean of data_1 is", fmean(data_1))
# print("Mean of data_2 is", fmean(data_2))

# # Đầu ra
# '''
# Traceback (most recent call last):
#   File "c:\Users\Admin\Desktop\TL_GK\52100174_Part1.py", line 59, in <module>
#     print("Mean of data_1 is", fmean(data_1))
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2288.0_x64__qbz5n2kfra8p0\lib\statistics.py", line 358, in fmean
#     raise StatisticsError('fmean requires at least one data point') from None
# statistics.StatisticsError: fmean requires at least one data point
# '''


# 3.geometric_mean()
# Dữ liệu đầu vào đúng định dạng
data_1 = [1, 2, 3, 4, 5,8,9]
data_2={1:"a", 2:"b", 3:"c", 4:"d", 5:"e"}

print("Mean of data_1: ", geometric_mean(data_1))
print("Mean of data_2: ", geometric_mean(data_2))
# Đầu ra:
'''
Mean of data_1:  3.650556765820694 
Mean of data_2:  2.6051710846973517
'''

# Dữ liệu không đúng định dạng
# data_1 = []
# print("Mean of data_1 is", geometric_mean(data_1))

# # Đầu ra
# '''
# Traceback (most recent call last):
#   File "c:\Users\Admin\Desktop\TL_GK\52100174_Part1.py", line 88, in <module>
#     print("Mean of data_1 is", geometric_mean(data_1))
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2288.0_x64__qbz5n2kfra8p0\lib\statistics.py", line 376, in geometric_mean
#     raise StatisticsError('geometric mean requires a non-empty dataset '
# statistics.StatisticsError: geometric mean requires a non-empty dataset containing positive numbers
# '''

# data_2={"a":1,"b":2,"c":3,"d":4,"e":5}
# data_3=[-1,-2,3,4,5]
# data_4=[0,1,2,3,4,5]
# print("Mean of data_2 is", geometric_mean(data_2))
# print("Mean of data_3 is", geometric_mean(data_3))
# print("Mean of data_4 is", geometric_mean(data_4))

# # Đầu ra
# '''
# Traceback (most recent call last):
#   File "c:\Users\Admin\Desktop\TL_GK\52100174_Part1.py", line 88, in <module>
#     print("Mean of data_1 is", geometric_mean(data_1))
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2288.0_x64__qbz5n2kfra8p0\lib\statistics.py", line 376, in geometric_mean
#     raise StatisticsError('geometric mean requires a non-empty dataset '
# statistics.StatisticsError: geometric mean requires a non-empty dataset containing positive numbers
# PS C:\Users\Admin\Desktop\TL_GK> python -u "c:\Users\Admin\Desktop\TL_GK\52100174_Part1.py"
# Traceback (most recent call last):
#   File "c:\Users\Admin\Desktop\TL_GK\52100174_Part1.py", line 88, in <module>
#     print("Mean of data_1 is", geometric_mean(data_1))
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2288.0_x64__qbz5n2kfra8p0\lib\statistics.py", line 376, in geometric_mean
#     raise StatisticsError('geometric mean requires a non-empty dataset '
# statistics.StatisticsError: geometric mean requires a non-empty dataset containing positive numbers
# PS C:\Users\Admin\Desktop\TL_GK> python -u "c:\Users\Admin\Desktop\TL_GK\52100174_Part1.py"
# Traceback (most recent call last):
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2288.0_x64__qbz5n2kfra8p0\lib\statistics.py", line 344, in fmean
#     n = len(data)
# TypeError: object of type 'map' has no len()

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "c:\Users\Admin\Desktop\TL_GK\52100174_Part1.py", line 103, in <module>
#     print("Mean of data_2 is", geometric_mean(data_2))
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2288.0_x64__qbz5n2kfra8p0\lib\statistics.py", line 374, in geometric_mean
#     return exp(fmean(map(log, data)))
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2288.0_x64__qbz5n2kfra8p0\lib\statistics.py", line 352, in fmean
#     total = fsum(count(data))
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2288.0_x64__qbz5n2kfra8p0\lib\statistics.py", line 350, in count
#     for n, x in enumerate(iterable, start=1):
# TypeError: must be real number, not str
# '''

# 4.harmonic_mean()
# Dữ liệu đầu vào đúng định dạng
data_1 = [1, 2, 3, 4, 5,8,9]
data_2={1:"a", 2:"b", 3:"c", 4:"d", 5:"e"}
data_3=[20,40]
weight_3=[30,70]
print("Mean of data_1: ", harmonic_mean(data_1))
print("Mean of data_2: ", harmonic_mean(data_2))
print("Mean of data_3: ", harmonic_mean(data_3,weight_3))

# Đầu ra:
'''
Mean of data_1:  2.7783902976846746
Mean of data_2:  2.18978102189781  
Mean of data_3:  30.76923076923077 
'''

# Dữ liệu không đúng định dạng
# data_1 = []
# print("Mean of data_1 is", harmonic_mean(data_1))
# # Đầu ra
# '''
# Traceback (most recent call last):
#   File "c:\Users\Admin\Desktop\TL_GK\52100174_Part1.py", line 161, in <module>
#     print("Mean of data_1 is", harmonic_mean(data_1))
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2288.0_x64__qbz5n2kfra8p0\lib\statistics.py", line 408, in harmonic_mean
#     raise StatisticsError('harmonic_mean requires at least one data point')
# statistics.StatisticsError: harmonic_mean requires at least one data point
# '''

# data_2={"a":1,"b":2,"c":3,"d":4,"e":5}
# data_3=[-1,-2,3,4,5]
# data_4=[0,1,2,3,4,5]
# print("Mean of data_2 is", harmonic_mean(data_2))
# print("Mean of data_3 is", harmonic_mean(data_3))
# print("Mean of data_4 is", harmonic_mean(data_4))

# # Đầu ra
# '''
# Traceback (most recent call last):
#   File "c:\Users\Admin\Desktop\TL_GK\52100174_Part1.py", line 175, in <module>
#     print("Mean of data_2 is", harmonic_mean(data_2))
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2288.0_x64__qbz5n2kfra8p0\lib\statistics.py", line 428, in harmonic_mean
#     T, total, count = _sum(w / x if w else 0 for w, x in zip(weights, data))
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2288.0_x64__qbz5n2kfra8p0\lib\statistics.py", line 186, in _sum
#     for typ, values in groupby(data, type):
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2288.0_x64__qbz5n2kfra8p0\lib\statistics.py", line 428, in <genexpr>
#     T, total, count = _sum(w / x if w else 0 for w, x in zip(weights, data))
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2288.0_x64__qbz5n2kfra8p0\lib\statistics.py", line 301, in _fail_neg
#     if x < 0:
# TypeError: '<' not supported between instances of 'str' and 'int'
# '''


# 5.median()
# Dữ liệu đầu vào đúng định dạng
data_1 = [1, 2, 3, 4, 5,8,9]
data_2={1:"a", 2:"b", 3:"c", 4:"d", 5:"e"}
data_3=[20,40]

print("Median of data_1: ", median(data_1))
print("Median of data_2: ", median(data_2))
print("Median of data_3: ", median(data_3))

# Đầu ra:
'''
Median of data_1:  4   
Median of data_2:  3   
Median of data_3:  30.0
'''


# # Dữ liệu không đúng định dạng
# data_1 = []
# print("Median of data_1 is", median(data_1))
# # Đâù ra
# '''
# Traceback (most recent call last):
#   File "c:\Users\Admin\Desktop\TL_GK\52100174_Part1.py", line 217, in <module>
#     print("Median of data_1 is", median(data_1))
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2288.0_x64__qbz5n2kfra8p0\lib\statistics.py", line 452, in median
#     raise StatisticsError("no median for empty data")
# statistics.StatisticsError: no median for empty data
# PS C:\Users\Admin\Desktop\TL_GK> python -u "c:\Users\Admin\Desktop\TL_GK\52100174_Part1.py"
# Traceback (most recent call last):
#   File "c:\Users\Admin\Desktop\TL_GK\52100174_Part1.py", line 217, in <module>
#     print("Median of data_1 is", median(data_1))
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2288.0_x64__qbz5n2kfra8p0\lib\statistics.py", line 452, in median
#     raise StatisticsError("no median for empty data")
# statistics.StatisticsError: no median for empty data
# '''


# 6.median_low()
# Dữ liệu đầu vào đúng định dạng
data_1 = [1, 2, 3, 4, 5,8,9]
data_2=[-2,-1,0,1,2,3,4,5]
print("Median_low of data_1: ", median_low(data_1))
print("Median_low of data_2: ", median_low(data_2))

# Đầu ra:
'''
Median_low of data_1:  4
Median_low of data_2:  1
'''

# # Dữ liệu không đúng định dạng
# data_1 = []
# print("Median_low of data_1 is", median_low(data_1))
# # Đầu ra
# '''
# Traceback (most recent call last):
#   File "c:\Users\Admin\Desktop\TL_GK\52100174_Part1.py", line 250, in <module>
#     print("Median_low of data_1 is", median_low(data_1))
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2288.0_x64__qbz5n2kfra8p0\lib\statistics.py", line 475, in median_low
#     raise StatisticsError("no median for empty data")
# statistics.StatisticsError: no median for empty data
# '''


# 7.median_high()
# Dữ liệu đầu vào đúng định dạng
data_1 = [1, 2, 3, 4, 5,8,9]
data_2=[-2,-1,0,1,2,3,4,5]
print("Median_high of data_1: ", median_high(data_1))
print("Median_high of data_2: ", median_high(data_2))

# Đầu ra
'''
Median_high of data_1:  4
Median_high of data_2:  2
'''

# # Dữ liệu không đúng định dạng
# data_1 = []
# print("Median_high of data_1 is", median_high(data_1))
# # Đầu ra
# '''
# Traceback (most recent call last):
#   File "c:\Users\Admin\Desktop\TL_GK\52100174_Part1.py", line 277, in <module>
#     print("Median_high of data_1 is", median_high(data_1))
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2288.0_x64__qbz5n2kfra8p0\lib\statistics.py", line 497, in median_high
#     raise StatisticsError("no median for empty data")
# statistics.StatisticsError: no median for empty data
# '''


# 8.median_grouped()
# Dữ liệu đầu vào đúng định dạng
data_1 = [1, 2, 3, 4, 5,8,9]
data_2=[-2,-1,0,1,2,3,4,5]
intervel_2=2
print("Median_grouped of data_1: ", median_grouped(data_1))
print("Median_grouped of data_2: ", median_grouped(data_2,intervel_2))
# Đầu ra
'''
Median_grouped of data_1:  4.0
Median_grouped of data_2:  1.0
'''

# # Dữ liệu không đúng định dạng
# data_1 = []
# print("Median_grouped of data_1 is", median_grouped(data_1))
# # Đầu ra
# '''
# Traceback (most recent call last):
#   File "c:\Users\Admin\Desktop\TL_GK\52100174_Part1.py", line 304, in <module>
#     print("Median_grouped of data_1 is", median_grouped(data_1))
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2288.0_x64__qbz5n2kfra8p0\lib\statistics.py", line 530, in median_grouped
#     raise StatisticsError("no median for empty data")
# statistics.StatisticsError: no median for empty data
# '''

# 9.mode()
# Dữ liệu đầu vào đúng định dạng
data_1 = [1, 1,2,4,5,4,2,3,-4,1]
data_2=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
print("Mode of data_1: ", mode(data_1))
print("Mode of data_2: ", mode(data_2))
# Đầu ra
'''
Mode of data_1:  1
Mode of data_2:  a
'''

# # Dữ liệu không đúng định dạng
# data_1 = []
# print("Mode of data_1 is", mode(data_1))
# # Đầu ra
# '''
# Traceback (most recent call last):
#   File "c:\Users\Admin\Desktop\TL_GK\52100174_Part1.py", line 329, in <module>
#     print("Mode of data_1 is", mode(data_1))
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2288.0_x64__qbz5n2kfra8p0\lib\statistics.py", line 583, in mode
#     raise StatisticsError('no mode for empty data') from None
# statistics.StatisticsError: no mode for empty data
# '''


# 10.multimode()
data_1 = [1, 1,2,4,5,4,2,3,-4,1]
data_2=["a","b","c","a","b"]
data_3=[]
print("Multimode of data_1: ", multimode(data_1))
print("Multimode of data_2: ", multimode(data_2))
print("Multimode of data_3: ", multimode(data_3))
# Đầu ra
'''
Multimode of data_1:  [1]        
Multimode of data_2:  ['a', 'b'] 
Multimode of data_3:  []
'''

# 11.quantiles()
# Dữ liệu đầu vào đúng định dạng
data_1 = [1, 2, 3, 4, 5,8,9]
data_2=[-2,-1,0,1,2,3,4,5]

print("Quantiles of data_1: ", quantiles(data_1))
print("Quantiles of data_2: ", quantiles(data_2, n=5, method='inclusive'))
# Đầu ra
'''
Quantiles of data_1:  [2.0, 4.0, 8.0]      
Quantiles of data_2:  [-0.6, 0.8, 2.2, 3.6]
'''

# # Dữ liệu không đúng định dạng
# data_1 = []
# print("Quantiles of data_1 is", quantiles(data_1))
# # Đầu ra
# '''
# Traceback (most recent call last):
#   File "c:\Users\Admin\Desktop\TL_GK\52100174_Part1.py", line 370, in <module>
#     print("Quantiles of data_1 is", quantiles(data_1))
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2288.0_x64__qbz5n2kfra8p0\lib\statistics.py", line 662, in quantiles
#     raise StatisticsError('must have at least two data points')
# statistics.StatisticsError: must have at least two data points
# '''

# 12.pstdev()
# Dữ liệu đầu vào đúng định dạng
data_1 = [1, 2, 3, 4, 5,8,9]
data_2=[-2,-1,0,1,2,3,4,5]
mu_2=2
print("pstdev of data_1: ", pstdev(data_1))
print("pstdev of data_2: ", pstdev(data_2, mu_2))
# Đầu ra
'''
pstdev of data_1:  2.770102775666474
pstdev of data_2:  2.345207879911715
'''

# # Dữ liệu không đúng định dạng
# data_1 = []
# print("pstdev of data_1 is", pstdev(data_1))
# # Đầu ra
# '''
# Traceback (most recent call last):
#   File "c:\Users\Admin\Desktop\TL_GK\52100174_Part1.py", line 396, in <module>
#     print("pstdev of data_1 is", pstdev(data_1))
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2288.0_x64__qbz5n2kfra8p0\lib\statistics.py", line 847, in pstdev
#     var = pvariance(data, mu)
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2288.0_x64__qbz5n2kfra8p0\lib\statistics.py", line 811, in pvariance
#     raise StatisticsError('pvariance requires at least one data point')
# statistics.StatisticsError: pvariance requires at least one data point
# '''

# 13.pvariance()
# Dữ liệu đầu vào đúng định dạng
data_1 = [1, 2, 3, 4, 5,8,9]
data_2=[-2,-1,0,1,2,3,4,5]
mu_2=3
print("pvariance of data_1: ", pvariance(data_1))
print("pvariance of data_2: ", pvariance(data_2, mu_2))
# Đầu ra
'''
pvariance of data_1:  7.673469387755102
pvariance of data_2:  7.5
'''

# # Dữ liệu không đúng định dạng
# data_1 = []
# print("pvariance of data_1 is", pvariance(data_1))
# # Đầu ra
# '''
# Traceback (most recent call last):
#   File "c:\Users\Admin\Desktop\TL_GK\52100174_Part1.py", line 424, in <module>
#     print("pvariance of data_1 is", pvariance(data_1))
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2288.0_x64__qbz5n2kfra8p0\lib\statistics.py", line 811, in pvariance
#     raise StatisticsError('pvariance requires at least one data point')
# statistics.StatisticsError: pvariance requires at least one data point
# '''


# 14.variance()
# Dữ liệu đầu vào đúng định dạng
data_1 = [1, 2, 3, 4, 5,8,9]
data_2=[-2,-1,0,1,2,3,4,5]
mu_2=3
print("variance of data_1: ", variance(data_1))
print("variance of data_2: ", variance(data_2, mu_2))
# Đầu ra
'''
variance of data_1:  8.952380952380953
variance of data_2:  8.571428571428571
'''

# # Dữ liệu không đúng định dạng
# data_1 = []
# print("variance of data_1 is", variance(data_1))
# # Đầu ra
# '''
# Traceback (most recent call last):
#   File "c:\Users\Admin\Desktop\TL_GK\52100174_Part1.py", line 451, in <module>
#     print("variance of data_1 is", variance(data_1))
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2288.0_x64__qbz5n2kfra8p0\lib\statistics.py", line 767, in variance
#     raise StatisticsError('variance requires at least two data points')
# statistics.StatisticsError: variance requires at least two data points
# '''

# 15.stdev()
# Dữ liệu đầu vào đúng định dạng
data_1 = [1, 2, 3, 4, 5,8,9]
data_2=[-2,-1,0,1,2,3,4,5]
mu_2=2
print("stdev of data_1: ", stdev(data_1))
print("stdev of data_2: ", stdev(data_2, mu_2))
# Đầu ra
'''
stdev of data_1:  2.9920529661723827
stdev of data_2:  2.5071326821120348
'''


# 16.covariance()
# Dữ liệu đầu vào đúng định dạng
data_1 = [1, 2, 3, 4, 5,8,9,2]
data_2=[-2,-1,0,1,2,3,4,5]
print("covariance of data_1: ", covariance(data_1,data_2))
# Đầu ra
'''
covariance of data_1:  4.142857142857143
'''

# # Dữ liệu không đúng định dạng
# data_1 = [1]
# data_2=[-2,-1,0,1,2,3,4,5]
# print("covariance of data_1 is", covariance(data_1,data_2))
# # Đầu ra
# '''
# Traceback (most recent call last):
#   File "c:\Users\Admin\Desktop\TL_GK\52100174_Part1.py", line 489, in <module>
#     print("covariance of data_1 is", covariance(data_1,data_2))
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2288.0_x64__qbz5n2kfra8p0\lib\statistics.py", line 880, in covariance
#     raise StatisticsError('covariance requires that both inputs have same number of data points')
# statistics.StatisticsError: covariance requires that both inputs have same number of data points
# '''


# 17.correlation()
# Dữ liệu đầu vào đúng định dạng
data_1 = [1, 2, 3, 4, 5,8,9,2]
data_2=[-2,-1,0,1,2,3,4,5]
print("correlation of data_1: ", correlation(data_1,data_2))
# Đầu ra
'''
correlation of data_1:  0.580116034811604
'''

# # Dữ liệu không đúng định dạng
# data_1 = [1]
# data_2=[-2,-1,0,1,2,3,4,5]
# print("correlation of data_1 is", correlation(data_1,data_2))
# # Đầu ra
# '''
# Traceback (most recent call last):
#   File "c:\Users\Admin\Desktop\TL_GK\52100174_Part1.py", line 514, in <module>
#     print("correlation of data_1 is", correlation(data_1,data_2))
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2288.0_x64__qbz5n2kfra8p0\lib\statistics.py", line 908, in correlation
#     raise StatisticsError('correlation requires that both inputs have same number of data points')
# statistics.StatisticsError: correlation requires that both inputs have same number of data points
# '''

# 18.linear_regression()
# Dữ liệu đầu vào đúng định dạng
data_1 = [1, 2, 3, 4, 5,8,9,2]
data_2=[-2,-1,0,1,2,3,4,5]
print("linear_regression of data_1: ", linear_regression(data_1,data_2))
# Đầu ra
'''
linear_regression of data_1:  LinearRegression(slope=0.48739495798319327, intercept=-0.5714285714285712)
'''