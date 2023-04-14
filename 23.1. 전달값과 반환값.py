def open_account(): # pen_account라는 함수를 정의
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money): # 입금하는함수 , balance = 잔액, money = 넣는금액
    print("입금이 완료되었습니다. 잔액은 {0}입니다".format(balance + money)) # 금액에따라 잔액을 반환 입금이 완료되었습니다. 잔액은 1000입니다
    return balance + money # 입금이 되었으므로 현재잔액에서 입금된 값을 반환

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
        return balance - money # balance - money를 뺀 금액을 반환
    else:
        print("출금이 완료되자 않았습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance # 출금이 되지 않았으므로 balance 반환
    
def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money -commission # commission - 수수료 받은 금액 , balance - money -commission - 잔액 - 나간금액 - 커미션 을 튜플형식으로 반환

balance = 0 # 초기금액
balance = deposit(balance, 1000) # deposit이라는 입금하는 함수를 호출해 1000원을 입금
# balance = withdraw(balance, 2000) # withdraw라는 함수를 사용하여 ballance 에서 2000원 출금
# balance = withdraw(balance, 500) # withdraw라는 함수를 사용하여 blalance 에서 500원 출금
commission , balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원 입니다.".format(commission, balance))