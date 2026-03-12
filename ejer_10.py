# 10. Academia de baile: asistencia

print("DANCE CLASS")

attendance = int(input("How many times have you attended classes?: "))

if attendance >= 0 and attendance <= 5:
    print("Low attendance")

elif attendance >= 5 and attendance <= 8:
    print("Medium attendance")

elif attendance >= 9:
    print("High attendance")
