import pandas as pd
import xml.etree.ElementTree as ET



class ModelExtractor():
    """
    Extracts model data from an XML Elements object
    """
    def __init__(self,root_element):
        self.root_element = root_element
        self.profile_stats_to_get = ["M","WS","BS","S","T","W","A","Ld"]
        self.nullValue = ""
    
    def extract(self):
        """"
        extracts models from a root element and returns a data frame
        """
        collated_profile_stats =[]
        for sharedProfile in self.root_element.iter('{http://www.battlescribe.net/schema/catalogueSchema}sharedProfiles'):
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
                        for stat in self.profile_stats_to_get:
                            try:
                                profile_stats[stat] = recorded_stats[stat]
                            except KeyError:
                                profile_stats[stat] = self.nullValue
                        collated_profile_stats.append(profile_stats)
        return(pd.DataFrame.from_records(collated_profile_stats))

class WeaponExtractor():
    """
    Extracts weapomn data from an XML Elements object
    """
    def __init__(self,root_element):
        self.root_element = root_element
        self.profile_stats_to_get = ["Range","Type","S","AP","D","Abilities"]
        self.nullValue = ""
    
    def extract(self):
        """"
        extracts weapons from a root element and returns a data frame
        """
        collated_profile_stats =[]
        for sharedProfile in self.root_element.iter('{http://www.battlescribe.net/schema/catalogueSchema}sharedProfiles'):
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
                        for stat in self.profile_stats_to_get:
                            try:
                                profile_stats[stat] = recorded_stats[stat]
                            except KeyError:
                                profile_stats[stat] = self.nullValue
                        collated_profile_stats.append(profile_stats)
        return(pd.DataFrame.from_records(collated_profile_stats))
                
            
    
            


