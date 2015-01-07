#include <iostream>

using namespace std;

unsigned long long squareVar = 1;
unsigned long long x = 3;

int main () 
{
	int i;
	for (i = 1; i < 1000000; i++)
		{
		squareVar = squareVar + x;
		x = x + 2;
		cout << squareVar << endl;
		}
}