person={'first_name': 'Asabeneh','last_name': 'Yetayeh','age': 250,'country': 'Finland','is_married': True,'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],'address': {'street': 'Space street','zipcode': '02210'}}
if 'skills' in person:
    print(person['skills'][(int((len(person['skills'])+1)/2))-1])
if 'Python' in person['skills']:
    print(person["skills"])
if person['country']=='Finland' and person['is_married']==True:
    print(person)
