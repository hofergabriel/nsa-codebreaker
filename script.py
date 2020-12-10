
def main():
  f = open('signal.ham', 'rb')
  bit=f.read(2)
  integer=bin(int.from_bytes(bit, byteorder='little', signed=False))[2:].zfill(16)
  while bit:
    print(bit)
    print(integer)
    bit=f.read(2)
    integer=bin(int.from_bytes(bit, byteorder='little', signed=False))[2:].zfill(16)

main()


