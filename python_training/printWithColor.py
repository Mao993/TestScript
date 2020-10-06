# 蓝色背景
def blue_print(*s, end='\n'):
    for item in s:
        print('\033[46m {} \033[0m'.format(item), end='')
    print(end=end)

# 高亮，绿色字体，红色背景
def green_print(*s, end='\n'):
    # print('\033[1m {} \033[0m'.format(s), end=end)
    for item in s:
        print('\033[1;32;41m {} \033[0m'.format(item), end='')
    print(end=end)


if __name__ == '__main__':
    # blue_print('asdf 1234')
    # print('-' * 30)
    blue_print(123, 'asdf')

    print('asdf', 1234, end='||||||||')
    print(end='\n')
    green_print('adsf', 1234, end='||||||||')
    print('\n')
    blue_print('hello world')
    blue_print('aaaa')