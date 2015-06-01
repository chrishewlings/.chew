// arrays

#include <iostream>
using namespace std;


int array_testScores[30]; // define an array of 30 integers
int array_things[] = { 0, 1, 2, 3, 4, 5 }; // a less boring way to initialize an array

// clever way to find out the number of elements in an array
int numThings = sizeof(array_things) / sizeof(array_things[0]); 


// n.b. arrays need to be declared with constant size, known at compile time
int i;

int main()
{
	array_testScores[0] = 30;
	array_testScores[1] = 30;
	array_testScores[2] = 30;

	cout << array_testScores[0] << endl << endl;

	for (i = 0; i < numThings; i++) // loop through an array
	{
		cout << array_things[i] << endl;
	}

	// use enums to keep track of array values for fun and profit
	enum StudentNames
	{
		KENNY,
		KYLE,
		STAN,
		MAX_STUDENTS
	};

	int spTestScores[MAX_STUDENTS];
	spTestScores[KYLE] = 76;
	// is equivalent to spTestScores[1]
	cout << spTestScores[KYLE] << endl;
	cout << spTestScores[1] << endl;


	
}