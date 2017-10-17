from func_test.name_function import get_formatted_name

print('Enter q at any time to quit')
while True:
    first = input("\nPlease input first name:")
    if 'q' == first:
        break
    last = input("\nPlease input last name:")
    if 'q' == last:
        break

    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name:" + formatted_name + '.')
