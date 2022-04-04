import math
try:
	import matplotlib.pyplot as plt
except:
	print("matplotlib 을 실행하는데 문제가 생겼습니다.")
	have_matplotlib = False
else:
	have_matplotlib = True

#----직접 적을 부분------

#m_pendulum : 탄동진자의 질량(kg)
#m_projectile : 포사체의 질량(kg)
#l_pendulum : 탄동진자의 길이(m)
m_pendulum = 10
m_projectile = 10
l_pendulum = 10

#degree_list : 탄동진자의 최대 각도 리스트(도)
#measure_v_initial_list : 측정한 v 초기속도 리스트
degree_list = []
measure_v_list = []

#------------------------

class Chapter_4:
	"""중력가속도를 비교해줍니다.
	사용방법: class Chapter_4(m_pendulum, m_projectile, l_pendulum, degree_list, measure_v_initial_list, have_matplotlib=True)
	m_pendulum : 탄동진자의 질량(kg)
	m_projectile : 포사체의 질량(kg)
	l_pendulum : 탄동진자의 길이(m)
	degree_list : 탄동진자의 최대 각도 리스트(도)
	measure_v_list : 측정한 v 초기속도 리스트
	is_radian : 입력한 값이 라디안인지 확인합니다.(기본값: False)
	have_matplotlib : matplotlib 라이브러리가 있는지 확인합니다.(기본값: True)"""
	def __init__(self, m_pendulum, m_projectile, l_pendulum, degree_list, measure_v_list, is_radian=False, have_matplotlib=True):
		self.g = 9.80665 #중력가속도(m/s^2) 입니다. 변수를 변경할수 있습니다.

		self.m_pendulum = m_pendulum
		self.m_projectile = m_projectile
		self.l_pendulum = l_pendulum
		self.measure_v_list = measure_v_list
		
		if self.is_radian:
			self.theta_list = degree_list
		else:
			self.theta_list = [theta*math.pi/180 for theta in theta_list]

		self.have_matplotlib = have_matplotlib
		self.is_same_size = len(self.degree_list) == len(self.measure_v_list)
		if not self.is_same_size:
			print("주의 : 주어진 시간에 대한 속력의 기울기와 구간별 가속도의 개수가 다릅니다.") 

		self.solve()

	def l_PendulumFormula(self, m_pendulum, l_pendulum, theta_list):
		self.h_pendulum_list = [l_pendulum*(1-math.cos(theta)) for theta in theta_list]

	def theory_vFormula(self, m_pendulum, m_projectile, h_pendulum_list):
		self.theory_v_list = [(m_projectile+m_pendulum/m_projectile)*math.sqrt(2*h_pendulum*self.g) for h_pendulum in h_pendulum_list]

	def solve(self):
		l_PendulumFormula(self.m_pendulum, self.l_pendulum, self.theta_list)
		theory_vFormula(self.m_pendulum, self.m_projectile, self.h_pendulum_list)


	def printResult(self, decimal=5, show_color=True):
		"""결과를 보여줍니다
		decimal : 소수점자리를 어디까지 출력해주는지 정합니다(기본값: 5).
		show color : 선을 색깔로 보여줄지 흑백으로 보여줄지 정합니다(기본값: True)."""
			print("-"*5+"개별 v 초기속도 구한 결과"+"-"*5)
		print('case\tθ\th\ttheory_v\tmeasure_v\terror')
		for case in zip([i+1 for i in range(len(self.theta_list))], self.theta_list, self.h_pendulum_list, self.theory_v_list, self.measure_v_list):
			print('{1}\t{2:.{0}f}\t{3:.{0}f}\t{4:.{0}f}\t{5:.{0}f}\t{6:.{0}f}'.format(decimal, case[0], case[1], case[2], case[3], case[4], ((case[3]+case[4])/case[3])*100))

		#matplotlib를 가지고 있을 겨웅 그래프를 출력해줍니다.
		if self.have_matplotlib:
			pass  # 아직 안만듬
		else:
			print('그래프를 실행 할 수 없습니다.')


#----작성할 부분---------

my_case = Chapter_4(v_inclination_list, mean_a_list, have_matplotlib=have_matplotlib)
my_case.printResult(show_color=False)

print("-"*30)
_=input("엔터를 눌러 종료..")