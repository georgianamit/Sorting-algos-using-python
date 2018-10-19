def selection_sort(ls):
    for i in range(len(ls)):
        min = i
        for j in range(i+1,len(ls)):
            if ls[min] > ls[j]:
                min = j

        ls[i],ls[min] = ls[min],ls[i]

def print_list(ls):
    for i in ls:
        print(i, end=" ")
        
ls = [34, 65, 26, 65, 59]
selection_sort(ls)
print_list(ls)
