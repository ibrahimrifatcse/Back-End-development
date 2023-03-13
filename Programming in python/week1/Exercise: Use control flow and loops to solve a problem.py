num_list = [33, 42, 5, 66, 77, 22, 16, 79, 36, 62, 78, 43, 88, 39, 53, 67, 89, 11]
sorted(num_list)
for i in range(len(num_list)):
    print(num_list[i], end=" ")
print('\n')
for i in range(len(num_list)):
    if num_list[i] > 45:
        print(num_list[i], end=" ")
print('\n')
for i in range(len(num_list)):
    if num_list[i] < 45:
        print(num_list[i], end=" ")
print('\n')
count = 0
for index, i in enumerate(num_list):
    if i==36:
        print(f"Number found at position: {index}")
        count += 1
        break
print(f"count : {count}")

      
