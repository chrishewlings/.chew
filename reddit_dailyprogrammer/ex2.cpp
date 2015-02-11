#include "iostream"
#include "string"

using namespace std;

int main(){
	float force, mass, acceleration;
	printf("Enter the value for mass: \n>> ");
	cin >> mass;
	printf("Enter the value for acceleration: \n>> ");
	cin >> acceleration;
	force = mass * acceleration;
	printf("The acceleration is %f\n", acceleration);
}