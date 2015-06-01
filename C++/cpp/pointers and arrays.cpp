// pointers, arrays, and pointer arithmetic

#include <iostream>
using namespace std;

int anArray[5] = {3,4,9,11,52} ; // define an array
int* dumbPointer;
// anArray is actually a pointer that points to the first element, anArray[0]

int main()
{
	cout << *anArray; // this prints the first element of anArray
	*anArray = *(anArray+1); // adding one to the location points to the next element. the brackets are to ensure +1 happens before *
	cout << *anArray;
	cout << endl << endl;
	
	// in standard C, pointer arithmetic is often used to loop through arrays

	char stringArray[] = "chewlings";
	int arraySize = sizeof(stringArray) / sizeof(stringArray[0]);
	for (char *stringArrayPtr = stringArray; stringArrayPtr < stringArray + arraySize; stringArrayPtr++)
		cout << *stringArrayPtr; // this convoluted ass loop uses a pointer to 'walk' along stringArray
	return 0;
}