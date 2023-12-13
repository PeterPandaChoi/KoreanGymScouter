score = 0

def printScore():
    print("\n\n헬스장 점수 : "+str(score)+"\n")
def yesOrNo(choi,sco,plus,minus):
    if choi == 'yes' or choi == 'y':
        sco += plus
    elif choi == 'no' or choi == 'n':
        sco -= minus
    else:
        sco += 0
    return sco
def finalScore(sco):
    print("헬스장 평가 최종 점수는 "+str(sco)+"입니다.")
    if sco<0:
        print("이런 헬스장을 다닐 생각입니까?")
    elif sco <40:
        print("다시 한번 생각해보세요")
    elif sco <60:
        print("이 헬스장 말고 옵션이 더 있는지 한번 보시겠어요?")
    elif sco <80:
        print("나쁘지 않군요. 더 나은 옵션이 없다면 무난할겁니다.")
    elif sco <100:
        print("본인 눈이 틀리지 않았다면 제법 괜찮은 곳입니다.")
    elif sco >=100:
        print("이렇게 좋은 헬스장이 있을 수가 있나요? 당장 계약하세요.")
    else:
        print("뭔가 잘못되었군요.")


print("- 헬스장과의 거리 -")
print("""
    1 - 5분이내\n
    2 - 10분이내\n
    3 - 15분이내\n
    4 - 20분이내\n
    5 - 20분 이상
    """)
choice = int(input(" 선택 (1~5 중 하나) : "))
distance= (6-choice)*5
score += distance

printScore()


print("- 헬스장 가격 -")
print("""
    1 - 한달 2만원\n
    2 - 한달 3만원\n
    3 - 한달 4만원\n
    4 - 한달 5만원\n
    5 - 한달 6만원 또는 그 이상
    """)
choice = int(input(" 선택 (1~5 중 하나) : "))
price = (6-choice)*3
score += price
printScore()

print("- 헬스장 청결도 -")
print("""
    1 - 오래된 가구에도 먼지가 없음\n
    2 - 먼지가 보통 없이 깔끔\n
    3 - 청소는 하는 것 같음\n
    4 - 공기청정기에 때가껴있음\n
    5 - 솔직히 많이 더럽다.
    """)
choice = int(input(" 선택 (1~5 중 하나) : "))
if choice==1:
    print("청결도 추가점수")
    clean = 15
else:
    clean = (6-choice)*2
score += clean
printScore()


print("- 헬스장 직원 매너 -")
print("""
    1 - 손님 입/퇴장시 인사를 한다.\n
    2 - 회원간 갈등을 중재한다.\n
    3 - 카운터 질문 등에 쾌활하게 답변한다.\n
    4 - 전체적으로 친절하고 매뉴얼적인 말투가 없다.\n
    5 - 청소나 상담 등 일에대한 태도가 불쾌하지 않다.
    """)
choice = int(input(" 위 내용 중 몇가지에 해당되는지 (1~5가지) : "))
manner = choice*2
score += manner
printScore()

trainer=0
print("- 트레이너 역량 평가 -")
print("\n 트레이너의 대응이 친절했다. \n")
choice = input("yes or no (y/n): ")
trainer = yesOrNo(choice,trainer,6,2)

print("\n 트레이너 프로필의 과도하게 노출이 없다. \n")
choice = input("yes or no (y/n): ")
trainer = yesOrNo(choice,trainer,6,2)

print("\n 트레이너가 운동에 대한 설명을 잘 한다. \n")
choice = input("yes or no (y/n): ")
trainer = yesOrNo(choice,trainer,6,2)

print("\n 트레이너가 질문을 친절하게 답변한다. \n")
choice = input("yes or no (y/n): ")
trainer = yesOrNo(choice,trainer,6,2)

print("\n 트레이너가 동성이다, 또는 이성인 경우 찝적대지 않는다. \n")
choice = input("yes or no (y/n): ")
trainer = yesOrNo(choice,trainer,6,2)

score +=trainer
printScore()

print("\n 비매너 회원이 있는 경우 중재를 해주냐고 물어본 뒤 답변 \n")
choice = input("yes or no (y/n): ")
arbitrate = 0
arbitrate = yesOrNo(choice,arbitrate,5,15)
score +=arbitrate
printScore()

print("\n -  환불 규정이 표준 헬스장 환불 규정과 다르다. - \n")
choice = input("yes or no (y/n): ")
if choice == 'yes' or choice =='y':
    print("※"*32+"\n※경고 : 해당 헬스장에서는 환불을 받기가 어려울 수 있습니다. \n※할부 또는 짧은 기간을 먼저 사용하는 것을 권장합니다.\n"+"※"*32)
refund = 0
refund = yesOrNo(choice,refund,-10,-10)
score +=refund
printScore()

print("- 시설 존재여부 -")
print("""
    1 - 화장실\n
    2 - 샤워실\n
    3 - 탈의실
    """)
choice = int(input(" 위 시설 중 몇가지가 있는지 (1~3가지) : "))
facility = choice
score += facility
printScore()

print("- 에어로빅/GX 존재여부 -")
choice = input("yes or no (y/n): ")
score = yesOrNo(choice,score,-5,0)
printScore()

finalScore(score)

#분야별로 점수를 다르게 받아서 어떤 부분에 어떤 점수를 받았는지 총량을 보여주고 분석.
#distance, price, manner, trainer, arbitrate, refund, facility
formatSentence = "| {0} : \t{1}{2}\t\t\t\t\t|"
print("----------------------------------------------------------------")
print(formatSentence.format("거리","■"*int(distance/5),"□"*int((25-distance)/5)))
print(formatSentence.format("가격","■"*int(price/3),"□"*int((15-price)/3)))
print(formatSentence.format("매너","■"*int(manner/2),"□"*int((10-manner)/2)))
print(formatSentence.format("trainer","■"*int(trainer/6),"□"*int((30-trainer)/6)))
if arbitrate>0:
    print(formatSentence.format("중재","■"*5,""))
else:
    print(formatSentence.format("중재","","□"*5))
if refund>0:
    print(formatSentence.format("환불","■"*5,""))
else:
    print(formatSentence.format("환불","","□"*5))
print(formatSentence.format("시설","■"*int(facility),"□"*int(3-facility)+"\t"))
print("----------------------------------------------------------------")


