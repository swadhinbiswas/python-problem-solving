#include<bits/stdc++.h>
using namespace std;
int main()
{

    int i,n,s=0;
    cin >> n;
    int cnt=0;
    for(i=1;i<=sqrt(n);i++)
    {
        if(n%i==0)
        {
            if(i==n/i) cnt++;
            else{
                cnt+=2;
            }
        }
    }
    cout << cnt-1 << endl;

    return 0;
}