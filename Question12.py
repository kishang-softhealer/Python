# Question 12: Bracket Matcher
# Have the function bracketMatcher(str) take the str parameter being passed and return 1 if the brackets are correctly matched and each one is accounted for. Otherwise, return 0. Only ( and ) will be used as brackets. If str contains no brackets, return 1.

# ●​ Input: "((hello)(world))"
# ●​ Output: 0
# ●​ Input: "(h(e)llo) (world)"
# ●​ Output: 1

def bracketMatcher(str):
    flage = False
    for i in str:
        if i == "(" and flage is False:
            flage = True
        elif i =="(" and flage is True:
            print(1)    
            return
        if i == ")" and flage is True:
            print(0)
            flage = False
    if flage:
      print(11)
    else:
      print(0)                

 
breket =  "((hello)(world))"
print(bracketMatcher(breket))
      
    
    
    
     
    