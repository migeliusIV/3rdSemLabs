import sys
import math

def get_coefs():
    coefs = []
    try:
        help = sys.argv[1:]
        coefs = [float(i) for i in help]
        if (len(help) != 3):
            raise ZeroDivisionError
    except:
        coefs = []
        for i in range(3):
            while(1):
                print(f"\nInput {i + 1} coeff.")
                try:                        
                    coefs.append(float(input()))
                    break
                except:
                    print("\nWrong type.")    
    return coefs


def get_roots(coefs):
    result = []
    D = pow(coefs[1], 2) - 4 * coefs[0] * coefs[2]
    if (D < 0):
        return result
    elif (D == 0):
        result.append(-coefs[1] / (2 * coefs[0]))
    else:
        result.append((-coefs[1] + math.sqrt(D)) / (2 * coefs[0]))
        result.append((-coefs[1] - math.sqrt(D)) / (2 * coefs[0]))
    for i in range(len(result)):
        try:
            result[i] = math.sqrt(result[i])
            if (result[i] != 0):
                result.append(-result[i])
        except:
            result.pop(i)
    return result

def solution():
    try:
        return get_roots(get_coefs())
    except:
        return []

def main():
    s = "go"
    while (s != "stop"):
        answer = solution()
        if (len(answer) == 0):
            print("No roots")
        else:
            print("Roots: ",*answer)
        print("If you want to stop processing - enter the \'Stop\'")
        s = input()
    


if __name__ == "__main__":
    main()