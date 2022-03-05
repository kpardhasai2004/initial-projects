from operator import index
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caster(input_text, shif_count):
  out_put=""
  if what_to_do=="decode":
      shif_count*=-1
  for char in input_text:
    if char in alphabet:
      input_text_position=alphabet.index(char)
      change_in_index=input_text_position+shif_count
      out_put+=alphabet[change_in_index]
    else:
      out_put+=char
  print(out_put)

should_end=False

while not should_end:
  what_to_do=input("select one 'encode' or 'decode': ").lower()
  initial=input("Enter a the text that has to be "+what_to_do+" : ")
  shift_count=(int(input("Enter the shift count: ")))% 26
  caster(input_text=initial,shif_count=shift_count)
  continue_=input("Do you want to continue select 'yes' or 'no': ")
  if continue_=="no":
    should_end=True
    print("Bye!")