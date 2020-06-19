num2word={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',
               11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',
               18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',
               70:'seventy',80:'eighty',90:'ninety',100:'hundred',1000:'thousand'}

def len_of_num(num):
    if num<=20:
        word=num2word[num]
        letters_of_num=len(word)
    elif num>20 and num<100:
        a=num%10
        if a==0:
            letters_of_num=len(num2word[num])
        else:
            b=num-a
            letters_of_num=len(num2word[b]+num2word[a])
    elif num>=100 and num<1000:
        a=num//100
        if num%100==0:
            letters_of_num=len(num2word[a]+num2word[100])
        else:
            b=num%100
            letters_of_num=len(num2word[a]+num2word[100]+'and')+len_of_num(b)
    else:
        a=num//1000
        if num%1000==0:
            letters_of_num=len(num2word[a]+num2word[1000])

    return(letters_of_num)



sum=0
for num in range(1,1001):
    sum+=len_of_num(num)

print(sum)


def len_of_num(num):
    try:
        return(len(num2word(num)))
    except:
