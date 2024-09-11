import random

def jugada():
    humano='x'
    while humano!='R' and humano!='P' and humano!='S':
        humano=input('Rock , Papper or Scissor?')
    comp=random.choice (['R','P','S'])
    return(humano,comp)
def ganador(h, c):
    if h==c :
        return ('tie')
    elif h=='R' and c=='S' or h=='S' and c=='P' or h=='P' and c=='R':
        return('won')
    return ('loser')
def main():
    h,c=   jugada()
    resultado=ganador(h,c)
    print(f'{h} vs {c}')
    print (resultado)
     
main()
        