#Writen under python 2.2.6

from Sort import Sort
import random

a = Sort()

b = [random.random() for _ in xrange(500)]

print ('PreSort: ')
print (b)
    
bubble = a.bubble_sort(b)

print ('Bubble Sort: ')
print (bubble)

merge = a.merge_sort(b)

print ('Merge Sort: ')
print (merge)