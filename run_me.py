import battlescribeextractor as bse
import time

def main():
    x = bse.ModelExtractor()
    pass

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f'time taken: {end - start:3f} seconds')
