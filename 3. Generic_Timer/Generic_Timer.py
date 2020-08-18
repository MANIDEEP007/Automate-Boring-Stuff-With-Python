import time

#Generic Timer
def Timer(func):
    #Function to calculate time for the execution of function
    def runner(*args,**kargs):
       start = time.time() #Note Start Time
       result = func(*args,**kargs) #Call the Function
       end = time.time() #Note End Time
       return (result,round((end-start),2)) #Return Output and execution time as Tuple
    return runner

#Applying Generice Timer to Function
@Timer
def delay(loop_num,num_sec):
   for _ in range(loop_num):
      time.sleep(num_sec)
   return "Invoked Delay for " + str( loop_num * num_sec) + " Seconds"

#Invoke Delay Function & Unpack the Results
Output, Time = delay(5,2)
#Print the Results
print("The Output is %s" % Output)
print("The timer for the execution of Delay function is %s" % Time)
