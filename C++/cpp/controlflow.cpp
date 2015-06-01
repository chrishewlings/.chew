// control flow

#include <cstdlib>
#include <iostream>

using namespace std;

int main()
{
	//cout << "This next line will halt the entire program.";
	//exit(1); // simplest control flow is killing execution

	// conditionals are another kind of flow control

	cout << "Enter a number: ";
	int userAnswer = 15;
	
	if (userAnswer > 10)
		cout << userAnswer << " is greater than 10" << endl;
	else
		cout << userAnswer << " is not greater than 10" << endl;

	// so are switch/case statements
	int x = 5;
	switch(x)
	{
		case 3:
			cout << "the number is three";
			break; // break is necessary to avoid fallthrough
		case 4:
			cout << "the number is four";
			break;
		case 5:
			cout << "the number is five";
			break;
	}

	// there are also goto statements
	int i = 1;

	tryAgain:
		cout << "did something";

		if(i != 1)
			goto tryAgain; // this sucks, don't do it


	return 0;
}