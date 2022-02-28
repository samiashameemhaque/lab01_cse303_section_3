#problem3
def compound_interest_2019_1_60_053():
    P = float(input("Enter your principle interest: "))
    R = float(input("Enter your interest rate: "))
    T = int(input("Enter your time: "))
    Interest = P*(pow((1+R/100),T))
    CI= Interest-P
    print(CI)

def Main():



    compound_interest_2019_1_60_053()




if __name__ == "__main__":
    Main()