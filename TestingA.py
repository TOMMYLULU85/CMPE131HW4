def someSort(covid_nums):
    #Removed arr because in order to test the list and we would need to define it as its variable and this case it's covid_nums
    #len allows us to read the number of items in the array and I removed it because it wouldn't count all of the items in the array
    n = len(covid_nums)
    
    for i in range(n):
        swapped = True
  
        for j in range(0, n-i-1):
            #Changed arr to covid_nums since it's the list that we're testing
            if covid_nums[j] > covid_nums[j+1] :
                covid_nums[j], covid_nums[j+1] = covid_nums[j+1], covid_nums[j]
                swapped = True
#Added in the output in order to test the function   
        if swapped == False:
            break       
covid_nums = [ 88, 85, 123, 96, 104, 81]
someSort(covid_nums)
print(covid_nums) # [81, 85, 88, 96, 104, 123]