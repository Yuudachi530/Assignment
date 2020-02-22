TotalValue = 0
ZeroCount = 0
for Index in range(100):
    TotalValue = TotalValue + Result[Index]
    if Result[Index] == 0.0:
        ZeroCount = ZeroCount + 1
print("the average is ", (TotalValue / 100))
print("The number of elements with a zero value is ", ZeroCount)