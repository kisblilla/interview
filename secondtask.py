# Check the obstacle input, if it is None give a value
# Call the functions, which pass the counter and add the number of possible steps of the queen
def all_possible_steps(n, rq, cq, obstacles=None):
    if obstacles is None:
        obstacles=[(0,0)]
    counter=0
    obstacles = sorted(obstacles)
    counter=positive_diagonal_right(n, rq, cq, obstacles, counter)
    counter=positive_diagonal_left(n, rq, cq, obstacles, counter)
    counter=negative_diagonal_right(n, rq, cq, obstacles, counter)
    counter=negative_diagonal_left(n, rq, cq, obstacles, counter)
    counter=horizontal_left(n, rq, cq, obstacles, counter)
    counter=horizontal_right(n, rq, cq, obstacles, counter)
    counter=vertical_down(n, rq, cq, obstacles, counter)
    counter=vertical_up(n, rq, cq, obstacles, counter)
    return(counter)

# Compare the current step (arr) to all obstacles, if there is match returns True
def compare(arr, obstacles):
    for k in range(len(obstacles)):
        obstac=(obstacles[k][0], obstacles[k][1])
        comparison=arr==obstac
        if comparison==True:
            return True

def positive_diagonal_right(n, rq,cq, obstacles,counter):
    i=1
    while ((rq+i)<=n and (cq+i)<=n):
        arr=(rq+i,cq+i)
        if compare(arr,obstacles)==True:
            return counter  
        counter= counter +1
        i=i+1
    return counter


def positive_diagonal_left(n, rq,cq, obstacles, counter):
    i=1
    while ((rq-i)>0 and (cq-i)>0):
        arr=(rq-i,cq-i)
        if compare(arr,obstacles)==True:
                return counter  
        counter=counter+1
        i=i+1
    return counter

 
def negative_diagonal_right(n, rq, cq, obstacles, counter):

    i=1
    while ((cq-i)>0 and (rq+i)<n) :
        arr=(rq+i,cq-i)
        if compare(arr,obstacles)==True:
                return counter  
        counter= counter +1
        i=i+1
    return (counter)

def negative_diagonal_left(n, rq, cq, obstacles, counter):

    i=1
    while (rq-i)>0 and (cq+i)<n:
        arr=(rq-i,cq+i)
        if compare(arr,obstacles)==True:
                return counter  
        counter= counter +1
        i=i+1
    return (counter)

def horizontal_right(n, rq, cq, obstacles, counter):

    i=1
    while (cq-i)>0:
        arr=(rq,cq-i)
        if compare(arr,obstacles)==True:
                return counter  
        counter= counter +1
        i=i+1
    return (counter)

def horizontal_left(n, rq, cq, obstacles, counter):

    i=1
    while (cq+i)<=n:
        arr=(rq,cq+i)
        if compare(arr,obstacles)==True:
                return counter  
        counter= counter +1
        i=i+1
    return (counter)
    

def vertical_down(n, rq, cq, obstacles, counter):

    i=1
    while (rq+i)<=n:
        arr=(rq+i,cq)
        if compare(arr,obstacles)==True:
                return counter  
        counter= counter +1
        i=i+1
    return (counter)


def vertical_up(n, rq, cq, obstacles, counter):

    i=1
    while (rq-i)>0:
        arr=(rq-i,cq)
        if compare(arr,obstacles)==True:
                return counter  
        counter= counter +1
        i=i+1
    return (counter)


#tests
assert all_possible_steps(2, 1,1)==3
assert all_possible_steps(3, 2,2, [(0,0),(0,0)])==6
assert all_possible_steps(8, 4,4, [(6,6)])==24
assert all_possible_steps(8, 4,4, [(3,5)])==24
assert all_possible_steps(8, 4,4, [(3,5), (6,6)])==21
assert all_possible_steps(14, 7,7)==51
assert all_possible_steps(14, 14,14)==39
assert all_possible_steps(14, 14,14, [(7,7), (14,7), (7,14)])==18
print("OK")
