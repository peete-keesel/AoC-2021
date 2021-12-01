
PREFIX_PATH = 'src/resources/'
DAY_1_DATA = 'day1_sonar_sweep.txt'


def read_txt_file_into_list(path): 
    data = []
    with open(path, 'r') as f: 
        data = f.readlines()
        data = [int(line.rstrip()) for line in data]

    return data