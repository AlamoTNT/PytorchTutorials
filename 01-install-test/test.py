#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""  
@Author: 44190@Liuyang
@Time: 2023/4/18 19:51
@Description: 测试GPU版本的Torch是否安装成功
"""

import torch


def test_cuda_available():
    print(torch.cuda.is_available())


if __name__ == '__main__':
    test_cuda_available()
