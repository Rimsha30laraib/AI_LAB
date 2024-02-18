
#COUNT LENGTH OF THE STRING IN THE GIVEN LIST
sample_list = ['abc', 'xyz', 'aba', '1221']
count=0
for s in sample_list:
    if len(s) >= 2 and s [0] == s [-1]:
       count=count+1
print ("Expected Result:", count)

