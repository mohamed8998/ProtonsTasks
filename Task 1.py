def min_removals_to_equal_frequency(s: str) -> int:

    freq_dict = {}
    for char in s:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    

    freq_values = list(freq_dict.values())
    
    freq_count = {}
    for freq in freq_values:
        if freq in freq_count:
            freq_count[freq] += 1
        else:
            freq_count[freq] = 1
    
    removals = 0
    max_freq = max(freq_count.keys())
    
    for freq_value in range(max_freq, 0, -1):
        while freq_value in freq_count and freq_count[freq_value] > 1:

            freq_count[freq_value] -= 1
            removals += 1
            if freq_value - 1 > 0:
                if freq_value - 1 in freq_count:
                    freq_count[freq_value - 1] += 1
                else:
                    freq_count[freq_value - 1] = 1
    
    return removals

print(min_removals_to_equal_frequency("aaabbbccc"))    
print(min_removals_to_equal_frequency("aabbccdde"))        
print(min_removals_to_equal_frequency("aaaaabbbbccccc"))   
print(min_removals_to_equal_frequency("abcabcabc"))    