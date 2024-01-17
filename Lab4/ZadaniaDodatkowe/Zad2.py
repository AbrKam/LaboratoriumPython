def main():
    
    minmax(2,4,5,6)
    minmax(7,4,2)
    
def minmax(*a):
    print(f'Max: {max(a)}\nMin: {min(a)}\n')
    
main()