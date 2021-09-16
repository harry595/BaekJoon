# https://www.acmicpc.net/problem/1958

A = input()
B = input()
answer = []
sstack = []
sstacknum = []
blen = len(B)
snum = 0
for word in A:
    if B[snum] == word:
        snum += 1
        sstacknum.append(snum)
        sstack += word
    elif B[0] == word:
        snum = 1
        sstacknum.append(snum)
        sstack += word
    else:
        answer += sstack
        answer += word
        sstack = []
        sstacknum = []
        snum = 0

    if snum == blen:
        while sstack:
            if ''.join(sstack[-blen:]) == B:
                del sstack[-blen:]
                del sstacknum[-blen:]
                try:
                    snum = sstacknum[-1]
                except:
                    snum = 0
            else:
                break
if answer:
    print(''.join(answer+sstack))
else:
    print("FRULA")
