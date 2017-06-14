#function to sort through a list of numbers and return the max and min numbers
def find_max_min(a_list):

    #if maximum number==the minimun number
    if max(a_list)== min(a_list):

        return (len(a_list))
    
    else:
       
        return ([min(a_list), max(a_list)], 'for', a_list)


            
