#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t; cin>>t;
	while(t--)
	{
	    int n,i=2; cin>>n;
	    while(n--)
	    {
	        i++;
	        if(i==4) i=1;
	        
	    }
	    if(i==1) cout<<"SMALL"<<endl;
	    else if(i==2) cout<<"NORMAL"<<endl;
	    else cout<<"HUGE"<<endl;
	}
	return 0;
}
