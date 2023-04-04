import xml.etree.ElementTree as ET

"""
get model attributes "name","M","WS","BS","S","T","W","A","Ld","Save" from a battlescribe .cat file at https://github.com/BSData/wh40k
"""


    
    
xml_file = 'F:\BattleScribeData\Data\wh40k-master\Imperium - Grey Knights.cat'

unit_attributes = extract_model_attributes(xml_file)

# Print the attributes for the first weapon in the list
# print(weapon_attributes[0])
print(len(unit_attributes))
for i in unit_attributes:
    print(i)