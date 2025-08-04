my_tuple =(1,'hi',69)
print(my_tuple)
#nested tuple
my_tuple=('tall',1,[2,'good','how are you'])
print(my_tuple)
# Accessing elements in a tuple
my_tuple =('p','q','r','s','t')
print(my_tuple[0])
print(my_tuple[2])
#nested tuple
my_tuple =('mouse',{2,3,4,4},(90,87))
#nested index
print("Nested tuple:")
print(my_tuple)
#slicing
print("sliced :", my_tuple[0:3])
#Iterating through a tuple
for letter in(my_tuple):
    print('hello',letter)