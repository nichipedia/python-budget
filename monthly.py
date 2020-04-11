from jinja2 import Environment, PackageLoader, select_autoescape
from datetime import datetime
from calendar import monthrange

now = datetime.now()


month = now.strftime('%B %Y')
monthNum = now.strftime('%m')
yearNum = now.strftime('%Y')

days = monthrange(int(yearNum), int(monthNum))[1]

env = Environment(
    loader=PackageLoader('monthly', './templates'),
)

expenses = {
    'recurringExpenses': [
        {
            'type': 'Loan Payment',
            'payments': [
                {
                    'description': 'Nissan Altima',
                    'company': 'Nissan Motor Credit',
                    'date': 15,
                    'payment': 350
                },
                {
                    'description': 'Nicks Student Loans',
                    'company': 'Nelnet',
                    'date': 17,
                    'payment': 0
                }, 
                {
                    'description': 'Allisons Student Loans',
                    'company': '???',
                    'date': 0,
                    'payment': 0
                },
                {
                    'description': 'Mac Laptop',
                    'company': 'BestBuy Credit',
                    'date': 21,
                    'payment': 180
                }, 
                {
                    'description': 'Allisons Loan',
                    'company': 'Some Credit Card Company',
                    'date': 20,
                    'payment': 50
                }
            ]
        },
        {
            'type': 'Insurance',
            'payments': [
                 {
                    'description': 'Nicks Insurance',
                    'company': 'GEICO',
                    'date': 28,
                    'payment': 83
                },
                {
                    'description': 'Allisons Insurance',
                    'company': 'progressive',
                    'date': 27,
                    'payment': 80
                }
            ]
        }, 
        {
            'type': 'Utility',
            'payments': [
                {
                    'description': 'Water',
                    'company': 'Lee Road Water',
                    'date': 8,
                    'payment': 45
                },
                {
                    'description': 'Internet',
                    'company': 'Charter',
                    'date': 21,
                    'payment': 45
                },
                {
                    'description': 'Nicks Phone',
                    'company': 'ATT',
                    'date': 15,
                    'payment': 150
                },
                {
                    'description': 'Allisons Phone',
                    'company': 'Verizon',
                    'date': 28,
                    'payment': 80
                },
                {
                    'description': 'Electric',
                    'company': 'WST',
                    'date': 12,
                    'payment': 130
                }
            ]
        },
        {
            'type': 'School Fees',
            'payments': [
                {
                    'description': 'Nicks UNO Fees',
                    'company': 'University of New Orleans',
                    'date': 10,
                    'payment': 0
                },
                {
                    'description': 'Allisons PRCC Fees',
                    'company': 'Pearl River Community College',
                    'date': 20,
                    'payment': 720
                }
            ]
        }
    ],
    'miscExpenses': [
        {
            'type': 'Food',
            'payments': [

            ]
        },
        {
            'type': 'Clothing',
            'payments': [

            ]
        },
        {
            'type': 'Misc Purchases',
            'payments': [

            ]
        }
    ]
}


investments: [
    {
        'description': 'Nicks TSP contributions',
        'company': 'NRL',
        'payment': 150
    },
    {
        'description': 'Family Index Fund',
        'company': 'Fiedelity',
        'payment': 0
    }
]

monthlyIncome = [
    {
        'description': 'Nicks Job at NRL',
        'person': 'Nick',
        'company': 'NRL',
        'payment': 3000
    },
    {
        'description': 'Allisons Job at SMH',
        'person': 'Allison',
        'company': 'SMH',
        'payment': 1400
    }
]

pieChartData = {
    'Loan Payment': {
        'amount': 0
    },
    'Insurance': {
        'amount': 0
    },
    'Utility': {
        'amount': 0
    },
    'School Fees': {
        'amount': 0
    }, 
    'Food': {
        'amount': 0
    },
    'Clothing': {
        'amount': 0
    },
    'Purchases': {
        'amount': 0
    }
}

barChartData = [0] * (days+1)


totalExpenses = 0


print(f'{"Table of Incomes":^64}')
print(f'{"-":-^64}')
print(f'{"Person":<16}{"Description":<32}{"Payment":<16}')
print(f'{"-":-^64}')

totalIncome = 0
for income in monthlyIncome:
    totalIncome = totalIncome + income['payment']
    print(f"{income['person']:<16}{income['description']:<32}${income['payment']:<16}")
print(f'{"-":-^64}')
print(f"{f'Total Monthly Income: ${totalIncome}':>64}")


print()


print(f'{"Table of Recurring Expenses":^96}')
print(f'{"-":-^96}')
print(f'{"Type":<16}{"Company":<32}{"Description":<32}{"Payment":<16}')
print(f'{"-":-^96}')
totalRecurringExpenses = 0

for recurring in expenses['recurringExpenses']:
    for expense in recurring['payments']:
        totalRecurringExpenses = totalRecurringExpenses + expense['payment']
        barChartData[expense['date']] = barChartData[expense['date']] + expense['payment']
        pieChartData[recurring['type']]['amount'] = pieChartData[recurring['type']]['amount'] + expense['payment']
        print(f"{recurring['type']:<16}{expense['company']:<32}{expense['description']:<32}${expense['payment']:<16}")


print(f'{"-":-^96}')
print(f"{f'Total Monthly Recurring Expenses: ${totalRecurringExpenses}':>96}")

print()

print(f'{"Table of Misc Expenses":^96}')
print(f'{"-":-^96}')
print(f'{"Type":<16}{"Company":<32}{"Description":<32}{"Payment":<16}')
print(f'{"-":-^96}')
totalMiscExpenses = 0

for misc in expenses['miscExpenses']:
    for expense in misc['payments']:
        totalmMiscExpenses = totalMiscExpenses + expense['payment']
        barChartData[expense['date']] = barChartData[expense['date']] + expense['payment']
        pieChartData[misc['type']]['amount'] = pieChartData[misc['type']]['amount'] + expense['payment']
        print(f"{misc['type']:<16}{expense['company']:<32}{expense['description']:<32}${expense['payment']:<16}")
print(f'{"-":-^96}')
print(f"{f'Total Monthly Misc Expenses: ${totalMiscExpenses}':>96}")

pieLabels = '["Loan Payments", "Insurance", "Utility", "School Fees", "Food", "Clothing", "Purchases"]'
pieData = '['
for key in pieChartData.keys():
    pieData = f'{pieData} {pieChartData[key]["amount"]},'
pieData = pieData.strip(',')
pieData = pieData + ']'

barLabels = '['
barData = '['
for i in range(1, days+1):
    barLabels = f'{barLabels}{str(i)},'
    barData = f'{barData}{barChartData[i]},'
barLabels = barLabels.strip(',')
barData = barData.strip(',')
barLabels = f'{barLabels}]'
barData = f'{barData}]'


template = env.get_template('report.html')
report = template.render(expenses=expenses, pieLabels=pieLabels, pieData=pieData, month=month, barLabels=barLabels, barData=barData)
reportFile = open('./reports/April_Report.html', 'w')
reportFile.write(report)
reportFile.close()
print(monthNum)