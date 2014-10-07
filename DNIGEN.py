#-------------------------------------------------------------------------------
# Name:        DNIGEN.py
#
# Author:      mmasser95
#
# Created:     07/10/2014
#                                                                           
# Licence:     GPLv3
#-------------------------------------------------------------------------------
import random
def main():
    dni = random.randint(10000000, 49999999)
    tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
    module = dni % 23
    dni = str(dni) + tabla[module]
    return dni

if __name__ == '__main__':
    for i in range(20):
        print main()
