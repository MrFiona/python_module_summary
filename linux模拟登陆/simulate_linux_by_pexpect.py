#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2018-04-25 21:52
# Author  : MrFiona
# File    : simulate_linux_by_pexpect.py
# Software: PyCharm


import pexpect

# user: ssh 主机的用户名
# host：ssh 主机的域名
# password：ssh 主机的密码
# command：即将在远端 ssh 主机上运行的命令
def ssh_command(user, host, password, command):
    """
    This runs a command on the remote host. This could also be done with the
    pxssh class, but this demonstrates what that class does at a simpler level.
    This returns a pexpect.spawn object. This handles the case when you try to
    connect to a new host and ssh asks you if you want to accept the public key
    fingerprint and continue connecting.
    """
    ssh_newkey = 'Are you sure you want to continue connecting'
    # 为 ssh 命令生成一个 spawn 类的子程序对象.
    child = pexpect.spawn('ssh -l %s %s %s' % (user, host, command))
    i = child.expect([pexpect.TIMEOUT, ssh_newkey, 'password: '])
    # 如果登录超时，打印出错信息，并退出.
    if i == 0:  # Timeout
        print('ERROR!')
        print('SSH could not login. Here is what SSH said:')
        print(child.before, child.after)
        return None
    # 如果 ssh 没有 public key，接受它.
    if i == 1:  # SSH does not have the public key. Just accept it.
        child.sendline('yes')
        child.expect('password: ')
        i = child.expect([pexpect.TIMEOUT, 'password: '])
        if i == 0:  # Timeout
            print('ERROR!')
            print('SSH could not login. Here is what SSH said:')
            print(child.before, child.after)
            return None
    # 输入密码.
    child.sendline(password)
    return child


def main():
    # 获得用户指定 ssh 主机域名.
    # host = input('Hostname: ')
    host = "192.168.222.129"
    # 获得用户指定 ssh 主机用户名.
    # user = input('User: ')
    user = "root"
    # 获得用户指定 ssh 主机密码.
    # password = input('Password: ')
    password = "qq08061635"
    # password = getpass.getpass()
    # 获得用户指定 ssh 主机上即将运行的命令.
    # command = input('Enter the command: ')
    command = "ls -trl"
    child = ssh_command(user, host, password, command)
    # 匹配 pexpect.EOF
    child.expect(pexpect.EOF)
    # 输出命令结果.
    print(child.before)


if __name__ == '__main__':
    # try:
    main()
    # except Exception as e:
    #     print(e)