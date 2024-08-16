package main

import (
	"fmt"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/widget"
)

type AppInfo struct {
	app     fyne.App
	window  fyne.Window
	content *fyne.Container
}

var (
	mainApp AppInfo
	buttons []fyne.CanvasObject = []fyne.CanvasObject{}
	Canvas  *fyne.Container
)

func main() {
	mainApp.app = app.New()
	mainApp.window = mainApp.app.NewWindow("실사구시 도우미")
	Canvas = container.NewStack()
	buttonInit()
	OpenMainWindow()

	mainApp.window.Resize(fyne.NewSize(700, 500))
	mainApp.window.SetFixedSize(true)
	mainApp.window.ShowAndRun()
}

func buttonInit() {
	for _, info := range Experiments {
		buttons = append(buttons, widget.NewButton(
			fmt.Sprintf("%d. %s", info.Index, info.Name),
			func() {
				Canvas.Objects = nil
				if info.Run != nil {
					Canvas.Objects = []fyne.CanvasObject{info.Run(mainApp.window)}
				} else {
					Canvas.Objects = []fyne.CanvasObject{widget.NewLabel("🚧 Work in Progress... 🚧")}
				}
			},
		))
	}
}

func OpenMainWindow() {
	mainApp.content = container.NewBorder(
		widget.NewLabel("실험 목록을 선택하세요🧪"),
		nil,
		container.NewVScroll(container.NewGridWithColumns(1, buttons...)),
		nil,
		Canvas,
	)
	mainApp.window.SetContent(mainApp.content)
}
