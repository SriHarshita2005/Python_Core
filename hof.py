# Given two lists: a = [1, 2, 3, 4] b = [10, 20, 30, 40]
# Use map() with a lambda to create a new list containing
# the sum of corresponding elements.
# What happens if the lists are of unequal length?

# a=[1,2,3,4]
# b=[10,20,30,40]
# n=list(map(lambda x,y : x+y , a,b))
# print(n)


# Given a list: nums = [12, 15, 7, 18, 20, 21, 25]
# Use filter() and lambda to keep numbers that are divisible
# by 3 OR divisible by 5 but NOT divisible by both.
# Explain how the logical condition works.

# nums=[12,15,7,18,20,21,25]
# result=list(filter(lambda x : (x%3==0 or x%5==0 ) and not (x%3==0 and x%5==0) , nums))
# print(result)

# Given a list: nums = [1, 2, 3, 4] Use reduce() with a lambda to compute the sum,
#  but start with an initial value of 10.
#  Explain how the initial value affects the reduction process.
 
# nums=[1,2,3,4]
# from functools import reduce
# result=reduce(lambda x,y: x+y , nums , 100)
# print(result)


# Consider the code below: nums = [[1, 2], [3, 4], [5, 6]]
# result = list(map(lambda x: x.append(10), nums))
# print("Result:", result) print("Nums:", nums)
# Questions • What will be the output of result? • What will be the output of nums? •
# Why does map() behave this way with list.append()? •
# How can you modify the lambda so that nums is not changed?

# nums = [[1, 2], [3, 4], [5, 6]]
# result = list(map(lambda x: x.append(10), nums))
# print("Result:", result)
# print("Nums:", nums)


#Use map() with a lambda to add 5 to every element of the following nested list
# [[1, 2], [3, 4], [5, 6]]

l=[[1,2],[3,4],[5,6]]
result=list(map(lambda subs: list(map(lambda x: x+5, subs)),l))
print(result)

'''

''' 
 Given a dictionary: d = {"apple": 100, "banana": 40, "cherry": 150} . 
 Use filter() to keep only the keys whose values are greater than 50.

d = {"apple": 100, "banana": 40, "cherry": 150}
result=list(filter(lambda key: d[key]>50 , d))
print(result)
'''

''' 
Use functools.reduce() with a lambda to find the largest number from a 
given list Dynamically.

from functools import reduce
nums=list(map(int,input("Enter numbers:").split()))
result=reduce(lambda x,y : x if(x>y) else y , nums)
print(result)

'''

'''
Use map() on a string to convert each character into its ASCII value
 (using ord()). Print the result list.

nums=[65,66,67]
result=list(map(lambda nums: ord(chr(nums)) , nums))
print(result)

nums=['a','b','c']
result=list(map(lambda nums: ord(nums) , nums))
print(result)
'''

'''
Use filter() to remove all vowels from a string and print the final string.


s=input()
vowels="aeiouAEIOU"
result=list(filter(lambda ch: ch not in vowels, s))
print(result)

'''

''' 
 Use reduce() to concatenate a list of characters into a single string.
Example input: ['P', 'y', 't', 'h', 'o', 'n'].

from functools import reduce
chars=['p','y','t','h','o','n']
result=reduce(lambda x,y:x+y,chars)
print(result)
'''

'''
Given a list of integers, use map() with id() to print the memory address
of each element. Example: [10, 350, 10, 350, 20] — explain why some addresses repeat.

nums = [10, 350, 10, 350, 20]
addresses = list(map(lambda x: id(x), nums))
print(addresses)
'''

''' 

'''



