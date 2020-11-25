
# Next work on a private auction contract

origin_location = input('What location are the items you want shipped?: ') 

destination = input('What destination would you like your items shipped?: ')

items = int(input('How many items will you be shipping?: '))



if items <= 500:
    tax = .07 * items
    total = items * tax
    fees = total - tax

    total = round(total, 2)
    print('Your total is '  + str(total))
    
    fees = round(fees, 2)
    print('You taxes and fees are ' + str(fees))
else:
    print('Contact cutomer support of orders over 500 items')

