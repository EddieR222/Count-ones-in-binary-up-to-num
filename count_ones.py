def ones_from_zero_to_num(num):
    bin_num = bin(num)
    bin_num_only_bin = bin_num[2:]
    len_bin_num = len(bin_num_only_bin)
    total_ones = 0;
    for i in range(0, len_bin_num):
        two_power = (2**(i+1))
        num_plus_one = num + 1 
        if num_plus_one % two_power == 0:
            total_ones = total_ones + ((num_plus_one)/two_power )* (two_power/2)
        else:
            floor_div = math.floor(num_plus_one/two_power);
            ones_in_full_groups = floor_div * (two_power/2);
            full_groups = floor_div * two_power;
            add_two = (num_plus_one - full_groups) - (two_power/2);
            if add_two > 0:
                total_ones = total_ones + ones_in_full_groups + add_two;
            else:
                total_ones = total_ones + ones_in_full_groups;
    return int(total_ones);
