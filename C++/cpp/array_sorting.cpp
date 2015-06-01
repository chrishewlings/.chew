// sorting with selection sort

#include <iostream>
#include <algorithm>

int anUnsortedArray[] = {0, 90, 30, 25, 60, 42, 80, 30, 90};
int arrayLength = sizeof(anUnsortedArray) / sizeof(anUnsortedArray[0]);
int main()
{
	using namespace std;
	
	for (int startIndex = 0; startIndex < arrayLength; startIndex++)
	{
		int smallestIndex = startIndex;
	
		for (int currentIndex = startIndex + 1; currentIndex < arrayLength; currentIndex++)
		{
			if (anUnsortedArray[currentIndex] < anUnsortedArray[smallestIndex])
				smallestIndex = currentIndex;
		}
	swap(anUnsortedArray[startIndex], anUnsortedArray[smallestIndex]);
	for( int i = 0; i < arrayLength; i++)
	{
		cout << anUnsortedArray[i] << "\t";
		if (i == arrayLength - 1)
		{
			cout << endl;
		}
	}
	}




}

