#!/usr/bin/env python
# -*- coding: utf-8 -*-
import docx
import json
import re

def parse_word_document(doc_path):
    """解析Word文档中的题目"""
    doc = docx.Document(doc_path)

    # 存储解析结果
    questions = {
        'singleChoice': [],
        'trueFalse': [],
        'shortAnswer': []
    }

    current_chapter = ''
    current_module = ''
    question_id = 1
    current_question_type = None
    current_question = None

    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            continue

        # 检测章节
        if text.startswith('###') or '章' in text:
            if '反对外国侵略的斗争' in text:
                current_module = '反对外国侵略的斗争'
            elif '对国家出路的早期探索' in text:
                current_module = '对国家出路的早期探索'
            elif '辛亥革命与君主专制制度的终结' in text:
                current_module = '辛亥革命与君主专制制度的终结'
            elif '开天辟地的大事变' in text:
                current_module = '开天辟地的大事变'
            elif '中国革命的新道路' in text:
                current_module = '中国革命的新道路'
            elif '中华民族的抗日战争' in text:
                current_module = '中华民族的抗日战争'
            elif '为新中国而奋斗' in text:
                current_module = '为新中国而奋斗'
            elif '社会主义制度在中国的确立' in text:
                current_module = '社会主义制度在中国的确立'
            elif '社会主义建设在探索中曲折发展' in text:
                current_module = '社会主义建设在探索中曲折发展'
            elif '中国特色社会主义' in text:
                current_module = '中国特色社会主义的开创与拓展'
            continue

        # 检测题目类型
        if '单项选择题' in text:
            current_question_type = 'singleChoice'
            continue
        elif '判断题' in text:
            current_question_type = 'trueFalse'
            continue
        elif '简答题' in text:
            current_question_type = 'shortAnswer'
            continue

        # 解析单选题
        if current_question_type == 'singleChoice':
            # 匹配题目：数字. 题目内容（）
            question_match = re.match(r'^(\d+)\.\s+(.+?)（[^）]+）\s*$', text)
            if question_match:
                q_num = question_match.group(1)
                q_text = question_match.group(2)
                current_question = {
                    'id': question_id,
                    'chapter': current_chapter,
                    'module': current_module,
                    'question': q_text,
                    'options': [],
                    'answer': ''
                }
                question_id += 1
                continue

            # 匹配选项：A. 选项内容
            option_match = re.match(r'^([A-D])\.\s+(.+?)\s*$', text)
            if option_match and current_question:
                current_question['options'].append(f"{option_match.group(1)}. {option_match.group(2)}")
                continue

            # 匹配答案：**答案：X**
            answer_match = re.match(r'^\*\*答案：([A-D])\*\*$', text)
            if answer_match and current_question:
                current_question['answer'] = answer_match.group(1)
                questions['singleChoice'].append(current_question)
                current_question = None
                continue

        # 解析判断题
        elif current_question_type == 'trueFalse':
            # 匹配题目：数字. 题目内容。
            question_match = re.match(r'^(\d+)\.\s+(.+?)。{2,}\s*$', text)
            if question_match:
                q_num = question_match.group(1)
                q_text = question_match.group(2)
                current_question = {
                    'id': question_id,
                    'chapter': current_chapter,
                    'module': current_module,
                    'question': q_text,
                    'answer': None
                }
                question_id += 1
                continue

            # 匹配答案：**答案：正确** 或 **答案：错误**
            answer_match = re.match(r'^\*\*答案：(正确|错误)\*\*$', text)
            if answer_match and current_question:
                current_question['answer'] = (answer_match.group(1) == '正确')
                questions['trueFalse'].append(current_question)
                current_question = None
                continue

        # 解析简答题
        elif current_question_type == 'shortAnswer':
            # 匹配题目：数字. 题目内容？
            question_match = re.match(r'^(\d+)\.\s+(.+？)\s*$', text)
            if question_match:
                q_num = question_match.group(1)
                q_text = question_match.group(2)
                current_question = {
                    'id': question_id,
                    'chapter': current_chapter,
                    'module': current_module,
                    'question': q_text,
                    'answer': ''
                }
                question_id += 1
                continue

            # 匹配答案：**答案：** ...
            if current_question and text.startswith('**答案：**'):
                answer_text = text.replace('**答案：**', '').strip()
                current_question['answer'] = answer_text
                questions['shortAnswer'].append(current_question)
                current_question = None
                continue

    return questions

if __name__ == '__main__':
    doc_path = r'C:\Users\liubaoshuo\OneDrive\Desktop\历史真题.docx'
    questions = parse_word_document(doc_path)

    # 输出JSON格式
    print(json.dumps(questions, ensure_ascii=False, indent=2))
