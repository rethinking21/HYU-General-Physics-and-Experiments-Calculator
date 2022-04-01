import math

#----직접 적을 부분------

#degree: 각도 (~도)
degree = 30
y_zero = 0.255
#초기 속도(리스트)
v_zero_list = [2.44,2.84,2.59]
#실제 도달거리(리스트)
real_R_list = [0.631,0.852,0.801]

#------------------------

class Chapter_2:
	def __init__(self,theta,y_zero,v_zero_list,real_R_list,is_radian=False):
		self.g = 9.80665 #중력가속도(m/s^2) 입니다. 변수를 변경할수 있습니다.
		self.v_zero_list = v_zero_list
		self.real_R_list = real_R_list
		self.theta = theta
		self.y_zero = y_zero

		if is_radian:
			self.theta = theta
		else:
			self.theta = theta * math.pi / 180 
		self.is_same_size = len(self.real_R_list) == len(self.v_zero_list)
		if not self.is_same_size:
			print("주의 : 주어진 초기 속도와 실제 도달거리 개수가 다릅니다.") 

	def additional_rFormula(self,v_zero):
		"""추가 도달거리를 구하는 공식"""

		#같은 함수를 두번 반복하지만..
		return v_zero*math.cos(self.theta)*self.delta_tFormula(v_zero)
		
	def delta_tFormula(self,v_zero):
		"""추가 진행시간을 구하는 공식"""
		return math.sqrt((v_zero*math.sin(self.theta)/self.g)**2+(2*self.y_zero/self.g)) - (v_zero*math.sin(self.theta)/self.g)

	def theory_RFormula(self,v_zero):
		return (v_zero**2 * math.sin(2*self.theta))/(self.g)

	def printResult(self,print_v_mean=True,print_individual=True,decimal=5):
		if print_individual and self.is_same_size:
			print("-"*5+"개별 수평도달거리 구한 결과"+"-"*5)
			delta_t_list = [self.delta_tFormula(v_zero) for v_zero in self.v_zero_list]
			additional_r_list = [self.additional_rFormula(v_zero) for v_zero in self.v_zero_list]
			measure_R_list = [real_R-additional_r for real_R,additional_r in zip(self.real_R_list,additional_r_list)]
			theory_R_list = [self.theory_RFormula(v_zero) for v_zero in self.v_zero_list]
			
			#오차율 계산이 확실치 않음
			error_list = [((theory_R-real_R)/theory_R)*100 for theory_R,real_R in zip(theory_R_list,self.real_R_list)]

			print("case\tΔt\tr\tR'\tR(measure)\tR(theory)\terror(%)")
			for i in range(len(self.real_R_list)):
				print(str(i+1) + "\t{0:.{1}f}".format(delta_t_list[i],decimal) + "\t{0:.{1}f}".format(additional_r_list[i],decimal) \
				+ "\t{0:.{1}f}".format(self.real_R_list[i],decimal) + "\t{0:.{1}f}".format(measure_R_list[i],decimal) \
				+ "\t{0:.{1}f}".format(theory_R_list[i],decimal) + "\t{0:.{1}f}".format(error_list[i],decimal))
		elif print_individual and not self.is_same_size:
			print("초기 속도와 실제 도달거리의 데이터 개수가 다릅니다.")

		if print_v_mean:
			print("-"*5+"평균으로 수평도달거리 구한 결과"+"-"*5)
			mean_v_zero = sum(self.v_zero_list) / len(self.v_zero_list)
			mean_real_R = sum(self.real_R_list) / len(self.real_R_list)

			mean_delta_t = self.delta_tFormula(mean_v_zero)
			mean_additional_r = self.additional_rFormula(mean_v_zero)
			mean_measure_R = mean_real_R - mean_additional_r
			mean_theory_R = self.theory_RFormula(mean_v_zero)

			#오차율 계산이 확실치 않음
			mean_error = ((mean_theory_R-mean_real_R)/mean_theory_R)*100

			print("mean v"+"\t{0:.{1}f}".format(mean_v_zero,decimal))
			print("Δt"+"\t{0:.{1}f}".format(mean_delta_t,decimal))
			print("R'"+"\t{0:.{1}f}".format(mean_real_R,decimal))
			print("R(measure)"+"\t{0:.{1}f}".format(mean_measure_R,decimal))
			print("R(theory)"+"\t{0:.{1}f}".format(mean_theory_R,decimal))
			print("error(%)"+"\t{0:.{1}f}".format(mean_error,decimal))


#----작성할 부분---------

my_case = Chapter_2(degree,y_zero,v_zero_list,real_R_list)
my_case.printResult()

print("-"*30)
_=input("엔터를 눌러 종료..")