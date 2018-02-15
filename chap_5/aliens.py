score = 0
alienColor = input("\nenter the alein color: G/Y/B\n")
alienColor = alienColor.lower()

if alienColor == "green":
    score = score + 10
    print("Awesome, you just earned 10 points")

elif alienColor == "red":
    score = score - 5
    print("Be careful you just lost 5 points")

elif alienColor == "blue":
    score = score + 20
    print("Super Awesome!! You just scored a 20 points and shot blue dragon")
