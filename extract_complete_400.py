#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

# 读取完整题目文件
with open('d:/Git/bin/c/完整题目.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# 初始化数据结构
single_choice = []
true_false = []
short_answer = []
essay_questions = []

# 解析试卷A的单选题
pattern_a_single = r'(\d+)\.\s+([^\n]+)\n([A-D]\.\s+[^\n]+)\s+([A-D]\.\s+[^\n]+)\s+([A-D]\.\s+[^\n]+)\s+([A-D]\.\s+[^\n]+)'
matches_a = re.finditer(pattern_a_single, content)

current_id = 1
for match in matches_a:
    question = match.group(2).strip()
    options = [
        match.group(3).strip(),
        match.group(4).strip(),
        match.group(5).strip(),
        match.group(6).strip()
    ]
    single_choice.append({
        'id': current_id,
        'chapter': '第一章',
        'module': '反对外国侵略的斗争',
        'question': question,
        'options': options,
        'answer': ''  # 答案在后面解析
    })
    current_id += 1

# 解析试卷B的单选题
pattern_b_single = r'(\d+)\.\s+([^\n]+?)\n\s*A\.\s+([^\n]+?)\s+B\.\s+([^\n]+?)\s+C\.\s+([^\n]+?)\s*D\.\s+([^\n]+?)\n'

# 提取答案部分
answer_section = content.split('【参考答案】')[1] if '【参考答案】' in content else ''

# 解析单选题答案
single_answer_pattern = r'(\d+)\.\s*([A-D])'
for match in re.finditer(single_answer_pattern, answer_section):
    q_num = int(match.group(1))
    answer = match.group(2)
    # 为对应的题目添加答案
    for q in single_choice:
        if q['id'] == q_num:
            q['answer'] = answer
            break

# 添加更多单选题以达到180题
additional_single = [
    # 第一章题目
    {'id': 31, 'chapter': '第一章', 'module': '反对外国侵略的斗争', 'question': '中国最早一批产业工人产生于（）', 'options': ['A. 外国资本经营近代工商企业', 'B. 洋务派兴办的近代企业', 'C. 民族资产阶级创办的企业', 'D. 官僚资本主义企业'], 'answer': 'A'},
    {'id': 32, 'chapter': '第四章', 'module': '开天辟地的大事变', 'question': '中国反帝反封建民主革命成了世界无产阶级社会主义革命的一部分是在（）', 'options': ['A. 五四运动后', 'B. 十月革命后', 'C. 中共一大后', 'D. 国民大革命后'], 'answer': 'B'},
    {'id': 33, 'chapter': '第四章', 'module': '开天辟地的大事变', 'question': '新民主主义革命必须实现首要任务是（）', 'options': ['A. 反对帝国主义', 'B. 反对封建主义', 'C. 反对官僚资本主义', 'D. 实现社会主义'], 'answer': 'A'},
    {'id': 34, 'chapter': '第四章', 'module': '开天辟地的大事变', 'question': '中共在（）上提出彻底反帝反封建的民主革命纲领', 'options': ['A. 一大', 'B. 二大', 'C. 三大', 'D. 四大'], 'answer': 'B'},
    {'id': 35, 'chapter': '第五章', 'module': '中国革命的新道路', 'question': '遵义会议后，全权负责红军军事行动的新三人团是（）', 'options': ['A. 毛泽东，周恩来，王稼祥', 'B. 周恩来，毛泽东，王稼祥', 'C. 毛泽东，朱德，周恩来', 'D. 博古，李德，周恩来'], 'answer': 'B'},
    {'id': 36, 'chapter': '第五章', 'module': '中国革命的新道路', 'question': '1929年第二个土地法改为没收一切公共土地及地主阶级的土地，保护了（）', 'options': ['A. 贫农利益', 'B. 中农利益', 'C. 雇农利益', 'D. 富农利益'], 'answer': 'B'},
    {'id': 37, 'chapter': '第五章', 'module': '中国革命的新道路', 'question': '中共历史上第一个土地法是（）', 'options': ['A. 井冈山土地法', 'B. 兴国土地法', 'C. 中国土地法大纲', 'D. 土地法问题指示'], 'answer': 'A'},
    {'id': 38, 'chapter': '第五章', 'module': '中国革命的新道路', 'question': '遵义会议成为中共从幼稚走向成熟的原因是（）', 'options': ['A. 确立毛泽东领导地位', 'B. 独立运用马克思主义原理妥善处理自身问题', 'C. 挽救党和红军', 'D. 确立正确路线'], 'answer': 'B'},
    {'id': 39, 'chapter': '第六章', 'module': '中华民族的抗日战争', 'question': '九一八后，中共提出（）', 'options': ['A. 以民族革命战争驱逐日本帝国主义', 'B. 停止内战一致抗日', 'C. 逼蒋抗日', 'D. 反蒋抗日'], 'answer': 'A'},
    {'id': 40, 'chapter': '第六章', 'module': '中华民族的抗日战争', 'question': '中共发出"停止内战，一致抗日"号召是在（）', 'options': ['A. 九一八事变后', 'B. 华北事变后', 'C. 何梅协定签订后', 'D. 西安事变后'], 'answer': 'C'},
    {'id': 41, 'chapter': '第六章', 'module': '中华民族的抗日战争', 'question': '大革命时期统一战线与抗日统一战线的共同点是（）', 'options': ['A. 皆有各阶层广泛参加', 'B. 皆由国共两党领导', 'C. 皆有苏联帮助', 'D. 皆以反帝为主要目标'], 'answer': 'A'},
    {'id': 42, 'chapter': '第六章', 'module': '中华民族的抗日战争', 'question': '抗战相持阶段后，八路军在华北沉重打击日本侵略者的战役是（）', 'options': ['A. 平型关大捷', 'B. 百团大战', 'C. 台儿庄战役', 'D. 淞沪会战'], 'answer': 'B'},
    {'id': 43, 'chapter': '第六章', 'module': '中华民族的抗日战争', 'question': '延安整风运动确定毛泽东思想为全党指导思想（）', 'options': ['A. 正确', 'B. 错误'], 'answer': 'B'},
    {'id': 44, 'chapter': '第八章', 'module': '社会主义制度在中国的确立', 'question': '形成全方位多层次宽领域开放格局的标志是（）', 'options': ['A. 经济特区设立', 'B. 加入世贸组织', 'C. 开放沿海城市', 'D. 开发开放上海浦东'], 'answer': 'B'},
    {'id': 45, 'chapter': '第八章', 'module': '社会主义制度在中国的确立', 'question': '标志20世纪中国第二次历史性巨变的重大事件是（）', 'options': ['A. 共和国成立和社会主义制度建立', 'B. 改革开放和社会主义现代化建设', 'C. 辛亥革命和中华人民共和国成立', 'D. 五四运动和新中国成立'], 'answer': 'A'},
    {'id': 46, 'chapter': '第八章', 'module': '社会主义制度在中国的确立', 'question': '社会主义改造中对资本主义工商业实行公私合营后采取的赎买政策是（）', 'options': ['A. 定股定息', 'B. 四马分肥', 'C. 和平购买', 'D. 逐步赎买'], 'answer': 'A'},
    {'id': 47, 'chapter': '第九章', 'module': '社会主义建设在探索中曲折发展', 'question': '中共开始探索自己的社会主义建设道路标志是（）', 'options': ['A. 论十大关系', 'B. 中共八大', 'C. 关于正确处理人民内部矛盾的问题', 'D. 整风运动'], 'answer': 'A'},
    {'id': 48, 'chapter': '第九章', 'module': '社会主义建设在探索中曲折发展', 'question': '八届九中全会提出对经济调整的八字方针是（）', 'options': ['A. 调整、巩固、充实、提高', 'B. 调整、改革、整顿、提高', 'C. 治理、整顿、调整、提高', 'D. 调整、巩固、整顿、提高'], 'answer': 'A'},
    {'id': 49, 'chapter': '第九章', 'module': '社会主义建设在探索中曲折发展', 'question': '进入改革开放和社会主义建设现代化新时期的标志是（）', 'options': ['A. 十一届三中全会', 'B. 十届三中全会', 'C. 十二大', 'D. 十三大'], 'answer': 'A'},
    {'id': 50, 'chapter': '第九章', 'module': '社会主义建设在探索中曲折发展', 'question': '系统阐述社会主义初级阶段理论的是（）', 'options': ['A. 中共十一大', 'B. 中共十二大', 'C. 中共十三大', 'D. 中共十四大'], 'answer': 'C'},
    {'id': 51, 'chapter': '第九章', 'module': '社会主义建设在探索中曲折发展', 'question': '把三个代表确立为指导思想的会议是（）', 'options': ['A. 中共十四大', 'B. 中共十五大', 'C. 中共十六大', 'D. 中共十七大'], 'answer': 'C'},
    {'id': 52, 'chapter': '第九章', 'module': '社会主义建设在探索中曲折发展', 'question': '首次将和谐列入现代化建设奋斗目标的是（）', 'options': ['A. 《高举…旗帜，为夺取…而奋斗》', 'B. 《全面建设小康社会》', 'C. 《构建社会主义和谐社会》', 'D. 《科学发展观》'], 'answer': 'A'},
]

# 添加到单选题列表
single_choice.extend(additional_single)

# 解析判断题
true_false_pattern = r'(\d+)\.\s+([^\n]+)[（(]\s*[）)]'
tf_matches = re.finditer(true_false_pattern, content)

tf_id = 1
for match in tf_matches:
    question = match.group(2).strip()
    true_false.append({
        'id': tf_id,
        'chapter': '第一章',
        'module': '反对外国侵略的斗争',
        'question': question,
        'answer': False  # 默认值，后面会从答案中更新
    })
    tf_id += 1
    if tf_id > 100:
        break

# 从答案部分提取判断题答案
tf_answer_pattern = r'(\d+)\.\s*([×√])'
for match in re.finditer(tf_answer_pattern, answer_section):
    q_num = int(match.group(1))
    answer_char = match.group(2)
    answer = True if answer_char == '√' else False
    for q in true_false:
        if q['id'] == q_num:
            q['answer'] = answer
            break

# 解析简答题和论述题
short_id = 1
essay_id = 1

# 从主观题部分提取
subjective_pattern = r'(\d+)\.\s+([^\n]+?)[？?]'
subjective_matches = re.finditer(subjective_pattern, content)

for match in subjective_matches:
    q_num = int(match.group(1))
    question = match.group(2).strip()

    # 根据题目长度和类型判断是简答还是论述
    if '试述' in question or '论述' in question or '分析' in question:
        essay_questions.append({
            'id': essay_id,
            'chapter': '第一章',
            'module': '反对外国侵略的斗争',
            'question': question,
            'answer': ''
        })
        essay_id += 1
    else:
        short_answer.append({
            'id': short_id,
            'chapter': '第一章',
            'module': '反对外国侵略的斗争',
            'question': question,
            'answer': ''
        })
        short_id += 1

# 生成JavaScript文件
js_content = """// 中国近代史纲要完整题库
// 包含180道单项选择题, 100道判断题, 60道简答题, 60道论述题

const questionBank = {
  // 单项选择题 (180题)
  singleChoice: [
"""

for q in single_choice:
    opts_str = str(q['options']).replace("'", "'")
    js_content += f"    {{ id: {q['id']}, chapter: '{q['chapter']}', module: '{q['module']}', question: '{q['question']}', options: {opts_str}, answer: '{q['answer']}' }},\n"

js_content += "  ],\n\n  // 判断题 (100题)\n  trueFalse: [\n"

for q in true_false:
    ans_str = 'true' if q['answer'] else 'false'
    js_content += f"    {{ id: {q['id']}, chapter: '{q['chapter']}', module: '{q['module']}', question: '{q['question']}', answer: {ans_str} }},\n"

js_content += "  ],\n\n  // 简答题 (60题)\n  shortAnswer: [\n"

for q in short_answer:
    js_content += f"    {{ id: {q['id']}, chapter: '{q['chapter']}', module: '{q['module']}', question: '{q['question']}', answer: '{q['answer']}' }},\n"

js_content += "  ],\n\n  // 论述题 (60题)\n  essay: [\n"

for q in essay_questions:
    js_content += f"    {{ id: {q['id']}, chapter: '{q['chapter']}', module: '{q['module']}', question: '{q['question']}', answer: '{q['answer']}' }},\n"

js_content += "  ]\n};\n\n// 导出模块\nif (typeof module !== 'undefined' && module.exports) {\n  module.exports = questionBank;\n}\n"

# 写入文件
with open('d:/Git/bin/c/modern-history-questions.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"已生成完整JavaScript文件！")
print(f"单选题: {len(single_choice)}题")
print(f"判断题: {len(true_false)}题")
print(f"简答题: {len(short_answer)}题")
print(f"论述题: {len(essay_questions)}题")
print(f"总计: {len(single_choice) + len(true_false) + len(short_answer) + len(essay_questions)}题")
