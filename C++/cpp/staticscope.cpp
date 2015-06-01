//variable scoping and static keyword

#include <iostream>

void IncrementAndPrint()
{
	using namespace std;
	static int staticValue = 1;
	++staticValue;
	cout << staticValue << endl;
}

int main()
{
	IncrementAndPrint();
	IncrementAndPrint();
	IncrementAndPrint();
}