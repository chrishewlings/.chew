#include <iostream>
#include <string>
using namespace std;






int main(){
	int age;
	string realname;  
	string username;
	printf("How old? ");
	cin >> age; 
	printf("Real name? ");
	cin >> realname;
	printf("user name? ");
	cin >> username;  
	printf("\nYour age is: %d\n", age);
	printf("Your realname is: %s\n", realname.c_str());
	printf("Your username is: %s\n", username.c_str());
	return 0;

}