// c style strings

#include <iostream>
#include <string>
using namespace std;

// c style strings are just arrays of chars, null terminated

char shittyOldString[] = "this is a C style string.";
string usefulString = "this is a C++ style string.";
int main()
{
	for (int i = 0; i < sizeof(shittyOldString) - 1; i++) // loop over the string to print it
		cout << shittyOldString[i];
	cout << endl;
	//however, c style strings are horrible and should be avoided
	cout << usefulString << endl; // wasn't that easier?
	// interactivity and flexibility way easier as well
	string userString;
	getline(cin, userString); // takes a full string including whitespace (except CR/LF)
	cout << userString << endl;

}