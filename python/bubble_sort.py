#Sorts array in increasing order
def bubble_sort(a):
	sortHuh = False
	length = len(a)

	while not sortHuh:								#While not sorted
		sortHuh = True
		for i in range (0,length-1):				
			if (a[i] > a[i+1]):						#If current is larger than next
				a[i], a[i+1] = a[i+1], a[i]			#Swap
				sortHuh = False
