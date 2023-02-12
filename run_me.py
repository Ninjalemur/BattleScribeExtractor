import battlescribeextractor as bse
import sys
import time
import pandas as pd

import xml.etree.ElementTree as ET


def main():
    # source_file = sys.argv[1]
    # print("Source File: {source_file}".format(source_file=source_file))

    # model_data, weapon_data = bse.FileExtractor(source_file)
    # print("model data: ")
    # print(model_data)
    # print("weapon data: ")
    # print(weapon_data)

    # source_folder= sys.argv[1]
    # print("Source Folder: {source_folder}".format(source_folder=source_folder))
    # bse.FolderExtractor(source_folder)

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
    print(received_output)

    pass

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f'time taken: {end - start:3f} seconds')
