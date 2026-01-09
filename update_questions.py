#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import json

def parse_questions():
    """解析题库文本"""

    # 模块映射
    module_map = {
        '第一章 反对外国侵略的斗争': '反对外国侵略的斗争',
        '第二章 对国家出路的早期探索': '对国家出路的早期探索',
        '第三章 辛亥革命与君主专制制度的终结': '辛亥革命与君主专制制度的终结',
        '第四章 开天辟地的大事变': '开天辟地的大事变',
        '第五章 中国革命的新道路': '中国革命的新道路',
        '第六章 中华民族的抗日战争': '中华民族的抗日战争',
        '第七章 为新中国而奋斗': '为新中国而奋斗',
        '第八章 社会主义基本制度在中国的确立': '社会主义制度在中国的确立',
        '第九章 社会主义建设在探索中曲折发展': '社会主义建设在探索中曲折发展',
        '第十章 中国特色社会主义的开创与接续发展': '中国特色社会主义的开创与接续发展',
        '第十一章 中国特色社会主义进入新时代': '中国特色社会主义进入新时代'
    }

    # 单选题解析
    single_choice = []
    # 从您提供的文本中提取单选题
    # 由于文本很长，我会用正则表达式匹配

    return {
        'singleChoice': single_choice,
        'trueFalse': [],
        'shortAnswer': []
    }

if __name__ == '__main__':
    result = parse_questions()
    print(json.dumps(result, ensure_ascii=False, indent=2))
