daily_sales = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
sales_of_the_week = 0.00

for position in range(len(days_of_week)):
    sales_of_the_day = float(input('Enter the sales for ' + days_of_week[position] + ': '))
    daily_sales[position] = sales_of_the_day

for amount in daily_sales:
    sales_of_the_week += float(amount)

print('Total sales for the week: $' + format(sales_of_the_week, '.2f'))
