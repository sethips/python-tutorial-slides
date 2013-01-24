def keyword_fnt(name, addr, birth, isGirl=True, *args, **argv):
    print('Getting name:', name)
    if isGirl:
        print('mei')
    else:
        print('(ry')
    print('length of args', len(args))
    print('length of argv', len(argv))
    vari_len_arg_fnt(None, args)
    vari_arg_dict_fnt(argv)


def vari_len_arg_fnt(arg1, *args):
    print('first arg:', arg1)
    affix_dict = {1: 'st', 2: 'nd', 3: 'rd'}
    for i, arg_i in enumerate(args):
        if i not in affix_dict:
            affix = 'th'
        else:
            affix = affix_dict[i]
        print(str(i) + affix, 'arg:', arg_i)


def vari_len_arg_inline(arg1, *args):
    print('arg1:', arg1)
    affix_dict = {1: 'st', 2: 'nd', 3: 'rd'}
    for i, arg_i in enumerate(args):
        print(str(i) + ('th' if i not in affix_dict else affix_dict[i]),
              'arg:', arg_i)


def vari_arg_dict_fnt(arg1=None, **argv):
    if not arg1:
        print('no arg1 given')
    else:
        print(arg1)
    for k, v in argv.items():
        print(k, v)


def test():
    # test these functions
    vari_len_arg_fnt('a must input', 'after that', 'I can put',
                     'as many args', 'as I want', 'YA')


def test_keyword():
    keyword_fnt('liang', 'Taipei', '1991', 'adsf', 'qwef', key=2)
    keyword_fnt('liang', 'Taipei', '1991', False, 'adsf', 'qwef', key=2)
    keyword_fnt('liang', 'Taipei', '1991', 'adsf', 'qwef',
                isGirl=False, key=2)

if __name__ == '__main__':
    test()
    test_keyword()
