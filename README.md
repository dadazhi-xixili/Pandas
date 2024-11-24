# 目录


## pandas
### [pandas.ExcelFile](12-读取\3-ExcelFile.ipynb)
    - 保持工作簿打开状态
### [pandas.ExcelWriter](13-保存\2-ExcelWriter.ipynb)
    - 保持工作簿打开状态
    - 实现对象的修改而非覆盖
### [pands.read_excel](12-读取\2-read_excel.ipynb)
    - 读取xlsx、xlsb、xls文件
### [pandas.read_csv](12-读取\1-read_csv.ipynb)
    - 读取文本文件


## pandas.DataFrame
### [Pandas.DataFrame](01-构成\2-DataFrame.ipynb)
    - 构建DataFrame

## pandas.Series
### [Pandas.Series](01-构成\1-Series.ipynb)
    - 构建Series

### pandas.Series.str | pd.Index.str
    - 构造str对象
#### [pd.Series.str.capitalize | pd.Index.str.capitalize](08-str\01-大小写\01-01-capitalize.ipynb)
    - 将字符串的第一个字符转换为大写，其余字符转换为小写。

#### [pd.Series.str.title | pd.Index.str.title](08-str\01-大小写\01-02-title.ipynb)
    - 将字符串中每个单词的首字母转换为大写，其他字母转换为小写。

#### [pd.Series.str.upper | pd.Index.str.upper](08-str\01-大小写\01-03-upper.ipynb)
    - 将字符串转换为大写。

#### [pd.Series.str.lower | pd.Index.str.lower](08-str\01-大小写\01-04-lower.ipynb)
    - 将字符串转换为小写。

#### [pd.Series.str.swapcase | pd.Index.str.swapcase](08-str\01-大小写\01-05-swapcase.ipynb)
    - 将字符串中的大写字符转换为小写，小写字符转换为大写。

#### [pd.Series.str.casefold | pd.Index.str.casefold](08-str\01-大小写\01-06-casefold.ipynb)
    - 将字符串转换为小写，用于非拉丁字母。
#### [pd.Series.str.center | pd.Index.str.center](08-str\02-格式\02-01-center.ipynb)
    - 于字符左右填充`fillchar`参数字符至`width`参数的长度。

#### [pd.Series.str.ljust | pd.Index.str.ljust](08-str\02-格式\02-02-ljust.ipynb)
    - 于字符右侧填充`fillchar`参数字符至`width`参数的长度。

#### [pd.Series.str.rjust | pd.Index.str.rjust](08-str\02-格式\02-03-rjust.ipynb)
    - 于字符左侧填充`fillchar`参数字符至`width`参数的长度。

#### [pd.Series.str.pad | pd.Index.str.pad](08-str\02-格式\02-04-pad.ipynb)
    - 与`ljust`、`rjust`、`center`方法功能相同。

#### [pd.Series.str.zfill | pd.Index.str.zfill](08-str\02-格式\02-05-zfill.ipynb)
    - 在数字左侧填充0至`width`参数的长度，跳过正负符号（'+'、'-'）

#### [pd.Series.str.strip | pd.Index.str.strip](08-str\02-格式\02-06-strip.ipynb)
    - 去除字符串左右`to_strip`参数指定的字符。

#### [pd.Series.str.lstrip | pd.Index.str.lstrip](08-str\02-格式\02-07-lstrip.ipynb)
    - 去除字符串左侧`to_strip`参数指定的字符。

#### [pd.Series.str.rstrip | pd.Index.str.rstrip](08-str\02-格式\02-08-rstrip.ipynb)
    - 去除字符串右侧`to_strip`参数指定的字符。
#### [pd.Series.str.slice_replace | pd.Index.str.slice_replace](08-str\03-删改\03-01-slice_replace.ipynb)
    - 用`repl`参数替换字符串中从`start`到`stop`位置的字符。

#### [pd.Series.str.replace | pd.Index.str.replace](08-str\03-删改\03-02-replace.ipynb)
    - 替换字符串,可使用正则表达式

#### [pd.Series.str.repeat | pd.Index.str.repeat](08-str\03-删改\03-03-repeat.ipynb)
    - 重复字符串

#### [pd.Series.str.removeprefix | pd.Index.str.removeprefix](08-str\03-删改\03-04-removeprefix.ipynb)
    - 删除字符串开头的字符

#### [pd.Series.str.removesuffix | pd.Index.str.removesuffix](08-str\03-删改\03-05-removesuffix.ipynb)
    - 删除字符串结尾的字符

#### [pd.Series.str.translate | pd.Index.str.translate](08-str\03-删改\03-06-translate.ipynb)
    - 映射字符串
#### [pd.Series.str.join | pd.Index.str.join](08-str\04-合并\04-01-join.ipynb)
    - 以指定的字符连接合并系列中的字符串序列。

#### [pd.Series.str.cat | pd.Index.str.cat](08-str\04-合并\04-02-cat.ipynb)
    - 合并系列中的元素，以指定的分隔符连接起来。
#### [pd.Series.str.split | pd.Index.str.split](08-str\05-拆分\05-01-spliy.ipynb)
    - 从左侧开始拆分字符串,可使用正则表达式

#### [pd.Series.str.rsplit | pd.Index.str.rsplit](08-str\05-拆分\05-02-rspliy.ipynb)
    - 从右侧开始拆分

#### [pd.Series.str.partition | pd.Index.str.partition](08-str\05-拆分\05-03-partition.ipynb)
    - 从左侧开始拆分字符串,返回包含拆分字符列在内的3个元素
#### [pd.Series.str.startswith | pd.Index.str.startswith](08-str\06-判断\06-01-startswith.ipynb)
    - 判断左侧字符是否匹配

#### [pd.Series.str.endswith | pd.Index.str.endswith](08-str\06-判断\06-02-endswith.ipynb)
    - 判断右侧字符是否匹配

#### [pd.Series.str.contains | pd.Index.str.contains](08-str\06-判断\06-03-contains.ipynb)
    - 判断是否包含字符串,可使用正则表达式

#### [pd.Series.str.match | pd.Index.str.match](08-str\06-判断\06-04-match.ipynb)
    - 正则表达式判断左侧字符是否匹配

#### [pd.Series.str.fullmatch | pd.Index.str.fullmatch](08-str\06-判断\06-05-fullmatch.ipynb)
    - 正则表达式判断是否匹配整个字符串

#### [pd.Series.str.isalnum | pd.Index.str.isalnum](08-str\06-判断\06-06-isalnum.ipynb)
    - 判断是否都为字母和数字

#### [pd.Series.str.isalpha | pd.Index.str.isalpha](08-str\06-判断\06-07-isalpha.ipynb)
    - 判断是否都为字母

#### [pd.Series.str.isdigit | pd.Index.str.isdigit](08-str\06-判断\06-08-isdigit.ipynb)
    - 判断是否都为数字,包含特殊数字

#### [pd.Series.str.isspace | pd.Index.str.isspace](08-str\06-判断\06-09-isspace.ipynb)
    - 判断是否都为空白字符

#### [pd.Series.str.islower | pd.Index.str.islower](08-str\06-判断\06-10-islower.ipynb)
    - 判断字母是否都为小写

#### [pd.Series.str.isupper | pd.Index.str.isupper](08-str\06-判断\06-11-isupper.ipynb)
    - 判断字母是否都为大写

#### [pd.Series.str.istitle | pd.Index.str.istitle](08-str\06-判断\06-12-istitle.ipynb)
    - 以空格分组,判断组内是否都为首字母大写

#### [pd.Series.str.isnumeric | pd.Index.str.isnumeric](08-str\06-判断\06-13-isnumeric.ipynb)
    - 判断是否都为数字,包含特殊数字,字符集比`isdigit`更多

#### [pd.Series.str.isdecimal | pd.Index.str.isdecimal](08-str\06-判断\06-14-isdecimal.ipynb)
    - 判断是否都为十进制数字
#### [pd.Series.str.find | pd.Index.str.find](08-str\07-数据\07-01-find.ipynb)
    - 从左侧开始查找，返回第一个匹配项的索引。

#### [pd.Series.str.rfind | pd.Index.str.rfind](08-str\07-数据\07-02-rfind.ipynb)
    - 从右侧开始查找，返回第一个匹配项的索引。

#### [pd.Series.str.count | pd.Index.str.count](08-str\07-数据\07-03-count.ipynb)
    - 使用正则表达式匹配,返回匹配项的个数。

#### [pd.Series.str.len | pd.Index.str.len](08-str\07-数据\07-04-len.ipynb)
    - 返回对象数量

#### [pd.Series.str.index | pd.Index.str.index](08-str\07-数据\07-05-index.ipynb)
    - 从左侧开始查找，返回第一个匹配项的索引。与`find`不同的是，如果未找到匹配项，会抛出异常。

#### [pd.Series.str.rindex | pd.Index.str.rindex](08-str\07-数据\07-06-rindex.ipynb)
    - 从右侧开始查找，返回第一个匹配项的索引。与`rfind`不同的是，如果未找到匹配项，会抛出异常。
#### [pd.Series.str.findall | pd.Index.str.findall](08-str\08-捕获\08-01-findall.ipynb)
    - 使用正则表达式匹配，返回所有匹配项。

#### [pd.Series.str.get | pd.Index.str.get](08-str\08-捕获\08-02-get.ipynb)
    - 获取对应索引单个字符

#### [pd.Series.str.slice | pd.Index.str.slice](08-str\08-捕获\08-03-slice.ipynb)
    - 索取对应索引范围字符串

#### [pd.Series.str.extract | pd.Index.str.extract](08-str\08-捕获\08-04-extract.ipynb)
    - 使用正则表达式匹配，捕获第一个匹配组。

#### [pd.Series.str.extractall | pd.Index.str.extractall](08-str\08-捕获\08-05-extractall.ipynb)
    - 使用正则表达式匹配，捕获所有匹配组。
