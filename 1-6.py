def find_max(list, n):
    if n == 1:
        return list[0]
    else:
        return max(list[n - 1], find_max(list, n - 1))

print(find_max([4, 1, 9, 2, 7],5))

'''
find_max([4,1,9,2,7], 5) = max(7, find_max(..., 4))
 find_max([4,1,9,2], 4) = max(2, find_max(..., 3))
 find_max([4,1,9], 3) = max(9, find_max(..., 2))
 find_max([4,1], 2) = max(1, find_max(..., 1))
 find_max([4], 1) = 4

بازگشت:
max(1, 4) = 4  
max(9, 4) = 9  
max(2, 9) = 9  
max(7, 9) = 9


find_max([4,1,9,2,7], 5)
 max(7, 
      find_max([4,1,9,2], 4)
          max(2, 
               find_max([4,1,9], 3)
                   max(9,
                        find_max([4,1], 2)
                            max(1, find_max([4], 1)) → 4

'''