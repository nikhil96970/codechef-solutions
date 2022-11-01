#include <iostream>

using namespace std;



int main() {

int n,x,y;

cin>>n;

while(n--){

    cin>>x;

    if(x%3==0)

    {

        cout<<"0\n";

    }

    else

    {

    y=(x/3)+1;

    cout<<y*3-x<<endl;

    }

    

}

	return 0;

}
