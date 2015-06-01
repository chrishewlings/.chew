// basic random numbers

#include <iostream>
#include <cstdlib>
#include <ctime> // use system clock for seed entropy


using namespace std;

int i = 0;

int main()
{
	srand(time(0)); // seed the PRNG with local system time

	while (i < 100)
	{
		cout << rand() << "\t"; // rand uses ranges up to a constant in cstdlib called RAND_MAX
		i++;
	}
}