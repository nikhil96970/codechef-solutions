#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--)
	{
	    int l,r;
	    cin>>l>>r;
	    int c=0;
	    for(int i=l;i<=r;i++)
	    {
	        if((i%10==2)||(i%10==3)||(i%10==9))
	        c++;
	    }
	        cout<<c<<endl;
	}
	return 0;
}
