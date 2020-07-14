# 유니코드
print(u'잘가\u0020세상 !')

# 메서드
## join()
slayer = ["버피", "앤", "아스틴"]
print(" ".join(slayer))
print("-<>-".join(slayer))
print("".join(slayer))
print("".join(reversed(slayer)))

# ljust(), rjust()
name = "스칼렛"
print(name.ljust(50, "-"))
print(name.rjust(50, "-"))

# format
print("{0} {1}".format("안녕", "파이썬!"))
print("이름 : {who}, 나이: {age}".format(who="제임스", age=17))
import decimal

print("{0} {0!s} {0!r} {0!a}".format(decimal.Decimal("99.9")))

# 문자열 언패킹
hero = "버피"
number = 999
print("{number}: {hero}".format(**locals()))

# splitlines()
slayers = "로미오\n줄리엣"
print(slayers.splitlines())

# split()
words = "버피*크리스-메리*16"
fields = words.split("*")
print(fields)
job = fields[1].split("-")
print(job)

# strip
words2 = "로미오 & 줄리엣999"
print(words2.strip("999"))

# swapcase()
words3 = "Buffy and Faith"
print(words3.swapcase())
