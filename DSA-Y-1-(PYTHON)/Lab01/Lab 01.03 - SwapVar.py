"""Lab 01.03 - SwapVar"""
def convert_string_to_tuples(text_in):
    """Lab 01.03 - SwapVar"""
    values = text_in.strip('()').split(', ')
    return tuple(map(float, values))
laongdao_data = convert_string_to_tuples(input())
print((laongdao_data[1],laongdao_data[0]))

