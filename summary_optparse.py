# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-08-25 14:33
# Author  : MrFiona
# File    : _optparse.py
# Software: PyCharm Community Edition



"""
    模块optparse使用类OptionParser来作为命令行选项的解析器;下面是该类的方法:
    1、OptionParser(self, prog=None, usage=None, description=None, epilog=None, option_list=None,
        option_class=<class optparse.Option>, version=None, conflict_handler='error', formatter=None, add_help_option=True)

    构造函数__init__(),用于创建一个命令行选项解析器实例;其中,参数:
    description:
        usage : 描述当前脚本程序的用法字符串;显示该用法之前,格式"%prog"将被格式化成当前脚本程序的名称
        prog : 默认为当前脚本程序的名称 os.path.basename(sys.argv[0])
        description : 当前脚本程序的简单描述、摘要、大纲;它会被显示在命令行选项的帮助之前
        epilog : 当前脚本程序的简单描述、摘要、大纲;它会被它会被显示在命令行选项的帮助之后
        conflict_handler : 命令行选项冲突处理器;比如,当命令行选项重复时,该如何让处理;可选值:error、resolve
        add_help_option : 是否自动生成帮助信息;True:是; False:否; 默认值是True
        option_list : 当前脚本程序的命令行选项列表;这个选项列表在standard_options_list中选项添加之后,
                        但是在版本和帮助选项添加之前;可以手工创建该列表,该列表中的元素都使用函数make_option()生成
                        例如 : option_list=[make_option("-f","--file",action="store",type="string",dest="filename"), ...]
        option_class : 在使用函数add_option()添加命令行选项到解析器时使用的类;默认为optparse.Option类
        version : 打印版本的信息
        formatter : 帮助信息格式;有两种格式:IndentedHelpFormatter和TitledHelpFormatter;
                    其中,参数prog在usage和version中使用格式字符串"%prog"代替os.path.basename(sys.argv[0])


    2、OptionParser.add_option(self, *args, **kwargs)

    该函数用于添加命令行选项;参数*args用于传递一个命令行选项的列表;**kwargs用于传递该命令行选项的属性;有几种用法:
        1、parser.add_option(self, optparse.Option):直接添加一个命令行选项类的实例
        2、parser.add_option(self, option_list):直接添加一个命令行选项列表;option_list=[make_option(), ...]
        3、parser.add_option(*opt_str, ..., kwarg=val, ...)

    常用的是第三种;这种用法的函数原型如下:
    optparse.OptionParser.add_option(short_option[, long_option], action="store", type="store", dest=None, nargs=1,
                default=None, help="help text", metavar="");其中,参数如下:

    description:
        short_option : 短选项字符串;例如,"-f"、"-X"
        long_option : 长选项字符串;例如,"--file"、"--start";长选项和短选项共同构成可选参数*args或*opt_str
        action : 行为字符串;它指示optparse当解析到一个命令行选项时该如何处理;可选值store、store_true、store_false、store_const、
                    append、append_const、count、callback、help、version;默认值是store,表示把命令行参数保存到options对象中
        type : 当action的值为存储方式时,type表示存储的数据的类型;有string、int、long、float、complex、choice
        dest : 当action的值为存储方式时,dest表示用于存储数据(当前命令行选项附加的参数值)的变量,它会成为函数parse_args()返回的options对象的属性,
                通过"对象名.属性名"的方式引用;如果不指定dest参数的值,则使用当前命令行选项的长选项名作为dest参数的缺省值和options对象的属性,
                来存储当前命令行选项的附加参数值;如果当前命令行选项没有指定长选项,则使用短选项名作为dest参数的缺省值和options对象的属性,
                来存储当前命令行选项的附加参数值
        nargs : 指定当前命令行选项应该需要接受的附加参数值的个数;默认值为1;多个参数值之间用空格隔开;当在命令行为该选项输入的附加参数值的个数多于
                nargs指定的个数时,则值取用前面的nargs个;当在命令行上为该选项输入的附加参数值的个数少于nargs所指定的个数时,则会报错;
                如果nargs>1,则python解释器会把这nargs个参数值组装成一个元组(tuple),然后把这个元组传递给当前程序使用
        default : 当action的值为存储方式时,default用于指定dest表示的属性变量的缺省值,即,当前命令行选项附加的参数的缺省值
        help : 当前命令行选项的帮助、说明信息
        metavar:占位字符串;用于在输出帮助信息时,代替当前命令行选项的附加参数的值进行输出;例如:"-f FILE --file FILE";这个例子中,字符串"FILE"就是metavar的值
                例如  :   add_option("-f", "--file", action="store", type="string", dest="fileName", default="file.txt", help="save host info", metavar="FILE");
            当调用parse_args()函数之后,会返回一个options对象,dest参数的值"fileName"将作为options对象的属性名使用,即:options.fileName;同时把当前命令行选项的
            附加参数值保存在该属性中,即:options.fileName="file.txt"

    3、(options,args) = optparse.OptionParser.parse_args(self, args=None, values=None)
    该函数用于解析命令行参数;其中,参数:
    description:
        args : 用于传递需要被解析的命令行选项列表;默认是sys.argv[1:]
        values : 用于传递命令行选项的附加参数值的对象;是optparse.Values类的对象;
                返回值:是一个包含(options,args)对的tuple
        args : 所有被处理的参数之后的剩余参数

    4、optparse.OptionParser.has_option(self, opt_str):
                该函数用于判断OptionParser实例是否有一个名为opt_str的命令行选项;返回值:True-有; False-无;
    5、optparse.OptionParser.get_option(self, opt_str):
                该函数用于获取命令行选项opt_str的实例;若没有该选项,则返回None;
    6、optparse.OptionParser.remove_option(self, opt_str):
                该函数用于移除命令行选项opt_str;若OptionParser对象中存在命令行选项opt_str,则移除,否则抛出ValueError异常;
                若存在多个opt_str的选项,则所有相关的选项都变成无效;
    7、optparse.OptionParser.destroy() : 该函数用于销毁OptionParser对象实例;

"""



import sys
import optparse

parser = optparse.OptionParser(usage="usage: %prog [options] arg1 arg2 .....", version="1.0",
                               description="This is optparse example code")


def doStop(option, opt_str, value, parser):  # 最小化定义,不需要接收参数;
    print("option:", option)
    print("opt_str", opt_str)
    print("value:", value)
    print("stopping the web server ......")
    print("largs:", parser.largs)
    print("rargs:", parser.rargs)


def doStart(option, opt_str, value, parser, *args, **kwargs):  # 最大化定义,需要接收参数;
    print("option:", option)
    print("opt_str", opt_str)
    print("value:", value)
    print("*args:", args)
    print("*kwargs:", kwargs)
    print("starting the web server ......")
    print("largs:", parser.largs)
    print("rargs:", parser.rargs)


parser.add_option("--start", action="callback", callback=doStart, callback_args=("192.168.0.253", 3307),
                  callback_kwargs={"user": "user", "pswd": "pwd"}, nargs=3, default=None, metavar="START")
parser.add_option("--stop", action="callback", callback=doStop, default=None, metavar="STOP")


def doStart(option, opt_str, value, parser, *args, **kwargs):
    print("option:", option)
    print("opt_str", opt_str)
    print("value:", value)
    print("*args:", args)
    print("*kwargs:", kwargs)
    print("starting the web server ......")
    print("largs:", parser.largs)
    print("rargs:", parser.rargs)


def doStop(option, opt_str, value, parser):
    print("option:", option)
    print("opt_str", opt_str)
    print("value:", value)
    print("stopping the web server ......")
    print("largs:", parser.largs)
    print("rargs:", parser.rargs)


def Main(argc, argv):
    strUsage = "Usage: %prog [option] args"
    parser = optparse.OptionParser(usage=strUsage, description="this program is used for study")
    parser.add_option("-f", "--file", action="store", type="string", dest="fileName", help="configation file",
                      metavar="FILE")
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=True)
    parser.add_option("-q", "--quit", action="store_false", dest="verbose", default=False)
    parser.add_option("-H", "--host", action="store", type="string", dest="strHost", nargs=3, default="127.0.0.1",
                      help="Remote Host IP(IP1 IP2 IP3)", metavar="IP")
    parser.add_option("-p", "--port", action="store", type="int", dest="iPort", nargs=3, default="3306",
                      help="Remote Host Port(Port1 Port2 Port3)", metavar="PORT")
    parser.add_option("-u", "--user", action="store", type="string", dest="strUserName", default="admin",
                      help="Your user name", metavar="UserName")
    parser.add_option("-P", "--password", action="store", type="string", dest="strPassword", default="admin",
                      help="Your password", metavar="Password")
    parser.add_option("-i", "--input", action="store", type="string", dest="strInput", default="input.txt",
                      help="as a file for input", metavar="FILE")
    parser.add_option("--start", action="callback", callback=doStart, callback_args=("192.168.0.253", 3307),
                      callback_kwargs={"user": "user", "pswd": "pwd"}, nargs=3, default=None, metavar="START")
    parser.add_option("--stop", action="callback", callback=doStop, default=None, metavar="STOP")

    parser.add_option("-a", action="store_const", dest="const_value", default='default_const_value',
                      const='store_const default value', help='Set a constant const value')
    parser.add_option("-c", action="store_true", dest="boolean_switch", default=True, help='Set a switch to True')
    parser.add_option("-d", action="store_false", dest="boolean_switch", default=False, help='Set a switch to False')
    parser.add_option("-e", action="append", dest="collection", default=[], help='Add repeated values to a list')
    parser.add_option("-W", action="append_const", dest="const_collection", const='value-1-to-append', default=[],
                      help='Add different values to list')
    parser.add_option("-D", action="append_const", dest="const_collection", const='value-2-to-append', default=[],
                      help='Add different values to list')

    if (argc < 1):
        parser.error("invalid argument for commond line;")
        parser.print_help()
        sys.exit(1)
    # 命令行参数解析和处理
    (options, largs) = parser.parse_args()
    if (options.fileName):
        print("read this file ......")
    if (options.strHost):
        print("connect to remote host ......")
    print("---------options-----------")
    print(options)
    print("---------largs-----------")
    print(largs)
    print("---------fileName-----------,", options.fileName)
    print("---------strHost-----------,", options.strHost)
    print("---------iPort-----------,", options.iPort, type(options.iPort))
    print("---------largs-----------,", parser.largs)
    print("---------rargs-----------,", parser.rargs)
    print("---------values-----------,", parser.values)
    print 'store_const:\t', options.const_value
    print 'boolean_switch:\t', options.boolean_switch
    print 'collection:\t', options.collection
    print 'const_collection:\t', options.const_collection
    print 'const_collection:\t', options.const_collection


if __name__ == "__main__":
    argv = sys.argv[1:]
    argc = len(argv)
    Main(argc, argv)