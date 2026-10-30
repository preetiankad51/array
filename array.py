# Accept array of scores
scores = list(map(int, input("Enter scores: ").split()))

# Calculate sum
total = sum(scores)

# Calculate average
average = total / len(scores)

print("Scores:", scores)
print("Sum of scores:", total)
print("Average of scores:", average)