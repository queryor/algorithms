import sys
import datetime
def gcd(a,b):
    if a < b:
        a,b = b,a     #保证a大于b
    while a%b != 0:
        a,b = b,a%b
    return b
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    a = list(map(int, line.split()))
    num = a[0]
    for i in range(1,len(a)):
        num = gcd(num,a[i])
    ans = 0
    for i in range(len(a)):
        ans+=a[i]//num
    print(ans)