package gravity

import (
	"strconv"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/widget"
)

var (
	data [][]string = [][]string{
		{"#", "시간에 대한 속력의 기울기", "구간별 가속도의 평균"},
	}
)

func Run(w fyne.Window) fyne.CanvasObject {
	table := widget.NewTable(
		func() (int, int) {
			if len(data) == 0 {
				return 0, 0
			}
			return len(data), len(data[0])
		},
		func() fyne.CanvasObject {
			entry := widget.NewEntry()
			return entry
		},
		func(tci widget.TableCellID, co fyne.CanvasObject) {
			entry := co.(*widget.Entry)
			// 읽기 전용 셀 처리
			if tci.Row == 0 || tci.Col == 0 {
				entry.SetText(data[tci.Row][tci.Col])
				entry.Disable()
			} else {
				entry.SetText(data[tci.Row][tci.Col])
				entry.OnChanged = func(text string) {
					_, err := strconv.ParseFloat(text, 64)
					if err != nil && text != "" {
						entry.Text = data[tci.Row][tci.Col]
					} else {
						data[tci.Row][tci.Col] = text
					}
				}
			}
		},
	)
	table.SetColumnWidth(0, 40)
	table.SetColumnWidth(1, 200)
	table.SetColumnWidth(2, 200)

	addButton := widget.NewButton(
		"데이터 추가",
		func() {
			data = append(data, []string{strconv.Itoa(len(data)), "", ""})
		},
	)

	deleteButton := widget.NewButton(
		"데이터 삭제",
		func() {
			if len(data) > 1 {
				data = data[:len(data)-1]
			}
		},
	)

	// TODO : 연속적으로 버튼을 누르면 오류가 남

	return container.NewBorder(
		widget.NewLabel("중력가속도 실험"),
		container.NewHBox(
			addButton,
			deleteButton,
		),
		nil,
		nil,
		container.NewPadded(table),
	)
}
