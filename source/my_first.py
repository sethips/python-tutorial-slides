import os


def getAllPy():
    py_list = []
    for f in os.listdir('.'):
        f_name, f_ext = os.path.splitext(f)
        if f_ext == '.py':
            py_list.append(f)

    return py_list


def main_fnt():
    py_list = getAllPy()
    print('There',
          'are' if len(py_list) > 1 else 'is',
          len(py_list),
          'files' if len(py_list) > 1 else 'file',
          'in', os.path.realpath(os.path.curdir))

    len_list = []
    for f_name in py_list:
        with open(f_name) as f:
            st = f.read()
            len_list.append([len(st), len(set(st.split(' ')))])

    print('Total char/word count:')
    print(', '.join(
        ['{:10s}: {:4d}/{:d}'.format(f, n[1], n[0])
         for f, n in zip(py_list, len_list)]
    ))


if __name__ == '__main__':
    main_fnt()
