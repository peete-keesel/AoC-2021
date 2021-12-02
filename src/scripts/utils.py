
PREFIX_PATH = 'src/resources/'
DAY_1_DATA = 'day1_sonar_sweep.txt'
DAY_2_DATA = 'day2_dive.txt'

def read_txt_file_into_list(path, day=1): 
    if day == 1: 
        data = []
        with open(path, 'r') as f: 
            data = f.readlines()
            data = [int(line.rstrip()) for line in data]
        return data
    elif day == 2: 
        directions, units = [], []
        with open(path, 'r') as f: 
            data = f.readlines()
            for l in data: 
                row = l.split(' ')
                directions.append(row[0])
                units.append(int(row[1].rstrip()))
        return directions, units