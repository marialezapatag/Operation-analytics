def yearly_cost(monthly_cost):
    return monthly_cost * 12

assert yearly_cost(100) == 1200
assert yearly_cost(0) == 0

result = yearly_cost(100)
print(result)
