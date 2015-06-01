//typedefs

#include <iostream>
using namespace std;

typedef long miles; // define miles as an alias for keyword 'long'

miles tripDistance = 800; //here it is clear that the value assigned is in miles

// helpful for documentation and legibility/comprehensibility
// also useful for changing the underlying type of many variables quickly

/* 
they are also commonly used to allow platform specific implementations
let's say if a system uses an 8bit int by default; but another uses 16bits;
one can do this to make sure there is no ambiguity: */

typedef char int8;
typedef int int16;
typedef long int64;

int8 eightBitInteger = 1;
int16 thirtytwoBitInteger = 1;
int64 sixtyfourBitInteger = 1;

int main()
{
	cout << sizeof(eightBitInteger) << " bytes, therefore this integer is " << 8 * sizeof(eightBitInteger) << " bits long." << endl;
	cout << sizeof(thirtytwoBitInteger) << " bytes, therefore this integer is " << 8 * sizeof(thirtytwoBitInteger) << " bits long." << endl; 
	cout << sizeof(sixtyfourBitInteger) << " bytes, therefore this integer is " << 8 * sizeof(sixtyfourBitInteger) << " bits long." << endl;
}