import docx
import json
import re

def read_docx_content(file_path):
    """读取Word文档内容"""
    doc = docx.Document(file_path)
    content = []
    for para in doc.paragraphs:
        if para.text.strip():
            content.append(para.text.strip())
    return content

def parse_exam_paper(content_lines):
    """解析试卷内容"""
    questions = {
        'single_choice': [],
        'multiple_choice': [],
        'true_false': [],
        'subjective': []
    }

    current_section = None
    current_question = None
    i = 0

    while i < len(content_lines):
        line = content_lines[i].strip()

        # 识别题型
        if '一、单选题' in line or '单项选择题' in line:
            current_section = 'single_choice'
            i += 1
            continue
        elif '二、多选题' in line or '多项选择题' in line:
            current_section = 'multiple_choice'
            i += 1
            continue
        elif '三、判断题' in line:
            current_section = 'true_false'
            i += 1
            continue
        elif '四、简答题' in line or '五、材料分析题' in line or '简答' in line or '论述' in line:
            current_section = 'subjective'
            i += 1
            continue

        # 解析题目
        if current_section == 'single_choice':
            # 匹配题目编号
            match = re.match(r'^(\d+)[.、](.+)', line)
            if match:
                if current_question:
                    questions['single_choice'].append(current_question)
                question_num = match.group(1)
                question_text = match.group(2)
                current_question = {
                    'number': question_num,
                    'question': question_text,
                    'options': []
                }
            elif line.startswith(('A.', 'A、', 'A ')) or line.startswith('A\t'):
                if current_question:
                    current_question['options'].append(line)
            elif line.startswith(('B.', 'B、', 'B ')) or line.startswith('B\t'):
                if current_question:
                    current_question['options'].append(line)
            elif line.startswith(('C.', 'C、', 'C ')) or line.startswith('C\t'):
                if current_question:
                    current_question['options'].append(line)
            elif line.startswith(('D.', 'D、', 'D ')) or line.startswith('D\t'):
                if current_question:
                    current_question['options'].append(line)

        elif current_section == 'multiple_choice':
            match = re.match(r'^(\d+)[.、](.+)', line)
            if match:
                if current_question and len(current_question.get('options', [])) >= 4:
                    questions['multiple_choice'].append(current_question)
                question_num = match.group(1)
                question_text = match.group(2)
                current_question = {
                    'number': question_num,
                    'question': question_text,
                    'options': []
                }
            elif line.startswith(('A.', 'A、', 'A ')) or line.startswith('A\t'):
                if current_question:
                    current_question['options'].append(line)
            elif line.startswith(('B.', 'B、', 'B ')) or line.startswith('B\t'):
                if current_question:
                    current_question['options'].append(line)
            elif line.startswith(('C.', 'C、', 'C ')) or line.startswith('C\t'):
                if current_question:
                    current_question['options'].append(line)
            elif line.startswith(('D.', 'D、', 'D ')) or line.startswith('D\t'):
                if current_question:
                    current_question['options'].append(line)

        elif current_section == 'true_false':
            match = re.match(r'^(\d+)[.、](.+)', line)
            if match:
                if current_question:
                    questions['true_false'].append(current_question)
                question_num = match.group(1)
                question_text = match.group(2)
                current_question = {
                    'number': question_num,
                    'question': question_text,
                    'answer': None
                }

        elif current_section == 'subjective':
            match = re.match(r'^(\d+)[.、](.+)', line)
            if match:
                if current_question:
                    questions['subjective'].append(current_question)
                question_num = match.group(1)
                question_text = match.group(2)
                current_question = {
                    'number': question_num,
                    'question': question_text,
                    'answer': None
                }

        i += 1

    # 添加最后一个问题
    if current_question:
        if current_section == 'single_choice':
            questions['single_choice'].append(current_question)
        elif current_section == 'multiple_choice':
            questions['multiple_choice'].append(current_question)
        elif current_section == 'true_false':
            questions['true_false'].append(current_question)
        elif current_section == 'subjective':
            questions['subjective'].append(current_question)

    return questions

# 读取四个文档
files = [
    r"C:\Users\liubaoshuo\OneDrive\Desktop\2023年华东师范大学公共课《中国近代史纲要》期末试卷A.docx",
    r"C:\Users\liubaoshuo\OneDrive\Desktop\2023年华东师范大学公共课《中国近代史纲要》期末试卷B.docx",
    r"C:\Users\liubaoshuo\OneDrive\Desktop\近代史各章节选择题.docx",
    r"C:\Users\liubaoshuo\OneDrive\Desktop\主观题.docx"
]

all_questions = {
    'single_choice': [],
    'multiple_choice': [],
    'true_false': [],
    'subjective': []
}

for idx, file_path in enumerate(files, 1):
    try:
        print(f"正在处理文件 {idx}: {file_path.split(chr(92))[-1]}")
        content = read_docx_content(file_path)
        questions = parse_exam_paper(content)

        for key in all_questions:
            all_questions[key].extend(questions[key])

        print(f"  - 单选题: {len(questions['single_choice'])} 道")
        print(f"  - 多选题: {len(questions['multiple_choice'])} 道")
        print(f"  - 判断题: {len(questions['true_false'])} 道")
        print(f"  - 主观题: {len(questions['subjective'])} 道")

    except Exception as e:
        print(f"处理文件时出错: {str(e)}")

# 统计
print("\n" + "="*60)
print("统计结果:")
print(f"单选题总数: {len(all_questions['single_choice'])}")
print(f"多选题总数: {len(all_questions['multiple_choice'])}")
print(f"判断题总数: {len(all_questions['true_false'])}")
print(f"主观题总数: {len(all_questions['subjective'])}")
print(f"总题数: {sum(len(v) for v in all_questions.values())}")

# 保存结果
output_file = r"d:\Git\bin\c\questions_output.json"
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

print(f"\n结果已保存到: {output_file}")
