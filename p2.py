import random


def product_list(lst):
    lst_product = []

    product = 1

    for x in range(len(lst)):
        product *= lst[x]

    for x in range(len(lst)):
        lst_product.append(int(product/lst[x]))

    return lst_product


def products(nums):
    # Generate prefix products
    prefix_products = []
    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)

    # Generate suffix products
    suffix_products = []
    for num in reversed(nums):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    suffix_products = list(reversed(suffix_products))

    # Generate result
    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(suffix_products[i + 1])
        elif i == len(nums) - 1:
            result.append(prefix_products[i - 1])
        else:
            result.append(prefix_products[i - 1] * suffix_products[i + 1])
    return result


def main():
    lst = []

    n = random.randint(5,6)

    for x in range(n):
        lst.append(random.randint(1,10))

    products(lst)

main()
