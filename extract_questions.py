import docx
import json

def extract_questions_from_doc(file_path):
    """从Word文档中提取题目"""
    doc = docx.Document(file_path)

    questions = {
        'single_choice': [],
        'multiple_choice': [],
        'true_false': [],
        'subjective': []
    }

    current_section = None
    current_question = None
    answer_section = False
    answers = {}

    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            continue

        # 检测答案部分
        if '参考答案' in text or '答案:' in text or '答案：' in text:
            answer_section = True
            continue

        # 识别题型标题
        if '一、' in text and '单选题' in text:
            current_section = 'single_choice'
            continue
        elif '二、' in text and '多选题' in text:
            current_section = 'multiple_choice'
            continue
        elif '三、' in text and '判断题' in text:
            current_section = 'true_false'
            continue
        elif '四、' in text or '五、' in text or '简答' in text or '论述' in text or '材料' in text:
            current_section = 'subjective'
            continue

        # 解析题目
        if not answer_section:
            if current_section in ['single_choice', 'multiple_choice']:
                # 检查是否是题目开始 (数字、)
                if text[0].isdigit() and (text[1] in ['、', '.']):
                    # 保存上一题
                    if current_question:
                        questions[current_section].append(current_question)

                    # 开始新题目
                    parts = text.split('、', 1)
                    if len(parts) == 2:
                        q_num = parts[0]
                        q_text = parts[1].rstrip('(（）  )')
                        current_question = {
                            'number': q_num,
                            'question': q_text,
                            'options': [],
                            'answer': None
                        }

                # 选项
                elif text.startswith('A.') or text.startswith('A、') or text.startswith('A\t'):
                    option_text = text[2:].strip()
                    if current_question:
                        current_question['options'].append('A. ' + option_text)
                elif text.startswith('B.') or text.startswith('B、') or text.startswith('B\t'):
                    option_text = text[2:].strip()
                    if current_question:
                        current_question['options'].append('B. ' + option_text)
                elif text.startswith('C.') or text.startswith('C、') or text.startswith('C\t'):
                    option_text = text[2:].strip()
                    if current_question:
                        current_question['options'].append('C. ' + option_text)
                elif text.startswith('D.') or text.startswith('D、') or text.startswith('D\t'):
                    option_text = text[2:].strip()
                    if current_question:
                        current_question['options'].append('D. ' + option_text)

            elif current_section == 'true_false':
                if text[0].isdigit() and (text[1] in ['、', '.']):
                    parts = text.split('、', 1)
                    if len(parts) == 2:
                        q_num = parts[0]
                        q_text = parts[1]
                        current_question = {
                            'number': q_num,
                            'question': q_text,
                            'answer': None
                        }
                        questions['true_false'].append(current_question)
                        current_question = None

            elif current_section == 'subjective':
                if text[0].isdigit() and (text[1] in ['、', '.']):
                    if current_question:
                        questions['subjective'].append(current_question)

                    parts = text.split('、', 1)
                    if len(parts) == 2:
                        q_num = parts[0]
                        q_text = parts[1]
                        current_question = {
                            'number': q_num,
                            'question': q_text,
                            'answer': None
                        }

        # 解析答案
        else:
            # 单选题答案
            if text[0].isdigit() and text[1] in ['、', '.']:
                parts = text.split('、', 1)
                if len(parts) == 2:
                    q_num = parts[0]
                    answer = parts[1].strip()
                    answers[q_num] = answer
            elif len(text) >= 2 and text[0].isdigit() and text[1] in ['、', '.']:
                # 处理多选题答案 (如 "16、BCD")
                parts = text.split('、', 1)
                if len(parts) == 2:
                    q_num = parts[0]
                    answer = parts[1].strip()
                    answers[q_num] = answer
            elif text.startswith('√') or text.startswith('×'):
                # 判断题答案 (需要对应题号)
                pass

    # 保存最后一个问题
    if current_question:
        if current_section in questions:
            questions[current_section].append(current_question)

    # 匹配答案
    for section in ['single_choice', 'multiple_choice', 'true_false']:
        for q in questions[section]:
            if q['number'] in answers:
                q['answer'] = answers[q['number']]

    return questions

def main():
    files = [
        {
            'path': r"C:\Users\liubaoshuo\OneDrive\Desktop\2023年华东师范大学公共课《中国近代史纲要》期末试卷A.docx",
            'name': '期末试卷A'
        },
        {
            'path': r"C:\Users\liubaoshuo\OneDrive\Desktop\2023年华东师范大学公共课《中国近代史纲要》期末试卷B.docx",
            'name': '期末试卷B'
        },
        {
            'path': r"C:\Users\liubaoshuo\OneDrive\Desktop\近代史各章节选择题.docx",
            'name': '各章节选择题'
        },
        {
            'path': r"C:\Users\liubaoshuo\OneDrive\Desktop\主观题.docx",
            'name': '主观题'
        }
    ]

    all_questions = {
        'single_choice': [],
        'multiple_choice': [],
        'true_false': [],
        'subjective': []
    }

    print("="*80)
    print("开始提取题目...")
    print("="*80)

    for file_info in files:
        try:
            print(f"\n正在处理: {file_info['name']}")
            questions = extract_questions_from_doc(file_info['path'])

            print(f"  单选题: {len(questions['single_choice'])} 道")
            print(f"  多选题: {len(questions['multiple_choice'])} 道")
            print(f"  判断题: {len(questions['true_false'])} 道")
            print(f"  主观题: {len(questions['subjective'])} 道")

            # 合并题目
            for key in all_questions:
                all_questions[key].extend(questions[key])

        except Exception as e:
            print(f"  处理出错: {str(e)}")
            import traceback
            traceback.print_exc()

    # 统计
    print("\n" + "="*80)
    print("统计结果:")
    print("="*80)
    print(f"单选题总数: {len(all_questions['single_choice'])} 道")
    print(f"多选题总数: {len(all_questions['multiple_choice'])} 道")
    print(f"判断题总数: {len(all_questions['true_false'])} 道")
    print(f"主观题总数: {len(all_questions['subjective'])} 道")
    print(f"-"*80)
    print(f"总题数: {sum(len(v) for v in all_questions.values())} 道")

    # 保存JSON
    output_file = r"d:\Git\bin\c\all_questions.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, ensure_ascii=False, indent=2)

    print(f"\n题目已保存到: {output_file}")

    # 生成可读文本
    generate_readable_output(all_questions, r"d:\Git\bin\c\题目整理.txt")

def generate_readable_output(questions, output_file):
    """生成可读的文本输出"""

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("="*100 + "\n")
        f.write("中国近代史纲要 - 题目整理\n")
        f.write("="*100 + "\n\n")

        # 单选题
        f.write("一、单选题\n")
        f.write("="*100 + "\n\n")
        for q in questions['single_choice']:
            f.write(f"{q['number']}. {q['question']}\n")
            for opt in q['options']:
                f.write(f"   {opt}\n")
            if q['answer']:
                f.write(f"   答案: {q['answer']}\n")
            f.write("\n")

        # 多选题
        f.write("\n二、多选题\n")
        f.write("="*100 + "\n\n")
        for q in questions['multiple_choice']:
            f.write(f"{q['number']}. {q['question']}\n")
            for opt in q['options']:
                f.write(f"   {opt}\n")
            if q['answer']:
                f.write(f"   答案: {q['answer']}\n")
            f.write("\n")

        # 判断题
        f.write("\n三、判断题\n")
        f.write("="*100 + "\n\n")
        for q in questions['true_false']:
            f.write(f"{q['number']}. {q['question']}\n")
            if q['answer']:
                f.write(f"   答案: {q['answer']}\n")
            f.write("\n")

        # 主观题
        f.write("\n四、主观题\n")
        f.write("="*100 + "\n\n")
        for q in questions['subjective']:
            f.write(f"{q['number']}. {q['question']}\n")
            if q['answer']:
                f.write(f"   参考答案: {q['answer']}\n")
            f.write("\n")

        # 统计
        f.write("\n" + "="*100 + "\n")
        f.write("统计\n")
        f.write("="*100 + "\n")
        f.write(f"单选题数量: {len(questions['single_choice'])}\n")
        f.write(f"多选题数量: {len(questions['multiple_choice'])}\n")
        f.write(f"判断题数量: {len(questions['true_false'])}\n")
        f.write(f"主观题数量: {len(questions['subjective'])}\n")
        f.write(f"总题数: {sum(len(v) for v in questions.values())}\n")

    print(f"可读文本已保存到: {output_file}")

if __name__ == '__main__':
    main()
