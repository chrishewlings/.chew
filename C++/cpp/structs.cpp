//structs

/* this demonstrates the usage of the 'struct' keyword to create grouped variables
this is a precursor to actual object orientation
the data types within the structs can be varied however you'd like

*/
#include <iostream>
using namespace std;

struct Employee
{
	int badgeNumber;
	int age;
	float hourlyRate;
}; //don't forget a semicolon at the end of the declaration of a struct!

void PrintInfo(Employee id); // we'll come back to this later


int main()
{
	Employee chewlings; //create a variable of type Employee

	// assign values to member variables

	chewlings.badgeNumber = 168963;
	chewlings.age = 27;
	chewlings.hourlyRate = 10.0;

	cout << chewlings.badgeNumber  << endl;
	cout << chewlings.age  << endl;
	cout << chewlings.hourlyRate  << endl;
	
	PrintInfo(chewlings);

}

void PrintInfo(Employee id)
{
	cout << "Badge Number:  " << id.badgeNumber << endl;
	cout << "Age:  " << id.age << endl;
	cout << "Wage:  " << id.hourlyRate << endl;
}