"""
6 - Faça um programa em C para exibir a tabuada de 0 a 9.
"""

for i in range(0,10):
    print("Tabuada do ",i)
    for t in range(0,11):
        print(i,"X", t, "=", i*t)
print("\n")