import numpy as np

# Task no 1
def function1():
    # create 2d array from 1,12 range 
    # dimension should be 6row 2 columns  
    # and assign this array values in x values in x variable
    # Hint: you can use arange and reshape numpy methods  
    x =  np.arange(1,13).reshape((6,2)) 

    return x
    """
    expected output:
    [[ 1  2]
    [ 3  4]
    [ 5  6]
    [ 7  8]
    [ 9 10]
    [11 12]]
    """
print(function1())


# Task2
def function2():
    #create 3D array (3,3,3)
    #must data type should have float64
    #array value should be satart from 10 and end with 36 (both included)
    # Hint: dtype, reshape 
    
    x = np.arange(10,37,dtype=np.float64).reshape((3,3,3))     
    
    #wrtie your code here


    return x
    """
    Expected: out put
    array([[[10., 11., 12.],
            [13., 14., 15.],
            [16., 17., 18.]],
           [[19., 20., 21.],
            [22., 23., 24.],
            [25., 26., 27.]],
           [[28., 29., 30.],
            [31., 32., 33.],
            [34., 35., 36.]]])    
    """
    
print(function2())





#task4
def function4():
    #Swap columns 1 and 2 in the array arr.
   
    arr = np.arange(9).reshape(3,3)
    arr[:,[0, 1]] = arr[:,[1, 0]]
    return arr
    """
    Expected Output:
          array([[1, 0, 2],
                [4, 3, 5],
                [7, 6, 8]])
    """

print(function4())



#task5
def function5():
    #Create a null vector of size 20 with 4 rows and 5 columns with numpy function
   
    z = np.zeros(20).reshape(4,5)
  
    return z
    """
    Expected Output:
          array([[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]])
    """ 

print(function5())




#task7
def function7():
    #  Create an array of zeros with the same shape and type as X. Dont use reshape method
    x = np.arange(4, dtype=np.int64)
  
    return np.zeros_like(x) #write your code here

    """
    Expected Output:
          array([0, 0, 0, 0], dtype=int64)
    """ 

print(function7())




#task8
def function8():
    # Create a new array of 2x5 uints, filled with 6.
    
    x = np.full((2, 5), 6)
  
    return x

    """
    Expected Output:
          array([[6, 6, 6, 6, 6],
                 [6, 6, 6, 6, 6]], dtype=uint32)
    """ 
print(function8())



#task9
def function9():
    # Create an array of 2, 4, 6, 8, ..., 100.
    
    a = np.arange(2,101,2)
  
    return a
    
print(function9())



#task10
def function10():
    # Subtract the 1d array brr from the 2d array arr, such that each item of brr subtracts from respective row of arr.
    
    arr = np.array([[3,3,3],[4,4,4],[5,5,5]])
    brr = np.array([1,2,3])
    subt = arr - brr[:,None]
  
    return subt

    """
    Expected Output:
    array([[2 2 2]
          [2 2 2]
          [2 2 2]])
    """ 

    
print(function10())



#task11
def function11():
    # Replace all odd numbers in arr with -1 without changing arr.
    
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    arr[arr % 2 == 1] = -1 
  
    return arr

    """
    Expected Output:
          array([ 0, -1,  2, -1,  4, -1,  6, -1,  8, -1])
    """ 
    
print(function11())



#task12
def function12():
    # Create the following pattern without hardcoding. Use only numpy functions and the below input array arr.
    # HINT: use stacking concept
    
    arr = np.array([1,2,3])
    ans = np.r_[np.repeat(arr, 3), np.tile(arr, 3)]
  
    return ans

    """
    Expected Output:
          array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])
    """ 
    
print(function12())



#task13
def function13():
    # Set a condition which gets all items between 5 and 10 from arr.
    
    
    arr = np.array([2, 6, 1, 9, 10, 3, 27])
    ans = arr[(arr >= 5) & (arr < 10)] 
  
    return ans

    """
    Expected Output:
          array([6, 9])
    """
    
print(function13())



#task14
def function14():
    # Create an 8X3 integer array from a range between 10 to 34 such that the difference between each element is 1 and then Split the array into four equal-sized sub-arrays.
    # Hint use split method
    
    
    arr = np.arange(10, 34, 1) #write reshape code
    ans = arr.reshape(8,3)
  
    return np.split(ans, 4)

    """
    Expected Output:
    [array([[10, 11, 12],[13, 14, 15]]), 
    array([[16, 17, 18],[19, 20, 21]]), 
    array([[22, 23, 24],[25, 26, 27]]), 
    array([[28, 29, 30],[31, 32, 33]])]
    """
    
print(function14())



#task15
def function15():
    #Sort following NumPy array by the second column
    
    
    arr = np.array([[ 8,  2, -2],[-4,  1,  7],[ 6,  3,  9]])
    ans = arr[arr[:,1].argsort()]
  
    return ans

    """
    Expected Output:
       array([[-4,  1,  7],
               [ 8,  2, -2],
               [ 6,  3,  9]])
    """ 
    
print(function15())



#task16
def function16():
    #Write a NumPy program to join a sequence of arrays along depth.
    
    
    x = np.array([[1], [2], [3]])
    y = np.array([[2], [3], [4]])
    ans = np.dstack((x, y))
  
    return ans

    """
    Expected Output:
            [[[1 2]]
             [[2 3]]
             [[3 4]]]
    """ 
    
print(function16())