#include <iostream>
using namespace std;
int main() {
	int T;
	cin>>T;
	while(T--){
	    int N;
	    cin>>N;
	    string arr[N];
	    for(int i=0; i<N; i++){
	        cin>>arr[i];
	    }
	   int count1=0; int count2=0;
	    for(int i=0; i<N; i++){
	        if(arr[i]=="START38"){
	          count1++;  
	        }else if(arr[i]=="LTIME108"){
	            count2++;
	        }
	    }
	    cout<<count1<<" "<<count2<<endl;
	}
	return 0;
}
