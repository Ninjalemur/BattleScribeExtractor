import battlescribeextractor as bse
import pandas as pd
import xml.etree.ElementTree as ET

def test_ModelExtractorSharedProfile():
    """
    Test that ModelExtractor correctly extracts Model data from root element

    Ensures that sharedProfiles > profile > characteristics path is extracted, but not others
    """
    test_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <catalogue id="0cc2-3545-6762-a3f7" name="Imperium - Grey Knights" revision="116" battleScribeVersion="2.03" authorName="BSData Developers" authorContact="@Tekton" authorUrl="https://www.bsdata.net/contact" library="false" gameSystemId="28ec-711c-d87f-3aeb" gameSystemRevision="238" xmlns="http://www.battlescribe.net/schema/catalogueSchema">
            <sharedProfiles>
                <profile id="f204-dc7f-aacf-e947" name="Grey Knight Terminator" hidden="false" typeId="800f-21d0-4387-c943" typeName="Unit">
                <characteristics>
                    <characteristic name="M" typeId="0bdf-a96e-9e38-7779">5&quot;</characteristic>
                    <characteristic name="WS" typeId="e7f0-1278-0250-df0c">3+</characteristic>
                    <characteristic name="BS" typeId="381b-eb28-74c3-df5f">3+</characteristic>
                    <characteristic name="S" typeId="2218-aa3c-265f-2939">4</characteristic>
                    <characteristic name="T" typeId="9c9f-9774-a358-3a39">4</characteristic>
                    <characteristic name="W" typeId="f330-5e6e-4110-0978">3</characteristic>
                    <characteristic name="A" typeId="13fc-b29b-31f2-ab9f">3</characteristic>
                    <characteristic name="Ld" typeId="00ca-f8b8-876d-b705">7</characteristic>
                    <characteristic name="Save" typeId="c0df-df94-abd7-e8d3">2+</characteristic>
                </characteristics>
                </profile>
                <profile id="8dda-c08b-39ae-a8f3" name="Nemesis Falchion" hidden="false" typeId="d5f97c0b-9fc9-478d-aa34-a7c414d3ea48" typeName="Weapon">
                <characteristics>
                    <characteristic name="Range" typeId="6fa97fa8-ea74-4a27-a0fb-bc4e5f367464">Melee</characteristic>
                    <characteristic name="Type" typeId="077c342f-d7b9-45c6-b8af-88e97cafd3a2">Melee</characteristic>
                    <characteristic name="S" typeId="59b1-319e-ec13-d466">User</characteristic>
                    <characteristic name="AP" typeId="75aa-a838-b675-6484">-2</characteristic>
                    <characteristic name="D" typeId="ae8a-3137-d65b-4ca7">1</characteristic>
                    <characteristic name="Abilities" typeId="837d-5e63-aeb7-1410">Each time the bearer fights, if it is equipped with one or more Nemesis flachions, it makes 1 additional attack using this profile</characteristic>
                </characteristics>
                </profile>
                <profile id="1037-1f6f-bee5-b1ea" name="Grey Knight" hidden="false" typeId="800f-21d0-4387-c943" typeName="Unit">
                <characteristics>
                    <characteristic name="M" typeId="0bdf-a96e-9e38-7779">6&quot;</characteristic>
                    <characteristic name="WS" typeId="e7f0-1278-0250-df0c">3+</characteristic>
                    <characteristic name="BS" typeId="381b-eb28-74c3-df5f">3+</characteristic>
                    <characteristic name="S" typeId="2218-aa3c-265f-2939">4</characteristic>
                    <characteristic name="T" typeId="9c9f-9774-a358-3a39">4</characteristic>
                    <characteristic name="W" typeId="f330-5e6e-4110-0978">2</characteristic>
                    <characteristic name="A" typeId="13fc-b29b-31f2-ab9f">3</characteristic>
                    <characteristic name="Ld" typeId="00ca-f8b8-876d-b705">7</characteristic>
                    <characteristic name="Save" typeId="c0df-df94-abd7-e8d3">3+</characteristic>
                </characteristics>
                </profile>
            </sharedProfiles>
        </catalogue>
        """
    expected_output = pd.DataFrame.from_records(
        [
            {"name":"Grey Knight Terminator","M":"5\"","WS":"3+","BS":"3+","S":"4","T":"4","W":"3","A":"3","Ld":"7","Save":"2+","pts":""},
            {"name":"Grey Knight","M":"6\"","WS":"3+","BS":"3+","S":"4","T":"4","W":"2","A":"3","Ld":"7","Save":"3+","pts":""}            
        ]
    )
    root = ET.fromstring(test_xml)
    received_output = bse.ModelExtractorSharedProfile(root)
    pd.testing.assert_frame_equal(expected_output,received_output)

def test_WeaponExtractorSharedProfile():
    """
    Test that WeaponExtractor correctly extracts Weapon data from root element

    Ensures that sharedProfiles > profile > characteristics path is extracted, but not others
    """
    test_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <catalogue id="0cc2-3545-6762-a3f7" name="Imperium - Grey Knights" revision="116" battleScribeVersion="2.03" authorName="BSData Developers" authorContact="@Tekton" authorUrl="https://www.bsdata.net/contact" library="false" gameSystemId="28ec-711c-d87f-3aeb" gameSystemRevision="238" xmlns="http://www.battlescribe.net/schema/catalogueSchema">
            <sharedProfiles>
                <profile id="f204-dc7f-aacf-e947" name="Grey Knight Terminator" hidden="false" typeId="800f-21d0-4387-c943" typeName="Unit">
                <characteristics>
                    <characteristic name="M" typeId="0bdf-a96e-9e38-7779">5&quot;</characteristic>
                    <characteristic name="WS" typeId="e7f0-1278-0250-df0c">3+</characteristic>
                    <characteristic name="BS" typeId="381b-eb28-74c3-df5f">3+</characteristic>
                    <characteristic name="S" typeId="2218-aa3c-265f-2939">4</characteristic>
                    <characteristic name="T" typeId="9c9f-9774-a358-3a39">4</characteristic>
                    <characteristic name="W" typeId="f330-5e6e-4110-0978">3</characteristic>
                    <characteristic name="A" typeId="13fc-b29b-31f2-ab9f">3</characteristic>
                    <characteristic name="Ld" typeId="00ca-f8b8-876d-b705">7</characteristic>
                    <characteristic name="Save" typeId="c0df-df94-abd7-e8d3">2+</characteristic>
                </characteristics>
                </profile>
                <profile id="8dda-c08b-39ae-a8f3" name="Nemesis Falchion" hidden="false" typeId="d5f97c0b-9fc9-478d-aa34-a7c414d3ea48" typeName="Weapon">
                <characteristics>
                    <characteristic name="Range" typeId="6fa97fa8-ea74-4a27-a0fb-bc4e5f367464">Melee</characteristic>
                    <characteristic name="Type" typeId="077c342f-d7b9-45c6-b8af-88e97cafd3a2">Melee</characteristic>
                    <characteristic name="S" typeId="59b1-319e-ec13-d466">User</characteristic>
                    <characteristic name="AP" typeId="75aa-a838-b675-6484">-2</characteristic>
                    <characteristic name="D" typeId="ae8a-3137-d65b-4ca7">1</characteristic>
                    <characteristic name="Abilities" typeId="837d-5e63-aeb7-1410">Each time the bearer fights, if it is equipped with one or more Nemesis flachions, it makes 1 additional attack using this profile</characteristic>
                </characteristics>
                </profile>
                <profile id="f7d8-8d94-0a86-534b" name="Psilencer" hidden="false" typeId="d5f97c0b-9fc9-478d-aa34-a7c414d3ea48" typeName="Weapon">
                <characteristics>
                    <characteristic name="Range" typeId="6fa97fa8-ea74-4a27-a0fb-bc4e5f367464">24&quot;</characteristic>
                    <characteristic name="Type" typeId="077c342f-d7b9-45c6-b8af-88e97cafd3a2">Heavy 6</characteristic>
                    <characteristic name="S" typeId="59b1-319e-ec13-d466">4</characteristic>
                    <characteristic name="AP" typeId="75aa-a838-b675-6484">-1</characteristic>
                    <characteristic name="D" typeId="ae8a-3137-d65b-4ca7">1</characteristic>
                    <characteristic name="Abilities" typeId="837d-5e63-aeb7-1410">-</characteristic>
                </characteristics>
                </profile>
            </sharedProfiles>
        </catalogue>
        """
    expected_output = pd.DataFrame.from_records(
        [
            {"name":"Nemesis Falchion","Range":"Melee","Type":"Melee","S":"User","AP":"-2","D":"1","Abilities":"Each time the bearer fights, if it is equipped with one or more Nemesis flachions, it makes 1 additional attack using this profile","pts":""},
            {"name":"Psilencer","Range":"24\"","Type":"Heavy 6","S":"4","AP":"-1","D":"1","Abilities":"-","pts":""}            
        ]
    )
    root = ET.fromstring(test_xml)
    received_output = bse.WeaponExtractorSharedProfile(root)
    pd.testing.assert_frame_equal(expected_output,received_output)

def test_WeaponExtractorSharedSelectionEntry():
    """
    Test that WeaponExtractor correctly extracts Weapon data from root element

    Ensures that sharedSelectionEntries > profile > characteristics path is extracted, but not others
    """
    test_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <catalogue id="0cc2-3545-6762-a3f7" name="Imperium - Grey Knights" revision="116" battleScribeVersion="2.03" authorName="BSData Developers" authorContact="@Tekton" authorUrl="https://www.bsdata.net/contact" library="false" gameSystemId="28ec-711c-d87f-3aeb" gameSystemRevision="238" xmlns="http://www.battlescribe.net/schema/catalogueSchema">
            <sharedSelectionEntries>
                <selectionEntry id="c97e-2928-fc16-ddc3" name="Dreadfist" hidden="false" collective="false" import="true" type="upgrade">
                    <profiles>
                        <profile id="70dc-ea63-61e4-f38a" name="Dreadfist" hidden="false" typeId="d5f97c0b-9fc9-478d-aa34-a7c414d3ea48" typeName="Weapon">
                        <characteristics>
                            <characteristic name="Range" typeId="6fa97fa8-ea74-4a27-a0fb-bc4e5f367464">Melee</characteristic>
                            <characteristic name="Type" typeId="077c342f-d7b9-45c6-b8af-88e97cafd3a2">Melee</characteristic>
                            <characteristic name="S" typeId="59b1-319e-ec13-d466">x2</characteristic>
                            <characteristic name="AP" typeId="75aa-a838-b675-6484">-3</characteristic>
                            <characteristic name="D" typeId="ae8a-3137-d65b-4ca7">2</characteristic>
                            <characteristic name="Abilities" typeId="837d-5e63-aeb7-1410">-</characteristic>
                        </characteristics>
                        </profile>
                    </profiles>
                    <costs>
                        <cost name=" PL" typeId="e356-c769-5920-6e14" value="0.0"/>
                        <cost name="CP" typeId="2d3b-b544-ad49-fb75" value="0.0"/>
                        <cost name="pts" typeId="points" value="0.0"/>
                    </costs>
                </selectionEntry>
            </sharedSelectionEntries>
        </catalogue>
        """
    expected_output = pd.DataFrame.from_records(
        [
            {"name":"Dreadfist","Range":"Melee","Type":"Melee","S":"x2","AP":"-3","D":"2","Abilities":"-","pts":"0.0"}            
        ]
    )
    root = ET.fromstring(test_xml)
    received_output = bse.WeaponExtractorSharedSelectionEntry(root)
    pd.testing.assert_frame_equal(expected_output,received_output)