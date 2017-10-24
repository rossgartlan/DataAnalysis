import math
from collections import Counter
from statistics	import stdev
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot
import pylab
from matplotlib.ticker import FormatStrFormatter

def mean(x):
	return sum(x)/len(x)


def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]
	
def sum_of_squares(n): return sum([x**2 for x in n])

def variance(x):
  n = len(x)
  deviations = de_mean(x)
  return sum_of_squares(deviations) / (n - 1)
  
def correlation(x, y):
    stdev_x = stdev(x)
    stdev_y = stdev(y)
    if stdev_x > 0 and stdev_y > 0:
        return	covariance(x,y)/stdev_x/stdev_y
    else:
        return 0
		
def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)

def standard_deviation(x):
  return math.sqrt(variance(x))

#dot function sums up the products of corresponding	pairs of elements
from numpy import dot

### Identified Outliers still present in the data

# 17293 mean no of hits with  to replace n/as
# 3944 mean of no of sales to replaces n/as
nodayslive =[502,189,76,518,423,234,155,543,1009,321,176,298,50,256,33,200,653,86,180,321,176,298,50,256,33,76,484,111,762,154,600,965,175,96,321,145,189,7,514,654,980,136,79,865,973,145,335,75,34,28,168,94,54,3,100000,264,433,42,354,87,522,1143,56,438,9,321,176,298,50,256,33,632,976,58,164,76,54,321,87,609,99,172,743,465,23,2,77,91,76,83,143,532,176,996,436,78,185,365,909,307]
downtime =  [80.3,51.2,27.3,64.3,75.4,5.1,31.4,64.2,1.3,61.3,24.5,43.8,0.5,31.42,1.3,18,126.8,4.7,23.2,47.1,42.2,41.5,0.3,31.4,1.1,4.1,86.2,3.2,152.9,6.9,114,201.6,12,2.9,47.1,4.8,3.2,241,93.4,126.9,305.2,3.64,5.1,177.6,203.52,4.8,1020,3.2,0,0,10.32,0.6,1,0,56.1,33,73.9,0.8,54.9,10.7,95.28,244.32,0.9,75.12,9,47,12.24,41.52,8,31.44,0.6,121.7,204.24,5.3,10.8,5.7,3.4,23.1,2,116.2,5.3,11.3,148.3,81.6,3.3,0,34.1,44.5,31.6,21.6,4.3,91.2,8,212,75,9,14.4,57.6,188.2,43.7]

stilllive = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,0]
noofsales =[3960,886,1273,4176,3400,1401,762,8919,23043,5376,3625,1397,1340,2056,555,1608,420,720,4827,2580,2948,1397,42,858,265,1724.4,6760,892,3573,1238,30150,6534,33,450,2581,403,1490,538.68,2410,32864,2000,3644,635,6954,7823,6575,1571,603,200,1350,756,6000,434,175,381,23000,21700,187,321,28929,0,4199,3700,7337,3522,6760,0,156,402,6760,884,296,0,272,1315,23,256,16170,4408,4907,798,1374,3481,3737,20003,0,619,427,1273,667,24,2,0,7689,7303,1306,840,172,8700,388]
avgsalesvalue = [15.67,19.99,398.1,1298.76,567.5,676.5,5.5,23.56,578.15,14.8,250.17,40.8,45.9,30.5,25.7,1056.89,75.5,50.9,77.5,156.9,300.1,98.5,567.14,23.6,256.75,276.75,0,176.5,23.84,124.5,673,1890,25000,32,75.9,15.99,324.7,45.67,129.99,98.1,150.99,67.5,76.5,43.6,23.56,78.15,14.8,250.17,30.8,45.9,1300.5,25.7,256.89,25.5,19.99,345,54.1,231,45,76.3,0,45.5,67.1,198.8,35.6,25.2,0,435,45,151,87.34,24,0,67,23.4,550,1345.87,33.3,23.4,92.1,499.99,56.,67.8,34.2,234.4,0,155.42,78.9,50.5,141.3,54.67,4230.12,0,287,25,643,25,154.98,543.15,50]
avgage  = [56,27,45,54,25,46,50,32,46,54,33,23,20,24,37,51,25,48,49,33,43,47,53,19,31,26,43,23,22,22,38,43,34,19,33,39,41,35,22,24,25,28,56,65,46,55,20,29,18,23,20,18,37,51,25,43,49,68,23,45,31,52,23,43,53,78,39,51,32,54,23,38,58,31,21	,22,27,43,42,53,23,33,23,20,19,37,51,25,43,49,33,43,42,53,43,56,183,19,31,5]
usabilityrating = [1,2,2,4,1,2,3,3,4,4,2,4,3,2,4,2,2,2,3,3,2,1,2,1,2,3,3,2,4,1,2,3,1,1,2,1,3,1,2,4,1,4,2,3,2,4,1,4,2,4,3,3,2,3,3,4,4,1,1,4,4,2,4,3,4,3,2,1,4,3,2,1,4,3,1,2,4,4,1,3,3,3,3,3,2,4,1,2,3,3,2,3,1,4,2,2,1,2,3,1]
no_of_hits = [3000,12663,4921,34798,28341,11678,10890,56785,57609,21507,51792,29966,3350,17131,2221,13454,43789,6000
,12067,21507,11792,19966,350,7152,2211,4311,124280,7437,51054,10318,40200,54444,275,6431,21509,1009,5963,4489,34438
,43818,65660,9112,5293,57955,65191,8767,22441,5025,2278,1876,11256,6298,3618,201,567,17688,29011,2678,23576,5892,34974
,345,3752,29346,609,21507,11792,10099,3350,17152,2211,42344,76543,3886,10966,18000,3651,21560,5878,40890,6632,11456,49879
,31145,1541,134,5159,6097,5092,5561,9581,356,11798,66732,29212,5226,12000,2456,18000,3233]
#noofsales =[3960,886,1273,4176,3400,1401,762,8919,23043,5376,3625,1397,1340,2056,555,1608,420,720,4827,2580,2948,1397,42,858,265,1724.4,NA,892,3573,1238,30150,6534,33,450,2581,403,1490,538.68,2410,32864,2000,3644,635,6954,7823,6575,1571,603,200,1350,756,6000,434,175,381,23000,21700,187,321,28929,0,4199,3700,7337,3522,NA,0,156,402,NA,884,296,0,272,1315,23,256,16170,4408,4907,798,1374,3481,3737,20003,0,619,427,1273,667,24,2,0,7689,7303,1306,840,172,8700,388]
no_of_sales = [3960,886,1273,4176,3400,1401,762,8919,23043,5376,3625,1397,1340,2056,555,1608,420,720,4827,2580,2948,1397,42,858,265,1724.4,3944,892,3573,1238,30150,6534,33,450,2581,403,1490,538.68,2410,32864,2000,3644,635,6954,7823,6575,1571,603,200,1350,756,6000,434,175,381,23000,21700,187,321,28929,0,4199,3700,7337,3522,3944,0,156,402,3944,884,296,0,272,1315,23,256,16170,4408,4907,798,1374,3481,3737,20003,0,619,427,1273,667,24,2,0,7689,7303,1306,840,172,8700,388]

from collections import Counter


print("counts" ,len(no_of_hits))
print("counts" ,len(no_of_sales))


#########################       Regression 1  NO OF HITS VS NO OF SALES   #########################################



#identifying correlation of the variables to determine the strenth of realtionships between the variables
rescorelation  = correlation(no_of_hits,no_of_sales)
print ("correlation(num of hits, amount of sales)", correlation(no_of_hits,no_of_sales))

# correlation of .27 indicates a weak corrleation an indicating a scatter of data from the regreassion line

n = len(no_of_hits)
no_of_hits_mean = mean(no_of_hits)
print("no_of_hits", no_of_hits_mean)

n = len(no_of_sales)
no_of_sales_mean = mean(no_of_sales)
print("mean salaries", no_of_sales_mean)

def dot(v,w):
	return sum(v_i * w_i for v_i,w_i in zip (v,w))

no_of_hitsno_of_sales = dot(no_of_hits,no_of_sales)
print("hits * sales",no_of_hitsno_of_sales)

def sum_of_squares(v):
	return dot(v,v)

hits = sum_of_squares(no_of_hits)
print("hits squared",hits)


numer = no_of_hitsno_of_sales-(n*(no_of_hits_mean*no_of_sales_mean))
print("numerator",numer)

denom = hits -(n*(no_of_hits_mean*no_of_hits_mean))
print("denomenator",denom)

b1 = numer/denom
print("b1",b1)

b0 = no_of_sales_mean -(b1*no_of_hits_mean)
print("b0",b0)

# least squares regression line for no of hits and sales is y = .085 x + 2344



def regresionsline(beta0,beta1,x):
	Y = beta0 + beta1*x
	return Y
	
# .0729 r squared value for no of hits and no of sales indicates
# that 7.29 percent of the variation in sales can be explained by the variation in hits


#  calculating residuals

y =(regresionsline(2343.5,.085,no_of_hits[0]))
print(y)

y_pred = [regresionsline(2343.5,.085,outputi) for outputi in no_of_sales]
print(y_pred)
	
def residuals_func(v,w):
	return[v_i - w_i for v_i,w_i in zip(v,w)]

residuals = residuals_func(no_of_sales,y_pred)
print(residuals)


matplotlib.pyplot.scatter(no_of_hits,residuals)
plt.axis([0,125000, -5000, 5000])
plt.title("Residuals for No hits Vs no Sales")
plt.xlabel("No of Hits")
plt.ylabel("No of Sales")
plt.axhline(0, color='black')
matplotlib.pyplot.show()

##############################   REGRESSION 2  USABILITY RATING VS NO OF SALES   ############################

#identifying correlation of the variables to determine the strenth of realtionships between the variables
rescorelation2  = correlation(usabilityrating,no_of_sales)
print ("Correlation(usabilityrating, num of sales)", correlation(usabilityrating,no_of_sales))


# correlation of .33 indicates a weak corrleation and indicating a large scatter of data from the regreassion line

n = len(usabilityrating)
usabilityrating_mean = mean(usabilityrating)
print("usabilityrating mean", usabilityrating_mean)

n = len(no_of_sales)
no_of_sales_mean = mean(no_of_sales)
print("mean salaries", no_of_sales_mean)

usabilityratingno_of_sales = dot(usabilityrating,no_of_sales)
print("usabilityrating * no_of_sales",usabilityratingno_of_sales)

ratings = sum_of_squares(usabilityrating)
print("hits squared",ratings)


numer2 = no_of_hitsno_of_sales-(n*(usabilityrating_mean*no_of_sales_mean))
print("numerator",numer2)

denom2 = hits -(n*(usabilityrating_mean*usabilityrating_mean))
print("denomenator",denom2)

b1 = numer2/denom2
print("b1",b1)

b0 = no_of_sales_mean -(b1*usabilityrating_mean)
print("b0",b0)

# .01108 r squared value for no of hits and no of sales indicates
# that 11.08 percent of the variation in sales can be explained by the variation in usability rating

y1 =(regresionsline(3944,.01397,usabilityrating[0]))
print(y1)

y_pred2 = [regresionsline(3944,.01397,outputi) for outputi in no_of_sales]
print(y_pred2)

matplotlib.pyplot.scatter(usabilityrating,residuals)
plt.axis([0,5, -5000, 5000])
plt.title("Usability Rating Vs no Sales")
plt.xlabel("Usability Rating")
plt.ylabel("No of Sales")
plt.axhline(0, color='black')
matplotlib.pyplot.show()
