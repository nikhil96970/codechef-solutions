#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t,a,b;
	cin>>t;
	while(t--){
	    cin>>a>>b;
	    if(b>(a*5)){
	        cout<<"NO"<<endl;
	    }
	    else{
	        cout<<"YES"<<endl;
	    }
	}
	return 0;
}
