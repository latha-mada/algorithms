#!/usr/bin/python


count=0
def bubble_sort(list):
 global count
 print "initial list is %r" %list
 for j in range(len(list), 1, -1):
  #print "next iteration"
  for i in range(0, j-1):
    if (list[i]>list[i+1]):
      list[i], list[i+1] = list[i+1], list[i]
      #print list
      count+=1
    else:
      #print list
      count+=1
   
 print "total comparisons=%d" %count
 return list 

def quick_sort(list):
 global count
 less=[]
 equal=[]
 more=[]
 
 if len(list) > 1:
   pivot=list[0]
   print "pivot= %d"%pivot
   for value in list:
     if value>pivot:
       more.append(value)
     elif value<pivot:
       less.append(value)
     else:
       equal.append(value)
   return quick_sort(less)+equal+quick_sort(more)
 else:
   return list
       
def sort(array=[12,4,5,6,7,3,1,15]):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

list=[2,7,3,5,1]
#list1=bubble_sort(list)
#less=[]
#more=[]
#equal=[]
print "initial list is %r" %list
list2=quick_sort(list)
print list2
