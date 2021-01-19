#! /bin/bash


go build -o AES-CBC.exe NewCBCDecrypter.go 
ciphertext=$(xxd -p ../Logs/one.log | head -n 2 | tr -d '\n' | cut -c1-64) 
echo $ciphertext
cat in2.txt | awk '{print $2}' | tr -d '\n' | ./tryall |
while read -r key
do
  plain=$(./AES-CBC.exe "$key" "$ciphertext")
  echo "plain: $plain"
  if [[ $plain == "\$GP"* ]]
  then
    echo "\n\n\n\n----------------------------------------" 
    printf "\n\n\n$plain\n\n\n"
    printf "KEY: $key\n\n\n"
    echo "----------------------------------------" 
    exit
  fi 
done 





