def dec_bin(dec):
    binval=""
    while(dec!=0):
        binval=str(dec%2)+binval
        dec//=2
    print(binval)
dec_bin(26)

def bin_dec(bin):
    n=len(bin)-1
    dec=0
    for i in bin:
        temp=int(i)
        dec+=temp*(2**n)
        n-=1
    print(dec)
bin_dec("11010")