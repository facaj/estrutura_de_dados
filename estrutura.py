import time

def bublesort(array):
	for i in range(len(array)):
		for j in range(len(array)):
			if array[i] < array[j]:
				array[i],array[j] = array[j],array[i]

	return array

#---------------------------------------------------------------------
def selectionsort(array):
	for i in range(len(array)):
		j = i +1
		while j < len(array):
			if array[j] < array[i]:
				array[j],array[i] = array[i], array[j]
			j=j+1
	return array

#--------------------------------------------------------------------
def insertionsort(array):
	for i in range(1,len(array)):
		j=i-1
		while array[j] > array[j+1] and j>=0:
			array[j+1] , array[j] = array[j] , array[j+1]
			j = j -1
	return array

#-------------------------------------------------------------------
def merge(array,inicio,meio,fim):
	i=inicio
	j=meio
	array_temp = []
	while i < meio and j < fim:
		print "i " + str(array[i]) + " j " + str(array[j])
		if array[i] <= array[j]:
			array_temp.append(array[i])
		else:
			array_temp.append(array[j])
		i=i+1
		j=j+1
	while i < meio:
		array_temp.append(array[i])
		i=i+1
	while j < fim:
		array_temp.append(array[j])
		j=j+1
	array = array_temp
def mergesort(array,inicio,fim):
	if inicio < fim:
		meio = (inicio + fim )// 2
		mergesort(array,inicio,meio)
		mergesort(array,meio+1,fim)
		merge(array,inicio,meio,fim)
	return array
#-------------------------------------------------------------------
def partition():

def quicksort(array,inicio,fim):
	if inicio < fim:
		q = partition(array,inicio,fim)
		quicksort(array,inicio,q)
		quicksort(array,q+1,fim)
	return array


array = [33, 12, 45,18, 69, 2, 20]
antes = time.time()
print ("Buble Sort O(n^2):     " + str(bublesort(array)) +" tempo: " + str(time.time() - antes))

array = [33, 12, 45,18, 69, 2, 20]
antes = time.time()
print ("Selection Sort O(n^2): " + str(selectionsort(array)) + " tempo: " + str(time.time() - antes))

array = [33, 12, 45,18, 69, 2, 20]
antes = time.time()
print ("Insertion Sort O(n^2): " + str(insertionsort(array)) + " tempo: " + str(time.time() - antes))

array = [33, 12, 45,18, 69, 2, 20]
antes = time.time()
print ("Merge Sort O(n log n): " + str(mergesort(array,0,len(array))) + " tempo: " + str(time.time() - antes))

array = [33, 12, 45,18, 69, 2, 20]
antes = time.time()
print ("Quick Sort O(n log n): " + str(quicksort(array,0,len(array))) + " tempo: " + str(time.time() - antes))
