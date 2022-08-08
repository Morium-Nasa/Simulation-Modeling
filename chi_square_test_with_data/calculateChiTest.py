def chiTest(Oi, totalClass):
    Dobs = 0
    Ei = totalClass

    for datum in Oi:
        Dobs += pow((datum - Ei), 2) / Ei

    print("D obs is: ", round(Dobs, 4))

    Dcritical = float(input("Enter D critical: "))

    if Dobs <= Dcritical:
        print("Test result is Accepted")
    else:
        print("Test result is Rejected")
