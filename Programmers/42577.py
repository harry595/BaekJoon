def solution(phone_book):
    phone_book.sort()
    for i in range(1,len(phone_book)):
        before_len=len(phone_book[i-1])
        if(phone_book[i][:before_len]==phone_book[i-1]):
            return False
    return True