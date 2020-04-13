#NearestNeighborClassification.py
#Athena Ohnemus
#I recieved no help on this code
#This script will classify a randomly generated point as either ckd positive or 
#negative based on the classification of the closest point or closest k points

#Please put your code for Step 2 and Step 3 in this file.

import numpy as np
import matplotlib.pyplot as plt
import random

#GLOBAL VARIABLES
k = 3

# FUNCTIONS
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

def graphData(glucose, hemoglobin, classification): 
    #takes glucose, hemoglobin, and classification
    #graphs the data and colors it to match classification
    #void function
    plt.figure()    
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "CKD positive")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Normal")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.title('Hemoglobin vs. Glucose levels for CKD tests')
    
def createTestCase():
    #has no parameters
    #creates a random hemoglobin and glucose value between 0 and 1
    #returns the new hemoglobin and glucose value
    newhemoglobin = random.random()
    newglucose = random.random()
    return newhemoglobin, newglucose

def calculateDistanceArray(newhemoglobin, newglucose, glucose, hemoglobin):
    #takes the new hemoglobin, new glucose, glucose data, and hemoglobin data as parameters
    #finds the distance between each data point and the new random hemoglobin, glucose point  
    #returns an array of these distances
    dist_arr = np.sqrt((hemoglobin - newhemoglobin)**2 + (glucose - newglucose)**2)
    return dist_arr

def nearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification):
    #takes the new glucose, new hemoglobin, glucose data, hemoglobin data, and their classification
    #finds the classification of the point closest to the new hemoglobin, new glucose point
    #returns the classification of that point
    dist_arr = calculateDistanceArray(newhemoglobin, newglucose, glucose, hemoglobin)
    min_index = np.argmin(dist_arr)
    nearest_class = classification[min_index]
    return nearest_class

def graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification):
    #takes the new glucose, new hemoglobin, glucose data, hemoglobin data, and their classification
    #graphs the data and the new point
    #void function
    graphData(glucose, hemoglobin, classification)
    plt.plot(newglucose, newhemoglobin, 'bo', markersize = 15)
    plt.show()
    
def kNearestNeighborClassifier(k, newglucose, newhemoglobin, glucose, hemoglobin, classification):
    #takes a k value, the new glucose, new hemoglobin, glucose data, hemoglobin data, and their classification
    #finds the classification of the k nearest points to the new random data point
    #returns the most common classification for the k points
    dist_arr = np.sqrt((hemoglobin - newhemoglobin)**2 + (glucose - newglucose)**2)
    sorted_dist = np.argsort(dist_arr)
    k_indices = sorted_dist[:k]
    class_list = classification[k_indices]
    newClass = round(sum(class_list)/k)
    return newClass

# MAIN SCRIPT
glucose, hemoglobin, classification = openckdfile()
glucose_scaled, hemoglobin_scaled, classification = normalizeData(glucose, hemoglobin, classification)
newhemoglobin, newglucose = createTestCase()

print(nearestNeighborClassifier(newhemoglobin, newglucose, glucose_scaled, hemoglobin_scaled, classification))
graphTestCase(newhemoglobin, newglucose, glucose_scaled, hemoglobin_scaled, classification)
print(kNearestNeighborClassifier(k, newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled, classification))
