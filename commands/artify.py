from command_base import Command


def _generate_ascii_art_dict():
	ascii_art_dict = {
		' ': """
   
   
   
   
   """,
		'!': """
  ! 
  !
  !
   
  !""",
		'"': """
" "
" "
   
   
   
""",
		'#': """
 # #
#####
 # #
#####
 # #""",
		'$': """
 $$$
$   
 $$$
   $
$$$""",
		'%': """
%  % 
  %  
 %   
%  % 
  %  """,
		'&': """
 &&& 
& & &
 && &
& & &
 && &""",
		"'": """
  '
  '
   
   
   
""",
		'(': """
  ( 
 (  
 (  
 (  
  ( """,
		')': """
 )  
(   
(   
(   
 )  """,
		'*': """
* * *
 ***
*****
 ***
* * *""",
		'+': """
  +  
  +  
+++++
  +  
  +  """,
		',': """
   
   
   
  , 
 ,  """,
		'-': """
   
   
---
   
   """,
		'.': """
   
   
   
   
 . """,
		'/': """
    /
   /
  /
 /
/    """,
		'0': """
 000 
0   0
0   0
0   0
 000 """,
		'1': """
  1  
 11  
  1  
  1  
 111""",
		'2': """
 222 
2   2
   2 
  2  
2222 """,
		'3': """
 333 
3   3
  33
3   3
 333 """,
		'4': """
4  4 
4  4 
4444 
   4 
   4 """,
		'5': """
5555 
5    
555  
   5 
555  """,
		'6': """
 666 
6    
666  
6   6 
 666 """,
		'7': """
7777 
   7 
  7  
 7   
 7   """,
		'8': """
 888 
8   8
 888 
8   8
 888 """,
		'9': """
 999 
9   9
 9999
    9
 999  """,
		':': """
   
 : 
   
 : 
   """,
		';': """
   
 ; 
   
  ;""",
		'<': """
  <
 < 
<  
 < 
  <""",
		'=': """
    
====
====
    
   """,
		'>': """
 >  
  > 
   >
  > 
 >  """,
		'?': """
 ??? 
?   ?
   ? 
  ?  
  ?  """,
		'@': """
 @@@ 
@   @
@ @@@
@    
 @@@@""",
		'A': """
  A  
 A A 
AAAAA
A   A
A   A""",
		'B': """
BBBB 
B   B
BBBB 
B   B
BBBB""",
		'C': """
 CCC 
C   C
C    
C   C
 CCC""",
		'D': """
DDD  
D  D 
D   D
D  D 
DDD  """,
		'E': """
EEEE 
E    
EEE  
E    
EEEE """,
		'F': """
FFFFF
F    
FFF  
F    
F    """,
		'G': """
 GGG 
G    
G GGG
G   G
 GGGG""",
		'H': """
H   H
H   H
HHHHH
H   H
H   H""",
		'I': """
 III 
  I  
  I  
  I  
 III """,
		'J': """
JJJJJ
   J 
   J 
J  J 
 JJ  """,
		'K': """
K   K
K  K 
KKK  
K  K 
K   K""",
		'L': """
L    
L    
L    
L    
LLLLL""",
		'M': """
M   M
MM MM
M M M
M   M
M   M""",
		'N': """
N   N
NN  N
N N N
N  NN
N   N""",
		'O': """
 OOO 
O   O
O   O
O   O
 OOO """,
		'P': """
PPPP 
P   P
PPPP 
P    
P    """,
		'Q': """
 QQQ 
Q   Q
Q Q Q
Q  QQ
 QQ Q""",
		'R': """
RRRR 
R   R
RRRR 
R R  
R  RR""",
		'S': """
 SSS 
S    
 SSS 
    S
SSSS """,
		'T': """
TTTTT
  T  
  T  
  T  
  T  """,
		'U': """
U   U
U   U
U   U
U   U
 UUU """,
		'V': """
V   V
V   V
V   V
 V V 
  V  """,
		'W': """
W   W
W   W
W W W
WW WW
W   W""",
		'X': """
X   X
 X X 
  X  
 X X 
X   X""",
		'Y': """
Y   Y
 Y Y 
  Y  
  Y  
  Y  """,
		'Z': """
ZZZZZ
   Z 
  Z  
 Z   
ZZZZZ""",
		'[': """
[[[  
[    
[    
[    
[[[  """,
		'\\': """
\    
 \   
  \  
   \ 
    \
    """,
		']': """
    ]]]
    ]
    ]
    ]
    ]]]  """,
		'^': """
         ^
         ^ ^


         """,
		'_': """




    _____""",
		'`': """
    `
    `


    """,
		'{': """
    {{
        {
            {{
                {
                    {{""",
		'|': """
|
|
|
|
|  """,
		'}': """
}}
}
}}
}
}}   """,
		'~': """
~~ \
~  ~ \


"""
	}
	return ascii_art_dict


class artify(Command):
	def __init__(self):
		name = 'artify'
		prefix = 'artify'
		help_text = 'Converts input text into ASCII art.'
		super().__init__(name, prefix, help_text)
		self.ascii_art_dict = _generate_ascii_art_dict()

	def execute(self, input_data):
		ascii_lines = ['' for _ in range(6)]
		for char in input_data.upper():
			if char in self.ascii_art_dict:
				char_art_lines = self.ascii_art_dict[char].split('\n')
				for i, line in enumerate(char_art_lines):
					ascii_lines[i] += line + '  '
			else:
				ascii_lines[0] += char + '  '
				for i in range(1, 5):
					ascii_lines[i] += ' ' * len(char) + '  '

		ascii_art = '\n'.join(ascii_lines)
		print(ascii_art)
