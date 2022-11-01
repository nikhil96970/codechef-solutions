#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int x,y,z;
	    cin>>x>>y>>z;
	    z-(y/x)<0?cout<<"0"<<endl:cout<<z-(y/x)<<endl;
	}
	return 0;
}
