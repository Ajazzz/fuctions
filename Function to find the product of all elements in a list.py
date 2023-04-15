def product_list(l):
    """
    Find the product of all elements in a list l
    """
    product = 1
    for i in l:
        product *= i
    return product
