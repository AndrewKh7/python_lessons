x = 2
y = 8

z = x + y
z = x/y # 0.25
z = y/x # 4 (float)

# the integer part of division
z = y//x # 4  
z = x//y # 0

#exponentiation
z=x**y # 256
z=x**0.5 # 1.414213...

#complex
z = -8**0.5 #1.7319..e-16+2.828...j

# import math
# #math
# z = 1.256
# z = math.trunc(z) # 1
# z = math.floor(z) # 1
# z = math.ceil(z)  # 2
# z = -1.256
# z = math.trunc(z) # 1
# z = math.floor(z) # 2
# z = math.ceil(z)  # 1

# z = math.sqrt(2)
# z = math.sin(math.pi / 4)

print(z)

str1 = "Hellow"
str2 = "world"
str3 = "Hellow, world"

print(str1[1],str1[3]) # e l
str4 = "%s = %d" % ("Number",17)  # "Number = 17"
str5 = "{} = {}".format('Number',17.3) #"Number = 17.3"
print(str4)