def potegowanie(pod, wyk):
    if wyk == 0:
        return 1
    else:
        print(wyk)
        return pod * potegowanie(pod, wyk - 1)

potegowanie(2, 5)