"""
虚拟环境的创建是通过执行venv命令完成的:
python3 -m venv /path/to/new/virtual/environment

运行这个命令可以创建目标目录 (创建任何不存在的父目录)，
并在其中放置一个 pyvenv.cfg 文件，
其主键指向运行该命令的 Python 安装（目标目录的常用名称是 .venv）。
它还会创建一个 bin (或 Windows 上的 Scripts) 子目录，
其中包含 Python 二进制文件/binaries 的拷贝/symlink (适合于环境创建时使用的平台或参数)。
它还会创建一个 (最初是空的) lib/pythonX.Y/site-packages 子目录 (在 Windows 上，这是 Lib\site-packages)。
如果指定了一个现有的目录，
它将被重新使用。

在Windows上，调用venv命令，如下所示:
c:\>c:\Python35\python -m venv c:\path\to\myenv

或者，如果你为你的Python安装配置了PATH和PATHEXT变量:
c:\>python -m venv c:\path\to\myenv

该命令如果与-h一起运行，将显示可用的选项：

usage: venv [-h] [--system-site-packages] [--symlinks | --copies] [--clear]
            [--upgrade] [--without-pip] [--prompt PROMPT] [--upgrade-deps]
            ENV_DIR [ENV_DIR ...]

在一个或多个目标目录中创建虚拟Python环境。

位置参数:
  ENV_DIR               用于创建环境的目录。

可选参数:
  -h, --help            显示此帮助信息并退出
  --system-site-packages
                        给予虚拟环境对系统站点-软件包目录的访问权。
  --symlinks            尽量使用符号链接，而不是复制，当符号链接 不是该平台的默认值。
  --copies              尽量使用拷贝而不是符号链接，即使在符号链接是该平台的默认值。
  --clear               在创建环境之前，如果环境目录已经存在，则删除该目录的内容。
  --upgrade             升级环境目录以使用这个版本的python，假设Python已经被就地升级了。
  --without-pip         跳过在虚拟环境中安装或升级pip（默认情况下，pip已被启动）。
  --prompt PROMPT       为这个环境提供一个替代的提示前缀。
  --upgrade-deps        升级核心依赖：Pip setuptools到PyPI中的最新版本。
一旦一个环境被创建，你可能希望激活它，例如通过在它的bin目录中寻找一个激活脚本。




"""