# I作J处理 ，如若输入明文字数为奇数，则在文本末尾添加一个字母Z

# 字母表
letter_list = 'ABCDEFGHJKLMNOPQRSTUVWXYZ'

# 密码表
key_letter = ['', '', '', '', '']


# 根据密钥建立密码表
def Create_Matrix(key):
    key = Remove_Duplicates(key)  # 移除重复字母
    key = key.replace(' ', '')  # 去空格

    for ch in letter_list:  # 获取新字母表
        if ch not in key:
            key += ch

    j = 0
    for i in range(len(key)):  # 将新的字母表里的字母逐个填入密码表中，组成5*5的矩阵
        key_letter[j] += key[i]  # j用来定位字母表的行
        if 0 == (i + 1) % 5:
            j += 1


# 移除字符串中重复的字母
def Remove_Duplicates(key):
    key = key.upper()  # 转成大写字母组成的字符串
    _key = ''
    for ch in key:
        if ch == 'I':
            ch = 'J'
        if ch in _key:
            continue
        else:
            _key += ch
    return _key


# 获取字符在密码表中的位置
def Get_MatrixIndex(ch):
    for i in range(len(key_letter)):
        for j in range(len(key_letter)):
            if ch == key_letter[i][j]:
                return i, j  # i为行，j为列


# 加密
def Encrypt(plaintext, key_letter):
    ciphertext = ''

    if len(plaintext) % 2 != 0:  # 如果新的明文长度为奇数，在其末尾添上'Z'
        plaintext += 'Z'

    i = 0
    while i < len(plaintext):  # 对明文进行遍历
        if True == plaintext[i].isalpha():  # 判断是否为字母
            j = i + 1  # 继续对该字母之后的明文进行遍历，
            while j < len(plaintext):  # 直到遍历到字母，进行加密
                if True == plaintext[j].isalpha():
                    if 'I' == plaintext[i].upper():  #
                        x = Get_MatrixIndex('J')  #
                    else:  #
                        x = Get_MatrixIndex(plaintext[i].upper())  # 对字符在密码表中的坐标
                    if 'I' == plaintext[j].upper():  # 进行定位,同时将'I'作为
                        y = Get_MatrixIndex('J')  # 'J'来处理
                    else:  #
                        y = Get_MatrixIndex(plaintext[j].upper())  #

                    if x[0] == y[0]:  # 如果在同一行
                        ciphertext += key_letter[x[0]][(x[1] + 1) % 5] + key_letter[y[0]][(y[1]+1) % 5]
                    elif x[1] == y[1]:  # 如果在同一列
                        ciphertext += key_letter[(x[0] + 1) % 5][x[1]] + key_letter[(y[0] + 1) % 5][y[1]]
                    else:  # 如果不同行不同列
                        ciphertext += key_letter[x[0]][y[1]] + key_letter[y[0]][x[1]]
                    break;  # 加密完成，结束遍历
                j += 1
            i = j + 1  # 从加密过后的明文的后一个明文开始的,结束本次循环
            continue
        else:
            ciphertext += plaintext[i]  # 如果明文不是字母，直接加到密文上
        i += 1

    return ciphertext


# 解密
def Decrypt(ciphertext, key_letter):
    plaintext = ''
    if len(ciphertext) % 2 != 0:  # 如果新的密文长度为奇数，在其末尾添上'Z'
        ciphertext += 'Z'

    i = 0
    while i < len(ciphertext):  # 对密文进行遍历
        if True == ciphertext[i].isalpha():  # 如果是密文是字母的话，
            j = i + 1  # 则开始对该字母之后的密文进行遍历，
            while j < len(ciphertext):  # 直到遍历到字母，进行解密
                if True == ciphertext[j].isalpha():
                    if 'I' == ciphertext[i].upper():  #
                        x = Get_MatrixIndex('J')  #
                    else:  #
                        x = Get_MatrixIndex(ciphertext[i].upper())  # 对字符在密码表中的坐标
                    if 'I' == ciphertext[j].upper():  # 进行定位,同时将'I'作为
                        y = Get_MatrixIndex('J')  # 'J'来处理
                    else:  #
                        y = Get_MatrixIndex(ciphertext[j].upper())  #

                    if x[0] == y[0]:  # 如果在同一行
                        plaintext += key_letter[x[0]][(x[1] - 1) % 5] + key_letter[y[0]][(y[1] - 1) % 5]
                    elif x[1] == y[1]:  # 如果在同一列
                        plaintext += key_letter[(x[0] - 1) % 5][x[1]] + key_letter[(y[0] - 1) % 5][y[1]]
                    else:  # 如果不同行不同列
                        plaintext += key_letter[x[0]][y[1]] + key_letter[y[0]][x[1]]
                    break;  # 每组密文对解密完成后，结束本次对密文的遍历
                j += 1
            i = j + 1  # 每次对密文的遍历是从解密过后的密文的后一个密文开始的,结束本次循环
            continue
        else:
            plaintext += ciphertext[i]  # 如果密文不是字母，直接加到明文上
        i += 1

    return plaintext


# 主函数
if __name__ == '__main__':
    print("加密请输入1,解密请输入2，用回车键确认:")
    user_input = input();
    while (user_input != '1' and user_input != '2'):  # 输入合法性检测
        print("输入有误!请重新输入:")
        user_input = input()

    print('请输入密钥，密钥由英文字母组成:')
    key = input()

    Create_Matrix(key)  # 建立密码表

    if user_input == '1':  # 加密
        print('请输入明文:')
        plaintext = input()
        print("密文为:\n%s" % Encrypt(plaintext, key_letter))
    else:  # 解密
        print('请输入密文:')
        ciphertext = input()
        print('明文为:\n%s' % Decrypt(ciphertext, key_letter))
