import docx
import sys

def analyze_doc_format(file_path):
    """分析Word文档格式"""
    doc = docx.Document(file_path)

    print(f"\n分析文件: {file_path.split(chr(92))[-1]}")
    print("="*80)

    for i, para in enumerate(doc.paragraphs[:50]):  # 只看前50行
        text = para.text.strip()
        if text:
            print(f"{i+1:3d}: [{text[:100]}]")

# 分析四个文件
files = [
    r"C:\Users\liubaoshuo\OneDrive\Desktop\2023年华东师范大学公共课《中国近代史纲要》期末试卷A.docx",
    r"C:\Users\liubaoshuo\OneDrive\Desktop\2023年华东师范大学公共课《中国近代史纲要》期末试卷B.docx",
]

for file_path in files:
    try:
        analyze_doc_format(file_path)
    except Exception as e:
        print(f"Error: {e}")
