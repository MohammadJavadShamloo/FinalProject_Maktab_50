def calculate_off(price, off_percent):
    return price * (1 - (off_percent // 100))


def calculate_tax(price, tax_percent):
    return price * (1 + (tax_percent // 100))
