# 2026.05.13
# programmers34.py

def solution(letter):
    
    letter_list = letter.split()
    
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    
    result = [morse[item] for item in letter_list if item in morse ]
    
    answer = ''.join(result)
    
    return answer
