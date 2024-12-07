from os import listdir
from shutil import copyfile
from json import load

src = r"G:\Workshop\Fields\Python\Projects\Jactithm New\code\trucks"
dirlist = listdir(src)
tab = "   "
result = ''

for i in dirlist:
    #获得元数据
    raw = load(open(src+'\\'+i+'\\'+'info.json','r',encoding='utf-8'))
    cts = ''

    #组装HTML5代码
    lines = ['                            <tr style="background-color: #c1c1c1;">',
             f'                                <td><img src="../images/trucks/{i}.jpg" width="150" height="150"></td>',
             '                                <td style="width: 20; background-color: #eaeaea;"></td>',
             '                                <td style="width: 630;" valign="top">',
             f'                                    <h3 style="text-align: center;">{i}</h3>',
             f'                                    <h3 style="text-align: center; line-height: 0.3;">{raw["composer"]}</h3>',
             f'                                    <h4>谱面数量：{len(raw["charts"])}</h4>',]
    for j in raw['charts']:
        cts += f'{j["level"]} {j["difficulty"]} by {j["charter"]}&nbsp;&nbsp;&nbsp;&nbsp;'
    lines.append(f'                                    <p>{cts}</p>')
    lines.append('                                </td>');lines.append('                            </tr>')

    for j in lines:
        result += f'{j}\n'

print(result)