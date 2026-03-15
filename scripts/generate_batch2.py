#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate batch_2.json for 大类3 and 大类4 of 中华人民共和国职业分类大典 2022版."""

import json
import os

entries = []

# ═══════════════════════════════════════
# 大类3: 办事人员和有关人员
# ═══════════════════════════════════════

MC3 = "办事人员和有关人员"

# 3-01 行政业务办理人员
mid = "行政业务办理人员"
entries.append({
    "code": "3-01-01", "name": "行政秘书", "major_category": MC3, "major_category_code": 3,
    "mid_category": mid,
    "description": "协助领导处理日常行政事务，负责文件起草、会议安排、公务接待及信息传递等综合协调工作。",
    "typical_tasks": ["起草公文、通知及会议纪要", "安排领导日程和会议议程", "接待来访人员并协调公务活动", "管理机要文件的收发与归档", "跨部门沟通协调落实领导批示"],
    "education": "本科", "salary_median_k": 8, "est_employment_wan": 80
})
entries.append({
    "code": "3-01-02", "name": "行政文员", "major_category": MC3, "major_category_code": 3,
    "mid_category": mid,
    "description": "从事办公室日常行政事务处理，包括文档管理、资料整理、办公用品采购及基础行政支持工作。",
    "typical_tasks": ["录入和整理各类办公文档与报表", "接听电话并记录转达信息", "管理办公用品采购与库存盘点", "协助组织员工活动和培训安排", "维护办公环境整洁并管理固定资产台账"],
    "education": "本科", "salary_median_k": 6, "est_employment_wan": 150
})
entries.append({
    "code": "3-01-03", "name": "人力资源管理人员", "major_category": MC3, "major_category_code": 3,
    "mid_category": mid,
    "description": "负责组织的人力资源规划、招聘配置、薪酬福利管理、绩效考核及员工关系维护等工作。",
    "typical_tasks": ["制定招聘计划并组织面试筛选候选人", "核算员工薪酬并办理社保公积金缴纳", "设计和实施绩效考核方案", "处理劳动合同签订、续签及离职手续", "组织员工培训并建立人才发展体系"],
    "education": "本科", "salary_median_k": 10, "est_employment_wan": 120
})
entries.append({
    "code": "3-01-04", "name": "财务出纳人员", "major_category": MC3, "major_category_code": 3,
    "mid_category": mid,
    "description": "负责单位现金收付、银行结算、票据管理及日常资金收支记录等基础财务工作。",
    "typical_tasks": ["办理现金收付和银行转账结算业务", "登记现金日记账和银行存款日记账", "审核报销单据并核对发票真伪", "管理库存现金和各类有价证券", "编制资金日报表并与银行对账"],
    "education": "本科", "salary_median_k": 7, "est_employment_wan": 200
})
entries.append({
    "code": "3-01-05", "name": "法务助理", "major_category": MC3, "major_category_code": 3,
    "mid_category": mid,
    "description": "协助法务部门处理合同审核、法律文书整理、诉讼支持及合规管理等法律事务工作。",
    "typical_tasks": ["审核各类商务合同条款并提出修改意见", "整理和归档诉讼案件材料", "收集法律法规变动信息并编写合规报告", "协助律师准备庭审文件和证据材料", "维护企业知识产权档案和商标注册台账"],
    "education": "本科", "salary_median_k": 9, "est_employment_wan": 30
})
entries.append({
    "code": "3-01-06", "name": "客户服务管理人员", "major_category": MC3, "major_category_code": 3,
    "mid_category": mid,
    "description": "负责客户服务体系建设和管理，处理客户投诉、维护客户关系，提升客户满意度和服务质量。",
    "typical_tasks": ["建立客户服务标准流程和质量考核体系", "处理重大客户投诉并协调跨部门解决", "分析客户满意度调查数据并制定改进措施", "培训和指导客服团队提升服务技能", "管理CRM系统维护客户信息和服务记录"],
    "education": "本科", "salary_median_k": 8, "est_employment_wan": 150
})
entries.append({
    "code": "3-01-07", "name": "行政主管", "major_category": MC3, "major_category_code": 3,
    "mid_category": mid,
    "description": "统筹管理单位行政事务，负责后勤保障、制度建设、资产管理及行政团队管理等综合管理工作。",
    "typical_tasks": ["制定和完善行政管理制度与工作流程", "统筹办公场所租赁装修及后勤保障", "编制行政预算并控制各项行政费用支出", "管理行政团队分配工作任务并考核绩效", "协调处理政府关系和对外接待事务"],
    "education": "本科", "salary_median_k": 10, "est_employment_wan": 60
})

# 3-02 安全保卫和消防人员
mid = "安全保卫和消防人员"
entries.append({
    "code": "3-02-01", "name": "人民警察", "major_category": MC3, "major_category_code": 3,
    "mid_category": mid,
    "description": "依法维护社会治安秩序，预防和打击违法犯罪活动，保护公民人身和财产安全的国家公务人员。",
    "typical_tasks": ["巡逻执勤维护辖区社会治安秩序", "受理群众报警并开展案件侦查取证", "调解民间纠纷和处置突发治安事件", "开展社区警务和治安防范宣传", "管理户籍和居民身份证办理工作"],
    "education": "本科", "salary_median_k": 10, "est_employment_wan": 200
})
entries.append({
    "code": "3-02-02", "name": "交通警察", "major_category": MC3, "major_category_code": 3,
    "mid_category": mid,
    "description": "负责道路交通秩序管理、交通事故处理、交通安全宣传及车辆和驾驶人管理等交通执法工作。",
    "typical_tasks": ["指挥疏导交通维护道路通行秩序", "处理道路交通事故并进行责任认定", "查处酒驾超速等交通违法行为", "审核驾驶证和机动车登记业务", "排查道路交通安全隐患并制定整改方案"],
    "education": "本科", "salary_median_k": 9, "est_employment_wan": 30
})
entries.append({
    "code": "3-02-03", "name": "消防救援人员", "major_category": MC3, "major_category_code": 3,
    "mid_category": mid,
    "description": "从事火灾扑救、抢险救援、消防监督检查及消防安全宣传培训等消防救援工作。",
    "typical_tasks": ["接警出动扑救各类火灾事故", "开展地震洪涝等自然灾害抢险救援", "对重点单位进行消防监督检查", "组织消防演练和消防安全知识宣传", "维护保养消防车辆装备和器材"],
    "education": "本科", "salary_median_k": 8, "est_employment_wan": 60
})
entries.append({
    "code": "3-02-04", "name": "司法警察", "major_category": MC3, "major_category_code": 3,
    "mid_category": mid,
    "description": "在法院、检察院等司法机关中负责值庭警卫、押解看管、送达文书及协助执行等司法保障工作。",
    "typical_tasks": ["维护法庭审判秩序和庭审安全", "押解和看管犯罪嫌疑人及被告人", "送达法律文书和协助强制执行", "保护司法机关办公场所安全", "协助办案人员进行搜查和扣押"],
    "education": "本科", "salary_median_k": 9, "est_employment_wan": 20
})

# 3-03 海关和边防人员
mid = "海关和边防人员"
entries.append({
    "code": "3-03-01", "name": "海关关员", "major_category": MC3, "major_category_code": 3,
    "mid_category": mid,
    "description": "在海关系统从事进出口货物监管、征收关税、查缉走私及出入境检验检疫等海关业务工作。",
    "typical_tasks": ["审核进出口货物报关单证和许可证件", "对进出口货物进行查验和放行", "征收关税和进口环节税费", "查缉走私违法犯罪活动", "对进出境动植物和食品实施检验检疫"],
    "education": "本科", "salary_median_k": 10, "est_employment_wan": 8
})
entries.append({
    "code": "3-03-02", "name": "边防检查人员", "major_category": MC3, "major_category_code": 3,
    "mid_category": mid,
    "description": "在口岸和边境地区从事出入境人员证件检查、边境巡逻管控及非法出入境查缉等边防管理工作。",
    "typical_tasks": ["检查出入境人员护照签证等证件", "对出入境交通工具进行检查监护", "巡逻管控边境线防范非法越境", "查缉偷渡和组织他人偷越国境犯罪", "采集出入境人员生物信息并录入系统"],
    "education": "本科", "salary_median_k": 9, "est_employment_wan": 5
})

# 3-04 税务和社保经办人员
mid = "税务和社保经办人员"
entries.append({
    "code": "3-04-01", "name": "税务征收管理人员", "major_category": MC3, "major_category_code": 3,
    "mid_category": mid,
    "description": "在税务机关从事税款征收、纳税评估、税务稽查及纳税服务等税收征收管理工作。",
    "typical_tasks": ["办理纳税人税务登记和发票领购业务", "审核纳税申报并征收各项税款", "开展纳税评估发现税收风险疑点", "实施税务稽查查处偷逃税行为", "辅导纳税人享受税收优惠政策"],
    "education": "本科", "salary_median_k": 10, "est_employment_wan": 50
})
entries.append({
    "code": "3-04-02", "name": "社会保险经办人员", "major_category": MC3, "major_category_code": 3,
    "mid_category": mid,
    "description": "在社保经办机构从事养老、医疗、失业等社会保险的参保登记、待遇核发和基金管理等经办服务工作。",
    "typical_tasks": ["办理企业和个人社会保险参保登记", "审核养老金和医疗报销等待遇申领", "核定社会保险缴费基数和费率", "管理社会保险基金收支和账户记录", "接待群众咨询并处理社保争议"],
    "education": "本科", "salary_median_k": 8, "est_employment_wan": 40
})
entries.append({
    "code": "3-04-03", "name": "市场监管执法人员", "major_category": MC3, "major_category_code": 3,
    "mid_category": mid,
    "description": "在市场监管部门从事市场主体登记、产品质量监管、反不正当竞争及消费者权益保护等市场监管执法工作。",
    "typical_tasks": ["办理企业工商注册登记和变更手续", "开展产品质量抽检和食品安全检查", "查处假冒伪劣和虚假广告等违法行为", "调解处理消费者投诉举报", "监督检查市场主体经营行为是否合规"],
    "education": "本科", "salary_median_k": 9, "est_employment_wan": 30
})

# 3-05 邮政和电信业务人员
mid = "邮政和电信业务人员"
entries.append({
    "code": "3-05-01", "name": "邮政业务人员", "major_category": MC3, "major_category_code": 3,
    "mid_category": mid,
    "description": "在邮政网点从事邮件收寄、分拣封发、投递以及邮政储蓄和汇兑等邮政综合业务工作。",
    "typical_tasks": ["收寄各类邮件包裹并称重计费", "分拣封发邮件并安排运输投递路线", "投递信件包裹并办理签收手续", "办理邮政储蓄存取款和汇兑业务", "销售邮票和集邮品并推广邮政增值服务"],
    "education": "高中/中专", "salary_median_k": 5, "est_employment_wan": 30
})
entries.append({
    "code": "3-05-02", "name": "电信业务人员", "major_category": MC3, "major_category_code": 3,
    "mid_category": mid,
    "description": "在电信运营商从事通信业务受理、话费结算、网络服务开通及客户维护等电信业务工作。",
    "typical_tasks": ["办理手机号码入网和套餐变更业务", "受理宽带安装移机和故障报修", "核算话费账单并处理缴费结算", "推广通信产品和增值业务套餐", "处理客户通信服务投诉和质量申告"],
    "education": "本科", "salary_median_k": 7, "est_employment_wan": 40
})

# 3-06 供应链和仓储管理人员
mid = "供应链和仓储管理人员"
entries.append({
    "code": "3-06-01", "name": "采购管理人员", "major_category": MC3, "major_category_code": 3,
    "mid_category": mid,
    "description": "负责企业物资采购计划编制、供应商开发管理、采购谈判及合同执行等供应链采购管理工作。",
    "typical_tasks": ["编制采购计划并发布询价招标文件", "考察评估供应商资质和供货能力", "进行采购价格谈判并签订采购合同", "跟踪采购订单执行进度和到货验收", "分析采购成本数据并优化采购策略"],
    "education": "本科", "salary_median_k": 9, "est_employment_wan": 80
})
entries.append({
    "code": "3-06-02", "name": "仓储管理人员", "major_category": MC3, "major_category_code": 3,
    "mid_category": mid,
    "description": "负责仓库日常运营管理，包括物资入库验收、在库保管、出库发货及库存盘点等仓储管理工作。",
    "typical_tasks": ["办理物资入库验收登记和货位分配", "定期盘点库存并编制库存报表", "按订单要求拣货包装并安排出库发货", "维护仓储环境确保物资安全存放", "操作仓储管理系统更新库存数据"],
    "education": "大专", "salary_median_k": 6, "est_employment_wan": 100
})
entries.append({
    "code": "3-06-03", "name": "物流调度管理人员", "major_category": MC3, "major_category_code": 3,
    "mid_category": mid,
    "description": "负责物流运输的调度管理，统筹安排运输路线、车辆调配和配送计划，确保货物高效准时送达。",
    "typical_tasks": ["制定运输配送计划并优化配送路线", "调度车辆和驾驶员匹配运输任务", "监控在途货物运输状态并处理异常", "协调发货方和收货方对接装卸事宜", "统计运输成本和时效数据并分析改进"],
    "education": "本科", "salary_median_k": 8, "est_employment_wan": 80
})

# 3-07 质量管理和检验人员
mid = "质量管理和检验人员"
entries.append({
    "code": "3-07-01", "name": "质量管理人员", "major_category": MC3, "major_category_code": 3,
    "mid_category": mid,
    "description": "负责企业质量管理体系建设和运行维护，组织质量改进活动，确保产品和服务符合质量标准要求。",
    "typical_tasks": ["建立和维护ISO等质量管理体系文件", "组织内部质量审核并跟踪不符合项整改", "分析质量数据识别质量问题并推动改进", "处理客户质量投诉并组织根本原因分析", "策划和实施全面质量管理培训活动"],
    "education": "本科", "salary_median_k": 9, "est_employment_wan": 60
})
entries.append({
    "code": "3-07-02", "name": "产品检验检测人员", "major_category": MC3, "major_category_code": 3,
    "mid_category": mid,
    "description": "使用检测仪器设备对产品进行理化指标和性能参数检验，出具检测报告确保产品合格。",
    "typical_tasks": ["按照检测标准对原材料和成品取样检验", "操作光谱仪色谱仪等精密检测仪器", "记录检测数据并编制检验检测报告", "校准和维护检测设备确保量值准确", "判定产品质量是否符合国家标准或企业标准"],
    "education": "本科", "salary_median_k": 7, "est_employment_wan": 80
})
entries.append({
    "code": "3-07-03", "name": "标准化管理人员", "major_category": MC3, "major_category_code": 3,
    "mid_category": mid,
    "description": "从事标准的制定、修订、宣贯和实施监督工作，推动企业和行业标准化体系建设。",
    "typical_tasks": ["起草和修订企业标准和行业标准文本", "跟踪国内外标准动态并评估影响", "组织标准宣贯培训并监督标准实施", "参与国际标准化组织技术委员会活动", "建立企业标准化信息管理系统和标准数据库"],
    "education": "本科", "salary_median_k": 9, "est_employment_wan": 15
})

# 3-08 环境和安全监测人员
mid = "环境和安全监测人员"
entries.append({
    "code": "3-08-01", "name": "环境监测人员", "major_category": MC3, "major_category_code": 3,
    "mid_category": mid,
    "description": "从事大气、水、土壤等环境要素的采样监测和数据分析，评价环境质量状况并提供监测报告。",
    "typical_tasks": ["采集大气水体土壤等环境样品", "操作监测仪器分析污染物浓度指标", "编制环境监测报告和质量评价报告", "维护自动监测站点设备正常运行", "参与突发环境污染事件的应急监测"],
    "education": "本科", "salary_median_k": 8, "est_employment_wan": 25
})
entries.append({
    "code": "3-08-02", "name": "职业安全健康监测人员", "major_category": MC3, "major_category_code": 3,
    "mid_category": mid,
    "description": "从事工作场所职业病危害因素监测、劳动者职业健康检查及职业安全风险评估等工作。",
    "typical_tasks": ["检测工作场所粉尘噪声化学毒物等危害因素", "组织劳动者上岗前和在岗期间职业健康检查", "评估工作场所职业病危害风险等级", "编制职业病危害因素检测与评价报告", "指导用人单位落实职业病防护措施"],
    "education": "本科", "salary_median_k": 8, "est_employment_wan": 15
})

# 3-09 知识产权管理人员
mid = "知识产权管理人员"
entries.append({
    "code": "3-09-01", "name": "专利代理人员", "major_category": MC3, "major_category_code": 3,
    "mid_category": mid,
    "description": "受委托代理专利申请、专利无效宣告等专利事务，撰写专利文件并提供专利法律咨询服务。",
    "typical_tasks": ["与发明人沟通技术方案并撰写专利申请文件", "答复国家知识产权局审查意见通知书", "进行专利检索分析和侵权风险评估", "代理专利无效宣告和复审请求", "为企业制定专利布局策略和知识产权保护方案"],
    "education": "本科", "salary_median_k": 12, "est_employment_wan": 8
})
entries.append({
    "code": "3-09-02", "name": "商标代理人员", "major_category": MC3, "major_category_code": 3,
    "mid_category": mid,
    "description": "受委托代理商标注册申请、商标异议和争议等商标事务，为客户提供商标法律咨询和品牌保护服务。",
    "typical_tasks": ["进行商标近似检索并评估注册成功率", "准备商标注册申请材料并提交注册", "代理商标异议答辩和无效宣告案件", "监测商标侵权行为并发送维权函", "为企业制定商标品牌保护和管理方案"],
    "education": "本科", "salary_median_k": 10, "est_employment_wan": 5
})

# ═══════════════════════════════════════
# 大类4: 社会生产服务和生活服务人员
# ═══════════════════════════════════════

MC4 = "社会生产服务和生活服务人员"

# 4-01 批发与零售服务人员
mid = "批发与零售服务人员"
entries.append({
    "code": "4-01-01", "name": "商品营业员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "在商场超市等零售场所从事商品陈列、销售推介、顾客接待及收银结账等商品零售服务工作。",
    "typical_tasks": ["整理货架陈列商品并更换价签标识", "接待顾客介绍商品功能和使用方法", "处理商品退换货并记录售后信息", "盘点货架库存并提交补货申请", "维护卖场环境整洁并执行促销活动方案"],
    "education": "高中/中专", "salary_median_k": 4, "est_employment_wan": 500
})
entries.append({
    "code": "4-01-02", "name": "收银员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "在商业场所负责商品扫码计价、收取货款、找零及开具票据等收银结算工作。",
    "typical_tasks": ["扫描商品条码并核对价格进行结算", "收取现金和处理移动支付及刷卡交易", "核对每日营业款项并编制收银日报", "办理会员积分和优惠券抵扣", "处理顾客退款并按规定开具发票"],
    "education": "高中/中专", "salary_median_k": 4, "est_employment_wan": 200
})
entries.append({
    "code": "4-01-03", "name": "商品采购员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "负责零售和批发企业的商品采购，包括市场调研、供应商洽谈、订单下达和到货验收等工作。",
    "typical_tasks": ["调研市场行情和消费趋势选定采购品类", "联系供应商询价比价并洽谈采购条件", "下达采购订单并跟踪供货交期", "验收到货商品核对品种数量和质量", "分析商品销售数据调整采购结构和库存"],
    "education": "本科", "salary_median_k": 7, "est_employment_wan": 60
})
entries.append({
    "code": "4-01-04", "name": "电子商务运营人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "负责电商平台店铺的日常运营管理，包括商品上架、活动策划、数据分析及客户维护等线上销售工作。",
    "typical_tasks": ["编辑商品详情页文案和主图并上架发布", "策划双十一等电商促销活动方案", "分析店铺流量转化率等运营数据指标", "优化关键词和付费推广提升搜索排名", "处理线上订单和售后问题维护店铺评分"],
    "education": "本科", "salary_median_k": 9, "est_employment_wan": 150
})
entries.append({
    "code": "4-01-05", "name": "药品销售人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "在药店或医药公司从事药品零售销售、用药咨询指导及药品库存管理等医药销售服务工作。",
    "typical_tasks": ["接待顾客并根据症状推荐非处方药品", "核对处方药品名称剂量并按方发药", "整理药品货架检查效期并及时下架近效期药品", "录入药品出入库记录并盘点库存", "向顾客讲解药品用法用量和注意事项"],
    "education": "本科", "salary_median_k": 7, "est_employment_wan": 40
})
entries.append({
    "code": "4-01-06", "name": "市场营销人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "从事市场调研、营销策划、品牌推广和销售支持等市场营销工作，促进产品和服务的市场拓展。",
    "typical_tasks": ["开展市场调研分析竞争对手和消费者需求", "制定年度营销计划和品牌推广方案", "策划线上线下营销活动并跟踪执行效果", "管理广告投放预算和媒体渠道合作", "编写营销分析报告并提出市场拓展建议"],
    "education": "本科", "salary_median_k": 9, "est_employment_wan": 200
})

# 4-02 交通运输服务人员
mid = "交通运输服务人员"
entries.append({
    "code": "4-02-01", "name": "汽车驾驶员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "驾驶各类汽车从事人员接送、公务用车及私人出行等驾驶服务工作，确保行车安全。",
    "typical_tasks": ["按照指定路线安全驾驶车辆", "出车前检查车辆油量胎压和各项功能", "定期送车保养维修并记录车辆使用情况", "保持车辆内外整洁卫生", "遵守交通法规处理行驶途中突发状况"],
    "education": "高中/中专", "salary_median_k": 6, "est_employment_wan": 1500
})
entries.append({
    "code": "4-02-02", "name": "城市公共交通驾驶员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "驾驶公共汽车、电车或有轨电车在固定线路上运行，为市民提供安全准时的城市公共交通服务。",
    "typical_tasks": ["按照线路时刻表准时发车运营", "规范进出站停靠并提醒乘客安全乘车", "处理车辆故障和乘客突发状况", "做好运营前后车辆安全检查", "填写行车日志和营运数据报表"],
    "education": "高中/中专", "salary_median_k": 6, "est_employment_wan": 100
})
entries.append({
    "code": "4-02-03", "name": "出租车和网约车驾驶员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "驾驶出租汽车或网约车为乘客提供个性化出行服务，按计价器或平台计费收取运费。",
    "typical_tasks": ["通过巡游揽客或接受平台派单接送乘客", "选择最优路线安全快捷送达目的地", "使用计价器或平台结算收取乘车费用", "保持车内环境整洁并提供必要乘车服务", "处理乘客遗失物品和服务纠纷"],
    "education": "高中/中专", "salary_median_k": 6, "est_employment_wan": 400
})
entries.append({
    "code": "4-02-04", "name": "货运驾驶员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "驾驶货运车辆从事各类货物的公路运输，负责货物装卸监督和运输途中安全保障工作。",
    "typical_tasks": ["按照运输合同装载货物并确认货物安全捆扎", "驾驶货车按规定路线和时限完成运输任务", "途中检查货物状态防止货损货差", "办理货物交接签收和运输单据", "遵守疲劳驾驶限制规定并做好行车记录"],
    "education": "高中/中专", "salary_median_k": 7, "est_employment_wan": 800
})
entries.append({
    "code": "4-02-05", "name": "列车乘务人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "在铁路旅客列车上从事旅客服务、车厢管理和安全保障等列车乘务工作。",
    "typical_tasks": ["检票验票并引导旅客对号入座", "巡视车厢维护车内秩序和环境卫生", "提供餐饮和卧铺服务照顾重点旅客", "播报到站信息并组织旅客安全上下车", "处理列车上突发事件和旅客投诉"],
    "education": "大专", "salary_median_k": 6, "est_employment_wan": 30
})
entries.append({
    "code": "4-02-06", "name": "航空乘务人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "在民航客机上从事旅客服务、客舱安全管理和应急处置等空中乘务工作。",
    "typical_tasks": ["航前检查客舱设备和应急器材完备性", "迎接旅客登机并协助放置行李", "进行客舱安全演示和起降安全检查", "为旅客提供餐饮和机上服务", "处理客舱突发医疗事件和安全事件"],
    "education": "大专", "salary_median_k": 10, "est_employment_wan": 15
})
entries.append({
    "code": "4-02-07", "name": "船舶驾驶人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "操纵和驾驶各类船舶在内河和海上航行，负责船舶航行安全和货物运输等船舶驾驶工作。",
    "typical_tasks": ["操纵船舶按照航线安全航行和靠离码头", "观察海况和气象条件调整航行计划", "指挥船员进行货物装卸和压载水操作", "使用雷达GPS等航海仪器定位和避碰", "填写航海日志并执行船舶安全检查"],
    "education": "大专", "salary_median_k": 8, "est_employment_wan": 20
})
entries.append({
    "code": "4-02-08", "name": "道路运输服务人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "在客运站、货运站等场所从事运输调度、票务服务、货物受理及安全管理等道路运输服务工作。",
    "typical_tasks": ["售卖客运车票并办理退改签手续", "受理货物托运并开具运输单据", "调度客货运班次和车辆排班", "检查旅客和货物安全确保违禁品不上车", "维护站场秩序并处理旅客服务投诉"],
    "education": "高中/中专", "salary_median_k": 5, "est_employment_wan": 50
})

# 4-03 仓储和快递服务人员
mid = "仓储和快递服务人员"
entries.append({
    "code": "4-03-01", "name": "仓储保管员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "在仓库中从事货物验收入库、在库保管、拣选出库及库存盘点等仓储保管工作。",
    "typical_tasks": ["验收入库货物核对品名数量并登记台账", "按货物特性分类存放并标识货位", "根据出库单拣选打包货物并交付发运", "定期巡查仓库防潮防火防盗防虫", "月末盘点实物库存与系统账目核对"],
    "education": "高中/中专", "salary_median_k": 5, "est_employment_wan": 150
})
entries.append({
    "code": "4-03-02", "name": "快递服务人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "从事快递包裹的收件、分拣、转运和派送等快递服务工作，确保包裹安全快速送达。",
    "typical_tasks": ["上门收取快递包裹并称重扫码录入", "在分拣中心按区域分拣快递包裹", "驾驶快递车辆按路线派送包裹到户", "通知收件人取件并处理签收事宜", "处理问题件和客户投诉并反馈处理结果"],
    "education": "高中/中专", "salary_median_k": 6, "est_employment_wan": 450
})
entries.append({
    "code": "4-03-03", "name": "外卖配送人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "通过外卖平台接单，到餐饮商家取餐并按时配送至顾客指定地点的即时配送服务工作。",
    "typical_tasks": ["通过手机APP接收外卖配送订单", "到商家门店等待取餐并核对订单内容", "规划配送路线骑行送餐至顾客地址", "联系顾客确认送达并完成订单签收", "处理顾客退单和配送异常等问题"],
    "education": "高中/中专", "salary_median_k": 6, "est_employment_wan": 700
})

# 4-04 住宿服务人员
mid = "住宿服务人员"
entries.append({
    "code": "4-04-01", "name": "前台接待员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "在酒店宾馆前台负责宾客入住登记、退房结账、预订管理及咨询服务等前台接待工作。",
    "typical_tasks": ["办理宾客入住登记并分配房间钥匙", "处理退房结账和费用核对", "接听预订电话和处理在线订房信息", "解答宾客咨询并提供旅游交通等信息", "处理宾客投诉和特殊需求并做好交接班记录"],
    "education": "大专", "salary_median_k": 5, "est_employment_wan": 60
})
entries.append({
    "code": "4-04-02", "name": "客房服务员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "在酒店宾馆负责客房清洁整理、布草更换、客用品补给及宾客房间服务等客房服务工作。",
    "typical_tasks": ["清洁客房卫生间并更换床上布草", "补充客房内洗漱用品和饮品", "检查客房设施设备运转并报修故障", "提供送餐洗衣等客房送物服务", "按标准做床铺和布置客房物品"],
    "education": "高中/中专", "salary_median_k": 4, "est_employment_wan": 100
})
entries.append({
    "code": "4-04-03", "name": "酒店管理人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "负责酒店日常运营管理，统筹前厅客房餐饮等部门协调，提升服务品质和经营效益。",
    "typical_tasks": ["制定酒店运营计划和服务质量标准", "管理各部门人员排班和绩效考核", "分析酒店入住率和收入数据制定营销策略", "处理重要宾客接待和重大投诉事件", "监督酒店安全卫生和消防管理落实情况"],
    "education": "大专", "salary_median_k": 7, "est_employment_wan": 30
})

# 4-05 餐饮服务人员
mid = "餐饮服务人员"
entries.append({
    "code": "4-05-01", "name": "中式烹调师", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "运用中式烹饪技法加工制作各类中餐菜品，包括炒菜、蒸煮、炖焖等中式烹调工作。",
    "typical_tasks": ["根据菜单备料切配食材进行初加工", "掌握火候运用炒炸蒸煮等技法制作菜品", "调配菜品口味并进行装盘美化出品", "研发新菜品并更新季节性菜单", "管理厨房食材库存确保食品安全卫生"],
    "education": "高中/中专", "salary_median_k": 6, "est_employment_wan": 600
})
entries.append({
    "code": "4-05-02", "name": "西式烹调师", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "运用西式烹饪技法制作各类西餐菜品，包括煎烤焗炸等西式烹调和冷菜沙拉制作。",
    "typical_tasks": ["按照西餐食谱准备和预处理食材", "运用煎烤焗等西式技法烹制牛排意面等菜品", "制作沙拉前菜和西式汤品", "进行西式菜品摆盘和装饰出品", "控制食材成本并保持厨房卫生标准"],
    "education": "高中/中专", "salary_median_k": 6, "est_employment_wan": 50
})
entries.append({
    "code": "4-05-03", "name": "中式面点师", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "制作包子饺子馒头面条等各类中式面点和小吃，掌握发面揉面等面点制作工艺。",
    "typical_tasks": ["和面揉面制作各种发酵面团和水调面团", "包制饺子包子馄饨等传统面点", "蒸制烤制炸制各类面点成品", "制作地方特色小吃和节令面点", "管理面点原料采购和面点间卫生"],
    "education": "高中/中专", "salary_median_k": 5, "est_employment_wan": 200
})
entries.append({
    "code": "4-05-04", "name": "西式面点师", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "制作蛋糕面包甜点等各类西式烘焙产品，掌握烘焙发酵裱花等西点制作工艺。",
    "typical_tasks": ["称量配比原料制作蛋糕面包面团和面糊", "操作烤箱控制温度和时间烘焙成品", "制作奶油裱花和翻糖装饰蛋糕", "制作慕斯提拉米苏等法式甜品", "开发新品并设计季节限定产品"],
    "education": "高中/中专", "salary_median_k": 5, "est_employment_wan": 30
})
entries.append({
    "code": "4-05-05", "name": "餐厅服务员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "在餐厅从事迎宾引座、点菜推荐、上菜服务、结账买单等餐饮前厅服务工作。",
    "typical_tasks": ["迎接顾客引导就座并递送菜单", "介绍菜品特色并为顾客点菜下单", "传菜上菜并为顾客提供就餐期间服务", "清理餐桌翻台并重新摆台布置", "办理顾客结账并处理发票开具"],
    "education": "高中/中专", "salary_median_k": 4, "est_employment_wan": 500
})
entries.append({
    "code": "4-05-06", "name": "调酒师和茶艺师", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "从事鸡尾酒调制或茶叶冲泡表演服务，为顾客提供专业的酒水饮品或茶文化体验服务。",
    "typical_tasks": ["根据配方调制各类鸡尾酒和特饮", "按照茶艺流程冲泡各类名茶并进行茶艺表演", "管理吧台酒水和茶叶原料库存", "向顾客推荐酒品或茶品并讲解品鉴知识", "保持吧台和茶台清洁并维护器具"],
    "education": "高中/中专", "salary_median_k": 5, "est_employment_wan": 30
})

# 4-06 信息传输和软件服务人员
mid = "信息传输和软件服务人员"
entries.append({
    "code": "4-06-01", "name": "呼叫中心服务人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "通过电话或在线渠道为客户提供业务咨询、问题解答、投诉受理及回访等呼叫中心客服工作。",
    "typical_tasks": ["接听客户来电解答业务咨询和使用问题", "受理客户投诉并记录工单转交处理", "按照话术脚本进行产品推荐和电话营销", "回访客户满意度并收集服务改进意见", "录入客户信息和通话记录至CRM系统"],
    "education": "大专", "salary_median_k": 5, "est_employment_wan": 100
})
entries.append({
    "code": "4-06-02", "name": "互联网营销师", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "利用互联网平台从事直播带货、短视频营销、社交媒体推广等新媒体营销工作。",
    "typical_tasks": ["策划和拍摄短视频内容进行产品推广", "开展直播带货介绍商品并促成成交", "运营微信微博抖音等社交媒体账号", "分析平台流量数据优化内容投放策略", "维护粉丝社群互动提升用户黏性和转化"],
    "education": "本科", "salary_median_k": 8, "est_employment_wan": 80
})
entries.append({
    "code": "4-06-03", "name": "用户运营和产品运营人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "负责互联网产品的用户增长、活跃度提升和留存管理，通过数据分析和运营策略提升产品价值。",
    "typical_tasks": ["制定用户增长策略并执行拉新活动", "分析用户行为数据绘制用户画像", "设计用户激励体系提升活跃度和留存率", "策划产品功能上线的运营推广方案", "收集用户反馈并撰写需求分析提交产品团队"],
    "education": "本科", "salary_median_k": 10, "est_employment_wan": 60
})

# 4-07 金融服务人员
mid = "金融服务人员"
entries.append({
    "code": "4-07-01", "name": "银行柜员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "在银行营业网点柜台从事存取款、转账汇款、账户开销户等银行柜面业务办理工作。",
    "typical_tasks": ["办理客户存取款和转账汇款业务", "开立和销户个人及对公银行账户", "兑换外币和办理银行承兑汇票业务", "清点核对现金和有价证券并轧账", "向客户推介银行理财和信用卡产品"],
    "education": "本科", "salary_median_k": 8, "est_employment_wan": 150
})
entries.append({
    "code": "4-07-02", "name": "证券服务人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "在证券公司从事证券经纪、投资顾问、证券承销等证券业务服务工作。",
    "typical_tasks": ["为客户办理证券账户开户和交易委托", "提供股票基金等证券投资咨询建议", "撰写行业和个股研究分析报告", "开发和维护证券客户拓展业务规模", "协助企业发行股票债券等证券承销工作"],
    "education": "本科", "salary_median_k": 12, "est_employment_wan": 40
})
entries.append({
    "code": "4-07-03", "name": "保险服务人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "从事保险产品销售、核保承保、理赔服务及客户维护等保险业务服务工作。",
    "typical_tasks": ["向客户介绍保险产品并制定投保方案", "收集投保资料进行核保审核和出单", "受理保险报案并协助客户准备理赔材料", "定期回访保单客户进行续保服务", "组织保险产品说明会开发新客户"],
    "education": "大专", "salary_median_k": 7, "est_employment_wan": 200
})
entries.append({
    "code": "4-07-04", "name": "信贷审核人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "负责贷款申请的调查审核，评估借款人信用状况和还款能力，控制信贷风险。",
    "typical_tasks": ["审核贷款申请材料核实借款人身份和收入", "查询征信记录评估借款人信用等级", "实地调查抵押物价值和贷款用途真实性", "撰写信贷调查报告并提出审批建议", "监控贷后还款情况并预警不良贷款风险"],
    "education": "本科", "salary_median_k": 10, "est_employment_wan": 50
})
entries.append({
    "code": "4-07-05", "name": "基金销售人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "从事公募基金和私募基金等基金产品的销售推介、客户服务及持续营销等基金销售服务工作。",
    "typical_tasks": ["根据客户风险偏好推荐合适的基金产品", "讲解基金产品策略收益和风险特征", "协助客户办理基金申购赎回和转换业务", "跟踪基金净值表现并定期向客户汇报", "举办基金投资策略宣讲会拓展客户"],
    "education": "本科", "salary_median_k": 10, "est_employment_wan": 20
})
entries.append({
    "code": "4-07-06", "name": "理财顾问", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "为客户提供个人或家庭财富管理规划，根据客户资产状况和理财目标制定综合理财方案。",
    "typical_tasks": ["评估客户资产状况和风险承受能力", "制定个性化资产配置和理财规划方案", "推荐银行理财保险基金等金融产品组合", "定期复盘客户资产表现并调整配置", "维护高净值客户关系并提供专属理财服务"],
    "education": "本科", "salary_median_k": 12, "est_employment_wan": 40
})

# 4-08 房地产服务人员
mid = "房地产服务人员"
entries.append({
    "code": "4-08-01", "name": "房地产经纪人", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "从事房屋买卖和租赁的居间代理服务，为客户提供房源推荐、带看、谈判和交易撮合等经纪服务。",
    "typical_tasks": ["开发房源和客源信息并录入管理系统", "带领客户实地看房并介绍房屋情况", "协调买卖双方价格谈判促成成交", "协助办理房产过户贷款等交易手续", "维护老客户关系获取转介绍资源"],
    "education": "大专", "salary_median_k": 8, "est_employment_wan": 150
})
entries.append({
    "code": "4-08-02", "name": "物业管理人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "负责住宅小区或商业楼宇的物业管理服务，包括设施维护、安保保洁、绿化管理及业主服务等工作。",
    "typical_tasks": ["处理业主报修并协调维修人员上门服务", "管理小区安保巡逻和门禁系统", "监督保洁绿化等外包服务质量", "收缴物业管理费并编制费用收支报表", "组织业主大会和社区文化活动"],
    "education": "大专", "salary_median_k": 5, "est_employment_wan": 500
})
entries.append({
    "code": "4-08-03", "name": "房地产估价师", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "对各类房地产进行专业价值评估，出具估价报告，为交易、抵押、征收等提供价值参考依据。",
    "typical_tasks": ["实地勘察房产位置面积和建筑状况", "收集分析房地产市场交易数据和可比案例", "运用估价方法计算房产市场价值", "撰写房地产估价报告并审核出具", "为法院拍卖和银行抵押提供专业估价意见"],
    "education": "本科", "salary_median_k": 12, "est_employment_wan": 10
})

# 4-09 租赁和商务服务人员
mid = "租赁和商务服务人员"
entries.append({
    "code": "4-09-01", "name": "广告服务人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "从事广告创意策划、设计制作、媒体投放及效果评估等广告服务工作。",
    "typical_tasks": ["与客户沟通需求并制定广告创意方案", "撰写广告文案并配合设计制作广告素材", "选择投放渠道制定媒体计划和预算分配", "监测广告投放效果并优化投放策略", "维护客户关系并拓展新广告业务"],
    "education": "本科", "salary_median_k": 9, "est_employment_wan": 50
})
entries.append({
    "code": "4-09-02", "name": "会展服务人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "从事展览会议的策划组织、场地布置、参展商服务及现场运营管理等会展服务工作。",
    "typical_tasks": ["策划展览和会议方案并编制预算", "联系布展搭建商并现场监督展位搭建", "招展招商联系参展企业并办理参展手续", "现场协调安保保洁等后勤保障工作", "统计参展参会数据并撰写活动总结报告"],
    "education": "大专", "salary_median_k": 7, "est_employment_wan": 20
})
entries.append({
    "code": "4-09-03", "name": "市场调查员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "从事市场信息收集、问卷调查、数据统计和分析报告撰写等市场调研工作。",
    "typical_tasks": ["设计调查问卷并制定抽样调查方案", "通过访谈电话网络等方式收集市场数据", "整理录入调查数据并进行统计分析", "撰写市场调研分析报告并提出建议", "监控竞争对手动态和行业发展趋势"],
    "education": "本科", "salary_median_k": 8, "est_employment_wan": 15
})
entries.append({
    "code": "4-09-04", "name": "管理咨询人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "为企业提供战略规划、组织管理、运营优化等专业管理咨询服务，帮助客户提升管理水平和经营效益。",
    "typical_tasks": ["调研诊断企业管理现状和核心问题", "收集分析行业数据和标杆企业最佳实践", "设计战略规划或管理优化方案并编制报告", "向客户高层汇报方案并推动落地实施", "跟踪咨询项目实施效果并提供后续指导"],
    "education": "本科", "salary_median_k": 15, "est_employment_wan": 25
})
entries.append({
    "code": "4-09-05", "name": "旅行社服务人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "在旅行社从事旅游线路设计、产品销售、团队组织和出行安排等旅行社业务工作。",
    "typical_tasks": ["设计旅游线路并核算报价制定产品方案", "接待客户咨询并推荐合适的旅游产品", "预订机票酒店景点门票等旅游资源", "办理游客出境签证和旅游保险手续", "协调处理旅途中突发问题和游客投诉"],
    "education": "大专", "salary_median_k": 6, "est_employment_wan": 30
})
entries.append({
    "code": "4-09-06", "name": "导游", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "带领旅游团队游览景区景点，为游客提供讲解服务、行程安排和旅途照顾等导游服务工作。",
    "typical_tasks": ["按照行程计划带领游客游览景区景点", "讲解景点历史文化和风土人情", "协调安排游客用餐住宿和交通", "处理游客旅途中的突发事件和求助", "提醒游客注意安全和遵守景区规定"],
    "education": "大专", "salary_median_k": 5, "est_employment_wan": 40
})

# 4-10 居民生活服务人员
mid = "居民生活服务人员"
entries.append({
    "code": "4-10-01", "name": "家政服务人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "为家庭提供日常保洁、洗涤、烹饪、采购等家务劳动服务，协助家庭维持良好生活环境。",
    "typical_tasks": ["清扫擦拭家庭各房间卫生", "清洗熨烫衣物被褥等家庭织物", "买菜烧饭准备家庭日常餐食", "整理收纳家庭物品保持居室整洁", "照看家中老人或儿童的日常起居"],
    "education": "初中及以下", "salary_median_k": 5, "est_employment_wan": 600
})
entries.append({
    "code": "4-10-02", "name": "月嫂和育婴师", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "为产妇和新生儿提供专业护理服务，包括产后恢复指导、婴幼儿喂养照料和早期智力开发等工作。",
    "typical_tasks": ["护理新生儿洗澡抚触脐带消毒和黄疸观察", "指导产妇母乳喂养和产后恢复", "制作月子营养餐并安排产妇饮食", "观察婴幼儿生长发育并进行早教互动", "记录婴儿每日哺乳睡眠排便等生活日志"],
    "education": "高中/中专", "salary_median_k": 8, "est_employment_wan": 100
})
entries.append({
    "code": "4-10-03", "name": "养老护理员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "在养老机构或居家环境中为老年人提供生活照料、基础护理和精神慰藉等养老护理服务。",
    "typical_tasks": ["协助老人穿衣洗漱进食等日常生活照料", "为卧床老人翻身擦洗预防褥疮", "监测老人血压血糖等基本健康指标", "陪伴老人聊天散步进行心理疏导", "协助老人进行康复锻炼和功能训练"],
    "education": "初中及以下", "salary_median_k": 4, "est_employment_wan": 200
})
entries.append({
    "code": "4-10-04", "name": "美容师", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "运用美容护肤技术为顾客提供面部和身体护理、皮肤管理及美容仪器操作等美容服务。",
    "typical_tasks": ["分析顾客肤质并制定护理方案", "为顾客进行面部清洁补水和按摩护理", "操作美容仪器进行光子嫩肤等项目", "为顾客进行身体SPA和经络按摩", "推荐适合顾客的护肤品和美容项目套餐"],
    "education": "高中/中专", "salary_median_k": 6, "est_employment_wan": 100
})
entries.append({
    "code": "4-10-05", "name": "美发师", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "运用理发剪发、烫发染发等技术为顾客设计和制作发型，提供头发护理等美发服务。",
    "typical_tasks": ["与顾客沟通需求并设计合适发型", "使用剪刀推子等工具为顾客剪发造型", "为顾客进行烫发和染发操作", "洗头并进行头皮按摩和头发护理", "关注流行趋势学习新的美发技术和造型"],
    "education": "高中/中专", "salary_median_k": 6, "est_employment_wan": 150
})
entries.append({
    "code": "4-10-06", "name": "婚庆服务人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "从事婚礼策划、现场布置、婚礼主持及跟妆等婚庆服务工作，为新人提供一站式婚礼服务。",
    "typical_tasks": ["与新人沟通需求制定婚礼策划方案", "设计婚礼主题布置婚礼现场和签到区", "主持婚礼仪式引导婚礼流程进行", "协调摄影摄像化妆等团队配合工作", "处理婚礼现场突发状况确保流程顺畅"],
    "education": "大专", "salary_median_k": 6, "est_employment_wan": 15
})
entries.append({
    "code": "4-10-07", "name": "摄影服务人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "从事人像摄影、商业摄影、活动摄影等摄影拍摄和后期修图工作，为客户提供专业摄影服务。",
    "typical_tasks": ["根据拍摄需求选择场景布置灯光", "操作相机拍摄人像婚纱商业等题材照片", "引导被拍摄者姿态表情获取最佳效果", "使用修图软件进行照片后期调色精修", "管理影像文件并制作相册和电子相册"],
    "education": "大专", "salary_median_k": 7, "est_employment_wan": 30
})
entries.append({
    "code": "4-10-08", "name": "洗染服务人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "从事衣物织物的干洗水洗、去渍、熨烫和染色修补等洗染服务工作。",
    "typical_tasks": ["检查衣物材质和污渍类型确定洗涤方式", "操作干洗机和水洗机清洗各类衣物", "对顽固污渍进行专业去渍处理", "熨烫整形衣物并分类包装上架", "提供皮具奢侈品养护和衣物修补服务"],
    "education": "高中/中专", "salary_median_k": 4, "est_employment_wan": 20
})

# 4-11 电力、燃气及水供应服务人员
mid = "电力、燃气及水供应服务人员"
entries.append({
    "code": "4-11-01", "name": "供电服务人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "从事电力营业、用电检查、电费抄核收及供电客户服务等供电营销服务工作。",
    "typical_tasks": ["办理居民和企业用电报装和变更手续", "抄录电表读数并核算电费账单", "对用户用电设备和计量装置进行检查", "处理用电故障报修和客户投诉", "开展安全用电和节约用电宣传"],
    "education": "本科", "salary_median_k": 8, "est_employment_wan": 60
})
entries.append({
    "code": "4-11-02", "name": "燃气服务人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "从事城市燃气管网运行维护、用户安检、抄表收费及燃气安全管理等燃气供应服务工作。",
    "typical_tasks": ["入户安检检查燃气管道和灶具安全状况", "抄录燃气表读数并核算燃气费用", "处理燃气泄漏报警并实施应急抢修", "安装调试燃气表具和安全阀门", "宣传安全用气知识并指导用户规范用气"],
    "education": "大专", "salary_median_k": 6, "est_employment_wan": 30
})
entries.append({
    "code": "4-11-03", "name": "供水服务人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "从事城市供水管网运行维护、水质监测、抄表收费及供水客户服务等供水服务工作。",
    "typical_tasks": ["巡检供水管网排查跑冒滴漏隐患", "抄录水表读数并核算水费", "处理用户报修并组织抢修爆管故障", "检测管网水质确保供水水质达标", "办理用水开户和水表安装变更手续"],
    "education": "大专", "salary_median_k": 5, "est_employment_wan": 25
})
entries.append({
    "code": "4-11-04", "name": "供热服务人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "从事城市集中供热系统的运行维护、用户报修、抄表收费及供热客户服务等供热服务工作。",
    "typical_tasks": ["监控供热管网运行参数调节供热温度", "处理用户报修排查暖气不热等故障", "在采暖季前进行供热设备检修和管网试压", "抄录热量表读数并核算采暖费用", "办理用热开户停热和面积变更手续"],
    "education": "大专", "salary_median_k": 5, "est_employment_wan": 20
})

# 4-12 修理服务人员
mid = "修理服务人员"
entries.append({
    "code": "4-12-01", "name": "汽车维修人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "从事汽车故障诊断、机械维修、电气维修和保养服务等汽车维修工作。",
    "typical_tasks": ["使用诊断仪读取故障码判断汽车故障原因", "拆装更换发动机变速箱等机械部件", "检修汽车电路和电子控制系统故障", "进行汽车常规保养更换机油滤芯刹车片等", "进行四轮定位和动平衡等底盘调整作业"],
    "education": "高中/中专", "salary_median_k": 6, "est_employment_wan": 300
})
entries.append({
    "code": "4-12-02", "name": "电器维修人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "从事冰箱空调洗衣机等家用电器的故障检修、维护保养和安装调试等电器维修服务工作。",
    "typical_tasks": ["上门检查诊断家用电器故障原因", "拆解维修和更换电器损坏部件", "安装调试空调冰箱等大型家用电器", "清洗保养空调油烟机等电器设备", "向用户讲解电器使用注意事项和保养方法"],
    "education": "高中/中专", "salary_median_k": 5, "est_employment_wan": 50
})
entries.append({
    "code": "4-12-03", "name": "计算机和手机维修人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "从事计算机和智能手机的硬件维修、软件故障排除、数据恢复及系统维护等维修服务工作。",
    "typical_tasks": ["检测电脑硬件故障并更换损坏部件", "安装调试操作系统和应用软件", "维修手机屏幕主板和电池等硬件", "恢复误删或损坏的重要数据和文件", "清理系统病毒和优化设备运行速度"],
    "education": "大专", "salary_median_k": 6, "est_employment_wan": 40
})
entries.append({
    "code": "4-12-04", "name": "管道和设备维修人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "从事建筑给排水管道、暖通设备及各类工业设备的安装维修和日常维护保养工作。",
    "typical_tasks": ["安装和维修建筑给排水管道和洁具", "疏通堵塞的下水管道和马桶", "检修暖通空调设备和中央新风系统", "维修和保养工业生产设备和传动装置", "更换阀门密封件等管道配件处理跑冒滴漏"],
    "education": "高中/中专", "salary_median_k": 6, "est_employment_wan": 60
})
entries.append({
    "code": "4-12-05", "name": "自行车和电动车维修人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "从事自行车、电动自行车的维修保养、配件更换和故障排除等维修服务工作。",
    "typical_tasks": ["修补更换自行车和电动车轮胎内外胎", "调整刹车系统和变速器确保安全骑行", "检修电动车电机控制器和线路故障", "更换电动车电池并检测电池性能", "维修车架车圈等结构部件和照明系统"],
    "education": "初中及以下", "salary_median_k": 4, "est_employment_wan": 30
})

# 4-13 文化、体育和娱乐服务人员
mid = "文化、体育和娱乐服务人员"
entries.append({
    "code": "4-13-01", "name": "健身和体育指导人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "在健身场馆或体育机构从事健身指导、运动教学和体能训练等体育服务工作。",
    "typical_tasks": ["评估会员体能状况制定个性化健身计划", "指导会员正确使用器械进行力量训练", "带领团体课程如瑜伽操课搏击等", "监督训练过程纠正动作预防运动损伤", "定期测评会员训练效果并调整训练方案"],
    "education": "大专", "salary_median_k": 7, "est_employment_wan": 60
})
entries.append({
    "code": "4-13-02", "name": "娱乐场所服务人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "在KTV、游乐场、棋牌室等娱乐场所从事接待服务、设备操作和场所管理等服务工作。",
    "typical_tasks": ["接待顾客办理入场手续并引导就座", "操作维护KTV点歌系统和音响设备", "管理游乐设施运行并确保顾客安全", "提供酒水餐饮等消费服务", "维护场所秩序和环境卫生"],
    "education": "高中/中专", "salary_median_k": 5, "est_employment_wan": 80
})
entries.append({
    "code": "4-13-03", "name": "旅游景区服务人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "在旅游景区从事售检票、游客接待、秩序维护和景区讲解等景区服务工作。",
    "typical_tasks": ["售卖和检验景区门票办理优惠票验证", "为游客提供景区游览路线咨询", "巡查景区设施安全并维护游览秩序", "提供景区讲解和导览服务", "处理游客投诉和突发事件"],
    "education": "高中/中专", "salary_median_k": 4, "est_employment_wan": 50
})
entries.append({
    "code": "4-13-04", "name": "电子竞技运营人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "从事电子竞技赛事组织、战队管理、内容制作和电竞场馆运营等电子竞技产业服务工作。",
    "typical_tasks": ["策划组织电子竞技赛事并制定赛程规则", "运营电竞战队管理选手训练和参赛", "制作电竞赛事直播内容和解说", "管理电竞场馆设备和日常运营", "开发电竞品牌合作和商业赞助资源"],
    "education": "本科", "salary_median_k": 8, "est_employment_wan": 10
})
entries.append({
    "code": "4-13-05", "name": "图书馆和博物馆服务人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "在图书馆或博物馆从事藏品管理、读者服务、展览布展和文化活动组织等公共文化服务工作。",
    "typical_tasks": ["办理图书借阅归还和读者证件管理", "整理上架图书和维护馆藏秩序", "布置博物馆展览并担任展品讲解", "组织读书会讲座等文化推广活动", "管理数字资源平台并提供在线服务"],
    "education": "大专", "salary_median_k": 5, "est_employment_wan": 15
})
entries.append({
    "code": "4-13-06", "name": "彩票销售人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "在彩票销售网点从事彩票销售、兑奖服务和彩票终端机操作等彩票零售服务工作。",
    "typical_tasks": ["操作彩票终端机出票销售各类彩票", "为中奖者办理小额兑奖手续", "向彩民介绍彩票玩法和购买规则", "核对每日销售数据并上缴彩票销售款", "维护彩票终端设备正常运行和店面整洁"],
    "education": "高中/中专", "salary_median_k": 4, "est_employment_wan": 30
})

# 4-14 健康服务人员
mid = "健康服务人员"
entries.append({
    "code": "4-14-01", "name": "健康管理师", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "对个人或群体的健康状况进行采集、评估和干预，提供健康咨询指导和慢性病管理等健康管理服务。",
    "typical_tasks": ["采集个人健康信息建立健康档案", "进行健康风险评估并识别危险因素", "制定个性化健康干预方案和生活方式建议", "跟踪管理慢性病患者的健康指标", "组织健康讲座和健康促进活动"],
    "education": "本科", "salary_median_k": 8, "est_employment_wan": 30
})
entries.append({
    "code": "4-14-02", "name": "营养师", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "运用营养学知识为个人或机构提供膳食指导、营养评估和饮食方案设计等营养服务工作。",
    "typical_tasks": ["评估个人营养状况和膳食结构", "制定个性化营养食谱和饮食调理方案", "为学校医院等机构设计集体营养配餐", "开展营养知识科普宣传和健康教育", "指导特殊人群如孕妇糖尿病患者的饮食管理"],
    "education": "本科", "salary_median_k": 8, "est_employment_wan": 15
})
entries.append({
    "code": "4-14-03", "name": "心理咨询师", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "运用心理学理论和方法为来访者提供心理评估、心理咨询和心理危机干预等心理健康服务。",
    "typical_tasks": ["与来访者进行初始访谈评估心理状态", "运用认知行为等方法进行心理咨询", "对焦虑抑郁等情绪问题进行疏导干预", "进行心理测验并撰写评估报告", "参与心理危机热线接听和危机干预"],
    "education": "本科", "salary_median_k": 10, "est_employment_wan": 20
})
entries.append({
    "code": "4-14-04", "name": "康复治疗人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "为骨科、神经科等患者提供物理治疗、作业治疗和言语治疗等康复训练服务。",
    "typical_tasks": ["评估患者运动功能和日常生活能力", "实施物理治疗如电疗超声波和手法治疗", "指导患者进行关节活动和肌力训练", "为脑卒中患者开展言语和吞咽功能训练", "制作和调整矫形支具辅助康复"],
    "education": "大专", "salary_median_k": 7, "est_employment_wan": 25
})
entries.append({
    "code": "4-14-05", "name": "中医理疗人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "运用推拿按摩、针灸艾灸、拔罐刮痧等中医传统疗法为客户提供理疗保健服务。",
    "typical_tasks": ["运用推拿手法为客户缓解颈肩腰腿疼痛", "根据经络穴位进行针灸和艾灸治疗", "为客户进行拔罐刮痧等传统理疗操作", "评估客户体质辨证制定调理方案", "指导客户日常养生保健和功法锻炼"],
    "education": "大专", "salary_median_k": 6, "est_employment_wan": 30
})

# 4-15 社会服务和公共管理人员
mid = "社会服务和公共管理人员"
entries.append({
    "code": "4-15-01", "name": "社会工作者", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "运用社会工作专业方法为困难群体提供心理疏导、资源链接、权益维护和社区发展等社会服务。",
    "typical_tasks": ["接待服务对象评估其需求并制定服务计划", "为困境儿童和留守老人提供关爱帮扶", "链接社会资源为服务对象对接救助政策", "组织社区互助活动促进社区融合发展", "记录个案工作过程并撰写服务评估报告"],
    "education": "本科", "salary_median_k": 7, "est_employment_wan": 80
})
entries.append({
    "code": "4-15-02", "name": "社区服务人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "在城乡社区从事居民服务、社区治理、活动组织和便民事务办理等基层社区服务工作。",
    "typical_tasks": ["接待社区居民办理各类证明和申请", "入户走访了解居民需求和困难情况", "组织社区文体活动和志愿服务", "协调处理邻里纠纷和社区事务", "落实上级政策和通知在社区的宣传执行"],
    "education": "大专", "salary_median_k": 5, "est_employment_wan": 100
})
entries.append({
    "code": "4-15-03", "name": "养老服务管理人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "在养老机构或社区养老服务中心从事养老服务规划、运营管理和质量监督等管理工作。",
    "typical_tasks": ["制定养老服务标准和机构运营管理制度", "评估入住老人护理等级并安排服务方案", "管理护理员团队的排班培训和考核", "监督养老服务质量并处理家属投诉", "对接政府购买服务项目并申报补贴"],
    "education": "大专", "salary_median_k": 6, "est_employment_wan": 30
})
entries.append({
    "code": "4-15-04", "name": "儿童福利服务人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "在儿童福利机构或未成年人保护中心从事孤残儿童养育、困境儿童帮扶和未成年人保护等服务工作。",
    "typical_tasks": ["照料福利机构内孤残儿童的日常生活", "评估困境儿童家庭状况并制定帮扶方案", "组织儿童开展教育和康复训练活动", "办理孤儿收养手续并进行收养后跟踪", "受理未成年人遭受侵害的举报并协调保护"],
    "education": "本科", "salary_median_k": 6, "est_employment_wan": 10
})
entries.append({
    "code": "4-15-05", "name": "殡葬服务人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "在殡仪馆或公墓从事遗体接运、整容化妆、火化、骨灰寄存及丧事礼仪服务等殡葬服务工作。",
    "typical_tasks": ["接运遗体并办理火化相关手续", "为逝者进行遗体整容化妆和穿衣", "操作火化设备进行遗体火化作业", "主持告别仪式和丧事礼仪活动", "管理骨灰寄存和公墓安葬服务"],
    "education": "高中/中专", "salary_median_k": 5, "est_employment_wan": 8
})

# 4-16 环境卫生服务人员
mid = "环境卫生服务人员"
entries.append({
    "code": "4-16-01", "name": "环卫工人", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "从事城市道路清扫保洁、垃圾收集运输及公共场所环境卫生维护等环卫保洁工作。",
    "typical_tasks": ["清扫城市道路和人行道上的垃圾杂物", "收集路边垃圾桶内的垃圾并装车运输", "清洗公共设施和道路护栏果皮箱等", "冬季除雪除冰保障道路通行安全", "维护责任区域全天候环境卫生整洁"],
    "education": "初中及以下", "salary_median_k": 3, "est_employment_wan": 350
})
entries.append({
    "code": "4-16-02", "name": "垃圾分类和处理人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "从事生活垃圾分类指导、垃圾分拣处理和再生资源回收等垃圾分类处理工作。",
    "typical_tasks": ["在垃圾投放点指导居民正确分类投放", "对混合垃圾进行二次分拣归类", "操作垃圾压缩和转运设备", "分拣可回收物并进行初步加工处理", "宣传垃圾分类知识和环保理念"],
    "education": "初中及以下", "salary_median_k": 4, "est_employment_wan": 50
})
entries.append({
    "code": "4-16-03", "name": "城市绿化养护人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "从事城市公园绿地、道路绿化带的树木花卉种植养护和园林景观维护等绿化养护工作。",
    "typical_tasks": ["修剪行道树和绿篱造型保持景观效果", "浇水施肥养护公园绿地和花坛花卉", "种植和移栽各类绿化苗木", "防治园林植物病虫害喷洒药物", "维护园林设施和绿地灌溉系统"],
    "education": "高中/中专", "salary_median_k": 4, "est_employment_wan": 60
})

# 4-17 教育培训服务人员
mid = "教育培训服务人员"
entries.append({
    "code": "4-17-01", "name": "职业培训师", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "为企业和机构提供职业技能培训、管理培训和职业素养培训等专业培训授课服务。",
    "typical_tasks": ["调研培训需求并设计培训课程体系", "开发培训课件和案例教学材料", "讲授管理技能和专业技术培训课程", "组织学员进行实操演练和情景模拟", "评估培训效果并编写培训总结报告"],
    "education": "本科", "salary_median_k": 10, "est_employment_wan": 50
})
entries.append({
    "code": "4-17-02", "name": "驾校教练", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "在驾校从事机动车驾驶技术教学，指导学员进行场地和道路驾驶训练并辅助学员通过考试。",
    "typical_tasks": ["讲解道路交通安全法规和驾驶理论知识", "指导学员进行倒车入库侧方停车等科目二训练", "带领学员进行道路驾驶和模拟考试训练", "纠正学员不良驾驶习惯确保训练安全", "维护教练车辆并保持车况良好"],
    "education": "高中/中专", "salary_median_k": 6, "est_employment_wan": 80
})
entries.append({
    "code": "4-17-03", "name": "艺术培训教师", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "在培训机构从事音乐、美术、舞蹈等艺术类课程的教学和指导工作。",
    "typical_tasks": ["根据学员水平制定艺术教学计划", "教授钢琴吉他声乐或绘画等专业课程", "指导学员参加艺术等级考试和比赛", "组织学员进行汇报演出和作品展示", "与家长沟通学员学习进度和培养建议"],
    "education": "大专", "salary_median_k": 7, "est_employment_wan": 60
})
entries.append({
    "code": "4-17-04", "name": "在线教育辅导人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "通过在线平台为学员提供课程辅导、学习规划、作业批改和答疑等线上教育服务。",
    "typical_tasks": ["通过直播或录播平台进行在线课程授课", "批改学员提交的在线作业并反馈点评", "在线答疑解惑帮助学员解决学习难点", "制定学员个性化学习计划并跟踪进度", "参与在线课程内容研发和题库建设"],
    "education": "本科", "salary_median_k": 8, "est_employment_wan": 40
})
entries.append({
    "code": "4-17-05", "name": "体育培训教练", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "在体育培训机构从事游泳、篮球、足球等体育项目的教学训练和技能提升指导工作。",
    "typical_tasks": ["制定学员体育技能训练计划和课时安排", "教授游泳篮球足球等运动项目基本技术", "组织学员进行体能训练和专项技战术练习", "带领学员参加比赛并进行赛前指导", "保障训练安全处理运动中突发伤病"],
    "education": "大专", "salary_median_k": 7, "est_employment_wan": 30
})

# 4-18 安保服务人员
mid = "安保服务人员"
entries.append({
    "code": "4-18-01", "name": "保安员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "在机关企事业单位和居民小区从事门卫值守、巡逻防范、安全检查及秩序维护等安保服务工作。",
    "typical_tasks": ["值守门岗对进出人员车辆进行登记查验", "按照规定路线巡逻排查安全隐患", "监控视频巡查并记录可疑情况", "维护停车场秩序引导车辆有序停放", "处理突发治安事件并配合公安机关调查"],
    "education": "初中及以下", "salary_median_k": 4, "est_employment_wan": 500
})
entries.append({
    "code": "4-18-02", "name": "安检人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "在机场车站地铁等公共场所从事人员和行李物品的安全检查，防止危险物品进入公共交通和重要场所。",
    "typical_tasks": ["操作X光安检机检查行李包裹中的违禁品", "使用手持金属探测器对人员进行安全检查", "对可疑物品进行开包检查和手工复检", "引导旅客有序通过安检通道", "发现并扣押违禁危险物品并做好记录"],
    "education": "高中/中专", "salary_median_k": 4, "est_employment_wan": 30
})
entries.append({
    "code": "4-18-03", "name": "消防设施操作员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "从事建筑消防设施的监控、操作、维护保养和检测等消防设施运行管理工作。",
    "typical_tasks": ["值守消防控制室监控火灾自动报警系统", "操作消防水泵防排烟等消防联动设备", "对建筑消防设施进行日常巡检和维护保养", "处理火灾报警信号并启动应急联动", "记录消防设施运行状况并填写巡检日志"],
    "education": "高中/中专", "salary_median_k": 5, "est_employment_wan": 20
})

# 4-19 宠物服务人员
mid = "宠物服务人员"
entries.append({
    "code": "4-19-01", "name": "宠物医师", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "在宠物医院从事宠物疾病诊断、治疗、手术和预防保健等兽医临床服务工作。",
    "typical_tasks": ["对宠物进行问诊触诊和辅助检查诊断疾病", "为宠物实施输液打针和手术等治疗", "开展宠物绝育和骨折修复等外科手术", "为宠物注射疫苗和进行定期驱虫保健", "指导宠物主人进行术后护理和日常喂养"],
    "education": "本科", "salary_median_k": 8, "est_employment_wan": 15
})
entries.append({
    "code": "4-19-02", "name": "宠物美容和寄养服务人员", "major_category": MC4, "major_category_code": 4,
    "mid_category": mid,
    "description": "为宠物提供洗浴美容造型和寄养看护等服务，满足宠物主人的日常护理和托管需求。",
    "typical_tasks": ["为宠物洗澡吹干并进行毛发修剪造型", "清洁宠物耳道修剪指甲和清理泪痕", "管理寄养宠物的饮食喂养和日常活动", "观察寄养宠物健康状况并记录异常", "与宠物主人沟通服务需求和宠物状态"],
    "education": "高中/中专", "salary_median_k": 5, "est_employment_wan": 10
})

# Write JSON output
output_path = "/Users/liuhongjie/software/project/china-ai-jobs/data/batch_2.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(entries, f, ensure_ascii=False, indent=2)

print(f"Generated {len(entries)} entries to {output_path}")

# Count by major category
mc3_count = sum(1 for e in entries if e["major_category_code"] == 3)
mc4_count = sum(1 for e in entries if e["major_category_code"] == 4)
print(f"  大类3 (办事人员和有关人员): {mc3_count} entries")
print(f"  大类4 (社会生产服务和生活服务人员): {mc4_count} entries")

# Validate all entries
for e in entries:
    assert len(e["typical_tasks"]) == 5, f"{e['code']} has {len(e['typical_tasks'])} tasks"
    assert e["education"] in ["初中及以下", "高中/中专", "大专", "本科", "硕士及以上"], f"{e['code']} bad edu"
    assert isinstance(e["salary_median_k"], int), f"{e['code']} salary not int"
    assert isinstance(e["est_employment_wan"], int), f"{e['code']} emp not int"
print("All entries validated successfully.")
