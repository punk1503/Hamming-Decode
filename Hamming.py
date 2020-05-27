from textwrap import wrap
#функция нахождения XOR защитных бит
def xor(arr, xorStep):
	tmpArr = []
	for i in range(xorStep-1, len(arr), xorStep*2):
		for j in range(i, i+xorStep):
			tmpArr.append(arr[j])
	counter = tmpArr.count('1')
	if counter%2==1:
		return 1
	else: 
		return 0

def convert(element):
	if(int(element)<32 or int(element)>255):
		return ""
	russian_codes = list(range(192, 256))
	russian_chars = [chr(i) for i in range(ord("А"), ord("я") + 1)]

	english_codes = list(range(ord(" "), ord("~") + 1))
	english_chars = [chr(i) for i in range(ord(" "), ord("~") + 1)]

	combined_chars = english_chars + russian_chars
	combined_codes = english_codes + russian_codes

	dic = dict(zip(combined_codes, combined_chars))
	return dic[int(element)]
	

def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]				

a = input()
a=a.replace(" ", "")
final=""
while(len(a) > 0):
	tmpArr = a[0:15]
	tmpArr = wrap(tmpArr, 1)
	a = a[15:len(a)]
	error = (xor(tmpArr, 8)*8 + xor(tmpArr, 4)*4 + xor(tmpArr, 2)*2 + xor(tmpArr, 1))-1
	if error<=0:
		error=0;
	if tmpArr[error]=="1":
		tmpArr[error]="0"
	else:
		tmpArr[error]="1"
	#удаляем защитные биты
	del tmpArr[7]
	del tmpArr[3]
	del tmpArr[1]
	del tmpArr[0]
	for i in range(len(tmpArr)):
		final+=tmpArr[i]
final = wrap(final, 8)
for i in range(len(final)):
	final[i]=convert_base(final[i], 10, 2)
finalstr=""
for i in range(len(final)):
	finalstr = finalstr+convert(final[i])
print(finalstr)
input()