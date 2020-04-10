recurringExpenses = {
    'carPayments': [
        {
            'title': 'Nissan Altima',
            'company': 'Nissan Motor Credit',
            'payment': 350
        }
    ],
    'carInsurance': [
        {
            'title': 'Nicks Insurance',
            'company': 'GEICO',
            'payment': 83
        },
        {
            'title': 'Allisons Insurance',
            'company': 'progressive',
            'payment': 80
        }
    ],
    'phoneBill': [
       
    ],
    'studentLoans': [
        {
            'title': 'Nicks Student Loans',
            'company': 'Nelnet',
            'payment': 0
        }, 
        {
            'title': 'Allisons Student Loans',
            'company': '???',
            'payment': 0
        }
    ],
    'personalLoans': [
        {
            'title': 'Mac Laptop',
            'company': 'BestBuy Credit',
            'payment': 180
        }, 
        {
            'title': 'Allisons Loan',
            'company': 'Some Credit Card Company',
            'payment': 50
        }
    ],
    'utilities': [
        {
            'title': 'Water',
            'company': 'Lee Road Water',
            'payment': 45
        },
        {
            'title': 'Internet',
            'company': 'Charter',
            'payment': 45
        },
        {
            'title': 'Nicks Phone',
            'company': 'ATT',
            'payment': 150
        },
        {
            'title': 'Allisons Phone',
            'company': 'Verizon',
            'payment': 80
        },
        {
            'title': 'Electric',
            'company': 'WST',
            'payment': 130
        }
    ],
    'school': [
        {
            'title': 'Nicks UNO Fees',
            'company': 'University of New Orleans',
            'payment': 0
        },
        {
            'title': 'Allisons PRCC Fees',
            'company': 'Pearl River Community College',
            'payment': 720
        }
    ]
}

miscExpenses = {
    'food': [

    ],
    'clothing': [

    ],
    'purchases': [

    ]
}

investments: [
    {
        'title': 'Nicks TSP contributions',
        'company': 'NRL',
        'payment': 150
    },
    {
        'title': 'Family Index Fund',
        'company': 'Fiedelity',
        'payment': 0
    }
]

monthlyIncome = [
    {
        'title': 'Nicks Job at NRL',
        'person': 'Nick',
        'company': 'NRL',
        'payment': 3000
    },
    {
        'title': 'Allisons Job at SMH',
        'person': 'Allison',
        'company': 'SMH',
        'payment': 1400
    }
]


totalExpenses = 0


print(f'{"Table of Incomes":^64}')
print(f'{"-":-^64}')
print(f'{"Person":<16}{"Description":<32}{"Payment":<16}')
print(f'{"-":-^64}')

totalIncome = 0
for income in monthlyIncome:
    totalIncome = totalIncome + income['payment']
    print(f"{income['person']:<16}{income['title']:<32}${income['payment']:<16}")
print(f'{"-":-^64}')
print(f"{f'Total Monthly Income: ${totalIncome}':>64}")


print()


print(f'{"Table of Recurring Expenses":^96}')
print(f'{"-":-^96}')
print(f'{"Type":<16}{"Company":<32}{"Description":<32}{"Payment":<16}')
print(f'{"-":-^96}')
totalRecurringExpenses = 0
for expense in recurringExpenses['carPayments']:
    totalRecurringExpenses = totalRecurringExpenses + expense['payment']
    print(f"{'Loan':<16}{expense['company']:<32}{expense['title']:<32}${expense['payment']:<16}")
for expense in recurringExpenses['carInsurance']:
    totalRecurringExpenses = totalRecurringExpenses + expense['payment']
    print(f"{'Insurance':<16}{expense['company']:<32}{expense['title']:<32}${expense['payment']:<16}")
for expense in recurringExpenses['studentLoans']:
    totalRecurringExpenses = totalRecurringExpenses + expense['payment']
    print(f"{'Loan':<16}{expense['company']:<32}{expense['title']:<32}${expense['payment']:<16}")
for expense in recurringExpenses['personalLoans']:
    totalRecurringExpenses = totalRecurringExpenses + expense['payment']
    print(f"{'Loan':<16}{expense['company']:<32}{expense['title']:<32}${expense['payment']:<16}")
for expense in recurringExpenses['utilities']:
    totalRecurringExpenses = totalRecurringExpenses + expense['payment']
    print(f"{'Utility':<16}{expense['company']:<32}{expense['title']:<32}${expense['payment']:<16}")
for expense in recurringExpenses['school']:
    totalRecurringExpenses = totalRecurringExpenses + expense['payment']
    print(f"{'School Fees':<16}{expense['company']:<32}{expense['title']:<32}${expense['payment']:<16}")
print(f'{"-":-^96}')
print(f"{f'Total Monthly Recurring Expenses: ${totalRecurringExpenses}':>96}")

print()

print(f'{"Table of Misc Expenses":^96}')
print(f'{"-":-^96}')
print(f'{"Type":<16}{"Company":<32}{"Description":<32}{"Payment":<16}')
print(f'{"-":-^96}')
totalMiscExpenses = 0
for expense in miscExpenses['food']:
    totalMiscExpenses = totalMiscExpenses + expense['payment']
    print(f"{'Food':<16}{expense['company']:<32}{expense['title']:<32}${expense['payment']:<16}")
for expense in miscExpenses['clothing']:
    totalMiscExpenses = totalMiscExpenses + expense['payment']
    print(f"{'Clothing':<16}{expense['company']:<32}{expense['title']:<32}${expense['payment']:<16}")
for expense in miscExpenses['purchases']:
    totalMiscExpenses = totalMiscExpenses + expense['payment']
    print(f"{'Misc Purchases':<16}{expense['company']:<32}{expense['title']:<32}${expense['payment']:<16}")
print(f'{"-":-^96}')
print(f"{f'Total Monthly Misc Expenses: ${totalMiscExpenses}':>96}")