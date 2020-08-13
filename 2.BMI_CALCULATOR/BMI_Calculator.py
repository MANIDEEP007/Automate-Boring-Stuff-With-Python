import numbers

"""
Find BMI Index
"""
def findBMI(weight_in_kg,height_in_cm):
    """
    Takes Weight in Kg and Height and returns
    BMI Index
    """
    #Check whether height and wieght are numbers and then calculate BMI
    if isinstance(weight_in_kg,numbers.Number) and \
       isinstance(height_in_cm,numbers.Number):
        return round(weight_in_kg/(height_in_cm/100)**2,1)
    else:
        return "Error. Both Height and Weight should be Numbers"

"""
Find and Analyze BMI Index
"""
def analyzeBMI(weight_in_kg,height_in_cm):
    """
    Takes Weight in Kg and Height and Returns
    BMI Index & Ideal Range of weight as per CDC
    """
    result = ""
    bmi_value = findBMI(weight_in_kg,height_in_cm)
    #Check BMI is Number or not and then analyze it
    if not isinstance(bmi_value,numbers.Number):
        return "Error. Both Height and Weight should be Numbers"
    result = "Your BMI is " + str(bmi_value) + "\n"
    if bmi_value < 18.5:
        result += "You are Underweighed\n"
    elif bmi_value >= 18.5 and bmi_value <= 24.9:
        result += "You are in Healthy Weight Range\n"
    elif bmi_value >= 25.0 and bmi_value <= 29.9:
        result += "You are Overweighed\n"
    else:
        result += "You are Obese\n"
    min_weight = 18.5 * (height_in_cm/100) ** 2
    max_weight = 24.9 * (height_in_cm/100) ** 2
    result += "Your Weight should be between " + \
           str(round(min_weight,1)) +\
           " and " +\
           str(round(max_weight,1))
    return result

print(analyzeBMI(81,170.18))
"""
Your BMI is 28.0
You are Overweighed
Your Weight should be between 53.6 and 72.1
"""
