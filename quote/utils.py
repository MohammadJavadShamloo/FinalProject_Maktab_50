def calculate_off(price, off_percent):
    """
    Calculate Discount
    :param price: Price
    :param off_percent: Discount Amount
    :return: Price With Discount
    """
    return price * (1 - (off_percent // 100))


def calculate_tax(price, tax_percent):
    """
    Calculate Taxation
    :param price: Price
    :param tax_percent: Tax Amount
    :return: Price With Tax
    """
    return price * (1 + (tax_percent // 100))
