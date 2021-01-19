#include <bits/stdc++.h> 
using namespace std; 
int main(){
  string s;
  while(cin>>s)
    for(int i=0;i<s.length()-8+1;i++){
      for(int j=0;j<4;j++)
        cout<<s.substr(i,8);
      cout<<'\n';
    }
}
