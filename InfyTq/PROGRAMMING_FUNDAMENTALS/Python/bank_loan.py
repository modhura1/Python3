#PF-Assgn-20

def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    cat = {'Car' : 0, 'House' : 1, 'Business' : 2, 'Car1' : 0}
    loan = [[25000, 'Car', 500000, 36], [50000, 'House', 6000000, 60], [75000, 'Business', 7500000, 84]]
    acc = str(account_number)
    eligible_loan_amount=loan[cat.get(loan_type)][2]
    bank_emi_expected=loan[cat.get(loan_type)][3]
    if (len(acc) != 4) or (acc[0] != '1') or account_balance < 100000 or (salary <= loan[cat.get(loan_type)][0]) or loan_amount_expected > loan[cat.get(loan_type)][2] or customer_emi_expected > loan[cat.get(loan_type)][3]: 
        if (len(acc) != 4) or (acc[0] != '1'):
            print("Invalid account number")
        elif account_balance < 100000 :
            print("Insufficient account balance")
        elif (salary <= loan[cat.get(loan_type)][0]):
            print("Invalid loan type or salary")
        elif loan_amount_expected > loan[cat.get(loan_type)][2] or customer_emi_expected > loan[cat.get(loan_type)][3]:
            print("The customer is not eligible for the loan")
    else:
        print("Account number:", account_number)
        print("The customer can avail the amount of Rs.", eligible_loan_amount)
        print("Eligible EMIs :", bank_emi_expected)
        print("Requested loan amount:", loan_amount_expected)
        print("Requested EMI's:",customer_emi_expected)
    #Start writing your code here
    #Populate the variables: eligible_loan_amount and bank_emi_expected

    #Use the below given print statements to display the output, in case of success
    #print("Account number:", account_number)
    #print("The customer can avail the amount of Rs.", eligible_loan_amount)
    #print("Eligible EMIs :", bank_emi_expected)
    #print("Requested loan amount:", loan_amount_expected)
    #print("Requested EMI's:",customer_emi_expected)

    #Use the below given print statements to display the output, in case of invalid data.
    #print("Insufficient account balance")
    #print("The customer is not eligible for the loan")
    #print("Invalid account number")
    #print("Invalid loan type or salary")
    # Also, do not modify the above print statements for verification to work


#Test your code for different values and observe the results
calculate_loan(1001,40000,250000,"Car",300000,30)
