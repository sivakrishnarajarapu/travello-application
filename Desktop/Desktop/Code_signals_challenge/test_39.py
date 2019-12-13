def knapsackLight(value1, weight1, value2, weight2, maxW):
    # max_weight=0
    if maxW>=weight1+weight2:
        return value1+value2
    elif maxW<weight1 or maxW>weight2:
        return value1
    elif maxW>weight1 or maxW<weight2:
        return value2
print(knapsackLight(5,3,7,4,6))




