##import re
##class person:
##    name = ""
##    birthdate = ""
##    company = ""
##    phone = ""
##
##class moo:
##    def _first(self, pslist):
##        with open('namecard.txt', 'w') as file:
##            for i in pslist:
##                file.write("{},".format(i.name))
##                file.write("{},".format(i.birthdate))
##                file.write("{},".format(i.company))
##                file.write("{}".format(i.phone))
##                file.write("\n")
##
##    def _se(self, pslist):
##        with open('namecard.txt', 'r') as file:
##            line = None
##            lst = []
##            for line in file:
##                ps = person()
##                lst = line.strip('\n')
##                lst = lst.split(",")
##                ps.name = lst[0]
##                ps.birthdate = lst[1]
##                ps.company = lst[2]
##                ps.phone = lst[3].strip('\n')
##                pslist.append(ps)
##
##pslist = []
##final = moo()
##final._se(pslist)
##
##while(1):
##    a = int(input("1. 명함 입력 \n2. 명함 검색 \n3. 명함 전체 출력 \n4. 명함 수정 \n5. 명함 삭제 \n6. 종료 \n"))
##    ps = person()
##    
##    if a == 1:
##        try :
##            ps.name = input("이름을 입력하세요 : ")
##            ps.birthdate = input("생년월일을 입력하세요 : ")
##            if(re.match("[1-9]{4}.[0-9]{2}.[0-9]{2}", ps.birthdate)  == None):
##                raise Exception("0000.00.00 형식으로 생년월일을 입력하세요 : ")
##            ps.company = input("회사를 입력하세요 : ")
##            ps.phone = input("전화번호를 입력하세요 : ")
##            if(re.match("010-[0-9]{4}-[0-9]{4}", ps.phone) == None):
##                raise Exception("010-0000-0000 형식으로 번호를 입력하세요 : ")
##            pslist.append(ps)
##        except Exception as e:
##            print(e)
##    elif a == 2:
##        n = input("이름을 입력하세요 : ")
##        for i in pslist:
##            if (i.name == n):
##                print("이름 : {}".format(i.name))
##                print("생년월일 : {}".format(i.birthdate))
##                print("회사 : {}".format(i.company))
##                print("전화번호 : {}".format(i.phone))
##    elif a == 3:
##        for i in pslist:
##            print("이름 : {}".format(i.name))
##            print("생년월일 : {}".format(i.birthdate))
##            print("회사 : {}".format(i.company))
##            print("전화번호 : {}".format(i.phone))
##
##    elif a == 4:
##        e = input("수정 할 이름을 입력하세요 : ")
##        for i in pslist:
##            if (i.name == e):
##                i.name = input("이름 : ")
##                i.birthdate = input("생년월일 : ")
##                i.company = input("회사 : ")
##                i.phone = input("전화번호 : ")
##
##    elif a == 5:
##        d = input("삭제 할 이름을 입력하세요 : ")
##        for i in pslist:
##            if (i.name == d):
##                pslist.remove(i)
##        
##    elif a == 6:
##        final._first(pslist)
##        print("종료되었습니다.")
##        break

##------------- 예외처리 ----------
##def test(a, b):
##    return a + b
##
##try :
##    test("tes", 10)
##    
##except Exception as e:
##    print("예외 발생!!", e)

##try :
##    x = int(input('나눌 숫자를 입력하세요 : '))
##    y = 10 / x
##
##except ZeroDivisionError :
##    print('숫자를 0으로 나눌 수 없습니다.')
##
##else :
##    print(y)
    
##try :
##    x = int(input('나눌 숫자를 입력하세요 : '))
##    y = 10 / x
##
##except ZeroDivisionError :
##    print('숫자를 0으로 나눌 수 없습니다.')
##
##else :
##    print(y)
##
##finally :
##    print('코드 실행이 끝났습니다.')

##------- 43장 정규식 ------------

##import re

##print(re.match("010-[1-9]?+[0-9]?+[0-9]?+[0-9]?+-[0-9]?+[0-9]?+[0-9]?+[0-9]?",
##               "010-9753-8046"))

##print(re.match("[0-9]{6}-[0-9]{7}", "020725-3895615"))
##---------------------------------------------------------##


##lst = []
##leng = int(input())
##lst = [[0 for i in range(leng)] for i in range(leng)]
##print(lst)
##for i in range(len(lst)):
##    lst[i] = list(map(int, input().split(" ")))
##
##total = 0
##for i in range(len(lst)):
##    for x in range(len(lst[i])):
##        if lst[i][x] == 0:
##            for cnt in range(len(lst)):
##                total = total + lst[i][cnt] + lst[cnt][x]
##
##print(total)
##-----------------------------------------##

##------ 0을 기준으로 x자 모양으로 좌표값 합계 -------
##leng = int(input()) 
##lst = []
##for i in range(leng):
##    lst.append(list(map(int, input().split(" "))))
##
##total = 0
##loc_x = 0
##loc_y = 0
##for i in range(len(lst)):
##    if (0 in lst[i]) == True:
##        loc_x = i
##        loc_y =  lst[i].index(0)
##
##for i in range(len(lst)):
##    for x in range(len(lst[i])):
##        if ((loc_x + loc_y) == i + x or (loc_y - loc_x) == x - i):
##            total = lst[i][x] + total
##
##print(total)
##----------------------------------------------------------------------            















