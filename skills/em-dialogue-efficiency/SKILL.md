---
name: em-dialogue-efficiency
description: 艾玛短剧 · 台词两步精修的兼容入口。用户点名台词效率或旧名称时，转入 em-dialogue 的 Step 1 场景与人物判断、Step 2 逐句效率删改；不再单独运行旧版评分流程。
---

# 台词效率：统一入口

读取并执行 [em-dialogue 主文件](../em-dialogue/SKILL.md)。先完成 Step 1，再完成 Step 2；本轮已经完成对应步骤则复用结果，不重复评分或改写。用户只要求某一步、只诊断或只要净稿时遵从其范围。

默认保留 F／E 双维度与 S=max(F,E) 的编辑口径、低于 5 删除和 5 至不足 7 重写门槛；具体定义、人物魅力与情绪保护、事实锁定、成文格式和交付以 em-dialogue 当前规则为准。不运行历史规则覆盖当前两步流程。

用户明确要求维护技能时，统一更新 em-dialogue 的相应规则与 references/dialogue-principles.md，不再产生两份冲突规则。两个目录应一起安装，兼容入口不能单独提供完整方法。

若当前列表未显示 em-dialogue，按名称查找已安装技能并读取；不能仅凭本转接页声称已执行完整两步。
