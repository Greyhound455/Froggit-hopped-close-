print ('Froggit hopped close')

battleStart = input('|Fight|Act|Item|Spare|')
def choice( battleStart ):
  switcher = {
    "fight": "You won! gained 2 gold and 5 EXP",
    "act": "Froggit didn't understand what you said but was flattered anyway. You won! gained 0 gold and 0 EXP",
    "item": "You have no items.",
    "spare": "You won! gained 0 gold and 0 EXP",
  }
  print( switcher.get( battleStart, "Please choose from the available opptions"))

choice( battleStart )