# -*- coding: utf-8 -*-

import sys
import time


__HEART__ = '''

          @@@@@@@@@@@                @@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@          @@@@@@@@@@@@@@@@@@
   @@@@@@@@@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                @@@@@@@@@@@@@@@@@@@@@@@@@@
                   @@@@@@@@@@@@@@@@@@@@
                       @@@@@@@@@@@@
                            @@

'''


# ================= TYPEWRITER EFFECT =================
def typewriter(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


# ================= COLOR CLASS =================
class Color:
    @property
    def RED(self):
        return '\033[91m'

    @property
    def BOLD_YELLOW(self):
        return '\033[93m'

    @property
    def NORMAL(self):
        return '\033[0m'


# ================= VALENTINE CLASS =================
class Valentine:
    def __init__(self, name):
        self.loved_one = name

    def romanticize(self):
        you_in_my_heart = __HEART__

        while '@' in you_in_my_heart:
            for letter in list(self.loved_one):
                you_in_my_heart = you_in_my_heart.replace('@', letter, 1)

        return you_in_my_heart

    def i_love_you(self):
        C = Color()

        # Print Heart
        print(C.RED + self.romanticize() + C.NORMAL)

        # Dramatic pause
        time.sleep(0.5)

        # Romantic message with typing effect
        message = f'''Everytime you smile, a flower blooms in my soul {self.loved_one}. 
in a world full of worries, you are my moment of happiness.
I Pray For You, Happy Valentine's Day!

i know you're tired, i know life has'nt been easy lately, 
but i also know how strong you are.
you carry so much more than anyone realizes...
just know this, i see you, i believe in you,
in the day that no one stand up for you,
i always here for you. 
you're never alone, not while i'm still breathing.

This song is for you...
Sempurna - Andra & The Backbone
https://open.spotify.com/track/2UgCs0i0rNHUH2jKE5NZHE?si=f2012365f7d24719 (Ctrl+Click)
'''

        print(C.BOLD_YELLOW, end='')
        typewriter(message, 0.05)
        print(C.NORMAL)


# ================= MAIN =================
def main():
    try:
        name = sys.argv[1]
    except IndexError:
        name = 'Zaskiya'

    my_beloved = Valentine(name)
    my_beloved.i_love_you()


if __name__ == '__main__':
    main()