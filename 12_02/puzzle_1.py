def has_duplicate_digits(num):
    num_str = str(num)
    length = len(num_str)
    if length % 2 != 0:
        return False
    half = length // 2
    return num_str[:half] == num_str[half:]


with open("input.txt") as f:
    line = f.read()

    ranges = line.split(",")
    valid_count = 0
    invalid_nums = []
    for range_str in ranges:
        start = int(range_str.split("-")[0])
        end = int(range_str.split("-")[1])

        for num in range(start, end + 1):
            if not has_duplicate_digits(num):
                valid_count += 1
            else:
                invalid_nums.append(num)

    print(f"Valid numbers without duplicates: {valid_count}")
    print(f"Sum of invalid numbers: {sum(invalid_nums)}")
