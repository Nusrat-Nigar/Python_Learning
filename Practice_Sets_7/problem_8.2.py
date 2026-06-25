def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print_details(name='Alice', age = 34, city = 'Pune')