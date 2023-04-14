#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int n;
	cin>>n;
	while(n--){
	    int a,b;
	    cin>>a>>b;
	    if(a+b<=6){
	        cout<<"NO"<<endl;
	    }
	    else
	        cout<<"YES"<<endl;
	}

	return 0;
}
