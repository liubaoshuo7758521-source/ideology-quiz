#!/usr/bin/env python
# -*- coding: utf-8 -*-
import docx
import json
import sys

# 尝试不同的编码
def try_decode(text):
    encodings = ['utf-8', 'gbk', 'gb2312', 'gb18030']
    for enc in encodings:
        try:
            return text.encode('latin-1').decode(enc)
        except:
            continue
    return text

def parse_word_document(doc_path):
    """解析Word文档中的题目"""
    try:
        doc = docx.Document(doc_path)
    except Exception as e:
        return {"error": f"无法打开文档: {str(e)}"}

    all_text = []
    for para in doc.paragraphs:
        try:
            text = para.text.strip()
            if text:
                all_text.append(text)
        except Exception as e:
            continue

    # 输出前100行用于调试
    return {
        "total_lines": len(all_text),
        "sample": all_text[:50]
    }

if __name__ == '__main__':
    doc_path = r'C:\Users\liubaoshuo\OneDrive\Desktop\历史真题.docx'
    result = parse_word_document(doc_path)

    # 输出JSON格式
    print(json.dumps(result, ensure_ascii=False, indent=2))
