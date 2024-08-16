package main

import (
	"HYU-Physics-and-Experiments-Calculator/Experiment/gravity"

	"fyne.io/fyne/v2"
)

type ExperimentInfo struct {
	Index int
	Name  string
	Run   func(fyne.Window) fyne.CanvasObject
}

var Experiments = []ExperimentInfo{
	{1, "중력가속도🍎", gravity.Run},
	{2, "포사체 운동🏹", nil},
	{3, "마찰계수🪨", nil},
	{4, "운동량 및 에너지 보존🏃", nil},
	{5, "원 운동과 구심력🟢", nil},

	{6, "빛의 전파와 역제곱 법칙🔦", nil},
	{7, "관성 모멘트🎠", nil},
	{8, "물리 진자🪀", nil},
	{9, "관의 공명🪈", nil},
	{10, "등전위선과 전기장⚡", nil},

	{11, "휘트스톤 브리지🌉", nil},
	{12, "측전기의 충방전🪫", nil},
	{13, "음극선의 편향➖", nil},
	{14, "상호유도에 의한 유도기전력🧲", nil},
	{15, "전류 주위의 자기장🧭", nil},

	{16, "빛의 반사와 굴절🪞", nil},
	{17, "빛의 회절과 간섭🌌", nil},
	{18, "회절격차🔬", nil},
}
