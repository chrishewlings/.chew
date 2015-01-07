#include <iostream>


using namespace std;


int main () 
{
	unsigned long long int i;
	unsigned long long int x;
	for (i = 1; i < 1000000; i++)
		{
		x = i * i;
		cout << x << endl;
		}
}