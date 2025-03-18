import random
import sys
import os
import msvcrt
import time

steno_to_outputs = {
    "s (left)": ["is", "s"],        
    "t (left)": ["it", "t"],       
    "p (left)": ["p","about"],             
    "h": ["had", "h"],            
    "k": ["can", "k"],             
    "w": ["with", "w"],            
    "r (left)": ["are", "r"],     
    "f": ["of", "f"],              
    "r (right)": ["are", "r"],   
    "p (right)": ["p","."],          
    "b": ["be", "b"],              
    "l": ["ll", "'ll"],           
    "g": ["ing"],                 
    "t (right)": ["t","the"],            
    "s (right)": ["es", "s", "ses"],      
    "d": ["ed", "d", "ded"],       
    "z": ["s", "z"],                
    "a": ['a'],
    "o": ['to'],
    "e": ['he'],
    "u": ['you']
}


steno = list(steno_to_outputs.keys())

def capture_plover_word():
    sys.stdout.flush()  
    
    word = ""
    last_input_time = time.time()
    buffer_timeout = 0.2  
    
    while True:
        if 'msvcrt' in sys.modules and msvcrt.kbhit():
            char = msvcrt.getch().decode('utf-8', errors='ignore')
            if char == "\b":  
                word = word[:-1] if word else ""
            elif char in "\r\n": 
                continue
            else:
                word += char
            last_input_time = time.time()
        else:
            if word and (time.time() - last_input_time > buffer_timeout):
                break
        time.sleep(0.01)  
    
    word = word.strip()

    return word

def main():
    print("Welcome to Steno Practice! Type the word for each key shown.")
    print("Press Ctrl+C to quit.\n")
    nIter = 0
    while True:
        item = random.randrange(len(steno))
        steno_key = steno[item]
        expected_outputs = steno_to_outputs[steno_key]
        
        print(f"{steno_key}")
        result = capture_plover_word()
        
        if not result:
            print("No input detected. Try again.")
            continue
        
       
        if any(result.lower() == output.lower() for output in expected_outputs):
            nIter +=1
            print(f"Good! {nIter}")
            
        else:
            print("Wrong.")
            nIter = 0
        
        print()  
        time.sleep(0.2)  

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nAlready done? :(")