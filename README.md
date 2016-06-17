# find-iphelper
Python script to find all interfaces with ip helper and replace with new

Script will search for all interfaces with an ip helper-address

It will look in the folder c:\configs for multiple config files

It will parse each config file seperately finding the hostname
and the interfaces with the ip helper-address configured

It will then output it's findings on screen and create new config
files in the configs folder that include:

hostname
interfacename
ip helper-address my.new.ip.add

It will save each new config file using hostname+_newconfig.txt
