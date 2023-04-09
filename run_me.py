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

    source_folder= sys.argv[1]
    print("Source Folder: {source_folder}".format(source_folder=source_folder))
    bse.FolderExtractor(source_folder)
       
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f'time taken: {end - start:3f} seconds')
