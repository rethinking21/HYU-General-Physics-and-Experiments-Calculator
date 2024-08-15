package main

import (
	"fmt"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/widget"
)

type AppInfo struct {
	app fyne.App
}

var MainApp AppInfo

func main() {
	MainApp.app = app.New()
	OpenMainWindow()
	MainApp.app.Run()
}

func OpenMainWindow() {
	w := MainApp.app.NewWindow("실사구시 도우미")
	w.SetContent(container.NewVBox(
		widget.NewLabel("실험 목록을 선택하세요🧪"),
		CreateExperimentButtonBox(3, w),
	))
	w.Resize(fyne.NewSize(500, 200))
	w.SetFixedSize(true)
	w.Show()
}

func CreateExperimentButtonBox(column int, window fyne.Window) fyne.CanvasObject {
	var Buttons []fyne.CanvasObject = []fyne.CanvasObject{}
	for _, info := range Experiments {
		Buttons = append(Buttons, widget.NewButton(
			fmt.Sprintf("%d. %s", info.Index, info.Name),
			func() {

			},
		))
	}
	return container.NewGridWithColumns(column, Buttons...)
}
