


x = [ [5,2,3], [10,8,9] ] 

x[1][0]=15
print(x)

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name']='Bryant'
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


def iterateDictionary2(students):
      for i in range(0, len(students)):
           print("first_name -",students[i]['first_name'],", last_name -",students[i]['last_name'])
       
def iterateDictionary(students):
   for i in range(0, len(students)):
           print(students[i]['first_name'],":",students[i]['last_name'])
    
def firstname(students):
   for i in range(0, len(students)):
           print(students[i]['first_name'])
def lastname(students):
   for i in range(0, len(students)):
           print(students[i]['last_name'])


students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def printInfo(dojo):
    for i in dojo:
        print(len(dojo[i]),i)
       
        for j in range(0,len(dojo[i])):
           print(dojo[i][j])
        print("\n")
        


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)
iterateDictionary(students) 
iterateDictionary2(students)

