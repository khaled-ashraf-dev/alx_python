import sys
args_list = sys.argv
args_len = len(args_list) - 1

if __name__ == '__main__':
    
    if args_len == 1:
        args_str = 'argument'
    
    else:
        args_str = 'arguments'
    
    if args_len == 0:
        print('{} {}.'.format(args_len, args_str))
    else:
        print('{} {}:'.format(args_len, args_str))
        counter = 1
        for arg in args_list[1:]:
            print('{}: {}'.format(counter, arg))
            counter += 1