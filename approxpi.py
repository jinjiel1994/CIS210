import math
import argparse

def my_pi(terms):
    sum = 0
    for i in range(terms):
        sum = sum + (-1)**i / ((2*i+1)*3**i)
    return sum * math.sqrt(12)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("terms", type=int)
    args = parser.parse_args()
    terms = args.terms
    approx_pi = my_pi(terms)
    print("Approximation for pi after summing", terms, "terms is", approx_pi)
    difference = math.fabs(approx_pi)
    print("percentage error relative to math.pi is", '{:5%}'.format(1-difference/math.pi))

if __name__ == "__main__":
    main()
    
