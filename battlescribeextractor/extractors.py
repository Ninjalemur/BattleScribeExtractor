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
            if file.lower().endswith(('.cat')) or file.lower().endswith(('.gst')):
                if verbose:
                    print("processing file: {root}/{file}".format(root=root,file=file))
                catalogue_name = file[:-4]
                model_data, weapon_data = FileExtractor(input_file=root+"/"+file)
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
    
    cumulative_model_data.drop_duplicates(subset='name',keep='first',inplace=True)
    cumulative_model_data.to_csv(model_outputfile,sep="\t",index=False)

    cumulative_weapon_data.drop_duplicates(subset='name',keep='first',inplace=True)
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
    profile_stats_to_get = ["M","WS","BS","S","T","W","A","Ld","Save"],
    points_string = "pts",
    nullValue = ""
    ):
    """
    Extracts model data from an XML Elements object and returns it as a DataFrame. Iterates over entryLinks in root element and calls SelectionEntryUnitExtractor to extract data from selectionEntries referenced by each entryLink.

    Parameters:
        root_element : xml root object
            xml root object from etree
        profile_stats_to_get : list
            list of stats other than name to get from sharedProfiles > profile > characteristics
        points_string : string
            string used to denote points cost in xml file. Will also be used for dataframe header
        nullValue : any
            value to use if value for characteristic is not found
    Returns:
        DataFrame
            dataframe that contains name and stats from profile_stats_to_get
    """
    namespace = root_element.tag.split("}")[0]+"}"

    
    collated_profile_stats =[]
    for sharedSelectionEntries in root_element.findall(namespace+'sharedSelectionEntries'):
        for selectionEntry in sharedSelectionEntries.findall(namespace+'selectionEntry'):
            # print("checking selectionEntry: "+selectionEntry.attrib["name"])
            if selectionEntry.attrib["type"] != "unit" and selectionEntry.attrib["type"] != "model":
                # print("selectionEntry: "+selectionEntry.attrib["name"]+" is neither a unit nor a model")
                continue
            else:
                collated_profile_stats += SelectionEntryUnitExtractor(selectionEntry,namespace,root_element,profile_stats_to_get,points_string,nullValue)

    
    # for entryLinks in root_element.findall(namespace+'entryLinks'):
    #     for entryLink in entryLinks.findall(namespace+'entryLink'):
    #         # print("checking entryLink: "+entryLink.attrib["name"])
    #         target_id = entryLink.attrib["targetId"]
    #         ref = root_element.find(".//*[@id='{target_id}']".format(target_id = target_id))
    #         if ref == None:
    #             # print("No reference found for entryLink: "+entryLink.attrib["name"])
    #             continue
    #         elif ref.attrib.get("type") == None:
    #             continue
    #         elif ref.attrib["type"] != "unit" and ref.attrib["type"] != "model":
    #             # print("entryLink: "+entryLink.attrib["name"]+" is neither a unit nor a model")
    #             continue
    #         else:
    #             collated_profile_stats += SelectionEntryUnitExtractor(ref,namespace,root_element,profile_stats_to_get,points_string,nullValue)

    return(pd.DataFrame.from_records(collated_profile_stats))

def SelectionEntryUnitExtractor(
    current_element,
    namespace,
    root_element,
    profile_stats_to_get = ["M","WS","BS","S","T","W","A","Ld","Save"],
    points_string = "pts",
    nullValue = ""
    ):
    """
    Iterates over all model selectionEntries in a unit selectionEntry. Calls SelectionEntryExtractor to extract data from model selectionEntries.

    Parameters:
        root_element : xml root object
            xml root object from etree
        namespace : string  
            namespace of xml file
        profile_stats_to_get : list
            list of stats other than name to get from sharedProfiles > profile > characteristics
        points_string : string
            string used to denote points cost in xml file. Will also be used for dataframe header
        nullValue : any
            value to use if value for characteristic is not found
    Returns:
        List
            list of profile dictionaries
    """
    if current_element == None:
        # print("current_element is None")
        return(None)
    collated_profile_stats = []

    selectionEntry_profile = SelectionEntryModelExtractor(
                current_element,
                namespace,
                root_element,
                profile_stats_to_get,
                points_string,
                nullValue)
    # print("initial selection extration")
    # print(selectionEntry_profile)
    # if selectionEntry_profile == None:
        # print("direct model extraction failed")
    if selectionEntry_profile != None:
        collated_profile_stats.append(selectionEntry_profile)

    for selectionEntry in current_element.findall(".//*[@type='model']"):
        profile_stats = SelectionEntryModelExtractor(
            selectionEntry,
            namespace,
            root_element,
            profile_stats_to_get,
            points_string,
            nullValue)
        if profile_stats == None:
            continue
        else:
            collated_profile_stats.append(profile_stats)
    entryLinks = current_element.find(namespace+"entryLinks")
    if entryLinks == None:
        return(collated_profile_stats)
    for entryLink in entryLinks.findall(namespace+"entryLink"):
        # print("checking entryLink "+entryLink.attrib["name"])
        target_id = entryLink.attrib["targetId"]
        ref = root_element.findall(".//*[@id='{target_id}']".format(target_id = target_id))
        for selectionEntry in ref:
            if selectionEntry == None:
                continue
            profile_stats = SelectionEntryModelExtractor(
                selectionEntry,
                namespace,
                root_element,
                profile_stats_to_get,
                points_string,
                nullValue)
            # print(profile_stats)
            if profile_stats == None:
                continue
            else:
                collated_profile_stats.append(profile_stats)
    return(collated_profile_stats)

def SelectionEntryModelExtractor(
    selectionEntry,
    namespace,
    root,
    profile_stats_to_get = ["M","WS","BS","S","T","W","A","Ld","Save"],
    points_string = "pts",
    nullValue = ""
    ):
    """
    Extracts profile data from a model selectionEntry object and returns it as a dictionary. Calls ProfileExtractor to extract profile. Extracts cost of model from selection entry

    Parameters:
        selectionEntry : xml selectionEntry object
            xml selectionEntry object from etree
        namespace : string  
            namespace of xml file
        root_element : xml root object
            xml root object from etree
        profile_stats_to_get : list
            list of stats other than name to get from profile > characteristics. To be passed to ProfileExtractor
        points_string : string
            string used to denote points cost in xml file. Will also be used for dataframe header
        nullValue : any
            value to use if value for characteristic is not found. To be passed to ProfileExtractor
    Returns:
        Dict
            dictionary that contains name and stats from profile_stats_to_get, as well as pts
    """
    try:
        points_cost = selectionEntry.find(namespace+"costs").find('.//*[@name="{points_string}"]'.format(points_string=points_string)).attrib["value"]
    except AttributeError:
        points_cost = "0.0"
    
    profile_stats = None
    # check profiles for profile first
    try:
        for profile in selectionEntry.find(namespace+"profiles").findall(namespace+"profile"):
            if profile.attrib["typeName"] == "Unit":
                profile_stats = ProfileExtractor(profile,namespace)
                if profile_stats["W"] == "N/A":
                    continue
                else:
                    break
        # print(" profile found for "+selectionEntry.attrib["name"])
    except AttributeError:
        # print("no profiles profile found for "+selectionEntry.attrib["name"])
        try:
            targetId = selectionEntry.find(namespace+"infoLinks").find(namespace+"infoLink").attrib["targetId"]
            profile = root.find(".//*[@id='{target_id}']".format(target_id = targetId))
            profile_stats = ProfileExtractor(profile,namespace)
        except AttributeError:
            # print("no info link profile found for "+selectionEntry.attrib["name"])
            profile = None
    # print("profile search for "+selectionEntry.attrib["name"]+" complete")
    if profile == None:
        return(None)
    model_name = selectionEntry.attrib["name"]
    # print("processing profile "+profile.attrib["name"])
    # profile_stats = ProfileExtractor(profile,namespace)
    if profile_stats == None:
        return(None)
    profile_stats["name"] = model_name
    profile_stats[points_string] = points_cost
    return(profile_stats)

def ProfileExtractor(
    profile,
    namespace,
    profile_stats_to_get = ["M","WS","BS","S","T","W","A","Ld","Save"],
    nullValue = ""
    ):
    """
    Extracts profile data from a profile XML Elements object and returns it as a dictionary

    Parameters:
        profile : xml profile object
            xml profile object from etree
        namespace : string  
            namespace of xml file
        profile_stats_to_get : list
            list of stats other than name to get from sharedProfiles > profile > characteristics
        nullValue : any
            value to use if value for characteristic is not found
    Returns:
        Dict
            dictionary that contains name and stats from profile_stats_to_get
    """
    try:
        profile.attrib["typeName"]
    except KeyError:
        return(None)
    if profile.attrib["typeName"] == "Unit":
        profile_stats = {}
        unitName = profile.attrib["name"]
        # print("Model name: "+unitName)
        profile_stats['name']= unitName

        recorded_stats = {}
        for characteristics in profile.iter(namespace+'characteristics'):
            for characteristic in characteristics.iter(namespace+'characteristic'):
                characteristicName = characteristic.attrib["name"]
                characteristicValue = characteristic.text
                recorded_stats[characteristicName] =  characteristicValue
        for stat in profile_stats_to_get:
            try:
                profile_stats[stat] = recorded_stats[stat]
            except KeyError:
                profile_stats[stat] = nullValue
        return(profile_stats)
    else:
        return(None)

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
    namespace = root_element.tag.split("}")[0]+"}"

    collated_profile_stats =[]
    for profile in root_element.findall(".//*[@typeName='Weapon']"):
        profile_stats = {}
        profile_stats['name']= profile.attrib["name"]

        recorded_stats = {}
        for characteristics in profile.iter(namespace+'characteristics'):
            for characteristic in characteristics.iter(namespace+'characteristic'):
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


def WeaponCostExtractor(
    root_element,
    nullValue = "0.0"
    ):
    """
    Extracts weapon cost data from an XML Elements object and returns it as a DataFrame.

    Flow of extraction:
    1. model level. Note down model id
    2. check entryLinks of model
    3. check costs of entryLinks
    4. follow each entryLink
    5. get cost in pts
    6. check modifiers
    7. for each modifier, apply cost modifer if condition or conditiongroup is met


    Parameters:
        root_element : xml root object
            xml root object from etree
        nullValue : any
            value to use if value for characteristic is not found
    """
    pass
            
    
            


