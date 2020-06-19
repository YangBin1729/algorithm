def digit_sum(a,b):
    x=[a] if a<10 else [a%10,a//10]
    for i in range(1,b):
        x = [2* i for i in x]
        for i in range(len(x)-1):
            if x[i] >= 10:
                x[i] -= 10
                x[i+1] += 1
            if x[-1]>=10:
                x[-1]-=10
                x.append(1)
    return(x)