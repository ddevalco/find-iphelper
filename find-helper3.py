# Script to find what interfaces have an "ip helper-address"
# Uses ciscoconfparse library, make sure its installed
#Importing the necessary modules.
import os
from ciscoconfparse import CiscoConfParse
os.chdir("c:\\configs")
for filename in os.listdir(os.getcwd()):
    parse = CiscoConfParse(filename, factory=True, syntax='ios')
    obj_list = parse.find_objects_dna(r'Hostname')
    inf_w_help = parse.find_parents_w_child(parentspec=r"^interface", childspec=r"ip helper-address")
    hostn = obj_list[0].hostname
    print hostn
    for interface in inf_w_help:
        print interface

    print("Write results to file...")
    newconfig = CiscoConfParse([])
    newconfig.append_line(hostn)
    for interface in inf_w_help:
        newconfig.append_line(interface)
        newconfig.append_line('ip helper-address my.new.ip.add1')
    newconfig.commit()
    newconfig.save_as(hostn + '_newconfig.txt')