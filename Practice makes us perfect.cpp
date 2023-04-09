#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int i ;
	int a[4];
	int c=0;
	for(i=0;i<4;i++)
	{
	    cin>>a[i];
	}
	for(i=0;i<4;i++)
	{
	    if(a[i]>=10)
	        c++;
	        
	}
	cout<<c<<endl;
	return 0;
}
