#convert seconds into hours minutes 

total_seconds = int(input("Please enter the amount of seconds: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print("{0:>20} {1:>20} {2:>20}".format("Hours", "Minutes", "Seconds"))
print(
    f"{hours:>20} {minutes:>20} {seconds:>20}"
    )


