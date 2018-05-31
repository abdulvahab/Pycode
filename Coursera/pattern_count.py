import re
def pattern_count(pattern,string):

    return len(re.findall("(?=%s)" % pattern, string))
print(pattern_count('ATA','CGATATATCCATAG'))
