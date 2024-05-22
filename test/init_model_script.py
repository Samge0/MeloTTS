#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author：samge
# date：2024-05-22 14:06
# describe：

import subprocess

language_list = {'ZH', 'JP', 'EN', 'ZH_MIX_EN', 'KR', 'FR', 'SP', 'ES'}


if __name__ == "__main__":
    """
    遍历语言列表，自动下载需要的模型到 xxx/.cache/huggingface 目录下
    
        cd test
        python init_model_script.py
    
    """
    for language in language_list:
        # 构建命令
        command = f"/bin/python /app/test/test_base_model_tts_package.py {language}"
        
        print(f"正在处理：{language}")
        # 调用系统命令
        subprocess.run(command, shell=True)
    print(f"all done")