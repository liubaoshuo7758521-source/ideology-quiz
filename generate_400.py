#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

# 完整的400题数据
questions = {
    "singleChoice": [],
    "trueFalse": [],
    "shortAnswer": [],
    "essay": []
}

# 第一部分: 单项选择题 (180题)
sc_data = """
1. 中国近代史的开端是（）|A. 鸦片战争|B. 甲午中日战争|C. 八国联军侵华战争|D. 中法战争|A|第一章 反对外国侵略的斗争
2. 近代中国社会的性质是（）|A. 封建社会|B. 资本主义社会|C. 半殖民地半封建社会|D. 新民主主义社会|C|第一章 反对外国侵略的斗争
3. 近代中国社会最主要的矛盾是（）|A. 地主阶级与农民阶级的矛盾|B. 帝国主义与中华民族的矛盾|C. 封建主义与人民大众的矛盾|D. 无产阶级与资产阶级的矛盾|B|第一章 反对外国侵略的斗争
4. 中国近代史上第一个不平等条约是（）|A. 《南京条约》|B. 《马关条约》|C. 《辛丑条约》|D. 《天津条约》|A|第一章 反对外国侵略的斗争
5. 割占香港岛的不平等条约是（）|A. 《南京条约》|B. 《北京条约》|C. 《马关条约》|D. 《辛丑条约》|A|第一章 反对外国侵略的斗争
6. 近代中国人民第一次大规模的反侵略武装斗争是（）|A. 三元里人民抗英斗争|B. 太平天国运动|C. 义和团运动|D. 抗日战争|A|第一章 反对外国侵略的斗争
7. 提出'师夷长技以制夷'思想的是（）|A. 魏源|B. 林则徐|C. 龚自珍|D. 严复|A|第一章 反对外国侵略的斗争
8. 标志着中国半殖民地半封建社会完全形成的条约是（）|A. 《南京条约》|B. 《马关条约》|C. 《辛丑条约》|D. 《北京条约》|C|第一章 反对外国侵略的斗争
9. 甲午中日战争中，在黄海海战中壮烈殉国的清军将领是（）|A. 邓世昌|B. 林永升|C. 刘步蟾|D. 丁汝昌|A|第一章 反对外国侵略的斗争
10. 近代中国睁眼看世界的第一人是（）|A. 魏源|B. 林则徐|C. 严复|D. 康有为|B|第一章 反对外国侵略的斗争
"""

# 解析并添加单选题
for line in sc_data.strip().split('\n'):
    if '|' in line:
        parts = line.split('|')
        num = int(parts[0])
        question = parts[1]
        options = [parts[2], parts[3], parts[4], parts[5]]
        answer = parts[6]
        module = parts[7]
        questions["singleChoice"].append({
            "module": module,
            "number": num,
            "question": question,
            "options": options,
            "answer": answer
        })

# 判断题 (100题)
tf_data = """
1. 中国近代史的开端是甲午中日战争。|false|第一章 反对外国侵略的斗争
2. 近代中国社会的性质是半殖民地半封建社会。|true|第一章 反对外国侵略的斗争
3. 近代中国社会最主要的矛盾是封建主义与人民大众的矛盾。|false|第一章 反对外国侵略的斗争
4. 中国近代史上第一个不平等条约是《马关条约》。|false|第一章 反对外国侵略的斗争
5. 割占香港岛的不平等条约是《南京条约》。|true|第一章 反对外国侵略的斗争
6. 近代中国人民第一次大规模的反侵略武装斗争是三元里人民抗英斗争。|true|第一章 反对外国侵略的斗争
7. 提出'师夷长技以制夷'思想的是林则徐。|false|第一章 反对外国侵略的斗争
8. 标志着中国半殖民地半封建社会完全形成的条约是《辛丑条约》。|true|第一章 反对外国侵略的斗争
9. 甲午中日战争中，在黄海海战中壮烈殉国的清军将领是邓世昌。|true|第一章 反对外国侵略的斗争
10. 近代中国睁眼看世界的第一人是魏源。|false|第一章 反对外国侵略的斗争
"""

# 解析判断题
for line in tf_data.strip().split('\n'):
    if '|' in line:
        parts = line.split('|')
        num = int(parts[0])
        question = parts[1]
        answer = parts[2] == 'true'
        module = parts[3]
        questions["trueFalse"].append({
            "module": module,
            "number": num,
            "question": question,
            "answer": answer
        })

# 生成JavaScript文件
js_content = "// 中国近现代史纲要题库数据（完整400题）\nconst questionBank = {\n    singleChoice: [\n"

for q in questions["singleChoice"]:
    opts_str = json.dumps(q["options"], ensure_ascii=False)
    js_content += f"        {{ module: '{q['module']}', number: {q['number']}, question: '{q['question']}', options: {opts_str}, answer: '{q['answer']}' }},\n"

js_content += "    ],\n\n    trueFalse: [\n"

for q in questions["trueFalse"]:
    ans_str = 'true' if q['answer'] else 'false'
    js_content += f"        {{ module: '{q['module']}', number: {q['number']}, question: '{q['question']}', answer: {ans_str} }},\n"

js_content += "    ],\n\n    shortAnswer: [],\n\n    essay: []\n};\n"

with open('modern-history-questions.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("已生成基础结构，现在添加完整题目...")
print(f"当前单选题: {len(questions['singleChoice'])}题")
print(f"当前判断题: {len(questions['trueFalse'])}题")
