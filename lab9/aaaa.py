# try:
#     b = 2/0
#     a = 1+ 'hundred'
# except Exception as e:
#     print('error :',e)

# try:
#     a = [10,20,30]
#     a[3]
# except Exception as e:
#     print('error: ',e)

# try:
#     n = int('20%')
# except Exception as e:
#     print('error: ',e)

# try:
#     a = 100 + '200'
# except Exception as e:
#     print('error: ',e)

# try:
#     a,b = input('두 수를 입혁하시오: ').split()
#     result = int(a) / int(b)
# except ZeroDivisionError:
#     print('오류: 0으로 나눔을 시도해습니다.')
# except ValueError:
#     print('오류 : 입력 값이 정수나 실수가 아닙니다.')
# except:
#     print('오류 : 10 2와 같이 두 정수를 입력하세요.')
# else:
#     print('{} / {} = {}'.format(a,b,result))
# finally:
#     print('good')

# a = [1,2,3,4,5]
# n = int(input("a의 요소를 하나 선택하시오 : "))


# U = (0,1)
# D = (0,-1)
# L = (-1,0)
# R = (1,0)

# r = 0
# c = 0

# move = input()
# for i in move:
#     if i == 'U':
#        r += U[0]
#        c += U[1]
#     elif i == 'D':
#         r += D[0]
#         c += D[1]
#     elif i == 'L':
#         r += L[0]
#         c += L[1]
#     elif i == 'R':
#         r += R[0]
#         c += R[1]

# print(r,c)


