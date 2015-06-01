// pointers and const

#include <iostream>

using namespace std;

// pointers can be declared constant
int value = 5;
const int constValue = 10;
int *const varPtr = &value; // pointer is constant but value is not
const int* constPtr = &constValue; // both pointer and value are constant

int main()
{
	cout << value << endl;
	cout << *varPtr << endl;
	*varPtr = 6; // we expect this to fail, but it won't, because what it points *to* is not constant
	cout << *varPtr << endl;

	// now if we try to modify a pointer/value pair marked as constant, weird shit happens
	cout << constValue << endl;
	cout << *constPtr << endl;
	//*constPtr = 25; // *THIS* will _actually_ fail.
	return 0;
}