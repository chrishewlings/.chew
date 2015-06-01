// structs part two

#include <iostream>
using namespace std;

//declarations
struct Employee
{
	int badgeNumber;
	int age;
	float hourlyRate;
};

struct Company
{
	Employee sCEO;
	int numberOfEmployees;
};

void PrintInfo(Employee id);

// structs can be nested inside each other





int main()
{


	// now we can initalize each member variable individually
	// which is annoying as fuck

	// ORRRRRR
	Employee chewlings = {168963, 27, 10.0}; // initialize all variables in order
	PrintInfo(chewlings);

	Company fruitStand = {{168963, 27, 10.0}, 5}; // even nested initialization!
	cout << fruitStand.sCEO.badgeNumber;
}

//functions

void PrintInfo(Employee id)
{
	cout << "Badge Number:  " << id.badgeNumber << endl;
	cout << "Age:  " << id.age << endl;
	cout << "Wage:  " << id.hourlyRate << endl;
}