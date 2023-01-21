import battlescribeextractor as bse
import sys
import time

import xml.etree.ElementTree as ET


def main():
    source_file = sys.argv[1]
    print("Source File: {source_file}".format(source_file=source_file))
    tree = ET.parse(source_file)
    root = tree.getroot()

    x = bse.ModelExtractor(root)
    stats = x.extract()
    print(stats)
    pass

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f'time taken: {end - start:3f} seconds')
