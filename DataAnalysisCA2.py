import math
from collections import Counter
from statistics	import stdev
from matplotlib import pyplot as plt


def mean(x):
	return sum(x)/len(x)
	
def quantile(x, p):
    """returns the pth-percentile value in x"""
    p_index = int(p * len(x))
    return sorted(x)[p_index]
	
def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)
	
# median
def median(v):
#finds the 'middle-most' value of v
	n = len(v)
	sorted_v = sorted(v)
	midpoint = n // 2

	if n % 2 == 1:
# if odd, return the middle value
		return sorted_v[midpoint]
	else:
# if even, return the average of the middle values
		lo = midpoint - 1
		hi = midpoint
		return (sorted_v[lo] + sorted_v[hi]) / 2
		
#mode
def mode(x):

	counts = Counter(x)
	max_count = max(counts.values())
	return [x_i for x_i, count in counts.items()if count == max_count]

# range
def data_range(x):
    return max(x) - min(x)
	
def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]
	
def sum_of_squares(n): return sum([x**2 for x in n])

def variance(x):
  n = len(x)
  deviations = de_mean(x)
  return sum_of_squares(deviations) / (n - 1)
  

def standard_deviation(x):
  return math.sqrt(variance(x))
  


#medical = 1
# fashion = 2
# electrical = 3
# government = 4
# property = 5
# furnature = 6
# educational = 7
# it = 8
# supermarket =9
# 10 = book
# 11 = gaming
# 12 =  sports equipment

#initial clean of data
#type =[1,2,3,4,5,6,7,8,8,1,2,2,2,2,1,2,8,4,3,7,3,3,2,6,3,5,6,2,2,2,3,5,1,8,7,2,9,8,2,7,2,9,2,10,1,9,2,10,11,12,2,11,11,4,6,1,3,7,11,5,10,2,2,8,1,4,5,2,11,2,7,5,2,2,7,12,11,7,11,12,3,2,2,8,5,12,7,1,9,10,3,5,12,7,3,2,2,8,7]
#nodayslive =[502,189,76,518,423,234,155,543,1009,321,176,298,50,256,33,200,653,86,180,321,176,298,50,256,33,76,484,111,762,154,600,965,175,96,321,145,189,7,514,654,980,136,79,865,973,145,335,75,34,28,168,94,54,3,100000,264,433,42,354,87,522,1143,56,438,9,321,176,298,50,256,33,632,976,58,164,76,54,321,87,609,99,172,743,465,23,2,77,91,76,83,143,532,176,996,436,78,185,365,909,307]
#downtime =  [80.3,51.2,27.3,64.3,75.4,5.1,31.4,64.2,1.3,61.3,24.5,43.8,0.5,31.42,1.3,18,126.8,4.7,23.2,47.1,42.2,41.5,0.3,31.4,1.1,4.1,86.2,3.2,152.9,6.9,114,201.6,12,2.9,47.1,4.8,3.2,241,93.4,126.9,305.2,3.64,5.1,177.6,203.52,4.8,1020,3.2,0,0,10.32,0.6,1,0,56.1,33,73.9,0.8,54.9,10.7,95.28,244.32,0.9,75.12,9,47,12.24,41.52,8,31.44,0.6,121.7,204.24,5.3,10.8,5.7,3.4,23.1,2,116.2,5.3,11.3,148.3,81.6,3.3,0,34.1,44.5,31.6,21.6,4.3,91.2,8,212,75,9,14.4,57.6,188.2,43.7]
#numhits = [3000,12663,4921,34798,28341,11678,10890,56785,57609,21507,51792,29966,3350,17131,2221,13454,43789,6000,12067,21507,11792,19966,350,7152,2211,4311,124280,7437,51054,10318,40200,54444,275,6431,21509,1009,5963,4489,34438,43818,65660,9112,5293,57955,65191,8767,22441,5025,2278,1876,11256,6298,3618,201,567,17688,29011,2678,23576,5892,34974,345,3752,29346,609,21507,11792,10099,3350,17152,2211,42344,76543,3886,10966,NA,3651,21560,5878,40890,6632,11456,49879,31145,1541,134,5159,6097,5092,5561,9581,356,11798,66732,29212,5226,12000,2456,NA,3233,43789,6000,12067,21507,11792,19966,350,7152,2211,4311,124280,7437,51054,10318,40200,54444,275,6431,21509,1009,5963,4489,34438,43818,65660,9112,5293,57955,65191,8767,22441,5025,2278,1876,11256,6298,3618,201,567,17688,29011,2678,23576,5892,34974,345,3752,29346,609,21507,11792,10099,3350,17152,2211,42344,76543,3886,10966,NA,3651,21560,5878,40890,6632,11456,49879,31145,1541,134,5159,6097,5092,5561,9581,356,11798,66732,29212,5226,12000,2456,NA,3233]
#stilllive = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,0]
#noofsales =[3960,886,1273,4176,3400,1401,762,8919,23043,5376,3625,1397,1340,2056,555,1608,420,720,4827,2580,2948,1397,42,858,265,1724.4,NA,892,3573,1238,30150,6534,33,450,2581,403,1490,538.68,2410,32864,2000,3644,635,6954,7823,6575,1571,603,200,1350,756,6000,434,175,381,23000,21700,187,321,28929,0,4199,3700,7337,3522,NA,0,156,402,NA,884,296,0,272,1315,23,256,16170,4408,4907,798,1374,3481,3737,20003,0,619,427,1273,667,24,2,0,7689,7303,1306,840,172,8700,388]
#avgsalesvalue [15.67,19.99,398.1,1298.76,567.5,676.5,5.5,23.56,578.15,14.8,250.17,40.8,45.9,30.5,25.7,1056.89,75.5,50.9,77.5,156.9,300.1,98.5,567.14,23.6,256.75,276.75,0,176.5,23.84,124.5,673,1890,25000,32,75.9,15.99,324.7,45.67,129.99,98.1,150.99,67.5,76.5,43.6,23.56,78.15,14.8,250.17,30.8,45.9,1300.5,25.7,256.89,25.5,19.99,345,54.1,231,45,76.3,0,45.5,67.1,198.8,35.6,25.2,0,435,45,NA,87.34,24,0,67,23.4,550,1345.87,33.3,23.4,92.1,499.99,56.,67.8,34.2,234.4,0,155.42,78.9,50.5,141.3,54.67,4230.12,0,287,25,643,25,154.98,543.15,50]
#avgage  = [56,27,45,54,25,46,50,32,46,54,33,23,20,24,37,51,25,48,49,33,43,47,53,19,31,26,43,23,22,22,38,43,34,19,33,39,41,35,22,24,25,28,56,65,46,55,20,29,18,23,20,18,37,51,25,43,49,68,23,45,31,52,23,43,53,78,39,51,32,54,23,38,58,31,21	,22,27,43,42,53,23,33,23,20,19,37,51,25,43,49,33,43,42,53,43,56,183,19,31,5]
#usabilityrating = [1,2,2,4,1,2,3,3,4,4,2,4,3,2,4,2,2,2,3,3,2,1,2,1,2,3,3,2,4,1,2,3,1,1,2,1,3,1,2,4,1,4,2,3,2,4,1,4,2,4,3,3,2,3,3,4,4,1,1,4,4,2,4,3,4,3,2,1,4,3,2,1,4,3,1,2,4,4,1,3,3,3,3,3,2,4,1,2,3,3,2,3,1,4,2,2,1,2,3,1]

######## DATA FORMATTING    ########     removal of n/a     non readable
typeR =[1,2,3,4,5,6,7,8,8,1,2,2,2,2,1,2,8,4,3,7,3,3,2,6,3,5,6,2,2,2,3,5,1,8,7,2,9,8,2,7,2,9,2,10,1,9,2,10,11,12,2,11,11,4,6,1,3,7,11,5,10,2,2,8,1,4,5,2,11,2,7,5,2,2,7,12,11,7,11,12,3,2,2,8,5,12,7,1,9,10,3,5,12,7,3,2,2,8,7]
noDaysLiveR =[502,189,76,518,423,234,155,543,1009,321,176,298,50,256,33,200,653,86,180,321,176,298,50,256,33,76,484,111,762,154,600,965,175,96,321,145,189,7,514,654,980,136,79,865,973,145,335,75,34,28,168,94,54,3,100000,264,433,42,354,87,522,1143,56,438,9,321,176,298,50,256,33,632,976,58,164,76,54,321,87,609,99,172,743,465,23,2,77,91,76,83,143,532,176,996,436,78,185,365,909,307]
downTimeR =  [80.3,51.2,27.3,64.3,75.4,5.1,31.4,64.2,1.3,61.3,24.5,43.8,0.5,31.42,1.3,18,126.8,4.7,23.2,47.1,42.2,41.5,0.3,31.4,1.1,4.1,86.2,3.2,152.9,6.9,114,201.6,12,2.9,47.1,4.8,3.2,241,93.4,126.9,305.2,3.64,5.1,177.6,203.52,4.8,1020,3.2,0,0,10.32,0.6,1,0,56.1,33,73.9,0.8,54.9,10.7,95.28,244.32,0.9,75.12,9,47,12.24,41.52,8,31.44,0.6,121.7,204.24,5.3,10.8,5.7,3.4,23.1,2,116.2,5.3,11.3,148.3,81.6,3.3,0,34.1,44.5,31.6,21.6,4.3,91.2,8,212,75,9,14.4,57.6,188.2,43.7]
stillLiveR = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,0]
noOfSalesR =[3960,886,1273,4176,3400,1401,762,8919,23043,5376,3625,1397,1340,2056,555,1608,420,720,4827,2580,2948,1397,42,858,265,1724.4,892,3573,1238,30150,6534,33,450,2581,403,1490,538.68,2410,32864,2000,3644,635,6954,7823,6575,1571,603,200,1350,756,6000,434,175,381,23000,21700,187,321,28929,0,4199,3700,7337,3522,0,156,402,884,296,0,272,1315,23,256,16170,4408,4907,798,1374,3481,3737,20003,0,619,427,1273,667,24,2,0,7689,7303,1306,840,172,8700,388]
avgSalesValueR = [15.67,19.99,398.1,1298.76,567.5,676.5,5.5,23.56,578.15,14.8,250.17,40.8,45.9,30.5,25.7,1056.89,75.5,50.9,77.5,156.9,300.1,98.5,567.14,23.6,256.75,276.75,0,176.5,23.84,124.5,673,1890,25000,32,75.9,15.99,324.7,45.67,129.99,98.1,150.99,67.5,76.5,43.6,23.56,78.15,14.8,250.17,30.8,45.9,1300.5,25.7,256.89,25.5,19.99,345,54.1,231,45,76.3,0,45.5,67.1,198.8,35.6,25.2,0,435,45,87.34,24,0,67,23.4,550,1345.87,33.3,23.4,92.1,499.99,56.,67.8,34.2,234.4,0,155.42,78.9,50.5,141.3,54.67,4230.12,0,287,25,643,25,154.98,543.15,50]
avgAgeR  = [56,27,45,54,25,46,50,32,46,54,33,23,20,24,37,51,25,48,49,33,43,47,53,19,31,26,43,23,22,22,38,43,34,19,33,39,41,35,22,24,25,28,56,65,46,55,20,29,18,23,20,18,37,51,25,43,49,68,23,45,31,52,23,43,53,78,39,51,32,54,23,38,58,31,21	,22,27,43,42,53,23,33,23,20,19,37,51,25,43,49,33,43,42,53,43,56,183,19,31,5]
usabilityRatingR = [1,2,2,4,1,2,3,3,4,4,2,4,3,2,4,2,2,2,3,3,2,1,2,1,2,3,3,2,4,1,2,3,1,1,2,1,3,1,2,4,1,4,2,3,2,4,1,4,2,4,3,3,2,3,3,4,4,1,1,4,4,2,4,3,4,3,2,1,4,3,2,1,4,3,1,2,4,4,1,3,3,3,3,3,2,4,1,2,3,3,2,3,1,4,2,2,1,2,3,1]
no_of_hits = [3000,12663,4921,34798,28341,11678,10890,56785,57609,21507,51792,29966,3350,17131,2221,13454,43789,6000
,12067,21507,11792,19966,350,7152,2211,4311,124280,7437,51054,10318,40200,54444,275,6431,21509,1009,5963,4489,34438
,43818,65660,9112,5293,57955,65191,8767,22441,5025,2278,1876,11256,6298,3618,201,567,17688,29011,2678,23576,5892,34974
,345,3752,29346,609,21507,11792,10099,3350,17152,2211,42344,76543,3886,10966,18000,3651,21560,5878,40890,6632,11456,49879
,31145,1541,134,5159,6097,5092,5561,9581,356,11798,66732,29212,5226,12000,2456,18000,3233]

from collections import Counter


print("counts" ,Counter(typeR))
#counts Counter({2: 26, 7: 11, 3: 10, 1: 8, 5: 8, 8: 8, 11: 7, 12: 5, 4: 4, 6: 4, 9: 4, 10: 4})



#
#  bar chart of types of site
#

sitesnum = [2,7,3,1,5,8,11,12,4,6,9,10]
sites = ["fash", "edu", "elec", "med", "prop","it","game","sport","gov","furn","su","book"]
num_sites = [26,11,10,8,8,8,7,5,4,4,4,4]
xstep = [i+0.1 for i, _ in enumerate(sites)]
plt.show()
xstep = [i+0.1 for i, _ in enumerate(sites)]
plt.bar(xstep, num_sites)
plt.xticks([i+0.5 for i, _ in enumerate(sites)], sites)
plt.title("sites")
plt.ylabel("# no of sites")
plt.show()






####################################  NO OF DAYS LIVE MEASURES OF SPREAD AND CENTRAL TENDANCIE #################################################
noDaysLiveOutlierRemov =[502,189,76,518,423,234,155,543,1009,321,176,298,50,256,33,200,653,86,180,321,176,298,50,256,33,76,484,111,762,154,600,965,175,96,321,145,189,7,514,654,980,136,79,865,973,145,335,75,34,28,168,94,54,3,264,433,42,354,87,522,1143,56,438,9,321,176,298,50,256,33,632,976,58,164,76,54,321,87,609,99,172,743,465,23,2,77,91,76,83,143,532,176,996,436,78,185,365,909,307]

sorted_noDaysLiveR = sorted(noDaysLiveR)         

print("Q1(x, 0.25)", quantile(sorted_noDaysLiveR , 0.25))
print("Q3(x, 0.75)", quantile(sorted_noDaysLiveR , 0.75))
print("interquartile_range(noDaysLiveR )", interquartile_range(sorted_noDaysLiveR ))  
# from geting the iqr and finding out if any extreme outliers exist i found there is one which is well over 3 iqrs away from the box 100000

sorted_noDaysLiveR = sorted(noDaysLiveOutlierRemov)
print("sorted_sorted_noDaysLiveR",noDaysLiveOutlierRemov)

largest_value = max(noDaysLiveOutlierRemov)         
smallest_value = min(noDaysLiveOutlierRemov)
print("Range noDaysLiveR with outlier removed ",largest_value-smallest_value) 
#### measures of spread
print("Q1(x, 0.25)", quantile(noDaysLiveOutlierRemov , 0.25))
print("Q3(x, 0.75)", quantile(noDaysLiveOutlierRemov, 0.75))
print("interquartile_range(noDaysLiveR )", interquartile_range(noDaysLiveOutlierRemov ))
print("variance no of days live outlier removed", variance(noDaysLiveOutlierRemov)) 
print("stdDev no of days live outlier removed", standard_deviation(noDaysLiveOutlierRemov))
##### measures of central tendancie
print("Mean of no of days live with outlier removed", mean(noDaysLiveOutlierRemov))
print("Median of no of days live with outlier removed", median(noDaysLiveOutlierRemov))
print("Mode of no of days live with outlier removed", mode(noDaysLiveOutlierRemov))

################################### DOWN TIME  MEASURES OF SPREAD AND CENTRAL TENDANCIE #############################################################################

#######  investigating for outliers
downTimeR =  [80.3,51.2,27.3,64.3,75.4,5.1,31.4,64.2,1.3,61.3,24.5,43.8,0.5,31.42,1.3,18,126.8,4.7,23.2,47.1,42.2,41.5,0.3,31.4,1.1,4.1,86.2,3.2,152.9,6.9,114,201.6,12,2.9,47.1,4.8,3.2,241,93.4,126.9,305.2,3.64,5.1,177.6,203.52,4.8,1020,3.2,0,0,10.32,0.6,1,0,56.1,33,73.9,0.8,54.9,10.7,95.28,244.32,0.9,75.12,9,47,12.24,41.52,8,31.44,0.6,121.7,204.24,5.3,10.8,5.7,3.4,23.1,2,116.2,5.3,11.3,148.3,81.6,3.3,0,34.1,44.5,31.6,21.6,4.3,91.2,8,212,75,9,14.4,57.6,188.2,43.7]
sorted_downTimeR = sorted(downTimeR )
print("sorted down time",sorted_downTimeR)
print("Q1(x, 0.25)", quantile(sorted_downTimeR , 0.25))
print("Q3(x, 0.75)", quantile(sorted_downTimeR, 0.75))
print("interquartile_range(downTimeR )", interquartile_range(sorted_downTimeR ))  
### from observing the iqr the value of 1020 hours there is an extreme outlier that effets the mean and others and will be removed
downTimeOutlierRemov =  [80.3,51.2,27.3,64.3,75.4,5.1,31.4,64.2,1.3,61.3,24.5,43.8,0.5,31.42,1.3,18,126.8,4.7,23.2,47.1,42.2,41.5,0.3,31.4,1.1,4.1,86.2,3.2,152.9,6.9,114,201.6,12,2.9,47.1,4.8,3.2,241,93.4,126.9,305.2,3.64,5.1,177.6,203.52,4.8,3.2,0,0,10.32,0.6,1,0,56.1,33,73.9,0.8,54.9,10.7,95.28,244.32,0.9,75.12,9,47,12.24,41.52,8,31.44,0.6,121.7,204.24,5.3,10.8,5.7,3.4,23.1,2,116.2,5.3,11.3,148.3,81.6,3.3,0,34.1,44.5,31.6,21.6,4.3,91.2,8,212,75,9,14.4,57.6,188.2,43.7]
#### measures of spread
largest_value1 = max(downTimeOutlierRemov)         
smallest_value1 = min(downTimeOutlierRemov)
print("Range downtime with outlier removed ",largest_value1-smallest_value1)
print("variance downtime outlier removed", variance(downTimeOutlierRemov)) 
print("stdDev downtime outlier removed", standard_deviation(downTimeOutlierRemov))



#################################   NO OF HITS  MEASURES OF SPREAD AND CENTRAL TENDANCIE   ##################################################

#########  investigating for outliers
#numHitsR = [3000,12663,4921,34798,28341,11678,10890,56785,57609,21507,51792,29966,3350,17131,2221,13454,43789,6000,12067,21507,11792,19966,350,7152,2211,4311,124280,7437,51054,10318,40200,54444,275,6431,21509,1009,5963,4489,34438,43818,65660,9112,5293,57955,65191,8767,22441,5025,2278,1876,11256,6298,3618,201,567,17688,29011,2678,23576,5892,34974,345,3752,29346,609,21507,11792,10099,3350,17152,2211,42344,76543,3886,10966,3651,21560,5878,40890,6632,11456,49879,31145,1541,134,5159,6097,5092,5561,9581,356,11798,66732,29212,5226,12000,2456,3233,43789,6000,12067,21507,11792,19966,350,7152,2211,4311,124280,7437,51054,10318,40200,54444,275,6431,21509,1009,5963,4489,34438,43818,65660,9112,5293,57955,65191,8767,22441,5025,2278,1876,11256,6298,3618,201,567,17688,29011,2678,23576,5892,34974,345,3752,29346,609,21507,11792,10099,3350,17152,2211,42344,76543,3886,10966,3651,21560,5878,40890,6632,11456,49879,31145,1541,134,5159,6097,5092,5561,9581,356,11798,66732,29212,5226,12000,2456,3233]
sorted_numHitsR= sorted(no_of_hits )
print("sorted no of hits",sorted_numHitsR)
print("Q1(x, 0.25)", quantile(sorted_numHitsR , 0.25))
print("Q3(x, 0.75)", quantile(sorted_numHitsR, 0.75))
print("interquartile_range(no of hits )", interquartile_range(sorted_numHitsR )) 
#####   from observing there are 2 outliiers both of value 124280
numHitsOutliersRemoved = [3000,12663,4921,34798,28341,11678,10890,56785,57609,21507,51792,29966,3350,17131,2221,13454,43789,6000,12067,21507,11792,19966,350,7152,2211,4311,7437,51054,10318,40200,54444,275,6431,21509,1009,5963,4489,34438,43818,65660,9112,5293,57955,65191,8767,22441,5025,2278,1876,11256,6298,3618,201,567,17688,29011,2678,23576,5892,34974,345,3752,29346,609,21507,11792,10099,3350,17152,2211,42344,76543,3886,10966,3651,21560,5878,40890,6632,11456,49879,31145,1541,134,5159,6097,5092,5561,9581,356,11798,66732,29212,5226,12000,2456,3233,43789,6000,12067,21507,11792,19966,350,7152,2211,4311,7437,51054,10318,40200,54444,275,6431,21509,1009,5963,4489,34438,43818,65660,9112,5293,57955,65191,8767,22441,5025,2278,1876,11256,6298,3618,201,567,17688,29011,2678,23576,5892,34974,345,3752,29346,609,21507,11792,10099,3350,17152,2211,42344,76543,3886,10966,3651,21560,5878,40890,6632,11456,49879,31145,1541,134,5159,6097,5092,5561,9581,356,11798,66732,29212,5226,12000,2456,3233] 
###### measures of spread
largest_value2 = max(sorted_numHitsR)         
smallest_value2 = min(sorted_numHitsR)
print("Range no of hits with outlier removed ",largest_value2-smallest_value2)
print("variance no of hits outlier removed", variance(sorted_numHitsR)) 
print("stdDev no of hitsoutlier removed", standard_deviation(sorted_numHitsR))
####  measures of central tendancie
print("Mean of no of hits with outlier removed", mean(sorted_numHitsR))
print("Median no of hits with outlier removed", median(sorted_numHitsR))
print("Mode no of hitswith outlier removed", mode(sorted_numHitsR))

#################################   NO OF SALES  MEASURES OF SPREAD AND CENTRAL TENDANCIE  ####################################################

########   investigating for outliers
sorted_noOfSales= sorted(noOfSalesR )
print("sorted no of SALES",sorted_noOfSales)
print("Q1(x, 0.25)", quantile(sorted_noOfSales , 0.25))
print("Q3(x, 0.75)", quantile(sorted_noOfSales, 0.75))
print("interquartile_range(no of sales )", interquartile_range(sorted_noOfSales )) 

####### not removing outliers on this data , approx 8 outliers

#######  measures of spread
largest_value3 = max(sorted_noOfSales)         
smallest_value3 = min(sorted_noOfSales)
print("Range NO OF SALES with outlier removed ",largest_value3-smallest_value3)
print("variance NO OF SALES outlier removed", variance(sorted_noOfSales)) 
print("stdDev NO OF SALES outlier removed", standard_deviation(sorted_noOfSales))
####  measures of central tendancie
print("Mean of NO OF SALES with outlier removed", mean(sorted_noOfSales))
print("Median NO OF SALES with outlier removed", median(sorted_noOfSales))
print("Mode NO OF SALES swith outlier removed", mode(sorted_noOfSales))

#################################  AVG SALES VALUE  MEASURES OF SPREAD AND CENTRAL TENDANCIE  ####################################################
########   investigating for outliers
sorted_avgSalesValue= sorted(avgSalesValueR )
print("sorted AVG SALES VALUE ",sorted_avgSalesValue)
print("Q1(x, 0.25)", quantile(sorted_avgSalesValue , 0.25))
print("Q3(x, 0.75)", quantile(sorted_avgSalesValue, 0.75))
print("interquartile_range(AVG SALES VALUE )", interquartile_range(sorted_avgSalesValue )) 

#########  5 extreme outliers removed 1298.76, 1300.5, 1345.87, 1890, 4230.12, 25000 that effect the average sales value 

avgSalesValueOutliersRemoved = [15.67,19.99,398.1,567.5,676.5,5.5,23.56,578.15,14.8,250.17,40.8,45.9,30.5,25.7,1056.89,75.5,50.9,77.5,156.9,300.1,98.5,567.14,23.6,256.75,276.75,0,176.5,23.84,124.5,673,32,75.9,15.99,324.7,45.67,129.99,98.1,150.99,67.5,76.5,43.6,23.56,78.15,14.8,250.17,30.8,45.9,25.7,256.89,25.5,19.99,345,54.1,231,45,76.3,0,45.5,67.1,198.8,35.6,25.2,0,435,45,87.34,24,0,67,23.4,550,33.3,23.4,92.1,499.99,56.,67.8,34.2,234.4,0,155.42,78.9,50.5,141.3,54.67,0,287,25,643,25,154.98,543.15,50]
#######  measures of spread
largest_value4 = max(avgSalesValueOutliersRemoved)         
smallest_value4 = min(avgSalesValueOutliersRemoved)
print("Range AVG SALES VALUE with outlier removed ",largest_value4-smallest_value4)
print("variance AVG SALES VALUE outlier removed", variance(avgSalesValueOutliersRemoved)) 
print("stdDev AVG SALES VALUE outlier removed", standard_deviation(avgSalesValueOutliersRemoved))
####  measures of central tendancie
print("Mean of AVG SALES VALUE with outlier removed", mean(avgSalesValueOutliersRemoved))
print("Median AVG SALES VALUE with outlier removed", median(avgSalesValueOutliersRemoved))
print("Mode AVG SALES VALUE with outlier removed", mode(avgSalesValueOutliersRemoved))

#################################    avgAge   MEASURES OF SPREAD AND CENTRAL TENDANCIE     ###############################################
sorted_avgAge = sorted( avgAgeR  )
print("sorted  avgAge VALUE ",sorted_avgAge )
print("Q1(x, 0.25)", quantile(sorted_avgAge , 0.25))
print("Q3(x, 0.75)", quantile(sorted_avgAge ,0.75))
print("interquartile_range(avg Age )", interquartile_range(sorted_avgAge )) 

#####   one outlier of average age 183 to be removed possible error permantanly removed 

avgAgeOutlierRemoved  = [56,27,45,54,25,46,50,32,46,54,33,23,20,24,37,51,25,48,49,33,43,47,53,19,31,26,43,23,22,22,38,43,34,19,33,39,41,35,22,24,25,28,56,65,46,55,20,29,18,23,20,18,37,51,25,43,49,68,23,45,31,52,23,43,53,78,39,51,32,54,23,38,58,31,21,22,27,43,42,53,23,33,23,20,19,37,51,25,43,49,33,43,42,53,43,56,19,31,5]
#######  measures of spread
largest_value5 = max(avgAgeOutlierRemoved)         
smallest_value5 = min(avgAgeOutlierRemoved)
print("Range avgAge with outlier removed ",largest_value5-smallest_value5)
print("variance avgAge outlier removed", variance(avgAgeOutlierRemoved)) 
print("stdDev avgAge outlier removed", standard_deviation(avgAgeOutlierRemoved))
####  measures of central tendancie
print("Mean of avgAge with outlier removed", mean(avgAgeOutlierRemoved))
print("Median avgAge with outlier removed", median(avgAgeOutlierRemoved))
print("Mode avgAgewith outlier removed", mode(avgAgeOutlierRemoved))

#################################    USABILITY RATING  MEASURES OF SPREAD AND CENTRAL TENDANCIE     ###############################################
sorted_userRating = sorted( usabilityRatingR )
print("sorted  user rating VALUE ",sorted_userRating)
print("Q1(x, 0.25)", quantile(sorted_userRating , 0.25))
print("Q3(x, 0.75)", quantile(sorted_userRating ,0.75))
print("interquartile_range(user rating )", interquartile_range(sorted_userRating ))

## no outliers
#######  measures of spread
largest_value6 = max(sorted_userRating)         
smallest_value6 = min(sorted_userRating)

print("Range usability rating  ",largest_value6-smallest_value6)
print("variance usability rating", variance(sorted_userRating))
print("stdDev usability rating", standard_deviation(sorted_userRating))
####  measures of central tendancie
print("Mean of usability rating", mean(sorted_userRating))
print("Median usability rating", median(sorted_userRating))
print("Mode usability rating", mode(sorted_userRating))

