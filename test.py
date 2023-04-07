import xml.etree.ElementTree as ET
import battlescribeextractor as bse
import sys
import time
import pandas as pd

"""
get model attributes "name","M","WS","BS","S","T","W","A","Ld","Save" from a battlescribe .cat file at https://github.com/BSData/wh40k
"""


    
    
xml_file = 'F:\BattleScribeData\Data\wh40k-master\Imperium - Grey Knights.cat'

tree = ET.parse(xml_file)
root = tree.getroot()
unit_attributes = bse.ModelExtractor(root)

# Print the attributes for the first weapon in the list
# print(weapon_attributes[0])
print(len(unit_attributes))
for i in unit_attributes:
    print(i)