#include <iostream>
#include <iomanip>

// thing to approximate value of pi


using namespace std;

double piVar = 4.0;
double pi = 3.1415926535897932384;

int main ()
{
	double x = 3.0;
	int i;
	for (i = 0; i < 5000000; i++){
		piVar = piVar - (4.0/x) + (4.0/(x+2));
		x = x + 4;
		cout << setprecision(15) << piVar << endl;
	}
	double variance = ((piVar - pi) / 100);
	cout << endl << endl << variance << endl;
}