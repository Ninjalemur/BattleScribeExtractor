import pandas as pd
import xml.etree.ElementTree as ET

def FolderExtractor(
    folder,
    outputfile="./output.tsv"
    ):
    """
    Extracts Model and Weapon data from BattleScribe .cat files in a folder and writes them to an output file
    
    Parameters:
        folder : folder path
            path to folder containing BattleScribe .cat files
        outputfile : file path
            path of desired output file
    """
    pass

def FileExtractor(
    input_file
    ):
    """
    Extracts Model and Weapon data from BattleScribe .cat file returns model and weapon data
    
    Parameters:
        input_file : file path
            path to BattleScribe .cat file
    Returns
        model_data : DataFrame
            dataframe containing model data
        weapon_data : DataFrame
            dataframe containing weapon data
    """
    tree = ET.parse(input_file)
    root = tree.getroot()

    model_data = ModelExtractor(root)
    weapon_data = WeaponExtractor(root)

    return(model_data, weapon_data)

def ModelExtractor(
    root_element,
    profile_stats_to_get = ["M","WS","BS","S","T","W","A","Ld","Save"],
    nullValue = ""
    ):
    """
    Extracts model data from an XML Elements object and returns it as a DataFrame

    Parameters:
        root_element : xml root object
            xml root object from etree
        profile_stats_to_get : list
            list of stats other than name to get from sharedProfiles > profile > characteristics
        nullValue : any
            value to use if value for characteristic is not found
    Returns:
        DataFrame
            dataframe that contains name and stats from profile_stats_to_get
    """
    
    collated_profile_stats =[]
    for sharedProfile in root_element.iter('{http://www.battlescribe.net/schema/catalogueSchema}sharedProfiles'):
        for profile in sharedProfile.iter('{http://www.battlescribe.net/schema/catalogueSchema}profile'):
                if profile.attrib["typeName"] == "Unit":
                    profile_stats = {}
                    unitName = profile.attrib["name"]
                    profile_stats['name']= unitName

                    recorded_stats = {}
                    for characteristics in profile.iter('{http://www.battlescribe.net/schema/catalogueSchema}characteristics'):
                        for characteristic in profile.iter('{http://www.battlescribe.net/schema/catalogueSchema}characteristic'):
                            characteristicName = characteristic.attrib["name"]
                            characteristicValue = characteristic.text
                            recorded_stats[characteristicName] =  characteristicValue
                    for stat in profile_stats_to_get:
                        try:
                            profile_stats[stat] = recorded_stats[stat]
                        except KeyError:
                            profile_stats[stat] = nullValue
                    collated_profile_stats.append(profile_stats)
    return(pd.DataFrame.from_records(collated_profile_stats))




def WeaponExtractor(
    root_element,
    profile_stats_to_get = ["Range","Type","S","AP","D","Abilities"],
    nullValue = ""
    ):
    """
    Extracts weapon data from an XML Elements object and returns it as a DataFrame

    Parameters:
        root_element : xml root object
            xml root object from etree
        profile_stats_to_get : list
            list of stats other than name to get from sharedProfiles > profile > characteristics
        nullValue : any
            value to use if value for characteristic is not found
    """
    collated_profile_stats =[]
    for sharedProfile in root_element.iter('{http://www.battlescribe.net/schema/catalogueSchema}sharedProfiles'):
        for profile in sharedProfile.iter('{http://www.battlescribe.net/schema/catalogueSchema}profile'):
                if profile.attrib["typeName"] == "Weapon":
                    profile_stats = {}
                    unitName = profile.attrib["name"]
                    profile_stats['name']= unitName

                    recorded_stats = {}
                    for characteristics in profile.iter('{http://www.battlescribe.net/schema/catalogueSchema}characteristics'):
                        for characteristic in profile.iter('{http://www.battlescribe.net/schema/catalogueSchema}characteristic'):
                            characteristicName = characteristic.attrib["name"]
                            characteristicValue = characteristic.text
                            recorded_stats[characteristicName] =  characteristicValue
                    for stat in profile_stats_to_get:
                        try:
                            profile_stats[stat] = recorded_stats[stat]
                        except KeyError:
                            profile_stats[stat] = nullValue
                    collated_profile_stats.append(profile_stats)
    return(pd.DataFrame.from_records(collated_profile_stats))


                
            
    
            


