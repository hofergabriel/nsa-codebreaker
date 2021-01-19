#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <string>
#include <iostream>
using namespace std;

int main(){

  string aescbc = "./AES-CBC.exe ";
  string hex_str2;
  string ciphertext="57a35e6a18336748833398b8b5f75433c784ed5aa2b462ad10f7135f5f5f900b";
  string arg;
  char plain[10000];
  char hex_str[33];

  for(unsigned int i=0x0 ; i<=0xffffffff; i++){
    sprintf(hex_str, "%08x%08x%08x%08x",i,i,i,i);

    hex_str2=hex_str; 

    cout<<hex_str<<endl;

    arg = aescbc + hex_str2 + " " + ciphertext + " ";

    FILE * fp = popen(arg.c_str(), "r");
    fscanf(fp, "%s", plain);
    cout << plain << endl;
    pclose(fp);

    if(i==0xffffffff) break;
    //system(arg.c_str());
  }
}





