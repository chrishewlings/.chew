#include <iostream>
#include "constants.h"
#include <iomanip>

using namespace std;


void printThings()
{
	cout << setprecision(16);
	cout << Constants::pi << endl;
	cout << Constants::e << endl;
	cout << Constants::root_two << endl;
}

int main()
{
	printThings();
	return 0;
}