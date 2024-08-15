OUT = physic

ifeq ($(OS),Windows_NT)
    # Windows에서의 삭제 명령어
    DEL_CMD = del /f $(OUT).exe
else
    # Unix 계열 시스템 (macOS, Linux)에서의 삭제 명령어
    DEL_CMD = rm -f $(OUT).exe
endif

build:
	go build -ldflags="-H=windowsgui" -o $(OUT).exe
	
debug:
	go build -o $(OUT).exe

run:
	go run -ldflags="-H=windowsgui" main.go

clean:
	$(DEL_CMD)