num_sides =int(input("Enter the number: "))
num_sides =int(input("Enter the number: "))

total_combinations = num_sides * num_sides
print(f"The total number of combinations is {total_combinations}")

combination_matrix = [[0 for _ in range(num_sides)] for _ in range(num_sides)]

for i in range(num_sides):
    for j in range(num_sides):
        combination_matrix[i][j] = i + j + 2  # Add 2 to shift the range from 0-11 to 2-12


for row in combination_matrix:
    print(row)

sum_occurrences = {}
for row in combination_matrix:
    for num in row:
        if num in sum_occurrences:
            sum_occurrences[num] += 1
        else:
            sum_occurrences[num] = 1

# Calculate the probability of each sum
for sum, occurrences in sum_occurrences.items():
    probability = occurrences / total_combinations
    print(f"P(Sum ={sum} ) = {probability}")
