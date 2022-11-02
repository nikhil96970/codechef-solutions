#include <bits/stdc++.h>
using namespace std;

void solve()
{
    int n,k;
    cin >> n >> k;
    int arr[n];
    
    for(int i = 0; i<n ; i++)
    {
        cin >> arr[i];
    }
    int count = 0;
    for(int i = 0; i<n ; i++)
    {
        if(arr[i] > k)
        {
            count++;
        }
    }
    cout << count << endl;
}

int main() {
    
    int t;
    cin>>t;
    
    while(t--)
    {
        solve();
    }
	
	return 0;
}
