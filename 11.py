number_of_tickets = int(input("Сколько Вам нужно билетов? "))

total = 0

for i in range(number_of_tickets):
    age = int(input("Введите возраст {i + 1}-го гостя: "))
    if age < 18:
        continue
    elif 18 <= age <= 25:
        total += 990
    else:
        total += 1390

if number_of_tickets > 3:
    print("Сумма к оплате с учëтом скидки: ", total - total / 100 * 10)
else:
    print("Сумма к оплате:", float(total))
