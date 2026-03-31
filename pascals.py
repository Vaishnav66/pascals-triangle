# Function to compute nth row of Pascal's Triangle
def get_row(n):
    row = [1]  # first element is always 1
    
    for k in range(1, n + 1):
        # Compute next value using previous value
        val = row[k-1] * (n - k + 1) // k
        row.append(val)
    
    return row

# Input
n = int(input())

# Get result
result = get_row(n)

# Output
print(*result)
