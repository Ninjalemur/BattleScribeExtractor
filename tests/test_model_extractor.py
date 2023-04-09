import battlescribeextractor as bse
import pandas as pd
import xml.etree.ElementTree as ET

def test_ModelExtractor():
    """
    Test that ModelExtractor correctly extracts Model data from root element

    Ensures that sharedProfiles > profile > characteristics path is extracted, but not others
    """
    test_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <catalogue id="0cc2-3545-6762-a3f7" name="Imperium - Grey Knights" revision="116" battleScribeVersion="2.03" authorName="BSData Developers" authorContact="@Tekton" authorUrl="https://www.bsdata.net/contact" library="false" gameSystemId="28ec-711c-d87f-3aeb" gameSystemRevision="238" xmlns="http://www.battlescribe.net/schema/catalogueSchema">
            <entryLinks>
                <entryLink id="0244-9f38-1f40-4689" name="Strike Squad" hidden="false" collective="false" import="true" targetId="e012-a289-720d-a36c" type="selectionEntry"/>
            </entryLinks>
            <sharedSelectionEntries>
                <selectionEntry id="e012-a289-720d-a36c" name="Strike Squad" hidden="false" collective="false" import="true" type="unit">
                    <modifiers>
                        <modifier type="increment" field="e356-c769-5920-6e14" value="6.0">
                        <conditions>
                            <condition field="selections" scope="e012-a289-720d-a36c" value="4.0" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9939-4098-d186-7d33" type="greaterThan"/>
                        </conditions>
                        </modifier>
                    </modifiers>
                    <infoLinks>
                        <infoLink id="f5b0-77e7-a206-5a81" name="Teleport Strike" hidden="false" targetId="a29c-ad1e-441b-2167" type="rule"/>
                        <infoLink id="181a-c718-dfd7-7b6a" name="Combat Squads" hidden="false" targetId="c046-073b-7a50-c436" type="rule"/>
                        <infoLink id="8b4a-a4c6-0a07-8e2a" name="Psyker" hidden="false" targetId="100e-a5f5-4af4-8c40" type="profile"/>
                        <infoLink id="2c54-c0bf-6bf7-b820" name="Smite" hidden="false" targetId="84d6-49a4-a9ff-162b" type="profile"/>
                        <infoLink id="bd98-cc12-361d-aa19" name="Knights of Titan" hidden="false" targetId="a26c-3bc4-cd1f-10bf" type="rule"/>
                        <infoLink id="8fb3-d428-cdd4-c8d6" name="Hammerhand" hidden="false" targetId="ded7-680d-4084-5679" type="profile"/>
                    </infoLinks>
                    <categoryLinks>
                        <categoryLink id="5d5b-974f-55d0-7536" name="New CategoryLink" hidden="false" targetId="31b6-b037-4c7a-f850" primary="false"/>
                        <categoryLink id="ea4a-dca4-00c7-e7e2" name="New CategoryLink" hidden="false" targetId="3d52-fccf-10c0-3fae" primary="false"/>
                        <categoryLink id="67e4-0fb7-09f1-ae31" name="New CategoryLink" hidden="false" targetId="e691-aad7-d21c-1023" primary="false"/>
                        <categoryLink id="8a86-b659-ce19-bb2e" name="New CategoryLink" hidden="false" targetId="5d76b6f5-20ae-4d70-8f59-ade72a2add3a" primary="true"/>
                        <categoryLink id="474b-fa13-9d5c-791c" name="New CategoryLink" hidden="false" targetId="ed14-046b-12ea-4e1d" primary="false"/>
                        <categoryLink id="8d44-e359-ca28-cbbd" name="Faction: Imperium" hidden="false" targetId="84e2-9fa9-ebe6-1d18" primary="false"/>
                        <categoryLink id="c981-0085-0aca-5f20" name="&lt;Brotherhood&gt;" hidden="false" targetId="4a9f-dcb0-00e7-1fcc" primary="false"/>
                        <categoryLink id="848f-ac1e-bab0-0f3a" name="Faction: Sanctic Astartes" hidden="false" targetId="bb46-a10a-ef92-c764" primary="false"/>
                        <categoryLink id="2688-9e1e-a269-e406" name="Core" hidden="false" targetId="08f1-d244-eb44-7e01" primary="false"/>
                        <categoryLink id="8213-f932-ab98-3f05" name="Psyk-out Grenades" hidden="false" targetId="e08a-4705-eaae-e4c2" primary="false"/>
                    </categoryLinks>
                    <selectionEntryGroups>
                        <selectionEntryGroup id="9939-4098-d186-7d33" name="Grey Knights" hidden="false" collective="false" import="true" defaultSelectionEntryId="9253-70bc-b620-f22f">
                        <constraints>
                            <constraint field="selections" scope="parent" value="4.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="dac9-ab51-5e89-c3a9" type="min"/>
                            <constraint field="selections" scope="parent" value="9.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="9638-8040-606e-e169" type="max"/>
                        </constraints>
                        <selectionEntries>
                            <selectionEntry id="1123-be87-fca2-f102" name="Grey Knight (Daemon Hammer)" hidden="false" collective="false" import="true" type="model">
                            <constraints>
                                <constraint field="selections" scope="parent" value="9.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="fce2-981c-aeff-ca82" type="max"/>
                            </constraints>
                            <infoLinks>
                                <infoLink id="6ec6-2485-3f16-57df" name="Grey Knight" hidden="false" targetId="1037-1f6f-bee5-b1ea" type="profile"/>
                            </infoLinks>
                            <entryLinks>
                                <entryLink id="19eb-8686-c09b-7d18" name="Storm Bolter" hidden="false" collective="false" import="true" targetId="fded-edb8-1d1e-99a5" type="selectionEntry"/>
                                <entryLink id="beb2-6803-3166-085f" name="Nemesis Daemon Hammer" hidden="false" collective="false" import="true" targetId="8fba-9c8d-73bd-fe8e" type="selectionEntry">
                                <constraints>
                                    <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="030a-2d90-bd64-8b59" type="max"/>
                                    <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="9750-9cfe-34c1-3aea" type="min"/>
                                </constraints>
                                </entryLink>
                            </entryLinks>
                            <costs>
                                <cost name="pts" typeId="points" value="20.0"/>
                                <cost name=" PL" typeId="e356-c769-5920-6e14" value="0.0"/>
                                <cost name="CP" typeId="2d3b-b544-ad49-fb75" value="0.0"/>
                            </costs>
                            </selectionEntry>
                            <selectionEntry id="b220-54cb-ba4a-7043" name="Grey Knight (Falchions)" hidden="false" collective="false" import="true" type="model">
                            <constraints>
                                <constraint field="selections" scope="parent" value="9.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="9cfc-6fdb-6325-7bc2" type="max"/>
                            </constraints>
                            <infoLinks>
                                <infoLink id="47c3-d153-5f99-ae12" name="New InfoLink" hidden="false" targetId="1037-1f6f-bee5-b1ea" type="profile"/>
                            </infoLinks>
                            <entryLinks>
                                <entryLink id="690b-3cc7-b7c2-e7f3" name="New EntryLink" hidden="false" collective="false" import="true" targetId="fded-edb8-1d1e-99a5" type="selectionEntry"/>
                                <entryLink id="d2be-46c9-ea53-15f5" name="Nemesis Falchion" hidden="false" collective="false" import="true" targetId="9beb-5ba2-8317-4b82" type="selectionEntry">
                                <constraints>
                                    <constraint field="selections" scope="parent" value="2.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="4325-d660-7e0e-854a" type="min"/>
                                    <constraint field="selections" scope="parent" value="2.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="ebd3-228e-3667-16bf" type="max"/>
                                </constraints>
                                </entryLink>
                            </entryLinks>
                            <costs>
                                <cost name="pts" typeId="points" value="20.0"/>
                                <cost name=" PL" typeId="e356-c769-5920-6e14" value="0.0"/>
                                <cost name="CP" typeId="2d3b-b544-ad49-fb75" value="0.0"/>
                            </costs>
                            </selectionEntry>
                            <selectionEntry id="6bcd-f4c5-d359-9671" name="Grey Knight (Halberd)" hidden="false" collective="false" import="true" type="model">
                            <constraints>
                                <constraint field="selections" scope="parent" value="9.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="11d9-88a9-91fd-89f3" type="max"/>
                            </constraints>
                            <infoLinks>
                                <infoLink id="1b0d-2c65-9cb0-21d4" name="New InfoLink" hidden="false" targetId="1037-1f6f-bee5-b1ea" type="profile"/>
                            </infoLinks>
                            <entryLinks>
                                <entryLink id="bf65-05ae-807e-5b52" name="New EntryLink" hidden="false" collective="false" import="true" targetId="fded-edb8-1d1e-99a5" type="selectionEntry"/>
                                <entryLink id="0888-83c3-a90b-ae84" name="New EntryLink" hidden="false" collective="false" import="true" targetId="bbe1-df34-13d0-7ed1" type="selectionEntry">
                                <constraints>
                                    <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="f6b9-0be9-ff2e-19ad" type="min"/>
                                    <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="d716-b58d-fd49-8603" type="max"/>
                                </constraints>
                                </entryLink>
                            </entryLinks>
                            <costs>
                                <cost name="pts" typeId="points" value="20.0"/>
                                <cost name=" PL" typeId="e356-c769-5920-6e14" value="0.0"/>
                                <cost name="CP" typeId="2d3b-b544-ad49-fb75" value="0.0"/>
                            </costs>
                            </selectionEntry>
                            <selectionEntry id="9253-70bc-b620-f22f" name="Grey Knight (Sword)" hidden="false" collective="false" import="true" type="model">
                            <constraints>
                                <constraint field="selections" scope="parent" value="9.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="0494-890e-a2da-a881" type="max"/>
                            </constraints>
                            <infoLinks>
                                <infoLink id="83ae-30d3-cb23-4dea" name="New InfoLink" hidden="false" targetId="1037-1f6f-bee5-b1ea" type="profile"/>
                            </infoLinks>
                            <entryLinks>
                                <entryLink id="d266-29e7-1cd3-506e" name="New EntryLink" hidden="false" collective="false" import="true" targetId="fded-edb8-1d1e-99a5" type="selectionEntry"/>
                                <entryLink id="46a5-729c-5cdb-eec9" name="Nemesis Force Sword" hidden="false" collective="false" import="true" targetId="9b71-6e0f-e71f-eacc" type="selectionEntry">
                                <constraints>
                                    <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="9d11-e011-e04b-c55b" type="min"/>
                                    <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="df64-25d6-1b58-fa00" type="max"/>
                                </constraints>
                                </entryLink>
                            </entryLinks>
                            <costs>
                                <cost name="pts" typeId="points" value="20.0"/>
                                <cost name=" PL" typeId="e356-c769-5920-6e14" value="0.0"/>
                                <cost name="CP" typeId="2d3b-b544-ad49-fb75" value="0.0"/>
                            </costs>
                            </selectionEntry>
                            <selectionEntry id="1271-d9a1-50d2-6af3" name="Grey Knight (Warding Stave)" hidden="false" collective="false" import="true" type="model">
                            <constraints>
                                <constraint field="selections" scope="parent" value="9.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="58eb-f81e-e28b-b013" type="max"/>
                            </constraints>
                            <infoLinks>
                                <infoLink id="0375-e644-a83e-0ad2" name="New InfoLink" hidden="false" targetId="1037-1f6f-bee5-b1ea" type="profile"/>
                            </infoLinks>
                            <entryLinks>
                                <entryLink id="5755-f360-74b4-11b8" name="New EntryLink" hidden="false" collective="false" import="true" targetId="fded-edb8-1d1e-99a5" type="selectionEntry"/>
                                <entryLink id="e191-5aef-49dc-295e" name="New EntryLink" hidden="false" collective="false" import="true" targetId="9dc6-e559-0099-005a" type="selectionEntry">
                                <constraints>
                                    <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="2244-3d0f-9e77-1ad7" type="min"/>
                                    <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="35b5-7195-0d95-8d60" type="max"/>
                                </constraints>
                                </entryLink>
                            </entryLinks>
                            <costs>
                                <cost name="pts" typeId="points" value="20.0"/>
                                <cost name=" PL" typeId="e356-c769-5920-6e14" value="0.0"/>
                                <cost name="CP" typeId="2d3b-b544-ad49-fb75" value="0.0"/>
                            </costs>
                            </selectionEntry>
                        </selectionEntries>
                        <selectionEntryGroups>
                            <selectionEntryGroup id="4449-0bb7-3409-60c8" name="Special Weapons" hidden="false" collective="false" import="true">
                            <modifiers>
                                <modifier type="increment" field="df0e-0c95-bf8c-492a" value="1.0">
                                <conditions>
                                    <condition field="selections" scope="parent" value="9.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" childId="9939-4098-d186-7d33" type="equalTo"/>
                                </conditions>
                                </modifier>
                            </modifiers>
                            <constraints>
                                <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="df0e-0c95-bf8c-492a" type="max"/>
                            </constraints>
                            <selectionEntries>
                                <selectionEntry id="17ee-24e8-af43-f4ef" name="Grey Knight (Incinerator)" hidden="false" collective="false" import="true" type="model">
                                <constraints>
                                    <constraint field="selections" scope="parent" value="2.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="9813-7fbb-9bea-e300" type="max"/>
                                </constraints>
                                <infoLinks>
                                    <infoLink id="0b54-380a-91b7-4c1c" name="New InfoLink" hidden="false" targetId="1037-1f6f-bee5-b1ea" type="profile"/>
                                </infoLinks>
                                <entryLinks>
                                    <entryLink id="96bd-8e9c-5d41-b61e" name="Incinerator" hidden="false" collective="false" import="true" targetId="6650-9429-ac09-255d" type="selectionEntry">
                                    <modifiers>
                                        <modifier type="set" field="points" value="0.0"/>
                                    </modifiers>
                                    <constraints>
                                        <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="a5b4-2545-7b23-3536" type="max"/>
                                        <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="433f-d35c-629f-8f5a" type="min"/>
                                    </constraints>
                                    </entryLink>
                                </entryLinks>
                                <costs>
                                    <cost name="pts" typeId="points" value="20.0"/>
                                    <cost name=" PL" typeId="e356-c769-5920-6e14" value="0.0"/>
                                    <cost name="CP" typeId="2d3b-b544-ad49-fb75" value="0.0"/>
                                </costs>
                                </selectionEntry>
                                <selectionEntry id="a459-a0b7-91c4-2e99" name="Grey Knight (Psycannon)" hidden="false" collective="false" import="true" type="model">
                                <constraints>
                                    <constraint field="selections" scope="parent" value="2.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="fda8-3d40-425e-f3ae" type="max"/>
                                </constraints>
                                <infoLinks>
                                    <infoLink id="4637-eee6-d32b-19b5" name="New InfoLink" hidden="false" targetId="1037-1f6f-bee5-b1ea" type="profile"/>
                                </infoLinks>
                                <entryLinks>
                                    <entryLink id="282c-728a-6183-2ebd" name="Psycannon" hidden="false" collective="false" import="true" targetId="c047-6362-b1bb-1ffd" type="selectionEntry">
                                    <modifiers>
                                        <modifier type="set" field="points" value="0.0"/>
                                    </modifiers>
                                    <constraints>
                                        <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="a703-4ab6-edc2-92cb" type="max"/>
                                        <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="cbe8-b7fc-e3ff-6b2b" type="min"/>
                                    </constraints>
                                    </entryLink>
                                </entryLinks>
                                <costs>
                                    <cost name="pts" typeId="points" value="20.0"/>
                                    <cost name=" PL" typeId="e356-c769-5920-6e14" value="0.0"/>
                                    <cost name="CP" typeId="2d3b-b544-ad49-fb75" value="0.0"/>
                                </costs>
                                </selectionEntry>
                                <selectionEntry id="66ab-7ff3-f2ce-9430" name="Grey Knight (Psilencer)" hidden="false" collective="false" import="true" type="model">
                                <constraints>
                                    <constraint field="selections" scope="parent" value="2.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="4987-7065-1188-1a9f" type="max"/>
                                </constraints>
                                <infoLinks>
                                    <infoLink id="2599-b0a6-81e7-b2e8" name="New InfoLink" hidden="false" targetId="1037-1f6f-bee5-b1ea" type="profile"/>
                                </infoLinks>
                                <entryLinks>
                                    <entryLink id="0584-76b5-4144-352b" name="Psilencer" hidden="false" collective="false" import="true" targetId="94c1-7cb5-a934-687a" type="selectionEntry">
                                    <modifiers>
                                        <modifier type="set" field="points" value="0.0"/>
                                    </modifiers>
                                    <constraints>
                                        <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="5356-3f32-c860-5220" type="max"/>
                                        <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="e619-812a-26de-85f9" type="min"/>
                                    </constraints>
                                    </entryLink>
                                </entryLinks>
                                <costs>
                                    <cost name="pts" typeId="points" value="20.0"/>
                                    <cost name=" PL" typeId="e356-c769-5920-6e14" value="0.0"/>
                                    <cost name="CP" typeId="2d3b-b544-ad49-fb75" value="0.0"/>
                                </costs>
                                </selectionEntry>
                            </selectionEntries>
                            </selectionEntryGroup>
                        </selectionEntryGroups>
                        </selectionEntryGroup>
                    </selectionEntryGroups>
                    <entryLinks>
                        <entryLink id="6bed-fae1-6fb0-5dbc" name="Grey Knight Justicar" hidden="false" collective="false" import="true" targetId="767b-e555-311f-cdbe" type="selectionEntry">
                        <constraints>
                            <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="false" includeChildSelections="false" includeChildForces="false" id="403a-512a-3225-44ed" type="max"/>
                            <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="3e03-77ff-3b4d-b0b4" type="min"/>
                        </constraints>
                        </entryLink>
                        <entryLink id="6f18-42b7-9b30-140e" name="Frag &amp; Krak grenades" hidden="false" collective="false" import="true" targetId="cddf-945e-1335-e681" type="selectionEntry">
                        <constraints>
                            <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="f4d7-7d56-5de1-a796" type="min"/>
                            <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="1e3b-5f04-18e9-d0f4" type="max"/>
                        </constraints>
                        </entryLink>
                        <entryLink id="05da-7b0a-b566-483b" name="Brotherhood Psyker Power" hidden="false" collective="false" import="true" targetId="d6ae-fe14-202c-6351" type="selectionEntry"/>
                    </entryLinks>
                    <costs>
                        <cost name=" PL" typeId="e356-c769-5920-6e14" value="6.0"/>
                        <cost name="pts" typeId="points" value="0.0"/>
                        <cost name="CP" typeId="2d3b-b544-ad49-fb75" value="0.0"/>
                    </costs>
                    </selectionEntry>
                    <selectionEntry id="767b-e555-311f-cdbe" name="Grey Knight Justicar" hidden="false" collective="false" import="true" type="model">
                    <profiles>
                        <profile id="9d07-0d02-74cf-b462" name="Grey Knight Justicar" hidden="false" typeId="800f-21d0-4387-c943" typeName="Unit">
                        <characteristics>
                            <characteristic name="M" typeId="0bdf-a96e-9e38-7779">6&quot;</characteristic>
                            <characteristic name="WS" typeId="e7f0-1278-0250-df0c">3+</characteristic>
                            <characteristic name="BS" typeId="381b-eb28-74c3-df5f">3+</characteristic>
                            <characteristic name="S" typeId="2218-aa3c-265f-2939">4</characteristic>
                            <characteristic name="T" typeId="9c9f-9774-a358-3a39">4</characteristic>
                            <characteristic name="W" typeId="f330-5e6e-4110-0978">2</characteristic>
                            <characteristic name="A" typeId="13fc-b29b-31f2-ab9f">4</characteristic>
                            <characteristic name="Ld" typeId="00ca-f8b8-876d-b705">8</characteristic>
                            <characteristic name="Save" typeId="c0df-df94-abd7-e8d3">3+</characteristic>
                        </characteristics>
                        </profile>
                    </profiles>
                    <entryLinks>
                        <entryLink id="fb52-5a60-2169-0454" name="Grey Knight Melee Weapons" hidden="false" collective="false" import="true" targetId="2619-cbc9-7327-dc75" type="selectionEntryGroup"/>
                        <entryLink id="da8e-18b3-b989-2026" name="Storm Bolter" hidden="false" collective="false" import="true" targetId="fded-edb8-1d1e-99a5" type="selectionEntry"/>
                        <entryLink id="dbdf-6ae0-4772-2bb9" name="Endowment in Extremis" hidden="false" collective="false" import="true" targetId="506e-52fd-0e8c-9276" type="selectionEntry"/>
                        <entryLink id="ae7b-ee6a-eb64-c1e4" name="Endowment in Extremis" hidden="false" collective="false" import="true" targetId="cf42-d211-9712-83c1" type="selectionEntryGroup"/>
                    </entryLinks>
                    <costs>
                        <cost name=" PL" typeId="e356-c769-5920-6e14" value="0.0"/>
                        <cost name="pts" typeId="points" value="20.0"/>
                        <cost name="CP" typeId="2d3b-b544-ad49-fb75" value="0.0"/>
                    </costs>
                    </selectionEntry>
            </sharedSelectionEntries>
            <sharedProfiles>
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
            {"name":"Grey Knight (Daemon Hammer)","M":"6\"","WS":"3+","BS":"3+","S":"4","T":"4","W":"2","A":"3","Ld":"7","Save":"3+","pts":"20.0"},
            {"name":"Grey Knight (Falchions)","M":"6\"","WS":"3+","BS":"3+","S":"4","T":"4","W":"2","A":"3","Ld":"7","Save":"3+","pts":"20.0"},
            {"name":"Grey Knight (Halberd)","M":"6\"","WS":"3+","BS":"3+","S":"4","T":"4","W":"2","A":"3","Ld":"7","Save":"3+","pts":"20.0"},
            {"name":"Grey Knight (Sword)","M":"6\"","WS":"3+","BS":"3+","S":"4","T":"4","W":"2","A":"3","Ld":"7","Save":"3+","pts":"20.0"},
            {"name":"Grey Knight (Warding Stave)","M":"6\"","WS":"3+","BS":"3+","S":"4","T":"4","W":"2","A":"3","Ld":"7","Save":"3+","pts":"20.0"},
            {"name":"Grey Knight (Incinerator)","M":"6\"","WS":"3+","BS":"3+","S":"4","T":"4","W":"2","A":"3","Ld":"7","Save":"3+","pts":"20.0"},
            {"name":"Grey Knight (Psycannon)","M":"6\"","WS":"3+","BS":"3+","S":"4","T":"4","W":"2","A":"3","Ld":"7","Save":"3+","pts":"20.0"},
            {"name":"Grey Knight (Psilencer)","M":"6\"","WS":"3+","BS":"3+","S":"4","T":"4","W":"2","A":"3","Ld":"7","Save":"3+","pts":"20.0"},
            {"name":"Grey Knight Justicar","M":"6\"","WS":"3+","BS":"3+","S":"4","T":"4","W":"2","A":"4","Ld":"8","Save":"3+","pts":"20.0"}
        ]
    )
    root = ET.fromstring(test_xml)
    received_output = pd.DataFrame.from_records(bse.ModelExtractor(root))
    pd.testing.assert_frame_equal(expected_output,received_output)

def test_SelectionEntryUnitExtractor_nested():
    """
    Test that SelectionEntryUnitExtractor correctly recurses selectionEntryGroups to extract selectionEntries. Depends on SelectionEntryModelExtractor and ProfileExtractor functioning correctly.
    """
    test_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <catalogue id="0cc2-3545-6762-a3f7" name="Imperium - Grey Knights" revision="116" battleScribeVersion="2.03" authorName="BSData Developers" authorContact="@Tekton" authorUrl="https://www.bsdata.net/contact" library="false" gameSystemId="28ec-711c-d87f-3aeb" gameSystemRevision="238" xmlns="http://www.battlescribe.net/schema/catalogueSchema">
            <sharedSelectionEntries>
                <selectionEntry id="e012-a289-720d-a36c" name="Strike Squad" hidden="false" collective="false" import="true" type="unit">
                    <modifiers>
                        <modifier type="increment" field="e356-c769-5920-6e14" value="6.0">
                        <conditions>
                            <condition field="selections" scope="e012-a289-720d-a36c" value="4.0" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9939-4098-d186-7d33" type="greaterThan"/>
                        </conditions>
                        </modifier>
                    </modifiers>
                    <infoLinks>
                        <infoLink id="f5b0-77e7-a206-5a81" name="Teleport Strike" hidden="false" targetId="a29c-ad1e-441b-2167" type="rule"/>
                        <infoLink id="181a-c718-dfd7-7b6a" name="Combat Squads" hidden="false" targetId="c046-073b-7a50-c436" type="rule"/>
                        <infoLink id="8b4a-a4c6-0a07-8e2a" name="Psyker" hidden="false" targetId="100e-a5f5-4af4-8c40" type="profile"/>
                        <infoLink id="2c54-c0bf-6bf7-b820" name="Smite" hidden="false" targetId="84d6-49a4-a9ff-162b" type="profile"/>
                        <infoLink id="bd98-cc12-361d-aa19" name="Knights of Titan" hidden="false" targetId="a26c-3bc4-cd1f-10bf" type="rule"/>
                        <infoLink id="8fb3-d428-cdd4-c8d6" name="Hammerhand" hidden="false" targetId="ded7-680d-4084-5679" type="profile"/>
                    </infoLinks>
                    <categoryLinks>
                        <categoryLink id="5d5b-974f-55d0-7536" name="New CategoryLink" hidden="false" targetId="31b6-b037-4c7a-f850" primary="false"/>
                        <categoryLink id="ea4a-dca4-00c7-e7e2" name="New CategoryLink" hidden="false" targetId="3d52-fccf-10c0-3fae" primary="false"/>
                        <categoryLink id="67e4-0fb7-09f1-ae31" name="New CategoryLink" hidden="false" targetId="e691-aad7-d21c-1023" primary="false"/>
                        <categoryLink id="8a86-b659-ce19-bb2e" name="New CategoryLink" hidden="false" targetId="5d76b6f5-20ae-4d70-8f59-ade72a2add3a" primary="true"/>
                        <categoryLink id="474b-fa13-9d5c-791c" name="New CategoryLink" hidden="false" targetId="ed14-046b-12ea-4e1d" primary="false"/>
                        <categoryLink id="8d44-e359-ca28-cbbd" name="Faction: Imperium" hidden="false" targetId="84e2-9fa9-ebe6-1d18" primary="false"/>
                        <categoryLink id="c981-0085-0aca-5f20" name="&lt;Brotherhood&gt;" hidden="false" targetId="4a9f-dcb0-00e7-1fcc" primary="false"/>
                        <categoryLink id="848f-ac1e-bab0-0f3a" name="Faction: Sanctic Astartes" hidden="false" targetId="bb46-a10a-ef92-c764" primary="false"/>
                        <categoryLink id="2688-9e1e-a269-e406" name="Core" hidden="false" targetId="08f1-d244-eb44-7e01" primary="false"/>
                        <categoryLink id="8213-f932-ab98-3f05" name="Psyk-out Grenades" hidden="false" targetId="e08a-4705-eaae-e4c2" primary="false"/>
                    </categoryLinks>
                    <selectionEntryGroups>
                        <selectionEntryGroup id="9939-4098-d186-7d33" name="Grey Knights" hidden="false" collective="false" import="true" defaultSelectionEntryId="9253-70bc-b620-f22f">
                        <constraints>
                            <constraint field="selections" scope="parent" value="4.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="dac9-ab51-5e89-c3a9" type="min"/>
                            <constraint field="selections" scope="parent" value="9.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="9638-8040-606e-e169" type="max"/>
                        </constraints>
                        <selectionEntries>
                            <selectionEntry id="1123-be87-fca2-f102" name="Grey Knight (Daemon Hammer)" hidden="false" collective="false" import="true" type="model">
                            <constraints>
                                <constraint field="selections" scope="parent" value="9.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="fce2-981c-aeff-ca82" type="max"/>
                            </constraints>
                            <infoLinks>
                                <infoLink id="6ec6-2485-3f16-57df" name="Grey Knight" hidden="false" targetId="1037-1f6f-bee5-b1ea" type="profile"/>
                            </infoLinks>
                            <entryLinks>
                                <entryLink id="19eb-8686-c09b-7d18" name="Storm Bolter" hidden="false" collective="false" import="true" targetId="fded-edb8-1d1e-99a5" type="selectionEntry"/>
                                <entryLink id="beb2-6803-3166-085f" name="Nemesis Daemon Hammer" hidden="false" collective="false" import="true" targetId="8fba-9c8d-73bd-fe8e" type="selectionEntry">
                                <constraints>
                                    <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="030a-2d90-bd64-8b59" type="max"/>
                                    <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="9750-9cfe-34c1-3aea" type="min"/>
                                </constraints>
                                </entryLink>
                            </entryLinks>
                            <costs>
                                <cost name="pts" typeId="points" value="20.0"/>
                                <cost name=" PL" typeId="e356-c769-5920-6e14" value="0.0"/>
                                <cost name="CP" typeId="2d3b-b544-ad49-fb75" value="0.0"/>
                            </costs>
                            </selectionEntry>
                            <selectionEntry id="b220-54cb-ba4a-7043" name="Grey Knight (Falchions)" hidden="false" collective="false" import="true" type="model">
                            <constraints>
                                <constraint field="selections" scope="parent" value="9.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="9cfc-6fdb-6325-7bc2" type="max"/>
                            </constraints>
                            <infoLinks>
                                <infoLink id="47c3-d153-5f99-ae12" name="New InfoLink" hidden="false" targetId="1037-1f6f-bee5-b1ea" type="profile"/>
                            </infoLinks>
                            <entryLinks>
                                <entryLink id="690b-3cc7-b7c2-e7f3" name="New EntryLink" hidden="false" collective="false" import="true" targetId="fded-edb8-1d1e-99a5" type="selectionEntry"/>
                                <entryLink id="d2be-46c9-ea53-15f5" name="Nemesis Falchion" hidden="false" collective="false" import="true" targetId="9beb-5ba2-8317-4b82" type="selectionEntry">
                                <constraints>
                                    <constraint field="selections" scope="parent" value="2.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="4325-d660-7e0e-854a" type="min"/>
                                    <constraint field="selections" scope="parent" value="2.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="ebd3-228e-3667-16bf" type="max"/>
                                </constraints>
                                </entryLink>
                            </entryLinks>
                            <costs>
                                <cost name="pts" typeId="points" value="20.0"/>
                                <cost name=" PL" typeId="e356-c769-5920-6e14" value="0.0"/>
                                <cost name="CP" typeId="2d3b-b544-ad49-fb75" value="0.0"/>
                            </costs>
                            </selectionEntry>
                            <selectionEntry id="6bcd-f4c5-d359-9671" name="Grey Knight (Halberd)" hidden="false" collective="false" import="true" type="model">
                            <constraints>
                                <constraint field="selections" scope="parent" value="9.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="11d9-88a9-91fd-89f3" type="max"/>
                            </constraints>
                            <infoLinks>
                                <infoLink id="1b0d-2c65-9cb0-21d4" name="New InfoLink" hidden="false" targetId="1037-1f6f-bee5-b1ea" type="profile"/>
                            </infoLinks>
                            <entryLinks>
                                <entryLink id="bf65-05ae-807e-5b52" name="New EntryLink" hidden="false" collective="false" import="true" targetId="fded-edb8-1d1e-99a5" type="selectionEntry"/>
                                <entryLink id="0888-83c3-a90b-ae84" name="New EntryLink" hidden="false" collective="false" import="true" targetId="bbe1-df34-13d0-7ed1" type="selectionEntry">
                                <constraints>
                                    <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="f6b9-0be9-ff2e-19ad" type="min"/>
                                    <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="d716-b58d-fd49-8603" type="max"/>
                                </constraints>
                                </entryLink>
                            </entryLinks>
                            <costs>
                                <cost name="pts" typeId="points" value="20.0"/>
                                <cost name=" PL" typeId="e356-c769-5920-6e14" value="0.0"/>
                                <cost name="CP" typeId="2d3b-b544-ad49-fb75" value="0.0"/>
                            </costs>
                            </selectionEntry>
                            <selectionEntry id="9253-70bc-b620-f22f" name="Grey Knight (Sword)" hidden="false" collective="false" import="true" type="model">
                            <constraints>
                                <constraint field="selections" scope="parent" value="9.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="0494-890e-a2da-a881" type="max"/>
                            </constraints>
                            <infoLinks>
                                <infoLink id="83ae-30d3-cb23-4dea" name="New InfoLink" hidden="false" targetId="1037-1f6f-bee5-b1ea" type="profile"/>
                            </infoLinks>
                            <entryLinks>
                                <entryLink id="d266-29e7-1cd3-506e" name="New EntryLink" hidden="false" collective="false" import="true" targetId="fded-edb8-1d1e-99a5" type="selectionEntry"/>
                                <entryLink id="46a5-729c-5cdb-eec9" name="Nemesis Force Sword" hidden="false" collective="false" import="true" targetId="9b71-6e0f-e71f-eacc" type="selectionEntry">
                                <constraints>
                                    <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="9d11-e011-e04b-c55b" type="min"/>
                                    <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="df64-25d6-1b58-fa00" type="max"/>
                                </constraints>
                                </entryLink>
                            </entryLinks>
                            <costs>
                                <cost name="pts" typeId="points" value="20.0"/>
                                <cost name=" PL" typeId="e356-c769-5920-6e14" value="0.0"/>
                                <cost name="CP" typeId="2d3b-b544-ad49-fb75" value="0.0"/>
                            </costs>
                            </selectionEntry>
                            <selectionEntry id="1271-d9a1-50d2-6af3" name="Grey Knight (Warding Stave)" hidden="false" collective="false" import="true" type="model">
                            <constraints>
                                <constraint field="selections" scope="parent" value="9.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="58eb-f81e-e28b-b013" type="max"/>
                            </constraints>
                            <infoLinks>
                                <infoLink id="0375-e644-a83e-0ad2" name="New InfoLink" hidden="false" targetId="1037-1f6f-bee5-b1ea" type="profile"/>
                            </infoLinks>
                            <entryLinks>
                                <entryLink id="5755-f360-74b4-11b8" name="New EntryLink" hidden="false" collective="false" import="true" targetId="fded-edb8-1d1e-99a5" type="selectionEntry"/>
                                <entryLink id="e191-5aef-49dc-295e" name="New EntryLink" hidden="false" collective="false" import="true" targetId="9dc6-e559-0099-005a" type="selectionEntry">
                                <constraints>
                                    <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="2244-3d0f-9e77-1ad7" type="min"/>
                                    <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="35b5-7195-0d95-8d60" type="max"/>
                                </constraints>
                                </entryLink>
                            </entryLinks>
                            <costs>
                                <cost name="pts" typeId="points" value="20.0"/>
                                <cost name=" PL" typeId="e356-c769-5920-6e14" value="0.0"/>
                                <cost name="CP" typeId="2d3b-b544-ad49-fb75" value="0.0"/>
                            </costs>
                            </selectionEntry>
                        </selectionEntries>
                        <selectionEntryGroups>
                            <selectionEntryGroup id="4449-0bb7-3409-60c8" name="Special Weapons" hidden="false" collective="false" import="true">
                            <modifiers>
                                <modifier type="increment" field="df0e-0c95-bf8c-492a" value="1.0">
                                <conditions>
                                    <condition field="selections" scope="parent" value="9.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" childId="9939-4098-d186-7d33" type="equalTo"/>
                                </conditions>
                                </modifier>
                            </modifiers>
                            <constraints>
                                <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="df0e-0c95-bf8c-492a" type="max"/>
                            </constraints>
                            <selectionEntries>
                                <selectionEntry id="17ee-24e8-af43-f4ef" name="Grey Knight (Incinerator)" hidden="false" collective="false" import="true" type="model">
                                <constraints>
                                    <constraint field="selections" scope="parent" value="2.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="9813-7fbb-9bea-e300" type="max"/>
                                </constraints>
                                <infoLinks>
                                    <infoLink id="0b54-380a-91b7-4c1c" name="New InfoLink" hidden="false" targetId="1037-1f6f-bee5-b1ea" type="profile"/>
                                </infoLinks>
                                <entryLinks>
                                    <entryLink id="96bd-8e9c-5d41-b61e" name="Incinerator" hidden="false" collective="false" import="true" targetId="6650-9429-ac09-255d" type="selectionEntry">
                                    <modifiers>
                                        <modifier type="set" field="points" value="0.0"/>
                                    </modifiers>
                                    <constraints>
                                        <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="a5b4-2545-7b23-3536" type="max"/>
                                        <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="433f-d35c-629f-8f5a" type="min"/>
                                    </constraints>
                                    </entryLink>
                                </entryLinks>
                                <costs>
                                    <cost name="pts" typeId="points" value="20.0"/>
                                    <cost name=" PL" typeId="e356-c769-5920-6e14" value="0.0"/>
                                    <cost name="CP" typeId="2d3b-b544-ad49-fb75" value="0.0"/>
                                </costs>
                                </selectionEntry>
                                <selectionEntry id="a459-a0b7-91c4-2e99" name="Grey Knight (Psycannon)" hidden="false" collective="false" import="true" type="model">
                                <constraints>
                                    <constraint field="selections" scope="parent" value="2.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="fda8-3d40-425e-f3ae" type="max"/>
                                </constraints>
                                <infoLinks>
                                    <infoLink id="4637-eee6-d32b-19b5" name="New InfoLink" hidden="false" targetId="1037-1f6f-bee5-b1ea" type="profile"/>
                                </infoLinks>
                                <entryLinks>
                                    <entryLink id="282c-728a-6183-2ebd" name="Psycannon" hidden="false" collective="false" import="true" targetId="c047-6362-b1bb-1ffd" type="selectionEntry">
                                    <modifiers>
                                        <modifier type="set" field="points" value="0.0"/>
                                    </modifiers>
                                    <constraints>
                                        <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="a703-4ab6-edc2-92cb" type="max"/>
                                        <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="cbe8-b7fc-e3ff-6b2b" type="min"/>
                                    </constraints>
                                    </entryLink>
                                </entryLinks>
                                <costs>
                                    <cost name="pts" typeId="points" value="20.0"/>
                                    <cost name=" PL" typeId="e356-c769-5920-6e14" value="0.0"/>
                                    <cost name="CP" typeId="2d3b-b544-ad49-fb75" value="0.0"/>
                                </costs>
                                </selectionEntry>
                                <selectionEntry id="66ab-7ff3-f2ce-9430" name="Grey Knight (Psilencer)" hidden="false" collective="false" import="true" type="model">
                                <constraints>
                                    <constraint field="selections" scope="parent" value="2.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="4987-7065-1188-1a9f" type="max"/>
                                </constraints>
                                <infoLinks>
                                    <infoLink id="2599-b0a6-81e7-b2e8" name="New InfoLink" hidden="false" targetId="1037-1f6f-bee5-b1ea" type="profile"/>
                                </infoLinks>
                                <entryLinks>
                                    <entryLink id="0584-76b5-4144-352b" name="Psilencer" hidden="false" collective="false" import="true" targetId="94c1-7cb5-a934-687a" type="selectionEntry">
                                    <modifiers>
                                        <modifier type="set" field="points" value="0.0"/>
                                    </modifiers>
                                    <constraints>
                                        <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="5356-3f32-c860-5220" type="max"/>
                                        <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="e619-812a-26de-85f9" type="min"/>
                                    </constraints>
                                    </entryLink>
                                </entryLinks>
                                <costs>
                                    <cost name="pts" typeId="points" value="20.0"/>
                                    <cost name=" PL" typeId="e356-c769-5920-6e14" value="0.0"/>
                                    <cost name="CP" typeId="2d3b-b544-ad49-fb75" value="0.0"/>
                                </costs>
                                </selectionEntry>
                            </selectionEntries>
                            </selectionEntryGroup>
                        </selectionEntryGroups>
                        </selectionEntryGroup>
                    </selectionEntryGroups>
                    <entryLinks>
                        <entryLink id="6bed-fae1-6fb0-5dbc" name="Grey Knight Justicar" hidden="false" collective="false" import="true" targetId="767b-e555-311f-cdbe" type="selectionEntry">
                        <constraints>
                            <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="false" includeChildSelections="false" includeChildForces="false" id="403a-512a-3225-44ed" type="max"/>
                            <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="3e03-77ff-3b4d-b0b4" type="min"/>
                        </constraints>
                        </entryLink>
                        <entryLink id="6f18-42b7-9b30-140e" name="Frag &amp; Krak grenades" hidden="false" collective="false" import="true" targetId="cddf-945e-1335-e681" type="selectionEntry">
                        <constraints>
                            <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="f4d7-7d56-5de1-a796" type="min"/>
                            <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="1e3b-5f04-18e9-d0f4" type="max"/>
                        </constraints>
                        </entryLink>
                        <entryLink id="05da-7b0a-b566-483b" name="Brotherhood Psyker Power" hidden="false" collective="false" import="true" targetId="d6ae-fe14-202c-6351" type="selectionEntry"/>
                    </entryLinks>
                    <costs>
                        <cost name=" PL" typeId="e356-c769-5920-6e14" value="6.0"/>
                        <cost name="pts" typeId="points" value="0.0"/>
                        <cost name="CP" typeId="2d3b-b544-ad49-fb75" value="0.0"/>
                    </costs>
                    </selectionEntry>
                    <selectionEntry id="767b-e555-311f-cdbe" name="Grey Knight Justicar" hidden="false" collective="false" import="true" type="model">
                    <profiles>
                        <profile id="9d07-0d02-74cf-b462" name="Grey Knight Justicar" hidden="false" typeId="800f-21d0-4387-c943" typeName="Unit">
                        <characteristics>
                            <characteristic name="M" typeId="0bdf-a96e-9e38-7779">6&quot;</characteristic>
                            <characteristic name="WS" typeId="e7f0-1278-0250-df0c">3+</characteristic>
                            <characteristic name="BS" typeId="381b-eb28-74c3-df5f">3+</characteristic>
                            <characteristic name="S" typeId="2218-aa3c-265f-2939">4</characteristic>
                            <characteristic name="T" typeId="9c9f-9774-a358-3a39">4</characteristic>
                            <characteristic name="W" typeId="f330-5e6e-4110-0978">2</characteristic>
                            <characteristic name="A" typeId="13fc-b29b-31f2-ab9f">4</characteristic>
                            <characteristic name="Ld" typeId="00ca-f8b8-876d-b705">8</characteristic>
                            <characteristic name="Save" typeId="c0df-df94-abd7-e8d3">3+</characteristic>
                        </characteristics>
                        </profile>
                    </profiles>
                    <entryLinks>
                        <entryLink id="fb52-5a60-2169-0454" name="Grey Knight Melee Weapons" hidden="false" collective="false" import="true" targetId="2619-cbc9-7327-dc75" type="selectionEntryGroup"/>
                        <entryLink id="da8e-18b3-b989-2026" name="Storm Bolter" hidden="false" collective="false" import="true" targetId="fded-edb8-1d1e-99a5" type="selectionEntry"/>
                        <entryLink id="dbdf-6ae0-4772-2bb9" name="Endowment in Extremis" hidden="false" collective="false" import="true" targetId="506e-52fd-0e8c-9276" type="selectionEntry"/>
                        <entryLink id="ae7b-ee6a-eb64-c1e4" name="Endowment in Extremis" hidden="false" collective="false" import="true" targetId="cf42-d211-9712-83c1" type="selectionEntryGroup"/>
                    </entryLinks>
                    <costs>
                        <cost name=" PL" typeId="e356-c769-5920-6e14" value="0.0"/>
                        <cost name="pts" typeId="points" value="20.0"/>
                        <cost name="CP" typeId="2d3b-b544-ad49-fb75" value="0.0"/>
                    </costs>
                    </selectionEntry>
            </sharedSelectionEntries>
            <sharedProfiles>
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
            {"name":"Grey Knight (Daemon Hammer)","M":"6\"","WS":"3+","BS":"3+","S":"4","T":"4","W":"2","A":"3","Ld":"7","Save":"3+","pts":"20.0"},
            {"name":"Grey Knight (Falchions)","M":"6\"","WS":"3+","BS":"3+","S":"4","T":"4","W":"2","A":"3","Ld":"7","Save":"3+","pts":"20.0"},
            {"name":"Grey Knight (Halberd)","M":"6\"","WS":"3+","BS":"3+","S":"4","T":"4","W":"2","A":"3","Ld":"7","Save":"3+","pts":"20.0"},
            {"name":"Grey Knight (Sword)","M":"6\"","WS":"3+","BS":"3+","S":"4","T":"4","W":"2","A":"3","Ld":"7","Save":"3+","pts":"20.0"},
            {"name":"Grey Knight (Warding Stave)","M":"6\"","WS":"3+","BS":"3+","S":"4","T":"4","W":"2","A":"3","Ld":"7","Save":"3+","pts":"20.0"},
            {"name":"Grey Knight (Incinerator)","M":"6\"","WS":"3+","BS":"3+","S":"4","T":"4","W":"2","A":"3","Ld":"7","Save":"3+","pts":"20.0"},
            {"name":"Grey Knight (Psycannon)","M":"6\"","WS":"3+","BS":"3+","S":"4","T":"4","W":"2","A":"3","Ld":"7","Save":"3+","pts":"20.0"},
            {"name":"Grey Knight (Psilencer)","M":"6\"","WS":"3+","BS":"3+","S":"4","T":"4","W":"2","A":"3","Ld":"7","Save":"3+","pts":"20.0"},
            {"name":"Grey Knight Justicar","M":"6\"","WS":"3+","BS":"3+","S":"4","T":"4","W":"2","A":"4","Ld":"8","Save":"3+","pts":"20.0"}
        ]
    )
    root = ET.fromstring(test_xml)
    namespace = root.tag.split("}")[0]+"}"
    firstSelectionEntry = root.find(".//*[@id='{target_id}']".format(target_id = 'e012-a289-720d-a36c'))
    received_output = pd.DataFrame.from_records(bse.SelectionEntryUnitExtractor(firstSelectionEntry,namespace,root))
    pd.testing.assert_frame_equal(expected_output,received_output)

def test_SelectionEntryUnitExtractor_direct():
    """
    Test that SelectionEntryUnitExtractor correctly calls SelectionEntryModelExtractor to extract profile and cost info from itself. Requires SelectionEntryModelExtractor and ProfileExtractor to be working correctly.
    """
    test_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <catalogue id="0cc2-3545-6762-a3f7" name="Imperium - Grey Knights" revision="116" battleScribeVersion="2.03" authorName="BSData Developers" authorContact="@Tekton" authorUrl="https://www.bsdata.net/contact" library="false" gameSystemId="28ec-711c-d87f-3aeb" gameSystemRevision="238" xmlns="http://www.battlescribe.net/schema/catalogueSchema">
            <sharedSelectionEntries>
                <selectionEntry id="630a-1d50-0a37-a639" name="Kaldor Draigo" publicationId="28ec-711c-pubN78977" page="182" hidden="false" collective="false" import="true" type="unit">
                    <constraints>
                        <constraint field="selections" scope="roster" value="1.0" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" id="2be2-fd1f-0903-8160" type="max"/>
                    </constraints>
                    <profiles>
                        <profile id="1d3f-632c-2f50-0b89" name="Lord Kaldor Draigo" hidden="false" typeId="800f-21d0-4387-c943" typeName="Unit">
                        <characteristics>
                            <characteristic name="M" typeId="0bdf-a96e-9e38-7779">5&quot;</characteristic>
                            <characteristic name="WS" typeId="e7f0-1278-0250-df0c">2+</characteristic>
                            <characteristic name="BS" typeId="381b-eb28-74c3-df5f">2+</characteristic>
                            <characteristic name="S" typeId="2218-aa3c-265f-2939">4</characteristic>
                            <characteristic name="T" typeId="9c9f-9774-a358-3a39">4</characteristic>
                            <characteristic name="W" typeId="f330-5e6e-4110-0978">7</characteristic>
                            <characteristic name="A" typeId="13fc-b29b-31f2-ab9f">6</characteristic>
                            <characteristic name="Ld" typeId="00ca-f8b8-876d-b705">9</characteristic>
                            <characteristic name="Save" typeId="c0df-df94-abd7-e8d3">2+</characteristic>
                        </characteristics>
                        </profile>
                        <profile id="6235-18e9-f81b-9686" name="Sanctum Sigilum" hidden="false" typeId="72c5eafc-75bf-4ed9-b425-78009f1efe82" typeName="Abilities">
                        <characteristics>
                            <characteristic name="Description" typeId="21befb24-fc85-4f52-a745-64b2e48f8228">This model has a 3+ invulnerable save</characteristic>
                        </characteristics>
                        </profile>
                        <profile id="a7be-6bb0-44fb-78dd" name="Psyker" hidden="false" typeId="bc97-dea9-9e88-bb7d" typeName="Psyker">
                        <characteristics>
                            <characteristic name="Cast" typeId="5afb-9914-904b-d3b3">2</characteristic>
                            <characteristic name="Deny" typeId="b5ac-9c20-5d5a-6f9b">2</characteristic>
                            <characteristic name="Powers Known" typeId="69d7-b45e-00a2-7e46">3</characteristic>
                            <characteristic name="Other" typeId="c2e2-f115-0003-5d7b">Smite</characteristic>
                        </characteristics>
                        </profile>
                    </profiles>
                    <infoLinks>
                        <infoLink id="5d7e-a30a-5e24-499c" name="Smite" hidden="false" targetId="84d6-49a4-a9ff-162b" type="profile"/>
                        <infoLink id="2ebd-3909-e123-cca4" name="Supreme Grand Master" hidden="false" targetId="0975-04aa-4a85-ef72" type="rule"/>
                        <infoLink id="86f3-2423-f6ee-d95c" name="Teleport Strike" hidden="false" targetId="a29c-ad1e-441b-2167" type="rule"/>
                        <infoLink id="484d-1f92-42d4-3785" name="Rites of Battle (Aura)" hidden="false" targetId="f836-3733-147c-9fb4" type="rule"/>
                        <infoLink id="0df6-30aa-1750-1811" name="Knights of Titan" hidden="false" targetId="a26c-3bc4-cd1f-10bf" type="rule"/>
                    </infoLinks>
                    <categoryLinks>
                        <categoryLink id="c0f0-9086-c653-45b0" name="New CategoryLink" hidden="false" targetId="848a6ff2-0def-4c72-8433-ff7da70e6bc7" primary="true"/>
                        <categoryLink id="5dc6-226c-5676-0803" name="New CategoryLink" hidden="false" targetId="31b6-b037-4c7a-f850" primary="false"/>
                        <categoryLink id="2f44-aa71-cfc1-9b56" name="New CategoryLink" hidden="false" targetId="e691-aad7-d21c-1023" primary="false"/>
                        <categoryLink id="6493-652e-ab92-de36" name="New CategoryLink" hidden="false" targetId="3d52-fccf-10c0-3fae" primary="false"/>
                        <categoryLink id="e510-d0eb-e3ea-7526" name="New CategoryLink" hidden="false" targetId="2821-762a-49dc-5a17" primary="false"/>
                        <categoryLink id="7408-561d-08a2-7c47" name="New CategoryLink" hidden="false" targetId="d7f3-e85c-9e30-c44c" primary="false"/>
                        <categoryLink id="1a6b-a791-e1c0-7c33" name="New CategoryLink" hidden="false" targetId="ef18-746a-369f-43a4" primary="false"/>
                        <categoryLink id="6684-9ae1-0b79-c774" name="Faction: Imperium" hidden="false" targetId="84e2-9fa9-ebe6-1d18" primary="false"/>
                        <categoryLink id="adf8-357a-399e-1289" name="Honoured Knight" hidden="false" targetId="736c-5b2d-201e-6df9" primary="false"/>
                        <categoryLink id="e581-525c-7be1-eb37" name="Psyk-out Grenades" hidden="false" targetId="e08a-4705-eaae-e4c2" primary="false"/>
                    </categoryLinks>
                    <entryLinks>
                        <entryLink id="bbad-f3d2-fb8f-1ccb" name="The Titansword" hidden="false" collective="false" import="true" targetId="f442-9be2-7fd2-2a94" type="selectionEntry">
                        <constraints>
                            <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="efec-ad3a-7642-f674" type="max"/>
                            <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="a4db-cfa7-36a5-2bd4" type="min"/>
                        </constraints>
                        </entryLink>
                        <entryLink id="20b0-c86b-8b73-267d" name="Master-crafted storm bolter" hidden="false" collective="false" import="true" targetId="5f78-3205-ec8a-c8ed" type="selectionEntry">
                        <modifiers>
                            <modifier type="set" field="points" value="0.0"/>
                        </modifiers>
                        <constraints>
                            <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="3f18-df94-3729-864b" type="max"/>
                            <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="0545-4f78-31aa-fd93" type="min"/>
                        </constraints>
                        </entryLink>
                        <entryLink id="9d91-6a8e-2078-26b5" name="Frag &amp; Krak grenades" hidden="false" collective="false" import="true" targetId="cddf-945e-1335-e681" type="selectionEntry">
                        <constraints>
                            <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="5412-4c34-f06d-9bd5" type="max"/>
                            <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="67f6-2dab-c1c4-37a5" type="min"/>
                        </constraints>
                        </entryLink>
                        <entryLink id="73e9-1c85-bec0-56b1" name="Warlord" hidden="false" collective="false" import="true" targetId="2516-dd30-d80e-f79a" type="selectionEntry"/>
                        <entryLink id="7b25-6e69-fe51-ec10" name="Grey Knight Warlord Trait" hidden="false" collective="false" import="true" targetId="87f6-76b7-a0d2-6b2c" type="selectionEntryGroup"/>
                        <entryLink id="e2c6-8442-d58b-64f9" name="Dominus Discipline" hidden="false" collective="false" import="true" targetId="f16b-4fb0-c9d1-7469" type="selectionEntryGroup">
                        <constraints>
                            <constraint field="selections" scope="parent" value="3.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="8124-119c-a203-6c3a" type="max"/>
                        </constraints>
                        </entryLink>
                        <entryLink id="870a-dea1-5df2-79e0" name="Shield of Humanity" hidden="false" collective="false" import="true" targetId="77cb-2eca-58ad-5616" type="selectionEntry"/>
                        <entryLink id="223c-fc27-1356-e8cd" name="Stratagem: Warlord Trait" hidden="false" collective="false" import="true" targetId="6771-6ab3-1672-6a39" type="selectionEntry"/>
                    </entryLinks>
                    <costs>
                        <cost name=" PL" typeId="e356-c769-5920-6e14" value="9.0"/>
                        <cost name="pts" typeId="points" value="165.0"/>
                        <cost name="CP" typeId="2d3b-b544-ad49-fb75" value="0.0"/>
                    </costs>
                </selectionEntry>
            </sharedSelectionEntries>    
        </catalogue>
    """
    expected_output = [
        {"name":"Kaldor Draigo","M":"5\"","WS":"2+","BS":"2+","S":"4","T":"4","W":"7","A":"6","Ld":"9","Save":"2+","pts":"165.0"}
        ]
    root = ET.fromstring(test_xml)
    namespace = root.tag.split("}")[0]+"}"
    firstSelectionEntry = root.find(".//*[@id='{target_id}']".format(target_id = '630a-1d50-0a37-a639'))
    received_output = bse.SelectionEntryUnitExtractor(firstSelectionEntry,namespace,root)
    assert expected_output == received_output

def test_SelectionEntryExtractorProfiles():
    """
    Test that selectionEntry data extraction from profiles in selectrionEntry for profile stats and points.  Depends on ProfileExtractor.
    """
    test_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <catalogue id="0cc2-3545-6762-a3f7" name="Imperium - Grey Knights" revision="116" battleScribeVersion="2.03" authorName="BSData Developers" authorContact="@Tekton" authorUrl="https://www.bsdata.net/contact" library="false" gameSystemId="28ec-711c-d87f-3aeb" gameSystemRevision="238" xmlns="http://www.battlescribe.net/schema/catalogueSchema">
            <sharedSelectionEntries>
                <selectionEntry id="767b-e555-311f-cdbe" name="Grey Knight Justicar" hidden="false" collective="false" import="true" type="model">
                    <profiles>
                        <profile id="9d07-0d02-74cf-b462" name="Grey Knight Justicar" hidden="false" typeId="800f-21d0-4387-c943" typeName="Unit">
                        <characteristics>
                            <characteristic name="M" typeId="0bdf-a96e-9e38-7779">6&quot;</characteristic>
                            <characteristic name="WS" typeId="e7f0-1278-0250-df0c">3+</characteristic>
                            <characteristic name="BS" typeId="381b-eb28-74c3-df5f">3+</characteristic>
                            <characteristic name="S" typeId="2218-aa3c-265f-2939">4</characteristic>
                            <characteristic name="T" typeId="9c9f-9774-a358-3a39">4</characteristic>
                            <characteristic name="W" typeId="f330-5e6e-4110-0978">2</characteristic>
                            <characteristic name="A" typeId="13fc-b29b-31f2-ab9f">4</characteristic>
                            <characteristic name="Ld" typeId="00ca-f8b8-876d-b705">8</characteristic>
                            <characteristic name="Save" typeId="c0df-df94-abd7-e8d3">3+</characteristic>
                        </characteristics>
                        </profile>
                    </profiles>
                    <entryLinks>
                        <entryLink id="fb52-5a60-2169-0454" name="Grey Knight Melee Weapons" hidden="false" collective="false" import="true" targetId="2619-cbc9-7327-dc75" type="selectionEntryGroup"/>
                        <entryLink id="da8e-18b3-b989-2026" name="Storm Bolter" hidden="false" collective="false" import="true" targetId="fded-edb8-1d1e-99a5" type="selectionEntry"/>
                        <entryLink id="dbdf-6ae0-4772-2bb9" name="Endowment in Extremis" hidden="false" collective="false" import="true" targetId="506e-52fd-0e8c-9276" type="selectionEntry"/>
                        <entryLink id="ae7b-ee6a-eb64-c1e4" name="Endowment in Extremis" hidden="false" collective="false" import="true" targetId="cf42-d211-9712-83c1" type="selectionEntryGroup"/>
                    </entryLinks>
                    <costs>
                        <cost name=" PL" typeId="e356-c769-5920-6e14" value="0.0"/>
                        <cost name="pts" typeId="points" value="20.0"/>
                        <cost name="CP" typeId="2d3b-b544-ad49-fb75" value="0.0"/>
                    </costs>
                </selectionEntry>
            </sharedSelectionEntries>
        </catalogue>
    """
    expected_output = {
            "name":"Grey Knight Justicar",
            "M":"6\"",
            "WS":"3+",
            "BS":"3+",
            "S":"4",
            "T":"4",
            "W":"2",
            "A":"4",
            "Ld":"8",
            "Save":"3+",
            "pts":"20.0"
            }
   
    root = ET.fromstring(test_xml)
    namespace = root.tag.split("}")[0]+"}"

    selectionEntry = root.find(namespace+'sharedSelectionEntries').find(namespace+'selectionEntry')
    received_output = bse.SelectionEntryModelExtractor(selectionEntry,namespace,root)
    assert expected_output == received_output

def test_SelectionEntryExtractorInfoLinks():
    """
    Test that selectionEntry data extraction from infoLinks in selectrionEntry for profile stats and points.  Depends on ProfileExtractor.
    """
    test_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <catalogue id="0cc2-3545-6762-a3f7" name="Imperium - Grey Knights" revision="116" battleScribeVersion="2.03" authorName="BSData Developers" authorContact="@Tekton" authorUrl="https://www.bsdata.net/contact" library="false" gameSystemId="28ec-711c-d87f-3aeb" gameSystemRevision="238" xmlns="http://www.battlescribe.net/schema/catalogueSchema">
            <sharedSelectionEntries>
                    <selectionEntry id="1123-be87-fca2-f102" name="Grey Knight (Daemon Hammer)" hidden="false" collective="false" import="true" type="model">
                        <constraints>
                            <constraint field="selections" scope="parent" value="9.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="fce2-981c-aeff-ca82" type="max"/>
                        </constraints>
                        <infoLinks>
                            <infoLink id="6ec6-2485-3f16-57df" name="Grey Knight" hidden="false" targetId="1037-1f6f-bee5-b1ea" type="profile"/>
                        </infoLinks>
                        <entryLinks>
                            <entryLink id="19eb-8686-c09b-7d18" name="Storm Bolter" hidden="false" collective="false" import="true" targetId="fded-edb8-1d1e-99a5" type="selectionEntry"/>
                            <entryLink id="beb2-6803-3166-085f" name="Nemesis Daemon Hammer" hidden="false" collective="false" import="true" targetId="8fba-9c8d-73bd-fe8e" type="selectionEntry">
                            <constraints>
                                <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="030a-2d90-bd64-8b59" type="max"/>
                                <constraint field="selections" scope="parent" value="1.0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="9750-9cfe-34c1-3aea" type="min"/>
                            </constraints>
                            </entryLink>
                        </entryLinks>
                        <costs>
                            <cost name="pts" typeId="points" value="20.0"/>
                            <cost name=" PL" typeId="e356-c769-5920-6e14" value="0.0"/>
                            <cost name="CP" typeId="2d3b-b544-ad49-fb75" value="0.0"/>
                        </costs>
                    </selectionEntry>
            </sharedSelectionEntries>
            <sharedProfiles>
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
    expected_output = {
            "name":"Grey Knight (Daemon Hammer)",
            "M":"6\"",
            "WS":"3+",
            "BS":"3+",
            "S":"4",
            "T":"4",
            "W":"2",
            "A":"3",
            "Ld":"7",
            "Save":"3+",
            "pts":"20.0"
            }
    
    root = ET.fromstring(test_xml)
    namespace = root.tag.split("}")[0]+"}"

    selectionEntry = root.find(namespace+'sharedSelectionEntries').find(namespace+'selectionEntry')
    received_output = bse.SelectionEntryModelExtractor(selectionEntry,namespace,root)
    assert expected_output == received_output

def test_ProfileExtractor():
    """
    Test that Profile is extracted correctly from profile element
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
            </sharedProfiles>
        </catalogue>
    """
    expected_output = {
        "name":"Grey Knight Terminator",
        "M":"5\"",
        "WS":"3+",
        "BS":"3+",
        "S":"4",
        "T":"4",
        "W":"3",
        "A":"3",
        "Ld":"7",
        "Save":"2+"
        }
    root = ET.fromstring(test_xml)
    namespace = root.tag.split("}")[0]+"}"
    profile = root.find(namespace+'sharedProfiles').find(namespace+'profile')
    received_output = bse.ProfileExtractor(profile,namespace)
    assert expected_output == received_output

def test_WeaponExtractor():
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
            <something>
                <selectionEntry id="9a96-abac-13ca-513d" name="Thunderhawk heavy cannon" hidden="false" collective="false" import="true" type="upgrade">
                    <profiles>
                        <profile id="c03a-36d6-e74a-4e93" name="Thunderhawk heavy cannon" hidden="false" typeId="d5f97c0b-9fc9-478d-aa34-a7c414d3ea48" typeName="Weapon">
                            <characteristics>
                                <characteristic name="Range" typeId="6fa97fa8-ea74-4a27-a0fb-bc4e5f367464">48&quot;</characteristic>
                                <characteristic name="Type" typeId="077c342f-d7b9-45c6-b8af-88e97cafd3a2">Heavy 2D6</characteristic>
                                <characteristic name="S" typeId="59b1-319e-ec13-d466">8</characteristic>
                                <characteristic name="AP" typeId="75aa-a838-b675-6484">-2</characteristic>
                                <characteristic name="D" typeId="ae8a-3137-d65b-4ca7">D3+2</characteristic>
                                <characteristic name="Abilities" typeId="837d-5e63-aeb7-1410">Blast</characteristic>
                            </characteristics>
                        </profile>
                    </profiles>
                    <costs>
                        <cost name=" PL" typeId="e356-c769-5920-6e14" value="0.0"/>
                        <cost name="pts" typeId="points" value="0.0"/>
                        <cost name="CP" typeId="2d3b-b544-ad49-fb75" value="0.0"/>
                    </costs>
                </selectionEntry>
            </something>
        </catalogue>
        """
    expected_output = pd.DataFrame.from_records(
        [
            {"name":"Nemesis Falchion","Range":"Melee","Type":"Melee","S":"User","AP":"-2","D":"1","Abilities":"Each time the bearer fights, if it is equipped with one or more Nemesis flachions, it makes 1 additional attack using this profile"},
            {"name":"Psilencer","Range":"24\"","Type":"Heavy 6","S":"4","AP":"-1","D":"1","Abilities":"-"},
            {"name":"Thunderhawk heavy cannon","Range":"48\"","Type":"Heavy 2D6","S":"8","AP":"-2","D":"D3+2","Abilities":"Blast"}        
        ]
    )
    root = ET.fromstring(test_xml)
    received_output = bse.WeaponExtractor(root)
    pd.testing.assert_frame_equal(expected_output,received_output)
