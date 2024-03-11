import string

def generate_options():
    options = []
    for i in range(50):
        first_char = 'J'
        third_char = '1'
        fifth_char = '-'
        fourth_eighth_char = str(i // 10 % 10)

        remaining_chars = str(i % 10).zfill(3)

        input_string = first_char + remaining_chars[0] + third_char + remaining_chars[1:] + fifth_char + fourth_eighth_char + remaining_chars[-1]
        options.append(input_string)

    return options

options_list = generate_options()
for option in options_list:
    print(option)