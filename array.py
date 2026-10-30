# Accept array of scores
scores = list(map(int, input("Enter scores: ").split()))

# Calculate sum
total = sum(scores)

# Calculate average
average = total / len(scores)

# Find maximum and minimum
maximum = max(scores)
minimum = min(scores)

# Display results
print("Scores:", scores)
print("Sum of scores:", total)
print("Average of scores:", average)
print("Maximum score:", maximum)
print("Minimum score:", minimum)