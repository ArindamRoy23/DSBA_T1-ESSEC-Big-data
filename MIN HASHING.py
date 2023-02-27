# Provide here few comment lines that describe your map function

def map_top_companies_by_y(read_lines):
    '''
    Input: Text file split by lines. Readlines() output prefferable, no headers
      Ex: ['1,2020,Data Scientist,MI,FT,"6,352,272.00",DE,DE,L,0\n',
          '2,2020,Machine Learning Scientist,SE,FT,"20,688,070.00",JP,JP,S,0\n']

    Output: List of tuples ( Year,Region)
      Ex: [( '2022','US')]
    '''
    return_list = []
    for i in read_lines:
        return_list.append((i.split(',')[1],
                            reverse_slicing(reverse_slicing(i).split(',')[2])))
    return (return_list)


# #Provide here few comment lines that describe your shuffle function

def shuffle_top_companiesby_y(map_list):
    '''
    Input: List of tuples ( Year,Region)
      Ex: [( '2022','US')]

    Output: Dictionary with key as Destination and value as list of designations
     {Year, [Regions]}
      Ex: {'2022': ['US','US','US','US']}
    '''

    d = {}
    for k, v in map_list:
        try:
            d[k].append(v)
        except:
            d[k] = [v]
    return (d)


# #Provide here few comment lines that describe your reduce function

def reduce_top_connectionsby_y(shuffle):
    '''
    Input: Dictionary with key as Destination and value as list of designations
     {Year, [Regions]}
      Ex: {'2022': ['US','US','US','US']}

    Output: Dict of year and top 5
      Ex: '2020': ['US', 'DE', 'FR', 'GB', 'IN']
    '''
    res = {}
    for k in shuffle:
        temp_dict = {}
        for val in shuffle[k]:
            try:
                temp_dict[val] = temp_dict[val] + 1
            except:
                temp_dict[val] = 1
        li_yr = list({k: v for k, v in sorted(temp_dict.items(),
                                              key=lambda item: item[1],
                                              reverse=True)}.keys())[:5]
        res[k] = li_yr

    return (res)