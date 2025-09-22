divisible_by_5=[]
not_divisible_by_5=[]
for i in range(1,5001):
    if i % 5 == 0:
        divisible_by_5.append(i)
        print(f"divisible_by_5 is:{divisible_by_5}")
    else:
        not_divisible_by_5.append(i)
        print(f"not divisible_by_5 is:{not_divisible_by_5}")

