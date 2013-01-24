def vari_len_arg_fnt(arg1, *args):
    print('first arg:', arg1)
    affix_dict = {1: 'st', 2: 'nd', 3: 'rd'}
    for i, arg_i in enumerate(args):
        if i not in affix_dict:
            affix = 'th'
        else:
            affix = affix_dict[i]
        print(str(i) + affix, 'arg:', arg_i)

vari_len_arg_fnt('must input', 'after that', 'I can put',
                 'as many args', 'as I want', 'YA')
