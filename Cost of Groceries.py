# Read the number of test cases
t = int(input())

# Process each test case
for i in range(t):
  # Read the number of items and the minimum freshness value
  n, x = map(int, input().split())

  # Read the freshness values of the items
  a = list(map(int, input().split()))

  # Read the costs of the items
  b = list(map(int, input().split()))

  # Initialize the total cost to zero
  total_cost = 0

  # Iterate through the items
  for j in range(n):
    # If the freshness value is greater than or equal to the minimum freshness value, add the cost of the item to the total cost
    if a[j] >= x:
      total_cost += b[j]

  # Print the total cost
  print(total_cost)
