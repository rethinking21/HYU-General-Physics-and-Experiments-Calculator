import math


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
	사용방법: class Chapter_3(v_i_list, v_f_list, S, degree, radian = False)
	v_i_list : v_i의 값들의 리스트
	v_f_list : v_f의 값들의 리스트
	S : 포토게이트 사이의 거리
	theta : 각도
	is_radian : 넣은 theta 값이 라디안인지 확인(기본값: False)"""
	def __init__(self,v_i_list,v_f_list,S,theta,is_radian = False):
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

		#checking
		if len(self.v_i_list) != len(self.v_f_list):
			print("caution : v_i_list와 v_f_list의 길이가 다릅니다. 도중에 에러를 일으 킬 수 있습니다.")

	def kf_formula(self,v_i,v_f):
		"""운동마찰계수를 구하는 공식입니다."""
		return math.tan(self.theta) - (v_f**2 - v_i**2)/(2*self.g*self.S*math.cos(self.theta))

	def meanKf(self):
		"""속도를 평균을 낸 다음에 운동마찰계수를 반환합니다."""
		g_mean_v_i = sum(self.v_i_list)/len(self.v_i_list)
		g_mean_v_f = sum(self.v_f_list)/len(self.v_f_list)

		return self.kf_formula(g_mean_v_i,g_mean_v_f)

	def individualKf(self):
		"""개별 실험 케이스마다 속도에 따른 운동마찰계수를 구합니다."""
		return [self.kf_formula(v_i,v_f) for v_i,v_f in zip(self.v_i_list,self.v_f_list)]

	def printResult(self,print_v_mean=True,print_individual_kf=True,decimal=5):
		print("-"*5+"개별 운동마찰계수 구한 결과"+"-"*5)

		temp_result = self.individualKf()
		print("case\tv_i\tv_f\tkinetic_friction")
		for i in range(len(self.v_i_list)):
			print(str(i+1)+"\t{0}".format(self.v_i_list[i])+"\t{0}".format(self.v_f_list[i])+"\t{0:.{1}f}".format(temp_result[i],decimal))
		print("-"*5+"속도 평균 구하고 나온 운동마찰계수"+"-"*5)
		print("{0:.{1}f}".format(self.meanKf(),decimal))

#----작성할 부분---------

my_case = Chapter_3(v_i_list,v_f_list,S,degree)
my_case.printResult()

print("-"*30)
_=input("엔터를 눌러 종료..")