def main():
    
    print(wspolne('kot','kot'))
    print(wspolne('kot','pies'))
    print(wspolne('123', '11'))
    print(wspolne('kokos','super kot'))
    
def wspolne(s, a):
    
    wspolne = []
    
    for i in s:
        if i in a and i not in wspolne: #'i not in wspolne' zeby nie bylo duplikatow
            wspolne.append(i)
        else:
            continue
        
    return wspolne
    
main()