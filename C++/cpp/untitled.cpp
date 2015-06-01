// basic random numbers

#include <iostream>
#include <cstdlib>

using namespace std;
int i = 0;
int main()
{
	srand(2236); // seed the PRNG

	while (i < 100)
	{
		cout << rand() << "\t";
		i++
	}
}