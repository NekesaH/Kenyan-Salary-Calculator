from django.shortcuts import render
from .forms import TaxesForm

# Create your views here.
def home(request):
    return render(request, 'calculator/home.html')



def add(request):

    basic_salary = int(request.POST['sal'])
    allowances = int(request.POST['allowance'])


    

    gross_pay = basic_salary + allowances
    
    personal_relief = 2400

    if gross_pay < 18000:

        nssf = 0.06 * gross_pay

    else:
        nssf = 1080

    if gross_pay <= 5999:
        nhif_deduct = 150

    elif gross_pay > 6000 and gross_pay <= 7999:
        nhif_deduct = 300

    elif gross_pay > 7999 and gross_pay <= 11999:
        nhif_deduct = 400

    elif gross_pay > 11999 and gross_pay <= 14999:
        nhif_deduct = 500

    elif gross_pay > 14999 and gross_pay <= 19999:
        nhif_deduct = 600

    elif gross_pay > 19999 and gross_pay <= 24999:
        nhif_deduct = 750

    elif gross_pay > 24999 and gross_pay <= 29999:
        nhif_deduct = 850

    elif gross_pay > 29999 and gross_pay <= 34999:
        nhif_deduct = 900

    elif gross_pay > 34999 and gross_pay <= 39999:
        nhif_deduct = 950

    elif gross_pay > 39999 and gross_pay <= 44999:
        nhif_deduct = 1000

    elif gross_pay > 44999 and gross_pay <= 49999:
        nhif_deduct = 1100

    elif gross_pay > 49999 and gross_pay <= 59999:
        nhif_deduct = 1200

    elif gross_pay > 59999 and gross_pay <= 69999:
        nhif_deduct = 1300

    elif gross_pay > 69999 and gross_pay <= 79999:
        nhif_deduct = 1400

    elif gross_pay > 79999 and gross_pay <= 89999:
        nhif_deduct = 1500

    elif gross_pay > 89999 and gross_pay <= 99999:
        nhif_deduct = 1600

    else:
        nhif_deduct = 1700



    


    income_after_pension = basic_salary -nssf
    taxable_income = gross_pay - nssf

    
    if taxable_income  <= 12298:

        income_tax = taxable_income * 0.1
        
    elif taxable_income  > 12298 and taxable_income <= 23885:
        income_tax = taxable_income * 0.15
       

    elif taxable_income > 23886 and taxable_income <= 35472:
        income_tax = taxable_income * 0.20
            
    elif taxable_income > 35472 and  taxable_income <= 47059:
        income_tax  = taxable_income * 0.25
        

    else:

        income_tax = taxable_income * 0.30


    if income_tax <= personal_relief:
        income_tax = 0.00
        tax_payable = 0.00
       
    else:
        tax_payable = income_tax - personal_relief
    
    total_deductions = nhif_deduct + tax_payable + nssf

    net_pay = gross_pay - total_deductions



    context ={'basic_salary':basic_salary, 'income_after_pension':income_after_pension, 'allowances':allowances, 'gross_pay':gross_pay, 'taxable_income':taxable_income, 'income_tax':income_tax  , 'tax_payable':tax_payable, 'nhif_deduct': nhif_deduct , 'nssf':nssf, 
    'total_deductions':total_deductions, 'net_pay':net_pay, 'personal_relief':personal_relief}



     
     

    return render(request, 'calculator/add.html', context)