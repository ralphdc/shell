1. python读取文件，带编码：
with open(self.config_file, mode='r', encoding='UTF-8') as f:


2. shell - sed - 高级用法：


sed行首删除一个字符
# enable snd-soc-wmt-fm34
sed -i '/snd-soc-wmt-fm34/s/^#//' fs_patch/load_drivers.sh

# disable snd-soc-wmt-fm34 back
sed -i '/snd-soc-wmt-fm34/s/^/#&/' fs_patch/load_drivers.sh

2.1). 
s/^#//表示将字符串开头的#字符替换为空(即去除行首的#字符)

2.2)
/snd-soc-wmt-fm34/表示匹配含有snd-soc-wmt-fm34字符串的行

2.3)
除了使用/regexp/的方式匹配特定行，sed还支持直接指定行号的方式进行操作，则上面的脚本也可以使用采用下面的方式完成：
sed -i '49s/^#//' fs_patch/load_drivers.sh


sed行首添加一个字符
sed -i '/snd-soc-wmt-fm34/s/^/#&/' fs_patch/load_drivers.sh
注意，这里和上面的删除操作唯一的不同就在于s/^/#&/部分。其中，^字符匹配行首，#字符是一般字符表示添加该字符，&字符是我们这里需要重点关心的。在上面的关于s/regexp/replacement/命令描述时有以下字段：

The replacement may contain the special character & to refer to that portion of  the  pattern space  which  matched,  and  the  special escapes \1 through \9 to refer to the corresponding matching sub-expressions in the regexp.

这里提到了两种特殊字符：

&：refer to that portion of  the  pattern space  which  matched，即表示前面的正则表达式匹配出来的部分，而在这里指的就是行首位置。实际上，在此处我们完全可以不要&字符，也是可以完成任务的。

\1...\9：refer to the corresponding matching sub-expressions in the regexp，主要用于多匹配时(如匹配行中的特定位置)分别表示前面的正则表达式匹配出来的部分，这里的多匹配需要使用()来进行分割，如上面的代码可以分别使用下面两种方式进行实现：

sed -i '/snd-soc-wmt-fm34/s/\(^\)/\1#/' fs_patch/load_drivers.sh
sed -i '/snd-soc-wmt-fm34/s/\(^\)\(.*\)/#\2/' fs_patch/load_drivers.sh

原文：https://blog.csdn.net/nfer_zhuang/article/details/44020599 
