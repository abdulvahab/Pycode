from itertools import combinations
lst = range(1,17)
def get_matrix(lst, n, n1, n2):
    combs = combinations(lst, 4)
    sum_it = lambda x: sum(map(int, list(str(x))))
    return (c for c in combs if sum(map(sum_it, c)) == n and n1 in c and n2 in c)
lst = range(1,17)
while True:
    try:
        n = int(input("Insert a number between 19 and 26: "))
        n1 = int(input("Insert the first number to include: "))
        n2 = int(input("Insert the second number to include: "))
    except:
        print("Please numbers.")
        continue
    if not 0 <= n < 100 or not n1 in lst or not n2 in lst:
        print("Number not allowed")
        continue
    res = get_matrix(lst, n, n1, n2)
    break
for r in res:
    print(r)
