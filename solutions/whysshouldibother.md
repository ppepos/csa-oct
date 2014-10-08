# whysshouldibother

Open the .pcap file in wireshark. Search all packets for the string `flag` in packet bytes. You will find a few
interesting packets but the interesting one is the FTP-Data stream. You can right click packet 413 and follow TCP
stream. You can see that the first few bytes are the magic numbers for a `.zip` file. `Save as...` and export it to
anything.zip and unzip it. There is a .png file in there with the flag.
