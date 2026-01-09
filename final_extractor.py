import docx
import json
import re

def extract_all_questions():
    """从所有文档中提取题目"""

    files = [
        r"C:\Users\liubaoshuo\OneDrive\Desktop\2023年华东师范大学公共课《中国近代史纲要》期末试卷A.docx",
        r"C:\Users\liubaoshuo\OneDrive\Desktop\2023年华东师范大学公共课《中国近代史纲要》期末试卷B.docx",
        r"C:\Users\liubaoshuo\OneDrive\Desktop\近代史各章节选择题.docx",
        r"C:\Users\liubaoshuo\OneDrive\Desktop\主观题.docx"
    ]

    all_data = {
        '试卷A': {'lines': []},
        '试卷B': {'lines': []},
        '选择题': {'lines': []},
        '主观题': {'lines': []}
    }

    # 读取所有内容
    for idx, file_path in enumerate(files):
        doc = docx.Document(file_path)
        content = [para.text.strip() for para in doc.paragraphs if para.text.strip()]
        key = list(all_data.keys())[idx]
        all_data[key]['lines'] = content
        print(f"读取 {key}: {len(content)} 行")

    # 解析并输出题目
    output_file = r"d:\Git\bin\c\完整题目.txt"

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("="*100 + "\n")
        f.write("中国近代史纲要 - 完整题目整理\n")
        f.write("="*100 + "\n\n")

        # 处理试卷A
        f.write("="*100 + "\n")
        f.write("试卷A\n")
        f.write("="*100 + "\n\n")
        process_and_write_questions(f, all_data['试卷A']['lines'], '试卷A')

        # 处理试卷B
        f.write("\n\n" + "="*100 + "\n")
        f.write("试卷B\n")
        f.write("="*100 + "\n\n")
        process_and_write_questions(f, all_data['试卷B']['lines'], '试卷B')

        # 处理选择题
        f.write("\n\n" + "="*100 + "\n")
        f.write("各章节选择题\n")
        f.write("="*100 + "\n\n")
        for line in all_data['选择题']['lines']:
            f.write(line + '\n')

        # 处理主观题
        f.write("\n\n" + "="*100 + "\n")
        f.write("主观题\n")
        f.write("="*100 + "\n\n")
        for line in all_data['主观题']['lines']:
            f.write(line + '\n')

    print(f"\n完整内容已保存到: {output_file}")
    return all_data

def process_and_write_questions(f, lines, source_name):
    """处理题目并写入文件"""

    stats = {
        'single_choice': 0,
        'multiple_choice': 0,
        'true_false': 0,
        'subjective': 0
    }

    current_section = None
    questions_buffer = []
    answer_section = False

    for i, line in enumerate(lines):
        # 识别题型
        if '一、' in line and ('单选' in line or '单项选择' in line):
            current_section = 'single_choice'
            f.write(f"\n【一、单选题】\n\n")
            continue
        elif '二、' in line and ('多选' in line or '多项选择' in line):
            current_section = 'multiple_choice'
            f.write(f"\n【二、多选题】\n\n")
            continue
        elif '三、' in line and '判断题' in line:
            current_section = 'true_false'
            f.write(f"\n【三、判断题】\n\n")
            continue
        elif ('四、' in line or '五、' in line) and ('简答' in line or '论述' in line or '材料' in line):
            current_section = 'subjective'
            f.write(f"\n【四、主观题】\n\n")
            continue
        elif '参考答案' in line or '答案:' in line or '答案：' in line:
            answer_section = True
            f.write(f"\n\n{'='*80}\n")
            f.write(f"【参考答案】\n")
            f.write(f"{'='*80}\n\n")
            continue

        # 处理题目
        if current_section:
            # 处理选择题和判断题
            if current_section in ['single_choice', 'multiple_choice', 'true_false']:
                # 检查是否是新题目 (以数字开头)
                match = re.match(r'^(\d+)[.、](.+)', line)
                if match:
                    q_num = match.group(1)
                    q_content = match.group(2)

                    if current_section in ['single_choice', 'multiple_choice']:
                        stats[current_section] += 1
                        f.write(f"{q_num}. {q_content}\n")
                    else:
                        stats[current_section] += 1
                        f.write(f"{q_num}. {q_content}\n")
                else:
                    # 可能是选项或答案
                    f.write(f"{line}\n")

            elif current_section == 'subjective':
                match = re.match(r'^(\d+)[.、](.+)', line)
                if match:
                    stats[current_section] += 1
                    q_num = match.group(1)
                    q_content = match.group(2)
                    f.write(f"{q_num}. {q_content}\n")
                else:
                    f.write(f"{line}\n")
        else:
            # 还没有识别到题型
            f.write(f"{line}\n")

    # 输出统计
    f.write(f"\n\n统计: 单选{stats['single_choice']}题, 多选{stats['multiple_choice']}题, "
            f"判断{stats['true_false']}题, 主观{stats['subjective']}题\n")

    print(f"\n{source_name} - 单选: {stats['single_choice']}, 多选: {stats['multiple_choice']}, "
          f"判断: {stats['true_false']}, 主观: {stats['subjective']}")

if __name__ == '__main__':
    print("开始提取题目...")
    extract_all_questions()
