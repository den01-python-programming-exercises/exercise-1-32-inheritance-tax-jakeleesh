def main():
    #write your code below this line
    inherit = int(input("Inheritance:"))
    years = int(input("Years since death:"))
    if (inherit <= 325000):
        tax = 0.0
    elif (years < 3):
        tax = (inherit - 325000) * 0.4
    elif (years >= 3 and years < 4):
        tax = (inherit - 325000) * 0.32
    elif (years >= 4 and years < 5):
        tax = (inherit - 325000) * 0.24
    elif (years >= 5 and years < 6):
        tax = (inherit - 325000) * 0.16
    elif (years >= 6 and years < 7):
        tax = (inherit - 325000) * 0.08
    else:
        tax = 0.0
    print("Tax: " + str(tax))

if __name__ == '__main__':
    main()
