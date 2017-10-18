import re
'''
Grab everything in between the numbers and Blah
'''
exampleString = '''
1	
Group 1
Blah
2	
Group 2
Blah
3	
Group 3
Blah
4
'''
result = re.findall(r'\d*(.*?)\nBlah', exampleString)
for i in result:
    print(i)
