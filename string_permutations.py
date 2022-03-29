def string_permutations(strs_list,n,fixed=None,up_to_n=False):
    """
    string_permutations(['a','b','c'],2) = 'aa','ab','ac','ba','bb','bc','ca','cb','cc']
    """
    if not fixed:
        fixed = ['']
    out = []
    
    loop_count = 0
    while loop_count <n:
        temp = []
        for f in fixed:
            for string in strs_list:
                out.append(f+string)
                temp.append(f+string)
        fixed = []
        loop_count += 1
        fixed.extend([t for t in temp])
    
    if not up_to_n:
        return fixed
    else:
        return out
