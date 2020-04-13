#KMeansClustering_driver.py
#Athena Ohnemus
#I recieved no help on this code
#This is the driver that takes the data, runs the functions, and graphs the outcome
#of a clustering of a data set into a certain number of groups

#Please place your FUNCTION code for step 4 here.

import KMeansClustering_functions as kmc #Use kmc to call your functions

#GLOBAL VARIABLES
k = 2
total = 0
true_negative = 0
true_positive = 0 
false_negative = 0
false_positive = 0

#MAIN SCRIPT
glucose, hemoglobin, classification = kmc.openckdfile()
glucose_scaled, hemoglobin_scaled, classification = kmc.normalizeData(glucose, hemoglobin, classification)
centroids = kmc.findCentroids(k)

for i in range(158):
    new_cent_assign = kmc.nearestCentroidClass(k, centroids, glucose_scaled, hemoglobin_scaled)
    centroids = kmc.updateCentroids(k, glucose_scaled, hemoglobin_scaled, new_cent_assign)

kmc.graphingKMeans(glucose_scaled, hemoglobin_scaled, new_cent_assign, centroids)

if k == 2:
#this finds the percent that the data matches if there are 2 clusters
    for i in range(len(new_cent_assign)):
        if new_cent_assign[i] == 0 and classification[i] == 0:
            total += 1
            true_negative += 1
        elif new_cent_assign[i] == 1 and classification[i] == 0:
            total += 1
            false_positive += 1
        elif new_cent_assign[i] == 1 and classification[i] == 1:
            total += 1
            true_positive += 1
        elif new_cent_assign[i] == 0 and classification[i] == 1:
            total += 1
            false_negative += 1
             
    percent_true_positive = print('True positive rate (sensitivity) = ' + str(kmc.percentage(true_positive, total)) + '%')
    percent_false_positive = print('False positive rate = ' + str(kmc.percentage(false_positive, total)) + '%')
    percent_true_negative = print('True negative rate (specificity) = ' + str(kmc.percentage(true_negative, total)) + '%')
    percent_false_negative = print('False negative rate = ' + str(kmc.percentage(false_negative, total)) + '%')

else:
    pass
   