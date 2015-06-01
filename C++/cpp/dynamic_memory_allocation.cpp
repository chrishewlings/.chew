// dynamic memory allocation

#include <iostream>

using namespace std;

// allocate a single variable dynamically

int *newValue = new int; // dynamically allocate an integer using 'new' keyword
						 // the 'new' operator returns the address of the variable
						 // that has been allocated. then deref the ptr to access the variable



int main()
{
	*newValue = 10;
	cout << *newValue;
	
	delete newValue; // delete keyword marks it for reassignment
	cout << *newValue; // THIS IS BAD. newValue still has a value although it may be changed dynamically at random
	*newValue = 0x0; // returns value to null, explicit dereferencing
	cout << *newValue;

	// if you have a pointer pointing to memory that has been deallocated, bad things will happen. srs.

	// n.b. avoid creating 'new' values without corresponding 'delete', as it will cause memory leaks
	return 0;
}