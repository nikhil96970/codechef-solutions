#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	int n1,n2,p1=0,p2=0;
	int winner=0,lead=0;
	cin>>t;
	while(t--){
	    cin>>n1>>n2;
	    p1=p1+n1;
	    p2=p2+n2;
	    int x=abs(p2-p1);
	    if(x>lead){
	        lead=x;
	        p1>p2?winner=1:winner=2;
        }
	    
	}
	cout<<winner<<" "<<lead<<endl;
	return 0;
}
