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
    single_choice_match = re.search(r'## 一、单项选择题（180题）.*?(?=## 二、)', content, re.DOTALL)
    if single_choice_match:
        single_choice_text = single_choice_match.group(0)
        # Split by question number pattern
        questions = re.split(r'\n(?=\d+\.\s)', single_choice_text)

        current_module = "第一章"
        question_num = 1

        for q in questions[1:]:  # Skip first empty element
            # Extract question number, text, options, and answer
            match = re.match(r'(\d+)\.\s*(.*?)\nA\.\s*(.*?)\s+B\.\s*(.*?)\s+C\.\s*(.*?)\s+D\.\s*(.*?)\s*答案[：:]\s*([A-D])', q, re.DOTALL)
            if match:
                num, question, opt_a, opt_b, opt_c, opt_d, answer = match.groups()

                # Clean up the question text
                question = question.strip()
                opt_a = opt_a.strip()
                opt_b = opt_b.strip()
                opt_c = opt_c.strip()
                opt_d = opt_d.strip()

                # Determine module based on question number
                if question_num <= 20:
                    current_module = "第一章 反对外国侵略的斗争"
                elif question_num <= 40:
                    current_module = "第二章 太平天国运动与洋务运动"
                elif question_num <= 60:
                    current_module = "第三章 辛亥革命与君主专制制度的终结"
                elif question_num <= 80:
                    current_module = "第四章 开天辟地的大事变"
                elif question_num <= 100:
                    current_module = "第五章 中国革命的新道路"
                elif question_num <= 120:
                    current_module = "第六章 中华民族的抗日战争"
                elif question_num <= 140:
                    current_module = "第七章 为新中国而奋斗"
                elif question_num <= 160:
                    current_module = "第八章 社会主义基本制度在中国的确立"
                elif question_num <= 180:
                    current_module = "第九章 社会主义建设在探索中曲折发展"
                elif question_num <= 200:
                    current_module = "第十章 改革开放与现代化建设新时期"

                single_choice.append({
                    'module': current_module,
                    'number': question_num,
                    'question': question,
                    'options': [f"A. {opt_a}", f"B. {opt_b}", f"C. {opt_c}", f"D. {opt_d}"],
                    'answer': answer
                })
                question_num += 1

    # Parse true/false questions (100 questions)
    true_false_match = re.search(r'## 二、判断题（100题）.*?(?=## 三、)', content, re.DOTALL)
    if true_false_match:
        true_false_text = true_false_match.group(0)
        questions = re.split(r'\n(?=\d+\.\s)', true_false_text)

        question_num = 1
        for q in questions[1:]:  # Skip first empty element
            match = re.match(r'(\d+)\.\s*(.*?)\s*答案[：:]\s*(正确|错误|√|×|true|false)', q, re.DOTALL)
            if match:
                num, question, answer = match.groups()
                question = question.strip()

                # Convert answer to boolean
                if answer in ['正确', '√', 'true']:
                    answer_bool = 'true'
                else:
                    answer_bool = 'false'

                # Determine module
                if question_num <= 10:
                    current_module = "第一章 反对外国侵略的斗争"
                elif question_num <= 20:
                    current_module = "第二章 太平天国运动与洋务运动"
                elif question_num <= 30:
                    current_module = "第三章 辛亥革命与君主专制制度的终结"
                elif question_num <= 40:
                    current_module = "第四章 开天辟地的大事变"
                elif question_num <= 50:
                    current_module = "第五章 中国革命的新道路"
                elif question_num <= 60:
                    current_module = "第六章 中华民族的抗日战争"
                elif question_num <= 70:
                    current_module = "第七章 为新中国而奋斗"
                elif question_num <= 80:
                    current_module = "第八章 社会主义基本制度在中国的确立"
                elif question_num <= 90:
                    current_module = "第九章 社会主义建设在探索中曲折发展"
                else:
                    current_module = "第十章 改革开放与现代化建设新时期"

                true_false.append({
                    'module': current_module,
                    'number': question_num,
                    'question': question,
                    'answer': answer_bool
                })
                question_num += 1

    # Parse short answer questions (60 questions)
    short_answer_match = re.search(r'## 三、简答题（60题）.*?(?=## 四、)', content, re.DOTALL)
    if short_answer_match:
        short_answer_text = short_answer_match.group(0)
        questions = re.split(r'\n(?=\d+\.\s)', short_answer_text)

        question_num = 1
        for q in questions[1:]:  # Skip first empty element
            match = re.match(r'(\d+)\.\s*(.*?)(?:\n答案[：:]\s*(.*?))?(?=\n\d+\.|$)', q, re.DOTALL)
            if match:
                num, question, answer = match.groups()
                question = question.strip()
                answer = (answer or "").strip()

                # Determine module
                if question_num <= 6:
                    current_module = "第一章 反对外国侵略的斗争"
                elif question_num <= 12:
                    current_module = "第二章 太平天国运动与洋务运动"
                elif question_num <= 18:
                    current_module = "第三章 辛亥革命与君主专制制度的终结"
                elif question_num <= 24:
                    current_module = "第四章 开天辟地的大事变"
                elif question_num <= 30:
                    current_module = "第五章 中国革命的新道路"
                elif question_num <= 36:
                    current_module = "第六章 中华民族的抗日战争"
                elif question_num <= 42:
                    current_module = "第七章 为新中国而奋斗"
                elif question_num <= 48:
                    current_module = "第八章 社会主义基本制度在中国的确立"
                elif question_num <= 54:
                    current_module = "第九章 社会主义建设在探索中曲折发展"
                else:
                    current_module = "第十章 改革开放与现代化建设新时期"

                short_answer.append({
                    'module': current_module,
                    'number': question_num,
                    'question': question,
                    'answer': answer
                })
                question_num += 1

    # Parse essay questions (60 questions)
    essay_match = re.search(r'## 四、论述题（60题）.*', content, re.DOTALL)
    if essay_match:
        essay_text = essay_match.group(0)
        questions = re.split(r'\n(?=\d+\.\s)', essay_text)

        question_num = 1
        for q in questions[1:]:  # Skip first empty element
            match = re.match(r'(\d+)\.\s*(.*?)(?:\n答案[：:]\s*(.*?))?(?=\n\d+\.|$)', q, re.DOTALL)
            if match:
                num, question, answer = match.groups()
                question = question.strip()
                answer = (answer or "").strip()

                # Determine module
                if question_num <= 6:
                    current_module = "第一章 反对外国侵略的斗争"
                elif question_num <= 12:
                    current_module = "第二章 太平天国运动与洋务运动"
                elif question_num <= 18:
                    current_module = "第三章 辛亥革命与君主专制制度的终结"
                elif question_num <= 24:
                    current_module = "第四章 开天辟地的大事变"
                elif question_num <= 30:
                    current_module = "第五章 中国革命的新道路"
                elif question_num <= 36:
                    current_module = "第六章 中华民族的抗日战争"
                elif question_num <= 42:
                    current_module = "第七章 为新中国而奋斗"
                elif question_num <= 48:
                    current_module = "第八章 社会主义基本制度在中国的确立"
                elif question_num <= 54:
                    current_module = "第九章 社会主义建设在探索中曲折发展"
                else:
                    current_module = "第十章 改革开放与现代化建设新时期"

                essay.append({
                    'module': current_module,
                    'number': question_num,
                    'question': question,
                    'answer': answer
                })
                question_num += 1

    return {
        'singleChoice': single_choice,
        'trueFalse': true_false,
        'shortAnswer': short_answer,
        'essay': essay
    }

def generate_javascript(questions):
    """Generate JavaScript file content"""

    js_content = "// 中国近现代史纲要题库数据（完整400题）\nconst questionBank = {\n"

    # Single choice questions
    js_content += "    singleChoice: [\n"
    for q in questions['singleChoice']:
        # Replace Chinese quotes with single quotes
        question = q['question'].replace('"', "'").replace('"', "'")
        options = [opt.replace('"', "'").replace('"', "'") for opt in q['options']]

        js_content += f"        {{ module: '{q['module']}', number: {q['number']}, question: '{question}', options: ['{options[0]}', '{options[1]}', '{options[2]}', '{options[3]}'], answer: '{q['answer']}' }},\n"
    js_content += "    ],\n\n"

    # True/false questions
    js_content += "    trueFalse: [\n"
    for q in questions['trueFalse']:
        question = q['question'].replace('"', "'").replace('"', "'")
        js_content += f"        {{ module: '{q['module']}', number: {q['number']}, question: '{question}', answer: {q['answer']} }},\n"
    js_content += "    ],\n\n"

    # Short answer questions
    js_content += "    shortAnswer: [\n"
    for q in questions['shortAnswer']:
        question = q['question'].replace('"', "'").replace('"', "'")
        answer = q['answer'].replace('"', "'").replace('"', "'").replace('\n', ' ')
        js_content += f"        {{ module: '{q['module']}', number: {q['number']}, question: '{question}', answer: '{answer}' }},\n"
    js_content += "    ],\n\n"

    # Essay questions
    js_content += "    essay: [\n"
    for q in questions['essay']:
        question = q['question'].replace('"', "'").replace('"', "'")
        answer = q['answer'].replace('"', "'").replace('"', "'").replace('\n', ' ')
        js_content += f"        {{ module: '{q['module']}', number: {q['number']}, question: '{question}', answer: '{answer}' }},\n"
    js_content += "    ]\n"

    js_content += "};\n"

    return js_content

if __name__ == '__main__':
    print("Parsing questions from 完整题目.txt...")
    questions = parse_questions()

    print(f"Found {len(questions['singleChoice'])} single choice questions")
    print(f"Found {len(questions['trueFalse'])} true/false questions")
    print(f"Found {len(questions['shortAnswer'])} short answer questions")
    print(f"Found {len(questions['essay'])} essay questions")

    print("\nGenerating JavaScript file...")
    js_content = generate_javascript(questions)

    with open(r'd:\Git\bin\c\modern-history-questions.js', 'w', encoding='utf-8') as f:
        f.write(js_content)

    print("Complete! JavaScript file generated.")
