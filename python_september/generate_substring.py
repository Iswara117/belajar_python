def generate_substrings(input_str):
    substrings = []

    for i in range(len(input_str)):
        for j in range(i + 1, len(input_str) + 1):
            substring = input_str[i:j]
            substrings.append(substring)

    return substrings

input_str = "program"
substrings = generate_substrings(input_str)

output = [s.split(",") for s in substrings if len(s) >= 3]


print(output)