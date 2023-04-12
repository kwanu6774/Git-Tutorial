def read_single_digit(digit):
    if digit==0:
        return "영"
    elif digit==1:
        return "일"
    elif digit==2:
        return "이"
    elif digit==3:
        return "삼"
    elif digit==4:
        return "사"
    elif digit==5:
        return "오"
    elif digit==6:
        return "육"
    elif digit==7:
        return "칠"
    elif digit==8:
        return "팔"
    elif digit==9:
        return "구"
def read_number(number):
    if number==0:
        return "영"
    elif number < 10:                      #1~9
        return read_single_digit(number)
    elif number <100:                      #10~99
        tens_digit = number//10 
        ones_digit = number%10
        if tens_digit==1:                             #10~19
            if ones_digit==0:
                return "십"
            else :
                return "십" + read_single_digit(ones_digit)
        else :                                          #20~99
            if ones_digit==0:
                return read_single_digit(tens_digit) + "십"
            else :
                return read_single_digit(tens_digit) + "십" + read_single_digit(ones_digit)
    else :                                            #100~999
        hundreds_digit= number//100
        tens_digit= (number //10)%10
        ones_digit= number%10
        if number == 100 :
            return "백"
        elif tens_digit == 0 and ones_digit == 0:
            return read_single_digit(hundreds_digit) + "백"
        elif tens_digit == 0:
            return read_single_digit(hundreds_digit) + "백" + "영" + read_single_digit(ones_digit)
        elif ones_digit == 0:
            return read_single_digit(hundreds_digit) + "백" + read_single_digit(tens_digit) + "십"
        else:
            return read_single_digit(hundreds_digit) + "백" + read_single_digit(tens_digit) + "십" + read_single_digit(ones_digit)


number=int(input("세 자리 정수 입력:"))
print(read_number(number))
