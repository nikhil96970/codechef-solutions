#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--)
	{
	    int p=0;
	    int k;
	    cin>>k;
	    for(int i=1;i<=k;i++)
	    {
	        if(i%2==0) p-=1;
	        else p+=3;
	        
	    }
	    cout<<p<<endl;
	}
	return 0;
}
