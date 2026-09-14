clock_value = 569
remaining = clock_value

bit_1 = remaining % 2
remaining = remaining // 2
bit_2 = remaining % 2
remaining = remaining // 2
bit_4 = remaining % 2
remaining = remaining // 2
bit_8 = remaining % 2
remaining = remaining // 2
bit_16 = remaining % 2
remaining = remaining // 2
bit_32 = remaining % 2
remaining = remaining // 2
bit_64 = remaining % 2
remaining = remaining // 2
bit_128 = remaining % 2
remaining = remaining // 2
bit_256 = remaining % 2
remaining = remaining // 2
bit_512 = remaining % 2
remaining = remaining // 2

print(bit_512, bit_256, bit_128, bit_64, bit_32, bit_16, bit_8, bit_4, bit_2, bit_1,)


clock_values = [13,42]
labels = ["hours", "minutes"]

clock_values.append(17)
labels.append("secconds")

selected_index = 2

clock_value = clock_values[selected_index]
label = labels[selected_index]

