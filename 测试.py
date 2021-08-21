def get_number(num):
    if '0' <= num <= '9':
        return num, True
    else:
        print('error')
        return None, False


get_number(5)
