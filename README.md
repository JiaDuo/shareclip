实现两台PC直接共享剪贴板

依赖：
sudo apt-get install xsel

config.ini中填入要共享主机的IP地址，端口默认使用9999
1.在两台机器上分别填入对方的IP地址
2.python main.py

使用python2.7测试通过，如果运行出现剪贴板pyperclip错误，请查询
https://pyperclip.readthedocs.io/en/latest/introduction.html#not-implemented-error
