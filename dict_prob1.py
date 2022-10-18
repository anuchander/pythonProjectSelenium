'''

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
'''

roll_number=[47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
new_list=[]

for i in sample_dict.keys():
    if sample_dict[i] in roll_number:
        new_list.append(sample_dict[i])

print(new_list)

