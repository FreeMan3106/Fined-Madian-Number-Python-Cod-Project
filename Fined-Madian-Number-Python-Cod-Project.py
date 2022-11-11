#task 4

firsr_number = float(input("Enter Firts NUmber : "))

secont_number = float(input("Enter Secont NUmber : "))

thirt_number = float(input("Enter Thirt NUmber : "))


if secont_number > firsr_number > thirt_number or secont_number < firsr_number < thirt_number:
    print(f"{firsr_number} is median number.")
elif firsr_number < secont_number < thirt_number or firsr_number > secont_number > thirt_number:
    print(f"{secont_number} is median number.")
else:
    print(f"{thirt_number} is median number.")

