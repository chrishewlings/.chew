// more control flow

#include <iostream>
using namespace std;

int main()
{
	// there are also while loops

	int i = 0;
	
	while (i < 5)
	{
		cout << "while looped " << i + 1 << " times." << endl;
		i++; // we need to increment the variable within the loop or else bad things
		// you can also conditionally use 'break' keyword to break out of infinite loops
	}

	// there are also do while statements, which guarantees at least one execution
	// even if the condition is false
	int j = 0;
	do
	{
		cout << "say something" << endl;
	} while (j != 0);

	// finally for loops, which are easy
	int k;
	for (k = 0; k < 5; k++)
	{
		cout << "for looped " << k + 1 << " times." << endl;
	}

	// n.b. there is also a 'continue' keyword opposite to break
	// which short circuits the loop and executes the next iteration
	return 0;
}