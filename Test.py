print('hello world')

# Use x[0~100] to access item inside of a tuple
tuple_list = [(12.8, 'a'), (-.178,'b'),(1.8,'c'),(-782.7,'d'),(99.8,'e'),(8.7,'f')]
output = []
while len(output) < len(tuple_list):
    output.append(x for x in tuple_list if x[0] == 1.8)
print(output)

exit()
tuple_list = [(12.8, 'a'), (-.178,'b'),(1.8,'c'),(-782.7,'d'),(99.8,'e'),(8.7,'f')]
x = 0
while x < len(tuple_list):
    print(tuple_list[x])
    x = x + 1

exit()
tuple_list = [(12.8, 'a'), (-.178,'b'),(1.8,'c'),(-782.7,'d'),(99.8,'e'),(8.7,'f')]
repl_rec = ('is', 2)
N = 1 
# Create an empty list to store the updated tuples
res = []
# Iterate over each tuple in the original list
for x in tuple_list:
    # Check if the Nth element of the tuple matches the Nth element of the replacement tuple
    if x[N] == repl_rec[N]:
        # If it matches, add the replacement tuple to the result list
        res.append(repl_rec)
    else:
        # If it doesn't match, add the original tuple to the result list
        res.append(x) 
# Print the updated list of tuples
print("The tuple after replacement is : " + str(res))

exit()

tuple_list = [(12.8, 'a'), (-.178,'b'),(1.8,'c'),(-782.7,'d'),(99.8,'e'),(8.7,'f')]
repl_rec = ('is', 2) # initializing change record
N = 1 # initializing N
 
# using filter function with lambda to remove tuples that don't match value of Nth element, and then adding repl_rec tuple to the list
tuple_list = list(filter(lambda x: x[N] != repl_rec[N], tuple_list)) + [repl_rec]
 
print("The tuple after replacement is : " + str(tuple_list)) # printing result

exit()
# List initialization
numbers =  [12.8, -.178, 1.8, -782.7, 99.8, 8.7]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f'] 
output = []
for y in zip(numbers, alphabet):
    output.append(y.sort())
    print(output)
        
exit()

for numbers in numbers:
    output = sorted(numbers, key = lambda x:float(x))

# Printing output
print(output)



x = [5, 2, 3]
for numbers in x:
    numbers:float(numbers)
    print(numbers)

exit()



numbers = 3, 4, 7, 1, 6, 2
n = len(numbers)
for i in range(n):
    for j in range(0, n-i-1):
        n = len(numbers)
        if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]