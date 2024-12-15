st_dict={'first_name':'Asabeneh','last_name':'Yetayeh','age':250,'country':'Finland','skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],'address':{'street':'Space street','zipcode':'02210'}}
print(st_dict,len(st_dict))
print(st_dict['skills'])
print(type(st_dict['skills']))
st_dict['skills'].append('sql')
print(st_dict['skills'])
print(st_dict.keys())
print(st_dict.values())
st_list=st_dict.items()
print(st_list)
st_dict.pop('last_name')
print(st_dict)
del st_dict