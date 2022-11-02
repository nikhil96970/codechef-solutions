#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        long long int n;
        cin >> n;
        int arr[n];
        for(int i = 0;i < n;i++){
            cin>>arr[i];
        }
        sort(arr,arr+n);
        int mx = 1;
        int basi = 1;
        for(int i = 0;i < n-1;i++){
            if(arr[i] == arr[i+1]){
                basi++;
            }
            else if(basi > mx)
            {
                mx = basi;
                basi = 1;
            }
            else
            {
                basi = 1;
            }
        }
        if (basi > mx)
        {
            mx = basi;
        }
        
        cout<<(n - mx)<<endl;
    }
    return 0;
}
