def exgcd(a, b):
    if b == 0:
        x, y = 1, 0
        return x, y, a
    x, y, gcd = exgcd(b, a % b)
    t = x
    x = y
    y = t - a // b * y
    return x, y, gcd


if __name__ == '__main__':
    print("输入两个正整数")
    a = int(input())
    b = int(input())
    temp = exgcd(a, b)
    x, y, gcd = temp[0], temp[1], temp[2]
    print(f"最大公因子:{gcd}")
    print(f"可以表示为\n{x} * {a} + {y} * {b} = {gcd}")
    if temp[2] == 1:
        print(f"{a}关于{b}的逆元为{x}")
    else:
        print("不存在逆元")
