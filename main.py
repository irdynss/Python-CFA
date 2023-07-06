#!/user/bin/env python

import main()

"""start a guessing genre music between "rhythm and blues","emo","soul music","jazz","classical music."""
     print("guess the genre music")

    x=random choice(music)
    guess=None

    while x !=guess:

   guess=int(input("pick a music genre:"))
    
   if x ==guess: 
       print ("congrats")
    else:
        print ("try again")
main()
