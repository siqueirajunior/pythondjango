kWh = float (input("Informe a qauntidade de kWh consumida:"))
tipoist = int(input("Informe o tipo de instalão:"))
R = residencia
I = industria
C = comercio
V = valor

if tipoist <= 500:
    R = KwH * 0.40
    
    else:
        if tipoist > 500:
            R = kWh * 0.65
            if tipoist <= 1000:
                R = kWh * 0.55
                else:
                    if tipoist > 1000
                    R = kWh * 0.60
                    if tipoist <= 5000:
                        R = kWh * 0.55
                        else:
                            if  tipoist > 5000:
                                R = kWm *0,60
print("O valor a ser pago é:", valor pago)
            
    