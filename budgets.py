# Set monthly limits per category
# Track remaining budget
# Warn when approaching limits
import db_connection, mysql.connector
from db_connection import mycursor

def save_budget_provisions():
    #Find a way to place restrictions of housing,insurance and savings question if they do not do it
    global total_budget,income,savings,insurance,transport,housing,food,toiletries,leisure
    income=float(input('Enter your income amount'))
    savings=float(input("Enter the budget for Savings"))
    insurance=float(input("Enter the budget for Insurance"))
    transport=float(input("Enter the budget for Transport"))
    housing =float(input("Enter the budget for Housing"))
    food=float(input("Enter the budget for Food"))
    toiletries=float(input("Enter the budget for Toiletries"))
    leisure=float(input("Enter the budget for Leisure"))
    
    total_budget= savings + insurance + transport +  housing+food + toiletries + leisure
    
    summarized_budget= '''
        Please see the revision below of your budget
        Savings : {savings}
        Insurance : {Insurance}
        Transport : {transport}
        Housing : {housing}
        Food : {food}
        Toiletries : {toiletries}
        Leisure : { leisure}
    '''
    changes = int(input("Would you like to make any changes?"))
    return summarized_budget,changes

def make_changes():
    # if changes ==1:
    #     #make changes 
    # else:
    #     #Don't make changes
    pass

def over_budget():
    if total_budget > income:
        print("Budget is greater than income amount.Please adjust the budget")
        save_budget_provisions()
    else:# We can add to the database
        query= "INSERT INTO {names}'s budget (Savings,Insurance,Transport,Housing,Food,Toiletries,Leisure) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        values= (savings,insurance,transport,housing,food,toiletries,leisure)
        mycursor.execute(query,values)
        connection.commit()
    
        
        