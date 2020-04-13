#KMeansClustering_functions.py
#Athena Ohnemus
#I recieved help from Jenn Cross, Alycia Wong, and Sejal Dua
#This code is the functions that allow a data set to be classified into any number of clusters  

#Please place your FUNCTION code for step 4 here.

import numpy as np
import matplotlib.pyplot as plt
import random

#FUNCTIONS
def openckdfile():
    #takes no parameters
    #opens the file of ckd data
    #returns the glucose, hemoglobin, and classification data
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def normalizeData(glucose, hemoglobin, classification):
    #takes glucose, hemoglobin, and classification as parameters
    #scales the file data to be between 0 and 1
    #returns the scaled data and classification
    glucose_scaled = (np.array(glucose) - 70) / 420
    hemo_scaled = (np.array(hemoglobin) - 3.1) / 14.7
    return glucose_scaled, hemo_scaled, classification

def findCentroids(k):
    #takes a number k
    #makes an array of k by 2 and fills it with random numbers 0 to 1
    #returns this array as a k number of random centroids
    centroids = np.random.rand(k,2)
    return centroids

def nearestCentroidClass(k, centroids, glucose, hemoglobin):
    #takes the k value, the centroid array, the glucose and the hemoglobin data
    #finds the smallest distance between each data point and a centroid and classifies
    #that data point as the index of the centroid
    #returns an array of the closest centroid indexes for each data point
    dist_arr = np.zeros((158, k))
    for i in range(k):
        hemo_c = centroids[i,0]
        gluc_c = centroids[i,1]
        cent_dist = np.sqrt((hemoglobin - hemo_c)**2+(glucose - gluc_c)**2)
        for x in range(len(cent_dist)):
            dist_arr[x][i] = cent_dist[x]
    cent_assign = np.argmin(dist_arr, axis = 1)
    return cent_assign
        
def updateCentroids(k, glucose, hemoglobin, cent_assign):
    #takes k values, the glucose data, hemoglobin data, and the array of assignments to each centroid
    #finds the mean of the data in each cluster and changes the centroids to be have those coordinates
    #returns the new centroids
    centroids = np.zeros((k,2))
    for i in range(k):
        new_gluc_cent = np.mean(glucose[cent_assign == i])
        new_hemo_cent = np.mean(hemoglobin[cent_assign == i])
        centroids[i,0] = new_hemo_cent
        centroids[i,1] = new_gluc_cent
    return centroids
        
def graphingKMeans(glucose, hemoglobin, assignment, centroids):
    #takes the glucose data, the hemoglobin data, their class based on the centroids, and the centroids
    #graphs the data and centroids and separates each cluster by color
    #void function
    plt.figure()
    for i in range(assignment.max()+1):
        rcolor = np.random.rand(3,)
        plt.plot(hemoglobin[assignment==i],glucose[assignment==i], ".", label = "Class " + str(i), color = rcolor)
        plt.plot(centroids[i, 0], centroids[i, 1], "D", label = "Centroid " + str(i), color = rcolor)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()
    
def percentage(part, whole):
    #takes two numbers a part and a whole
    #finds the percent the first number is of the second number to two decimal places
    #returns the percent
    percent = round((part/whole) * 100, 2)
    return percent
 