import random

def pass_gen(p_qua, p_len, src, dig, low, upp, sym):
    res, psw, c0 = [], '', 0
    while c0 != p_qua:
        c1, c2, c3, c4 = 0, 0, 0, 0
        if dig == []: c1 = 1
        elif low == []: c2 = 1
        elif upp == []: c3 = 1
        elif sym == []: c4 = 1       
        for _ in range(p_len):
            psw += (random.choice(src))   
        for j in psw:
            if j in dig: c1 += 1 
            elif j in low: c2 += 1 
            elif j in upp: c3 += 1 
            elif j in sym: c4 += 1
            if c1 > 0 < c2 and c3 > 0 < c4: 
                res.append(psw)
                psw = ''
                c0 += 1
                break
        if not (c1 * c2 * c3 * c4): psw = ''           
    return res
                         
def is_num(n):
    while True:
        if not n.isdigit():
            n = input('Incorrect input, only digits allowed! Try again: ')
            continue
        else:
            return int(n)
    
def check_answ(answ):
    while True:
        if answ != 'y' and answ != 'n':
            if answ == '':
                answ = 'y'
                return answ
            answ = input('Unclear, try again ... [y - yes, n - no]: ')
            continue
        else:
            return answ

def check_len(p_len):
    while True:
        if int(p_len) < 4:
            p_len = input('Password length is too short, try again: ')
            continue
        else:
            return int(p_len)

def ambi_detect(data):
    new_data = []
    for i in range(len(data)):
        if data[i] == 'i' and data[i] == 'l' and  data[i] == 'o' and data[i] == 'O' and data[i] == 'L' and data[i] == '0' and data[i] == '1':
            continue
        else:
            new_data.append(data[i])
    return new_data              

print("--> Let's make some magic ! <--")
pass_q = is_num(input('> How many passwords would you like to generate?: '))
pass_len = check_len(is_num(input('> Password length: ')))
digits = ['0','1','2','3','4','5','6','7','8','9'] if check_answ(input('* [Enter] key is setting up for [yes] mode by default \n> Whether to include digits? [y/n]: ').lower()) == 'y' else []
locase_l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] if check_answ(input('> Whether to include lowercase letters? [y/n]: ').lower()) == 'y' else []
upcase_l = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] if check_answ(input('> Whether to include capital letters? [y/n]: ').lower())  == 'y' else [] 
symbols = ['!','#','$','%','&','*','+','-','=','?','@','^','_'] if check_answ(input('> Whether to include special characters(!#$%&*+-=?@^_)? [y/n]: ').lower())  == 'y' else [] 
ambi_sym = True if check_answ(input('> Whether to exclude ambiguous characters(il1Lo0O)? [y/n]: ').lower())  == 'n' else False 

if ambi_sym == False:
    digits = ambi_detect(digits)   
    locase_l = ambi_detect(locase_l)   
    upcase_l = ambi_detect(upcase_l)  
    
source = []

random.shuffle(digits)
random.shuffle(locase_l)
random.shuffle(upcase_l)
random.shuffle(symbols)

source.extend(digits)
source.extend(locase_l)
source.extend(upcase_l)
source.extend(symbols)

random.shuffle(source)

x_pass = pass_gen(pass_q, pass_len, source, digits, locase_l, upcase_l, symbols)
for i in range(len(x_pass)):
    print(i + 1, 'password:', x_pass[i])


