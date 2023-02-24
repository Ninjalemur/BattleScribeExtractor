import xml.etree.ElementTree as ET

def extract_unit_attributes(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    unit_attributes = []
    for unit in root.findall(".//*[@typeName='Unit']"):
        name = unit.get('name')
        move = unit.find(".//*[@name='M']").text
        weapon_skill = unit.find(".//*[@name='WS']").text
        ballistic_skill = unit.find(".//*[@name='BS']").text
        strength = unit.find(".//*[@name='S']").text
        toughness = unit.find(".//*[@name='T']").text
        wounds = unit.find(".//*[@name='W']").text
        attacks = unit.find(".//*[@name='A']").text
        leadership = unit.find(".//*[@name='Ld']").text
        save = unit.find(".//*[@name='Save']").text
        unit_attributes.append({'name': name, 'M': move, 'WS': weapon_skill, 'BS': ballistic_skill, 'S': strength, 'T': toughness, 'W': wounds, 'A': attacks, 'Ld': leadership, 'Save': save})
    return unit_attributes

def extract_weapon_attributes(xml_file):
    root = ET.parse(xml_file).getroot()

    weapon_attributes = []
    for weapon in root.findall(".//*[@typeName='Weapon']"):
        name = weapon.get('name')
        range_ = weapon.find(".//*[@name='Range']").text
        weapon_type = weapon.find(".//*[@name='Type']").text
        strength = weapon.find(".//*[@name='S']").text
        ap = weapon.find(".//*[@name='AP']").text
        damage = weapon.find(".//*[@name='D']").text
        abilities = weapon.find(".//*[@name='Abilities']").text
        weapon_attributes.append({'name': name, 'Range': range_, 'Type': weapon_type, 'S': strength, 'AP': ap, 'D': damage, 'Abilities': abilities})
    return weapon_attributes
    
xml_file = 'F:\BattleScribeData\Data\wh40k-master\Imperium - Grey Knights.cat'
# weapon_attributes = extract_weapon_attributes(xml_file)

# # Print the attributes for the first weapon in the list
# # print(weapon_attributes[0])
# print(len(weapon_attributes))
# for i in weapon_attributes:
#     print(i)

unit_attributes = extract_unit_attributes(xml_file)

# Print the attributes for the first weapon in the list
# print(weapon_attributes[0])
print(len(unit_attributes))
for i in unit_attributes:
    print(i)