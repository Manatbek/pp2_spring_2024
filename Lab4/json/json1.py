import json

jsontime = open('example.json').read()

json_object = json.loads(jsontime)
print(
    "=======================================================================================" "\n"
    "DN                                                 Description           Speed    MTU" "\n" 
    "-------------------------------------------------- --------------------  ------  ------")
imtime = json_object["imdata"]
for i in imtime:
        dn = i["l1PhysIf"]["attributes"]["dn"]
        descr = i["l1PhysIf"]["attributes"]["descr"]
        speed = i["l1PhysIf"]["attributes"]["speed"]
        mtu = i["l1PhysIf"]["attributes"]["mtu"]
        
        print("{0:50} {1:20} {2:7} {3:6}".format(dn,descr,speed,mtu))