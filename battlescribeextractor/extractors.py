import pandas as pd
import xml.etree.ElementTree as ET
import os

def FolderExtractor(
    input_folder,
    model_outputfile="./model_data.tsv",
    weapon_outputfile="./weapon_data.tsv",
    verbose = True
    ):
    """
    Extracts Model and Weapon data from BattleScribe .cat files in a folder and writes them to an output files
    
    Parameters:
        folder : folder path
            path to folder containing BattleScribe .cat files
        model_outputfile : file path
            path of desired model output file
        weapon_outputfile : file path
            path of desired weapon output file
    """
    #check if input is a folder
    if not os.path.isdir(input_folder):
        raise TypeError("Only folder inputs are allowed")

    
    for (root,dirs,files) in os.walk(input_folder):
        for file in files:
            if file.lower().endswith(('.cat')):
                if verbose:
                    print("processing file: {root}\{file}".format(root=root,file=file))
                catalogue_name = file[:-4]
                model_data, weapon_data = FileExtractor(root+"/"+file)
                # model_data['catalogue_name'] = catalogue_name
                # weapon_data['catalogue_name'] = catalogue_name
                model_data.insert(loc=0,column ="catalogue_name",value = len(model_data.axes[0])*[catalogue_name])
                weapon_data.insert(loc=0,column ="catalogue_name",value = len(weapon_data.axes[0])*[catalogue_name])
                try:
                    cumulative_model_data
                except NameError:
                    cumulative_model_data = model_data
                else:
                    cumulative_model_data = pd.concat([cumulative_model_data,model_data])
                try:
                    cumulative_weapon_data
                except NameError:
                    cumulative_weapon_data = weapon_data
                else:
                    cumulative_weapon_data = pd.concat([cumulative_weapon_data,weapon_data])
            else:
                continue
    
    cumulative_model_data.to_csv(model_outputfile,sep="\t",index=False)
    cumulative_weapon_data.to_csv(weapon_outputfile,sep="\t",index=False)


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
    profile_stats_to_get = ["M","WS","BS","S","T","W","A","Ld","Save","pts"],
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
    pass

def ModelExtractorSharedProfile(
    root_element,
    profile_stats_to_get = ["M","WS","BS","S","T","W","A","Ld","Save","pts"],
    nullValue = ""
    ):
    """
    Extracts model data from ShareProfles section of an XML Elements object and returns it as a DataFrame

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
    profile_stats_to_get = ["Range","Type","S","AP","D","Abilities","pts"],
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
    pass

def WeaponExtractorSharedProfile(
    root_element,
    profile_stats_to_get = ["Range","Type","S","AP","D","Abilities","pts"],
    nullValue = ""
    ):
    """
    Extracts weapon data from SharedProfiles section of an XML Elements object and returns it as a DataFrame

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

def WeaponExtractorSharedSelectionEntry(
    root_element,
    profile_stats_to_get = ["Range","Type","S","AP","D","Abilities","pts"],
    nullValue = ""
    ):
    """
    Extracts weapon data from SharedProfiles section of an XML Elements object and returns it as a DataFrame

    Parameters:
        root_element : xml root object
            xml root object from etree
        profile_stats_to_get : list
            list of stats other than name to get from sharedProfiles > profile > characteristics
        nullValue : any
            value to use if value for characteristic is not found
    """
    collated_profile_stats =[]
    for sharedSelectionEntry in root_element.iter('{http://www.battlescribe.net/schema/catalogueSchema}sharedSelectionEntries'):
        for profiles in sharedSelectionEntry.iter('{http://www.battlescribe.net/schema/catalogueSchema}profiles'):
            for profile in profiles.iter('{http://www.battlescribe.net/schema/catalogueSchema}profile'):
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
        for costs in sharedSelectionEntry.iter('{http://www.battlescribe.net/schema/catalogueSchema}costs'):
            for cost in costs.iter('{http://www.battlescribe.net/schema/catalogueSchema}cost'):
                costName = cost.attrib["name"]
                costValue = cost.attrib["value"]
                recorded_stats[costName] =  costValue
        for stat in profile_stats_to_get:
            try:
                profile_stats[stat] = recorded_stats[stat]
            except KeyError:
                profile_stats[stat] = nullValue
        collated_profile_stats.append(profile_stats)
    return(pd.DataFrame.from_records(collated_profile_stats))


                
            
    
            


