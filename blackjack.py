number = ["2", "3", "4", "5", "6"]
null = ["7", "8", "9"]
letter = ["10", "J", "Q", "K", "A"]

card = 0

def card_count(card):
    
    choose = (input("Choose a card: "))
    if choose in number:
        card += 1
        return f"{card} Bet"        
    elif choose in null:
        card = 0  
        return f"{card} Hold"        
    elif choose in letter:
        card -=1
        return f"{card} Hold"
    
decision = (card_count(card))
print(decision)