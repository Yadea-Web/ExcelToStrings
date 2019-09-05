## 多语言文件转换

### Excel文件转客户端多语言文件

* 只支持.xls文件
* 文件命名为`language.xls`
* 表格格式参考`language.xls`
	* 第一列为key，命名格式参考文件中的key说明
	* 第一列之后为文案，第一行为语言类别，会与生成文件的名字有关
	* 数据从第三行开始有
* 生成的文件带有`语言类别`后缀，重命名一下文件就可以
	* 安卓生成文件名规则：`strings-语言类别.xml`
	* iOS生成文件名：`Localizable-语言类别.strings`
	* Web生成文件名：`语言类别.js`

	
### 执行
* 命令行(会生成三个平台的文件)： `python generateLanguage.py`
* 生成iOS平台的文件：`python generateLanguage.py iOS`
* 生成Android平台的文件：`python generateLanguage.py Android`
* 生成Web平台的文件：`python generateLanguage.py Web`
* 注意事项
	* `generateLanguage.py`和多语言xls文件要在同一个目录下，在当前目录执行命令行


项目开始前准备好对应文案记录到Excel中，然后用工具生成不同平台的多语言文件，导入到项目中即可。