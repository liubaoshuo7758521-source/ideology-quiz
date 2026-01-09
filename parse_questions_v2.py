#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Parse all 400 questions from 完整题目.txt and convert to JavaScript format
"""

import re
import json

def parse_questions():
    """Parse the complete questions file"""

    with open(r'd:\Git\bin\c\完整题目.txt', 'r', encoding='utf-8') as f:
        content = f.read()

    # Initialize question lists
    single_choice = []
    true_false = []
    short_answer = []
    essay = []

    # Parse single choice questions (180 questions)
    # Pattern: number. question text\nA. option1 B. option2 C. option3 D. option4\n答案：X

    # Find the single choice section
    single_choice_match = re.search(r'## 第一部分 单项选择题.*?(?=## 第二部分)', content, re.DOTALL)
    if single_choice_match:
        single_choice_text = single_choice_match.group(0)
        # Split by question number pattern
        questions = re.split(r'\n(?=\d+\.\s)', single_choice_text)

        current_module = "第一章"
        question_num = 1

        for q in questions[1:]:  # Skip first empty element
            # Extract question number, text, options, and answer
            match = re.match(r'(\d+)\.\s*(.*?)\nA\.\s*(.*?)\nB\.\s*(.*?)\nC\.\s*(.*?)\nD\.\s*(.*?)\n\*\*答案[：:]\s*([A-D\*]+)\*\*', q, re.DOTALL)
            if match:
                num, question, opt_a, opt_b, opt_c, opt_d, answer = match.groups()

                # Clean up the question text and options
                question = question.strip().replace('*', '')
                opt_a = opt_a.strip()
                opt_b = opt_b.strip()
                opt_c = opt_c.strip()
                opt_d = opt_d.strip()
                answer = answer.strip().replace('*', '')

                # Determine module based on question number
                if question_num <= 20:
                    current_module = "反对外国侵略的斗争"
                elif question_num <= 40:
                    current_module = "对国家出路的早期探索"
                elif question_num <= 60:
                    current_module = "辛亥革命与君主专制制度的终结"
                elif question_num <= 80:
                    current_module = "开天辟地的大事变"
                elif question_num <= 100:
                    current_module = "中国革命的新道路"
                elif question_num <= 120:
                    current_module = "中华民族的抗日战争"
                elif question_num <= 140:
                    current_module = "为新中国而奋斗"
                elif question_num <= 160:
                    current_module = "社会主义基本制度在中国的确立"
                elif question_num <= 170:
                    current_module = "社会主义建设在探索中曲折发展"
                elif question_num <= 180:
                    current_module = "中国特色社会主义的开创与接续发展"

                single_choice.append({
                    'module': current_module,
                    'number': question_num,
                    'question': question,
                    'options': [f"A. {opt_a}", f"B. {opt_b}", f"C. {opt_c}", f"D. {opt_d}"],
                    'answer': answer
                })
                question_num += 1

    # Parse true/false questions (100 questions)
    true_false_match = re.search(r'## 第二部分 判断题.*?(?=## 第三部分)', content, re.DOTALL)
    if true_false_match:
        true_false_text = true_false_match.group(0)
        questions = re.split(r'\n(?=\d+\.\s)', true_false_text)

        question_num = 1
        for q in questions[1:]:  # Skip first empty element
            match = re.match(r'(\d+)\.\s*(.*?)\（([×√]+)\）', q, re.DOTALL)
            if match:
                num, question, answer = match.groups()
                question = question.strip()

                # Convert answer to boolean
                if answer == '√':
                    answer_bool = 'true'
                else:
                    answer_bool = 'false'

                # Determine module
                if question_num <= 10:
                    current_module = "反对外国侵略的斗争"
                elif question_num <= 20:
                    current_module = "对国家出路的早期探索"
                elif question_num <= 30:
                    current_module = "辛亥革命与君主专制制度的终结"
                elif question_num <= 40:
                    current_module = "开天辟地的大事变"
                elif question_num <= 50:
                    current_module = "中国革命的新道路"
                elif question_num <= 60:
                    current_module = "中华民族的抗日战争"
                elif question_num <= 70:
                    current_module = "为新中国而奋斗"
                elif question_num <= 80:
                    current_module = "社会主义基本制度在中国的确立"
                elif question_num <= 90:
                    current_module = "社会主义建设在探索中曲折发展"
                else:
                    current_module = "中国特色社会主义的开创与接续发展"

                true_false.append({
                    'module': current_module,
                    'number': question_num,
                    'question': question,
                    'answer': answer_bool
                })
                question_num += 1

    # Parse short answer questions (60 questions)
    short_answer_match = re.search(r'## 第三部分 简答题.*?(?=## 第四部分)', content, re.DOTALL)
    if short_answer_match:
        short_answer_text = short_answer_match.group(0)
        questions = re.split(r'\n(?=\d+\.\s)', short_answer_text)

        question_num = 1
        for q in questions[1:]:  # Skip first empty element
            match = re.match(r'(\d+)\.\s*(.*?)\n\*\*答案\*\*[：:]\s*(.*?)(?=\n\d+\.|$)', q, re.DOTALL)
            if match:
                num, question, answer = match.groups()
                question = question.strip()
                answer = answer.strip() if answer else ""

                # Determine module
                if question_num <= 6:
                    current_module = "反对外国侵略的斗争"
                elif question_num <= 12:
                    current_module = "对国家出路的早期探索"
                elif question_num <= 18:
                    current_module = "辛亥革命与君主专制制度的终结"
                elif question_num <= 24:
                    current_module = "开天辟地的大事变"
                elif question_num <= 30:
                    current_module = "中国革命的新道路"
                elif question_num <= 36:
                    current_module = "中华民族的抗日战争"
                elif question_num <= 42:
                    current_module = "为新中国而奋斗"
                elif question_num <= 48:
                    current_module = "社会主义基本制度在中国的确立"
                elif question_num <= 51:
                    current_module = "社会主义建设在探索中曲折发展"
                elif question_num <= 54:
                    current_module = "中国特色社会主义的开创与接续发展"
                else:
                    current_module = "中国特色社会主义进入新时代"

                short_answer.append({
                    'module': current_module,
                    'number': question_num,
                    'question': question,
                    'answer': answer
                })
                question_num += 1

    # Parse essay questions (60 questions)
    essay_match = re.search(r'## 第四部分 论述题.*', content, re.DOTALL)
    if essay_match:
        essay_text = essay_match.group(0)
        # Split by question number
        questions = re.split(r'\n(?=\d+\.\s)', essay_text)

        question_num = 1
        for q in questions[1:]:  # Skip first empty element
            # Remove markdown formatting
            q_clean = re.sub(r'\*\*', '', q)
            # Extract question (everything up to the next number or end)
            match = re.match(r'(\d+)\.\s*(.*?)(?=\n\d+\.|$)', q_clean, re.DOTALL)
            if match:
                num, question = match.groups()
                question = question.strip()

                # Determine module
                if question_num <= 6:
                    current_module = "反对外国侵略的斗争"
                elif question_num <= 12:
                    current_module = "对国家出路的早期探索"
                elif question_num <= 18:
                    current_module = "辛亥革命与君主专制制度的终结"
                elif question_num <= 24:
                    current_module = "开天辟地的大事变"
                elif question_num <= 30:
                    current_module = "中国革命的新道路"
                elif question_num <= 36:
                    current_module = "中华民族的抗日战争"
                elif question_num <= 42:
                    current_module = "为新中国而奋斗"
                elif question_num <= 48:
                    current_module = "社会主义基本制度在中国的确立"
                elif question_num <= 51:
                    current_module = "社会主义建设在探索中曲折发展"
                elif question_num <= 54:
                    current_module = "中国特色社会主义的开创与接续发展"
                else:
                    current_module = "中国特色社会主义进入新时代"

                essay.append({
                    'module': current_module,
                    'number': question_num,
                    'question': question,
                    'answer': ''
                })
                question_num += 1

    return {
        'singleChoice': single_choice,
        'trueFalse': true_false,
        'shortAnswer': short_answer,
        'essay': essay
    }

def escape_js_string(s):
    """Escape special characters for JavaScript strings"""
    if not s:
        return ""
    s = s.replace('\\', '\\\\')  # Backslash first!
    s = s.replace('"', '\\"')    # Double quote
    s = s.replace("'", "\\'")    # Single quote
    s = s.replace(''', "\\'")    # Chinese single quote left
    s = s.replace(''', "\\'")    # Chinese single quote right
    s = s.replace('\n', '\\n')   # Newline
    s = s.replace('\r', '\\r')   # Carriage return
    s = s.replace('\t', '\\t')   # Tab
    return s

def generate_javascript(questions):
    """Generate JavaScript file content"""

    js_content = "// 中国近代史纲要完整题库\n// 包含180道单项选择题, 100道判断题, 60道简答题, 60道论述题\n\nvar modernHistoryQuestions = {\n"

    # Single choice questions
    js_content += "  // 单项选择题 (180题)\n"
    js_content += "  singleChoice: [\n"
    for i, q in enumerate(questions['singleChoice']):
        # Escape special characters for JavaScript
        question = escape_js_string(q['question'].replace('\n', ' '))
        options = [escape_js_string(opt.replace('\n', ' ')) for opt in q['options']]
        answer = escape_js_string(q['answer'])

        js_content += f"    {{ id: {i+1}, chapter: '第{get_chapter(q['module'])}章', module: '{q['module']}', question: '{question}', options: ['{options[0]}', '{options[1]}', '{options[2]}', '{options[3]}'], answer: '{answer}' }},\n"
    js_content += "  ],\n\n"

    # True/false questions
    js_content += "  // 判断题 (100题)\n"
    js_content += "  trueFalse: [\n"
    for i, q in enumerate(questions['trueFalse']):
        question = escape_js_string(q['question'].replace('\n', ' '))
        js_content += f"    {{ id: {i+1}, chapter: '第{get_chapter(q['module'])}章', module: '{q['module']}', question: '{question}', answer: {q['answer']} }},\n"
    js_content += "  ],\n\n"

    # Short answer questions
    js_content += "  // 简答题 (60题)\n"
    js_content += "  shortAnswer: [\n"
    for i, q in enumerate(questions['shortAnswer']):
        question = escape_js_string(q['question'].replace('\n', ' '))
        answer = escape_js_string(q['answer'].replace('\n', ' '))
        js_content += f"    {{ id: {i+1}, chapter: '第{get_chapter(q['module'])}章', module: '{q['module']}', question: '{question}', answer: '{answer}' }},\n"
    js_content += "  ],\n\n"

    # Essay questions
    js_content += "  // 论述题 (60题)\n"
    js_content += "  essay: [\n"
    for i, q in enumerate(questions['essay']):
        question = escape_js_string(q['question'].replace('\n', ' '))
        answer = escape_js_string(q['answer'].replace('\n', ' '))
        js_content += f"    {{ id: {i+1}, chapter: '第{get_chapter(q['module'])}章', module: '{q['module']}', question: '{question}', answer: '{answer}' }},\n"
    js_content += "  ]\n"

    js_content += "};\n\n// 导出到全局变量供浏览器使用\nvar questionBank = modernHistoryQuestions;\n\n// 导出模块供 Node.js 使用\nif (typeof module !== 'undefined' && module.exports) {\n  module.exports = modernHistoryQuestions;\n}\n"

    return js_content

def get_chapter(module_name):
    """Get chapter number based on module name"""
    modules = {
        "反对外国侵略的斗争": 1,
        "对国家出路的早期探索": 2,
        "辛亥革命与君主专制制度的终结": 3,
        "开天辟地的大事变": 4,
        "中国革命的新道路": 5,
        "中华民族的抗日战争": 6,
        "为新中国而奋斗": 7,
        "社会主义基本制度在中国的确立": 8,
        "社会主义建设在探索中曲折发展": 9,
        "中国特色社会主义的开创与接续发展": 10,
        "中国特色社会主义进入新时代": 11
    }
    for name, num in modules.items():
        if name in module_name:
            return num
    return 1

if __name__ == '__main__':
    print("正在解析 完整题目.txt...")
    questions = parse_questions()

    print(f"解析完成：")
    print(f"  单选题：{len(questions['singleChoice'])} 题")
    print(f"  判断题：{len(questions['trueFalse'])} 题")
    print(f"  简答题：{len(questions['shortAnswer'])} 题")
    print(f"  论述题：{len(questions['essay'])} 题")
    print(f"  总计：{len(questions['singleChoice']) + len(questions['trueFalse']) + len(questions['shortAnswer']) + len(questions['essay'])} 题")

    print("\n正在生成 JavaScript 文件...")
    js_content = generate_javascript(questions)

    with open(r'd:\Git\bin\c\modern-history-questions.js', 'w', encoding='utf-8') as f:
        f.write(js_content)

    print("完成！JavaScript 文件已生成：modern-history-questions.js")
