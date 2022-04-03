import math
try:
	import matplotlib.pyplot as plt
except:
	print("matplotlib 을 실행하는데 문제가 생겼습니다.")
	have_matplotlib = False
else:
	have_matplotlib = True

#----직접 적을 부분------

#v_i: 처음속도, v_f: 나중속도 (단위는 m/s)
v_i_list = [1.1,1.1,1.06,1.01,1.01]
v_f_list = [2.2,1.99,1.97,2.17,1.85]
#S: 포토게이트 사이의 거리(단위: m)
S = 0.5
#degree: 각도 (~도)
degree = 30

#------------------------

class Chapter_3:
	"""마찰계수를 구해줍니다.
	사용방법: class Chapter_3(v_i_list, v_f_list, S, degree, radian = False, have_matplotlib=True)
	v_i_list : v_i의 값들의 리스트
	v_f_list : v_f의 값들의 리스트
	S : 포토게이트 사이의 거리
	theta : 각도
	is_radian : 넣은 theta 값이 라디안인지 확인합니다.(기본값: False)
	have_matplotlib : matplotlib 라이브러리가 있는지 확인합니다.(기본값: True)"""
	def __init__(self, v_i_list, v_f_list, S, theta, is_radian = False, have_matplotlib=True):
		self.g = 9.80665 #중력가속도(m/s^2) 입니다. 변수를 변경할수 있습니다.
		self.v_i_list = v_i_list
		self.v_f_list = v_f_list
		self.S = S
		if is_radian:
			self.theta = theta
		else:
			self.theta = theta * math.pi / 180 
		self.kinetic_friction = None
		self.static_friction = None
		self.have_matplotlib = have_matplotlib
		
		#checking
		if len(self.v_i_list) != len(self.v_f_list):
			print("caution : v_i_list와 v_f_list의 길이가 다릅니다. 도중에 에러를 일으 킬 수 있습니다.")

	def kf_formula(self, v_i, v_f):
		"""운동마찰계수를 구하는 공식입니다."""
		return math.tan(self.theta) - (v_f**2 - v_i**2)/(2*self.g*self.S*math.cos(self.theta))

	def meanKf(self):
		"""속도를 평균을 낸 다음에 운동마찰계수를 반환합니다."""
		g_mean_v_i = sum(self.v_i_list) / len(self.v_i_list)
		g_mean_v_f = sum(self.v_f_list) / len(self.v_f_list)

		return self.kf_formula(g_mean_v_i,g_mean_v_f)

	def individualKf(self):
		"""개별 실험 케이스마다 속도에 따른 운동마찰계수를 구합니다."""
		return [self.kf_formula(v_i, v_f) for v_i, v_f in zip(self.v_i_list, self.v_f_list)]

	def printResult(self, decimal=5, show_color=True):
		"""결과를 보여줍니다
		decimal : 소수점자리를 어디까지 출력해주는지 정합니다(기본값: 5).
		show color : 선을 색깔로 보여줄지 흑백으로 보여줄지 정합니다(기본값: True)."""
		print("-"*5+"개별 운동마찰계수 구한 결과"+"-"*5)

		temp_result = self.individualKf()
		print("case\tv_i\tv_f\tkinetic_friction")
		for i in range(len(self.v_i_list)):
			print(str(i+1) + "\t{0:.{1}f}".format(self.v_i_list[i], decimal) + "\t{0:.{1}f}".format(self.v_f_list[i], decimal) + "\t{0:.{1}f}".format(temp_result[i], decimal))
		print("-"*5+"속도 평균 구하고 나온 운동마찰계수"+"-"*5)
		temp_mean = self.meanKf()
		print("{0:.{1}f}".format(temp_mean, decimal))

		#matplotlib를 가지고 있을 겨웅 그래프를 출력해줍니다.
		if self.have_matplotlib:
			max_value = max(temp_result)
			min_value = min(temp_result)

			plt.xlabel('case')
			plt.ylabel('value')
			plt.axis([0,len(temp_result)+1, 0, max(1,max_value+0.2)])
			if show_color:
				plt.plot([i+1 for i in range(len(temp_result))], [temp_mean for i in range(len(temp_result))], color='g')
				plt.plot([i+1 for i in range(len(temp_result))], temp_result, color='b')
			else:
				plt.plot([i+1 for i in range(len(temp_result))], [temp_mean for i in range(len(temp_result))], color='b', linestyle=':')
				plt.plot([i+1 for i in range(len(temp_result))], temp_result, color='b', linestyle='-')

			plt.legend(['mean μk','μk'])
			plt.show()
		else:
			print('그래프를 실행 할 수 없습니다.')

#----작성할 부분---------

my_case = Chapter_3(v_i_list,v_f_list,S,degree)
my_case.printResult(show_color=False)

print("-"*30)
_=input("엔터를 눌러 종료..")