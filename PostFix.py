#!/usr/bin/python3

''' table that has both binary and hex representation of numbers from 0 - 15'''
tableValues = [("0","0000"),("1","0001"), 
                ("2","0010"),("3","0011"),         
                ("4","0100"),("5","0101"),
                ("6","0110"),("7","0111"),
                ("8","1000"),("9","1001"),         
                ("a","1010"),("b","1011"),         
                ("c","1100"),("d","1101"),         
                ("e","1110"),("f","1111")]


def ValueLookUp(num: str):    
    
    for i in range(0,len(tableValues)):        
        if(tableValues[i][1] == num):            
            return tableValues[i][0]    
    for i in range(0,len(tableValues)):        
        if(tableValues[i][0] == num):            
            return tableValues[i][1]
tos = 0

def Push(stack: [], element):
    global tos    
    stack[tos] = element    
    tos = (tos + 1)


def Pop(stack: []):    
    global tos    
    symbol = stack[tos - 1]    
    tos = (tos - 1)    
    return symbol
    
    
def BitTwiddle(expression ):    
    
    def Shift(direction: str, expr: str):
        binary = ValueLookUp(expr)        
        string = ""        
        if(direction == "<"):            
            for i in range(1,len(binary)):                
                string = string + binary[i]            
            string = string + "0"        
        else:            
            string = string + "0"            
            for i in range(0, len(binary)-1):                
                string = string + binary[i]        
        return string    
    def Not(expr: str):
        binary = ValueLookUp(expr)        
        newStr = ""        
        for i in range(0,len(binary)):            
            if(binary[i] == "1"):                
                newStr = newStr + "0"            
            else:                
                newStr = newStr + "1"        
        return newStr    
    def And(expr1: str, expr2: str):        
        binary1 = ValueLookUp(expr1)        
        binary2 = ValueLookUp(expr2)        
        result = ""        
        for i in range(0,len(binary1)):            
            if(binary1[i] == "1" and binary2[i] == "1"):                
                result = result + "1"            
            else:                
                result = result + "0"        
        return result    
    
    def Xor(expr1: str, expr2:str):        
        binary1 = ValueLookUp(expr1)        
        binary2 = ValueLookUp(expr2)        
        result = ""        
        for i in range(0,len(binary1)):            
            if(binary1[i] ==  binary2[i] ):                
                result = result + "0"            
            else:                
                result = result + "1"        
        return result    
    
    def Or(expr1: str, expr2: str):        
        binary1 = ValueLookUp(expr1)        
        binary2 = ValueLookUp(expr2)        
        result = ""        
        for i in range(0, len(binary1)):            
            if (binary1[i] == "0" and binary2[i] == "0"):                
                result = result + "0"            
            else:                
                result = result + "1"        
        return result    
    stack = [None] * 200    
    
    
    for symbol in expression:        
        if(symbol == "~"):            
            binary = Not(Pop(stack))            
            val = ValueLookUp(binary)            
            Push(stack, val)        
        elif (symbol == ">"):            
            binary = Shift(">",Pop(stack))            
            val = ValueLookUp(binary)            
            Push(stack, val)        
        elif (symbol == "<"):            
            binary = Shift("<",Pop(stack))            
            val = ValueLookUp(binary)
            Push(stack, val)        
        elif (symbol == "&"):            
            binary = And(Pop(stack),Pop(stack))            
            val = ValueLookUp(binary)            
            Push(stack, val)        
        elif (symbol == "^"):            
            binary = Xor(Pop(stack),Pop(stack))            
            val = ValueLookUp(binary)            
            Push(stack, val)        
        elif (symbol == "|"):            
            binary = Or(Pop(stack),Pop(stack))            
            val = ValueLookUp(binary)            
            Push(stack, val)        
        else:            
            Push(stack,symbol)    
    return Pop(stack)
    
    
string = input("enter string here to test\n")
#string = "8<>1><|~" 
print("String in hex = " + BitTwiddle(string))
string2 = input("enter string here to test\n")
#string = "8<>1><|~" 
print("String in hex = " + BitTwiddle(string2))
string3 = input("enter string here to test\n")
#string = "8<>1><|~" 
print("String in hex = " + BitTwiddle(string3))
string4 = input("enter string here to test\n")
#string = "f9>&3~8^|c~b||" 
print("String in hex = " + BitTwiddle(string4))
string5 = input("enter string here to test\n")
#string = "8<>1><|~" 
print("String in hex = " + BitTwiddle(string5))