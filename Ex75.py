while True:
    n = int(input("Quer ver a tabuada de qual número? "))
    
    if n < 0: break
    
    print(f"\n===== Tabuada de {n} =====\n")
    for i in range(10):
        print(f"{i+1} x {n} = {n*(i+1)}")
    print("\n============================\n")