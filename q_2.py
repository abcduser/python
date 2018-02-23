def main():
    dvd_price = 25
    oldies_price = 15
    rent_p_day = 3
    tax_rate = 10

    dvds = int(input('How many DVD\'s to Buy?'))
    old_dvds = int(input('How many Oldies to Buy?'))
    rent_dvds = int(input('How many DVD\'s to Rent?'))
    rent_days = int(input('For how many days you want to Rent?'))

    bill_before_tax = dvds * dvd_price + old_dvds * oldies_price + (rent_dvds * rent_p_day) * rent_days

    tax = tax_rate / 100 * bill_before_tax

    bill_after_tax = bill_before_tax + tax

    print('Bill before Tax is $ {}'.format(str(bill_before_tax)))
    print('Bill after Tax is $ {}'.format(str(bill_after_tax)))


main()
