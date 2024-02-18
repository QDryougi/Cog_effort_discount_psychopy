# 认知努力折扣范式——psychopy builder版本
# cognitive effort discounting paradigm

## 1 简介
这是一个使用psychopy v2021.2.3 编写的认知努力折扣范式实验程序。使用了python的random库，适用于本地运行。

程序包括3个部分：

1. N-back练习：1~6-back任务，循环3轮。不同难度的任务通过刺激的颜色进行区分，目的是被试熟悉刺激颜色与难度之间关系。本部分参考pasychopy官方文档进行编写(https://workshops.psychopy.org/tutorials/n-back.html)
2. 认知努力折扣范式：要求被试进行采用二则一的迫选判断，在完成低报酬的简单任务与高报酬的困难任务间进行选择，高报酬的价值恒定，低报酬的单位每一轮减半，最终缩减至一个相对较小的数值，实现对主观认知努力价值的评估。(Westbrook, A., Kester, D., & Braver, T. S. (2013). What Is the Subjective Cost of Cognitive Effort? Load, Trait, and Aging Effects Revealed by Economic Preference. PLOS ONE, 8(7), e68210. https://doi.org/10.1371/journal.pone.0068210)
3. N-back反馈任务：1个block的较短N-back任务，抽取自被试在第二部分的选择。

其中，第一部分程序为N-back文件夹，第2、3部分程序为cog-effort_evaluation文件夹。

## 2 环境参数
程序的默认显示参数为1920*1080像素，主要影响指导语的排版。

## 3 N-back任务

## 4 认知努力折扣范式

![](https://komarev.com/ghpvc/?username=QDryougi)
