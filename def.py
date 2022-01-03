import os
import sys
import pefile

def main3():
    print("LIBRARY _"+sys.argv[1])
    print("EXPORTS")
    filepath = sys.argv[1]
    pe = pefile.PE(filepath)
    exportTable = pe.DIRECTORY_ENTRY_EXPORT.symbols
    for sym in exportTable:
        dllh = sym.ordinal
        dllhs = sym.name.decode('utf8')
        print("    "+str(dllhs)+" = "+"_"+sys.argv[1]+"."+str(dllhs)+" @"+str(dllh))

main3()