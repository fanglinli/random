#include <vector>

// Sorts array of type T in ascending order
template <typename T> void bubbleSort(std::vector<T>& v) {
	int len = v.size();
	T temp;
	bool changedHuh = true;	

	for (typename std::vector<T>::iterator i = v.begin(); i != v.end(); ++i) {
		changedHuh = false;

		for (typename std::vector<T>::iterator j = v.begin() - 1; j != v.end(); ++j) {
			if (*i < *(j+1)) {			// Checks if current is larger than next
				temp = *i;				// If so, swap
				*i = *(j+1);
				*(j+1) = temp;
				changedHuh = true;
			}
		}

		if (!changedHuh) break;
	}	
}
