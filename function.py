# functions.py
import WordsCo
def calculate(token,words):
    n=len(token)
    c,b,d,a,sum=0
    for i in range(n):
        for x in words:
            if token[i]=='not' and token[i+1]=='so':
                c = c+1
                s=words.get(x)
                sum+= s
                break
            
            if token[i]=='not' and token[i+1]==x: 

                c = c+1
                s=words.get(x)
                sum+= -s
                break
            elif token[i]=='so' and token[i+1]==x:
                
                b=b+1
                sum+= 100
                break
            elif token[i]=='very' and token[i+1]==x:
                d=d+1
                sum+= 100
                break
            elif(token[i]==x and c==0 and b==0 and d==0):
                a=a+1
                sum+=words.get(x)
                break
            else:
                sum+=0
    if(c == 0 and b==0 and d==0 and a==0):
        return 0
    
    else :
        avg = sum/(a+b+c+d) 
     
    print(avg)        
    return avg


 
def tokenization(str):
    
    print(str)
    n = len(str)
    str = str.lower()
    token = str.split()
    print(token)
    return token

def StopWord(str,word):
    
    for i in str:
        if i in word:
            str.remove(i)
         
    return str
def index(user):
    
    # userI = gui.display.entry.get()
    userI=user
    str1 = tokenization(userI)
    str= StopWord(str1,WordsCo.stop_word)
     
 
    negative = WordsCo.negative_words
    neg = calculate(str,negative)
    if(neg==0):
        print(neg," nutral sentance")
    else:
        print(neg,'%nagative sentance')
    positive = WordsCo.positive_words
    pos = calculate(str,positive)
    if(pos==0):
        print(pos," nutral sentance")
    else:
        print(pos,'% Positive sentance')

    final_Output = pos - neg
     
    print("over all sentimant analisis" , final_Output)
    return  final_Output
