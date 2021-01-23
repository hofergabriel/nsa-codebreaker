#! /bin/bash


key1='4e4e325753544b46465656554b3543504f4a5646533452514a5a32484b553244'
key2='49593457345642554b424155365154454a4a3355345252574f4a425736513344'
key3='473557444152424e494e575536354b324e353257455243374b4e59555333534f'
key4='4a4a3248515453554a4641564151324a50423244414e42564d46484743594b44'

key='6eb7d794c1a6d861f282017e5436ca44f7b22550cd2f5556a80c44cf00ac3ce0'


go build -o AES-CBC.exe NewCBCDecrypter.go 
ciphertext1=$(xxd -p ../../Logs/one.log | head -n 10 | tr -d '\n' | cut -c1-256) 
ciphertext2=$(xxd -p ../../Logs/two.log | head -n 10 | tr -d '\n' | cut -c1-256) 
ciphertext3=$(xxd -p ../../Logs/thr.log | head -n 10 | tr -d '\n' | cut -c1-256) 
ciphertext4=$(xxd -p ../../Logs/fou.log | head -n 10 | tr -d '\n' | cut -c1-256) 

plain1=$(./AES-CBC.exe "$key" "$ciphertext1" | hexdump -C)
plain2=$(./AES-CBC.exe "$key" "$ciphertext2" | hexdump -C)
plain3=$(./AES-CBC.exe "$key" "$ciphertext3" | hexdump -C)
plain4=$(./AES-CBC.exe "$key" "$ciphertext4" | hexdump -C)
echo "$plain1" ; echo ; echo
read
echo "$plain2" ; echo ; echo
read
echo "$plain3" ; echo ; echo
read
echo "$plain4" ; echo ; echo

exit





## cat in2.txt | awk '{print $2}' | tr -d '\n' | ./tryall |
## while read -r key
## do
##   plain=$(./AES-CBC.exe "$key" "$ciphertext")
##   echo "plain: $plain"
##   if [[ $plain == "\$GP"* ]]
##   then
##     echo "\n\n\n\n----------------------------------------" 
##     printf "\n\n\n$plain\n\n\n"
##     printf "KEY: $key\n\n\n"
##     echo "----------------------------------------" 
##     exit
##   fi 
## done 





