import sys
if __name__ == "__main__":
    # 读取第一行的n
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()
    a = a.split()
    b = b.split()
    s = []
    n = len(a)
    for i in range(n):
        s.append(a[i])
        s.append(b[i])
    m = len(s)
    Set = {}
    ans_a = 0
    ans_b = 0
    q = []
    for i in range(m):
        if s[i] not in Set:
            Set[s[i]]=len(q)
            q.append(s[i])
        else:
            ans = 1
            ans+=len(q)-Set[s[i]]
            index = Set[s[i]]
            for j in q[Set[s[i]]:]:
                Set.pop(j)
            q = q[:index]
            if i%2==0:
                ans_a+=ans
            else: 
                ans_b+=ans
    if ans_a>ans_b:
        print("Byte")
    elif ans_a==ans_b:
        print("Draw")
    else: 
        print("Dance")