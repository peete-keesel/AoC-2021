"""
https://adventofcode.com/2021/day/3
"""
ZERO = '0'
ONE = '1'

def find_day3_binary_diagnostic_solution_part_1(data): 
    """Returns the used power consumption."""
    gamma_bin, eps_bin = '', ''
    pos_count = {}

    for bin_num in data:
        for j, bit in enumerate(bin_num):
            if j not in pos_count.keys(): pos_count[j] = {ZERO: 0, ONE: 0}
            if bit == ZERO: pos_count[j][ZERO] += 1
            elif bit == ONE: pos_count[j][ONE] += 1

    for k, v in pos_count.items(): 
        print(f"{k}  {v}")
        if v[ZERO] > v[ONE]:
            gamma_bin += ZERO
            eps_bin += ONE
        elif v[ZERO] < v[ONE]: 
            gamma_bin += ONE
            eps_bin += ZERO

    gamma_dec, eps_dec = int(gamma_bin, 2), int(eps_bin, 2)

    return gamma_dec*eps_dec

def find_day3_binary_diagnostic_solution_part_2(data): 
    """Returns the life support rating."""
    oxy, co2 = 0, 0
    gamma_bin, eps_bin = '', ''

    oxy_data = data
    nth_bit = 0
    while len(oxy_data) > 1:
        pos_count = {}
        for i, bin_num in enumerate(oxy_data):
            for j, bit in enumerate(bin_num):
                if j < nth_bit: continue
                if j not in pos_count.keys(): 
                    pos_count[j] = {ZERO: [0, set()], ONE: [0, set()]}
                if bit == ZERO: 
                    pos_count[j][ZERO][0] += 1
                    pos_count[j][ZERO][1].add(i)
                elif bit == ONE: 
                    pos_count[j][ONE][0] += 1
                    pos_count[j][ONE][1].add(i) 

        old_data = oxy_data
        oxy_data = []
        for k, v in pos_count.items(): 
            # Oxygen
            if v[ZERO][0] > v[ONE][0]:
                oxy_data = [old_data[i] for i in list(v[ZERO][1])]
            elif v[ZERO][0] <= v[ONE][0]: 
                oxy_data = [old_data[i] for i in list(v[ONE][1])]
            break

        nth_bit += 1

    print(f"oxygen generator rating = {oxy_data} = {int(oxy_data[0], 2)}")

    co2_data = data
    nth_bit = 0
    while len(co2_data) > 1:
        pos_count = {}
        for i, bin_num in enumerate(co2_data):
            for j, bit in enumerate(bin_num):
                if j < nth_bit: continue
                if j not in pos_count.keys(): 
                    pos_count[j] = {ZERO: [0, set()], ONE: [0, set()]}
                if bit == ZERO: 
                    pos_count[j][ZERO][0] += 1
                    pos_count[j][ZERO][1].add(i)
                elif bit == ONE: 
                    pos_count[j][ONE][0] += 1
                    pos_count[j][ONE][1].add(i) 

        old_data = co2_data
        co2_data = []
        for k, v in pos_count.items(): 
            # CO2
            if v[ZERO][0] <= v[ONE][0]:
                co2_data = [old_data[i] for i in list(v[ZERO][1])]
            elif v[ZERO][0] > v[ONE][0]: 
                co2_data = [old_data[i] for i in list(v[ONE][1])]
            break

        nth_bit += 1

    return int(oxy_data[0], 2) * int(co2_data[0], 2)      