from statistics import *

# mean()
data1 =[1,2,3,4,5,6,7,8,9,10]
data2=[-5,5,10,15,20,25,30]
print("Mean data1:",mean(data1))
print("Mean data2:",mean(data2))

# fmean()
data1 =[1,2,3,4,5,6,7,8,9,10]
data2=[-5,5,10,15,20,25,30]
print("Fmean data1:",fmean(data1))
print("Fmean data2:",fmean(data2))

# geometric_mean()
data1 =[1,2,3,4,5,6,7,8,9,10]
data2=[5,5,10,15,20,25,30]
print("Geometric mean data1:",geometric_mean(data1))
print("Geometric mean data2:",geometric_mean(data2))

# harmonic_mean()
data1 =[1,2,3,4,5,6,7,8,9,10]
data2=[5,5,10,15,20,25,30]
print("Harmonic mean data1:",harmonic_mean(data1))
print("Harmonic mean data2:",harmonic_mean(data2))

# median()
data1 =[1,2,3,4,5,6,7,8,9,10]
data2=[5,5,10,15,20,25,30]
print("Median data1:",median(data1))
print("Median data2:",median(data2))

# median_low()
data1 =[1,2,3,4,5,6,7,8,9,10]
data2=[5,5,10,15,20,25,30]
print("Median low data1:",median_low(data1))
print("Median low data2:",median_low(data2))

# median_high()
data1 =[1,2,3,4,5,6,7,8,9,10]
data2=[5,5,10,15,20,25,30]
print("Median high data1:",median_high(data1))
print("Median high data2:",median_high(data2))

# median_grouped()
data1 =[1,2,3,4,5,6,7,8,9,10]
data2=[5,5,10,15,20,25,30]
print("Median grouped data1:",median_grouped(data1))
print("Median grouped data2:",median_grouped(data2))

# mode()
data1 =[1,2,3,4,5,6,7,8,9,10]
data2=[5,5,10,15,20,25,30]
print("Mode data1:",mode(data1))
print("Mode data2:",mode(data2))

# multimode()
data1 =[1,2,3,4,5,6,7,8,9,10]
data2=[5,5,10,15,20,25,30]
print("Multimode data1:",multimode(data1))
print("Multimode data2:",multimode(data2))

# quantiles()
data1 =[1,2,3,4,5,6,7,8,9,10]
data2=[5,5,10,15,20,25,30]
print("Quantiles data1:",quantiles(data1))
print("Quantiles data2:",quantiles(data2,n=3))

# pstdev()
data1 =[1,2,3,4,5,6,7,8,9,10]
data2=[5,5,10,15,20,25,30]
print("Pstdev data1:",pstdev(data1))
print("Pstdev data2:",pstdev(data2))

# pvariance()
data1 =[1,2,3,4,5,6,7,8,9,10]
data2=[5,5,10,15,20,25,30]
print("Pvariance data1:",pvariance(data1))
print("Pvariance data2:",pvariance(data2))

# stdev()
data1 =[1,2,3,4,5,6,7,8,9,10]
data2=[5,5,10,15,20,25,30]
print("Stdev data1:",stdev(data1))
print("Stdev data2:",stdev(data2))

# variance()
data1 =[1,2,3,4,5,6,7,8,9,10]
data2=[5,5,10,15,20,25,30]
print("Variance data1:",variance(data1))
print("Variance data2:",variance(data2))

# covariance()
data1 =[1,2,3,4,5,6,7]
data2=[5,5,10,15,20,25,30]
print("Covariance data1:",covariance(data1,data2))

# correlation()
data1 =[1,2,3,4,5,6,7]
data2=[5,5,10,15,20,25,30]
print("Correlation data1:",correlation(data1,data2))

# linear_regression()
data1 =[1,2,3,4,5,6,7]
data2=[5,5,10,15,20,25,30]
print(linear_regression(data1,data2))


