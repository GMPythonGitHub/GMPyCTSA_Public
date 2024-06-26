# gm_class_numbers_b.py: coded by Kinya MIURA 230418
# ---------------------------------------------------------
print('*** class GMNumbersB: operating numbers ***')
print('   *** with functions for calculations ***')

# =========================================================
print('### --- section_class: (GMNumbersB) describing class --- ###')
class GMNumbersB():
    ## --- section_ca: initializing class instance --- ##
    def __init__(self) -> None:
        self.aa, self.bb = None, None  # instance variables
    ## --- section_cb: functions for arithmetics --- ##
    def add(self) -> float: return self.aa + self.bb
    def sub(self) -> float: return self.aa - self.bb
    def calc(self) -> tuple:
        return self.add(), self.sub()

# =========================================================
print('### --- section_main: (GMMumbersB) main process --- ###')
## --- section_ma: calculating arithmetics --- ##
numbs = GMNumbersB()  # creating instance
numbs.aa, numbs.bb = 3, 2
print(f'{numbs.aa = }, {numbs.bb = }')
add, sub = numbs.calc()  # using instance functions
print(f'{add = }, {sub = }')
## --- section_mb: calculating arithmetics --- ##
numbs.aa, numbs.bb = 7, 3  # setting instance valuables
print(f'{numbs.aa = }, {numbs.bb = }')
add, sub = numbs.calc()  # using instance functions
print(f'{add = }, {sub = }\n')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** class GMNumbersB: operating numbers ***
   *** with functions for calculations ***
### --- section_class: (GMNumbersB) describing class --- ###
### --- section_main: (GMMumbersB) main process --- ###
numbs.aa = 3, numbs.bb = 2
add = 5, sub = 1
numbs.aa = 7, numbs.bb = 3
add = 10, sub = 4
'''
