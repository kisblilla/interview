

def object_area(input):
    #check the input numbers
    towers_heights=input
    if towers_heights==[] or any(x<1 for x in towers_heights)==True:
        raise ValueError("The list is empty or there's negative or zero input")
        
    #check the input towers number
    towers_number=len(towers_heights)
    if towers_number == 1:
        return one_tower(towers_heights)
    if towers_number>1:
        return more_tower(towers_heights)


#if there is only one element in the input (one tower)
def one_tower(towers_heights):
    if towers_heights[0]==1:
        return 6
    elif towers_heights[0]==2:  
        return 10
    else:
        one_tower_surface = ((towers_heights[0]-2)*4+10) 
        return (one_tower_surface)



def more_tower_calculation(n):
        one_tower_surface = ((n-2)*4+10) 
        return (one_tower_surface)


#if there is more element in the list (more tower)
#it compares the heights of the towers, then from within calculate the connection level/surface
def more_tower(towers_heights):
    connection_surface=0
    previous=0
    for i in towers_heights:
        if i<previous:
            previous=i
            connection_surface=connection_surface+i
        else:
            connection_surface=connection_surface+previous
            previous=i
   
    surface=0
    for i in towers_heights:
        surface=surface+more_tower_calculation(i)
    all_surface=surface-2*connection_surface
    return all_surface
    


#tests
assert object_area([1])==6
assert object_area([9])==38
assert object_area([1,2])==14
assert object_area([9,9])==58
assert object_area([9,9])==58
assert object_area([6,1,12])==78
assert object_area([1,1,1,1,1])==22
assert object_area([3,7,10])==66
print("OK")

