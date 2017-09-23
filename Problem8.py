def mergeSort(l1,l2):
    l3 = l1 + l2
    l3.sort()
    print("sorted merged list",l3)
    
listone , listtwo = [1, 8, 2] , [6, 9, 4] 
mergeSort(l1=listone,l2=listtwo)
