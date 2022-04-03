import math
try:
	import matplotlib.pyplot as plt
except:
	print("matplotlib 을 실행하는데 문제가 생겼습니다.")
	have_matplotlib = False
else:
	have_matplotlib = True

#----직접 적을 부분------

#v_inclination_list : 시간에 대한 속력의 기울기
v_inclination_list = [9.7,8.9,10,9,9.3,8]
#mean_a_list : 구간별 가속도의 평균
mean_a_list = [9.3,9.2,10,8,9.3,9.9]

#------------------------

class Chapter_1:
	"""중력가속도를 비교해줍니다.
	사용방법: class Chapter_1(v_inclination_list, mean_a_list, have_matplotlib=True)
	v_inclination_list : 시간에 대한 속력의 기울기 리스트
	mean_a_list : 구간별 가속도의 평균
	have_matplotlib : matplotlib 라이브러리가 있는지 확인합니다.(기본값: True)"""
	def __init__(self, v_inclination_list, mean_a_list, have_matplotlib=True):
		self.g = 9.80665 #중력가속도(m/s^2) 입니다. 변수를 변경할수 있습니다.
		self.v_inclination_list = v_inclination_list
		self.mean_a_list = mean_a_list
		self.have_matplotlib = have_matplotlib

		self.is_same_size = len(self.mean_a_list) == len(self.v_inclination_list)
		if not self.is_same_size:
			print("주의 : 주어진 시간에 대한 속력의 기울기와 구간별 가속도의 개수가 다릅니다.") 


	def printResult(self, decimal=5, show_color=True):
		"""결과를 보여줍니다
		decimal : 소수점자리를 어디까지 출력해주는지 정합니다(기본값: 5).
		show color : 선을 색깔로 보여줄지 흑백으로 보여줄지 정합니다(기본값: True)."""
		print('v 기울기 평균 :', "{0:.{1}f}".format(sum(self.v_inclination_list)/len(self.v_inclination_list), decimal))
		print('a 평균 :', "{0:.{1}f}".format(sum(self.mean_a_list)/len(self.mean_a_list), decimal))

		#matplotlib를 가지고 있을 겨웅 그래프를 출력해줍니다.
		if self.have_matplotlib:
			max_value = max(self.mean_a_list + self.v_inclination_list)
			min_value = min(self.mean_a_list + self.v_inclination_list)
			plt.xlabel('case')
			plt.ylabel('value')
			plt.axis([0,len(self.v_inclination_list)+1, 0, max(10,max_value+1)])

			if show_color:
				plt.plot([i+1 for i in range(len(self.v_inclination_list))], self.v_inclination_list, color='r')
				plt.plot([i+1 for i in range(len(self.mean_a_list))], self.mean_a_list, color='g')
				plt.plot([i+1 for i in range(len(self.mean_a_list))], [self.g for i in range(len(self.mean_a_list))], color='b')
			else:
				plt.plot([i+1 for i in range(len(self.v_inclination_list))], self.v_inclination_list, linestyle='-', color='b')
				plt.plot([i+1 for i in range(len(self.mean_a_list))], self.mean_a_list, linestyle='--', color='b')
				plt.plot([i+1 for i in range(len(self.mean_a_list))], [self.g for i in range(len(self.mean_a_list))], linestyle=':', color='b')
			
			plt.legend(['v_inclination','mean_a', 'g'])
			plt.show()
		else:
			print('그래프를 실행 할 수 없습니다.')


#----작성할 부분---------

my_case = Chapter_1(v_inclination_list, mean_a_list, have_matplotlib=have_matplotlib)
my_case.printResult(show_color=False)

print("-"*30)
_=input("엔터를 눌러 종료..")