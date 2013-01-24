def vari_len_arg_fnt(arg1, *args):
    print('first arg:', arg1)
    affix_dict = {1: 'st', 2: 'nd', 3: 'rd'}
    for i, arg_i in enumerate(args):
        print(str(i) + ('th' if i not in affix_dict else affix_dict[i]),
              'arg:', arg_i)
