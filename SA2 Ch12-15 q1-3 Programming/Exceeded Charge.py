while True:
    TicketType = input("Choose your TicketType 'E' or 'S': " )
    if TicketType == 'E' or TicketType == 'S':
        break
    else:
        print('Unexpected choice, please enter again')

while True:
    BaggageWeight = eval(input('Enter your baggage weight: '))
    if BaggageWeight > 0:
        break
    else:
        print('The number cannot be negative or zero, please try again')

if TicketType == 'E':
    BaggageAllowance = 16
    ChargeRate = 3.5
else:
    BaggageAllowance = 20
    ChargeRate = 5.75

ExcessWeight = BaggageWeight - BaggageAllowance

if ExcessWeight > 0:
    Charge = ExcessWeight * ChargeRate
else:
    Charge = 0

print('The charge for exceeded weight is: ', Charge)












