// pointers. ofuck. 

// pointers are declared with an asterisk
// and many syntaxes are acceptable by the compiler

#include <iostream>

using namespace std;

int *integer_pointer;
double* double_pointer;
float * float_pointer; // all of these are valid pointers!

int testValue = 5;
int *value_pointer = &testValue; // & assigns the memory address of value to value_pointer

int main()
{
	cout << *value_pointer << " is the value of testValue, pointed to by value_pointer;" << endl;
	cout << value_pointer << " is the address value_pointer points to." << endl;
	cout << endl;
	cout << &testValue << " is the address of testValue." << endl;

	// pointers can also be reassigned like other variables
	// we can even make them point to null by pointing to address 0 

	int *nullPtr;
	nullPtr = NULL;
	cout << nullPtr << " is the null pointer memory location" << endl;

	// a null pointer is also useful as a boolean
	if (!nullPtr)
		cout << "nullPtr is indeed, pointed at null." << endl;


	return 0; 
}