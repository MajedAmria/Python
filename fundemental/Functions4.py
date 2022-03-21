


x = [ [5,2,3], [10,8,9] ] 
for key in x:
    if key[0]==10:
       key[0]=15
    print(key)
"""
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name']='Braynt'
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0]='andres'
print(sports_directory)
z = [ {'x': 10, 'y': 20} ]  
z[0]['y']='30'                                                                                                                                                                                                                                                                                                                                                                               
print(z)
"""
"""
def iterateDictionary2(key, some_list):
    for i in some_list:
       return some_list[key]
def iterateDictionary(students):
    for key in students:
        print(key)
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 
print(iterateDictionary2('first_name', students))
"""