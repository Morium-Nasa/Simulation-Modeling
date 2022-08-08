#include <iostream>
#include<math.h>
using namespace std;
int myrandomint(int x, int a, int c, int m)
{
    int xi = (a*x + c) % m;
    return xi;
}
int main()
{   int x,a,c,m,n;
   cout << "Enter the value of x :" << endl;
    cin >> x;
    cout << "Enter the value of a :" << endl;
    cin >> a;
    cout << "Enter the value of c :" << endl;
    cin >> c;
    cout << "Enter the value of m :" << endl;
    cin >> m;
    cout << "Enter how many random number :" << endl;
    cin >> n;
    int i;
    for(i=0; i<n; i++)
    {
        x = myrandomint(x, a, c, m);
        double r = (double)x/(double)m;
        cout<<r;
    }
  return 0;
}
