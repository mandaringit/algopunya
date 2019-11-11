'''
1)
*
**
***
****

2)
*
**
***
****
*
**
***
****

3)
     *
    ***
   *****
  *******
 *********
***********
'''

# for i in range(1,5):
#     print("*"*i)

# i = 1;
# while i<=4 :
#     print("*"*i)
#     i += 1

# for i in range(1,3):
#     for j in range(1,5):
#         print("*"*j)

for i in range(1,12,2):
    print("{0:^11}".format("*"*i))
