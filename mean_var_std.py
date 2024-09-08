import numpy as np

def  Calculate():
    List = input("Enter the 9 random numbers:").split(',')
    if len(List) == 9:
        # Convert the list of strings to a list of integers or floats if needed
        array = np.array(list(map(int, List)))
        Matrix = np.reshape(array, (3, 3))  # to reshapee the list received from the user
        Mean = {}
        mean_axis0  = np.mean(Matrix,axis = 0).tolist()      # to find the mean along the axis = 0, tolist is used to convert array into list
        mean_axis1 = np.mean(Matrix,axis = 1).tolist()       # to find the mean along the axis = 1
        mean_flattened = np.mean(array).tolist()             # to find the mean along the list
        Mean ['axis0'] = mean_axis0
        Mean ['axis1'] = mean_axis1
        Mean ['flattened'] = mean_flattened
        Variance = {}
        variance_axis0 = np.var(Matrix,axis = 0).tolist()    # to find the variance along the axis = 0
        variance_axis1 = np.var(Matrix,axis = 1).tolist()    # to find the variance along the axis = 1
        variance_flattened = np.var(array).tolist()          # to find the variance along the flattened list
        Variance ['axis0'] = variance_axis0
        Variance ['axis1'] = variance_axis1
        Variance ['flattened'] = variance_flattened
        Standard_deviation = {}
        stand_dev_axis0 = np.std(Matrix,axis = 0).tolist()    # to find the Standard deviation  along the axis = 0
        stand_dev_axis1 = np.std(Matrix,axis = 1).tolist()    # to find the Standard deviation  along the axis = 1
        stand_dev__flattened = np.std(array).tolist()         # to find the Standard deviation  along the flattened list
        Standard_deviation  ['axis0'] = stand_dev_axis0
        Standard_deviation  ['axis1'] = stand_dev_axis1
        Standard_deviation  ['flattened'] = stand_dev__flattened
        Max = {} 
        max_axis0 = np.max(Matrix,axis = 0).tolist()           # to find the max  along the axis = 0
        max_axis1 = np.max(Matrix,axis = 1).tolist()           # to find the max along the axis = 1
        max_flattened= np.max(array).tolist()                  # to find the max  along flattened list
        Max ['axis0'] = max_axis0 
        Max ['axis1'] = max_axis1
        Max ['flattened'] = max_flattened
        Min = {}
        min_axis0 = np.min(Matrix,axis = 0).tolist()           # to find the min  along the axis = 0
        min_axis1 = np.min(Matrix,axis = 1).tolist()           # to find the min  along the axis = 1
        min_flattened= np.min(array).tolist()                  # to find the min  along the flatnned list
        Min ['axis0'] = min_axis0 
        Min ['axis1'] = min_axis1
        Min ['flattened'] = min_flattened
        Sum = {}
        sum_axis0 = np.sum(Matrix,axis = 0).tolist()         # to find the sum along the axis = 0
        sum_axis1 = np.sum(Matrix,axis = 1).tolist()          # to find the sum along the axis = 1
        sum_flattened= np.sum(array).tolist()                  # to find the sum  along the flattened line
        Sum ['axis0'] = sum_axis0 
        Sum ['axis1'] = sum_axis1
        Sum ['flattened'] = sum_flattened
        print('Mean:', Mean)
        print('Variance:', Variance)
        print('Standard deviation:',Standard_deviation)
        print('Max:', Max)
        print('Min:', Min)
        print('sum:', Sum)
        
        
        
        
       
    else:
        # If the length is not 9,show error
        print("Please enter exactly 9 numbers.")
        print("You entered", len(List), "numbers.")
    


        
        
        
    
        
        
        



                    
    
    


