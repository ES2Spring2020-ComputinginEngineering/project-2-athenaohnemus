Project 2
Athena Ohnemus

This project is based on an example and dataset from Data Science course developed at Berkeley (Data8.org).

Introduciton:
This code takes an uploaded data set and analyzes it through a variety of classification techniques. There are three main files and five important graphs included in this analysis. The system is relatively easy to use. If you run the NearestNeighborClassifier you will get a graph of the data set with a larger point, which is the new data point being classified. The function will print the classification of that new point based on the nearest data point and the k nearest. Changing the k value will compare the classification of more closest points to the new one. If you run the KMeansClustering_driver you will get a graph of the final clusters and centroids. Each group will have a different color and the centroids will be larger than the other data points. Change the k-value in the global variables section to see a different number of clusters. If the k-value is 2 a list of percentages will be printed indicating the percent of false positives, false negatives, true positives, and true negatives when compared to the classification of the original data.

Summary of Files:
- NearestNeighborClassifier:
This code includes both the functions and the main script to find the classification of a random new point based on the known classifications of a data set. It finds the classification by both looking at the closest point and by looking at the k-closest points. It then graphs the new data point on a graph of the data set for a visual of where in the data this point falls.

- KMeansClustering_funcitons
This script simply includes the functions to perform K-means clustering. 
	Function Descriptions:
	- Open file:
This function takes no parameters. It just opens the file of data and returns arrays of the glucose, hemoglobin, and their classifications.

	- Normalize Data:
This funciton takes the arrays of glucose and hemoglobin data and scales them to be from 0 to 1 in order to make the graph look accurate. It returns these scaled arrays of hemoglobin and glucose data.

	- Find centroids:
This function takes k, a given number, as parameter. It will make a k by 2  array of random numbers from 0 to 1. This array of data point will be returned as the centroids.

	- Nearest centroid class:
This function takes parameters k, the centroids array, the glucose data, and the hemoglobin data. It will find which centroid is closest to each data point and classify each point as the index of the closest centroid. The function returns an array of closest centroid assignments for each data point.

	- Update centroids:
This funciton takes the designated k-value, the glucose data, hemoglobin data, and array of centroid assignments to finds the average of the points that match with each centroid and then changes the centroids to have the coordinates of the mean hemoglobin and mean glucose. It returns the array of centroids with new coordinates.

	- Graphing K-Means:
This function takes the scaled glucose and hemoglobin as well as the centroid assignment array and the updated centroids. It uses this information to make a graph which shows what data is in which cluster by color and has the centroids stand out as larger points. It is a void function.

	- Percentage:
This function takes two numbers (part and whole) and finds what percent the first number is of the second number to the hundreths place. It returns that percentage.
	
- KMeansClustering_driver:
This code runs all the functions from the KMeansClustering_functions file. The global variable k can be changed to increase or decrease the number of clusters. The organization of this file allows the data to be sorted into different clusters and then be graphed. If the k value is 2 this file will calculate the percent differences of this clustering versus the original classifications of the CKD data set.

