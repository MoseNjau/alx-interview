# Pascal Triangle

Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of n:

    Returns an empty list if n <= 0
    It is assumed that n will be always an integer
---
#### Example:
    Given 3 the function returns [[1],[1,1],[1,2,1]]
---
#### [Solution 1](./0-pascal_triangle.py)
```
def pascal_triangle(n):
    if n < 1:
        return []

    solution = [[1]]
    results = [1]

    for i in range(n-1):
        temp = [0] + results + [0]
        results = []
        for j in range(len(temp) - 1):
            results.append(temp[j] + temp[j+1])

        solution.append(results)

    return solution
```