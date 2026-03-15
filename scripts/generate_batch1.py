#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate batch_1.json with occupations for 大类1 and 大类2."""

import json
import os

entries = []

# ═══════════════════════════════════════
# 大类1: 党的机关、国家机关、群众团体和社会组织、企事业单位负责人
# ═══════════════════════════════════════
MC1 = "党的机关、国家机关、群众团体和社会组织、企事业单位负责人"

# 1-01 中国共产党机关负责人
entries.append({"code":"1-01-01","name":"中共中央和省级机关负责人","major_category":MC1,"major_category_code":1,"mid_category":"中国共产党机关负责人","description":"在中共中央和省级党委机关中担任领导职务，负责贯彻执行党的路线方针政策和重大决策部署的负责人。","typical_tasks":["贯彻落实党中央重大决策部署与战略规划","主持召开党委常委会议和全体会议","审议和决定本级党组织重大事项","部署推进全面从严治党和党风廉政建设","协调推动经济社会发展重点工作"],"education":"本科","salary_median_k":18,"est_employment_wan":15})
entries.append({"code":"1-01-02","name":"中共地市级和县级机关负责人","major_category":MC1,"major_category_code":1,"mid_category":"中国共产党机关负责人","description":"在中共地市级和县级党委机关中担任领导职务，负责本地区党务工作和经济社会发展的负责人。","typical_tasks":["组织实施上级党委决策部署和工作要求","研究制定本地区经济社会发展规划","主持召开地方党委会议并部署重点任务","推动基层党组织建设和干部队伍管理","统筹协调本地区维护稳定和民生保障工作"],"education":"本科","salary_median_k":12,"est_employment_wan":60})

# 1-02 国家机关负责人
entries.append({"code":"1-02-01","name":"立法机关负责人","major_category":MC1,"major_category_code":1,"mid_category":"国家机关负责人","description":"在各级人民代表大会及其常务委员会中担任领导职务，负责立法、监督等工作的负责人。","typical_tasks":["组织制定和审议地方性法规与决议","主持人大常委会会议和人大代表大会","监督本级政府和司法机关依法履职","组织开展执法检查和专题询问","联系和服务人大代表，处理代表议案建议"],"education":"本科","salary_median_k":15,"est_employment_wan":8})
entries.append({"code":"1-02-02","name":"行政机关负责人","major_category":MC1,"major_category_code":1,"mid_category":"国家机关负责人","description":"在各级人民政府及其组成部门中担任领导职务，负责行政管理和公共服务等工作的负责人。","typical_tasks":["制定和实施本地区行政管理政策与措施","主持政府常务会议和专题工作会议","统筹协调经济建设和社会事业发展","组织编制和执行财政预算方案","处置突发事件和应急管理工作"],"education":"本科","salary_median_k":15,"est_employment_wan":120})
entries.append({"code":"1-02-03","name":"审判机关负责人","major_category":MC1,"major_category_code":1,"mid_category":"国家机关负责人","description":"在各级人民法院中担任领导职务，负责审判管理和司法行政等工作的负责人。","typical_tasks":["组织部署审判执行工作和司法改革任务","主持审判委员会讨论重大疑难案件","监督和指导各类案件的审理质量与效率","推进司法公开和智慧法院建设","协调处理涉法涉诉信访和维护司法公正"],"education":"本科","salary_median_k":14,"est_employment_wan":15})
entries.append({"code":"1-02-04","name":"检察机关负责人","major_category":MC1,"major_category_code":1,"mid_category":"国家机关负责人","description":"在各级人民检察院中担任领导职务，负责检察工作和法律监督等工作的负责人。","typical_tasks":["组织部署刑事检察和公益诉讼等业务工作","主持检察委员会讨论重大案件和重要事项","推进检察机关司法体制改革","监督和指导检察业务质量与办案规范","组织开展法律监督和社会治理相关工作"],"education":"本科","salary_median_k":14,"est_employment_wan":12})
entries.append({"code":"1-02-05","name":"监察机关负责人","major_category":MC1,"major_category_code":1,"mid_category":"国家机关负责人","description":"在各级监察委员会中担任领导职务，负责国家监察和反腐败等工作的负责人。","typical_tasks":["组织部署反腐败和党风廉政建设工作","审批和指导重大监察案件的调查处置","推动监察体制改革和制度机制建设","统筹协调纪检监察工作和巡视巡察","组织开展廉政教育和警示教育活动"],"education":"本科","salary_median_k":14,"est_employment_wan":8})

# 1-03 民主党派和工商联负责人
entries.append({"code":"1-03-01","name":"民主党派机关负责人","major_category":MC1,"major_category_code":1,"mid_category":"民主党派和工商联负责人","description":"在各民主党派中央和地方组织中担任领导职务，负责参政议政和民主监督等工作的负责人。","typical_tasks":["组织开展参政议政和建言献策工作","主持民主党派各级委员会会议","推动民主党派自身建设和组织发展","参与政治协商和民主监督活动","组织社会服务和调查研究工作"],"education":"本科","salary_median_k":13,"est_employment_wan":3})
entries.append({"code":"1-03-02","name":"工商联机关负责人","major_category":MC1,"major_category_code":1,"mid_category":"民主党派和工商联负责人","description":"在各级工商业联合会中担任领导职务，负责联系服务民营经济和非公有制企业的负责人。","typical_tasks":["联系服务非公有制经济人士和民营企业","组织开展民营经济领域调查研究","推动民营企业参与社会公益事业","反映民营企业诉求和促进政策落实","组织工商联机关日常管理和队伍建设"],"education":"本科","salary_median_k":13,"est_employment_wan":2})

# 1-04 人民团体和群众团体负责人
entries.append({"code":"1-04-01","name":"工会和共青团负责人","major_category":MC1,"major_category_code":1,"mid_category":"人民团体和群众团体负责人","description":"在各级工会和共青团组织中担任领导职务，负责维护职工权益和服务青年发展的负责人。","typical_tasks":["组织开展职工权益维护和集体协商","策划组织青年思想教育和实践活动","推动基层工会和团组织建设","开展劳动竞赛和职工技能培训","参与协调劳动关系和社会治理工作"],"education":"本科","salary_median_k":10,"est_employment_wan":30})
entries.append({"code":"1-04-02","name":"妇联及其他群众团体负责人","major_category":MC1,"major_category_code":1,"mid_category":"人民团体和群众团体负责人","description":"在各级妇联及其他群众团体中担任领导职务，负责维护妇女儿童权益和服务群众的负责人。","typical_tasks":["组织开展妇女权益保护和维权服务","策划实施妇女儿童发展项目和活动","推动基层妇联组织建设和改革","开展家庭文明建设和家庭教育指导","协调推动性别平等和妇女发展政策落实"],"education":"本科","salary_median_k":10,"est_employment_wan":15})

# 1-05 社会组织负责人
entries.append({"code":"1-05-01","name":"社会团体负责人","major_category":MC1,"major_category_code":1,"mid_category":"社会组织负责人","description":"在各类社会团体中担任领导职务，负责组织运营、行业协调和会员服务等工作的负责人。","typical_tasks":["制定社会团体发展规划和年度工作计划","组织召开会员大会和理事会议","推动行业自律和行业标准制定","开展行业调查研究和政策建议","组织会员培训交流和公共服务活动"],"education":"本科","salary_median_k":10,"est_employment_wan":20})
entries.append({"code":"1-05-02","name":"基金会负责人","major_category":MC1,"major_category_code":1,"mid_category":"社会组织负责人","description":"在各类基金会中担任领导职务，负责基金会运营管理、项目开展和资金募集等工作的负责人。","typical_tasks":["制定基金会战略规划和项目方案","组织开展公益慈善项目和社会服务","策划实施资金募集和捐赠管理","监督基金会财务运营和信息公开","推动基金会规范化建设和品牌传播"],"education":"本科","salary_median_k":12,"est_employment_wan":5})
entries.append({"code":"1-05-03","name":"民办非企业单位负责人","major_category":MC1,"major_category_code":1,"mid_category":"社会组织负责人","description":"在民办非企业单位中担任领导职务，负责机构运营管理和社会服务等工作的负责人。","typical_tasks":["制定机构发展规划和管理制度","统筹组织机构日常运营和人员管理","开展社会服务项目和公益活动","编制年度财务预算和工作报告","推动机构合规运营和品牌建设"],"education":"本科","salary_median_k":10,"est_employment_wan":30})

# 1-06 基层群众自治组织负责人
entries.append({"code":"1-06-01","name":"村民委员会负责人","major_category":MC1,"major_category_code":1,"mid_category":"基层群众自治组织负责人","description":"在农村村民委员会中担任主要领导职务，负责村级事务管理和服务群众等工作的负责人。","typical_tasks":["组织召开村民会议和村民代表会议","落实农村各项惠民政策和民生保障","管理村集体资产和财务收支","协调处理邻里纠纷和矛盾调解","推进美丽乡村建设和人居环境整治"],"education":"高中/中专","salary_median_k":4,"est_employment_wan":280})
entries.append({"code":"1-06-02","name":"居民委员会负责人","major_category":MC1,"major_category_code":1,"mid_category":"基层群众自治组织负责人","description":"在城市社区居民委员会中担任主要领导职务，负责社区治理和居民服务等工作的负责人。","typical_tasks":["组织开展社区治理和网格化管理","协调解决居民诉求和矛盾纠纷调解","落实城市管理和社区服务各项政策","组织社区文化活动和志愿服务","管理社区公共设施和环境卫生"],"education":"大专","salary_median_k":5,"est_employment_wan":120})

# 1-07 企业负责人
entries.append({"code":"1-07-01","name":"大中型企业负责人","major_category":MC1,"major_category_code":1,"mid_category":"企业负责人","description":"在大中型企业中担任总经理、董事长等高级管理职务，负责企业经营管理和战略决策的负责人。","typical_tasks":["制定企业发展战略和年度经营计划","主持企业重大经营决策和投资项目审批","统筹企业人力资源、财务和运营管理","推动企业技术创新和市场拓展","对接政府部门和维护重要客户关系"],"education":"本科","salary_median_k":25,"est_employment_wan":80})
entries.append({"code":"1-07-02","name":"小型企业负责人","major_category":MC1,"major_category_code":1,"mid_category":"企业负责人","description":"在小型企业中担任主要管理职务，负责企业日常经营管理和业务发展的负责人。","typical_tasks":["制定企业经营策略和业务发展规划","管理企业日常运营和团队建设","开拓客户资源和维护商业合作关系","控制企业成本和资金流转管理","处理企业合规和风险防控事务"],"education":"本科","salary_median_k":15,"est_employment_wan":350})
entries.append({"code":"1-07-03","name":"微型企业和个体工商户负责人","major_category":MC1,"major_category_code":1,"mid_category":"企业负责人","description":"微型企业和个体工商户的经营者，负责小规模商业经营和日常业务管理的负责人。","typical_tasks":["管理店铺或作坊的日常经营活动","采购原材料和商品并控制库存","开展产品销售和客户服务","办理工商税务等证照和申报手续","管理员工和协调日常生产经营"],"education":"高中/中专","salary_median_k":8,"est_employment_wan":600})
entries.append({"code":"1-07-04","name":"外商和港澳台投资企业负责人","major_category":MC1,"major_category_code":1,"mid_category":"企业负责人","description":"在外商及港澳台投资企业中担任高级管理职务，负责企业在华经营管理和业务拓展的负责人。","typical_tasks":["制定企业在华发展战略和市场布局","管理跨国企业在华日常运营和团队","协调总部与中国区业务沟通和资源配置","确保企业遵守中国法律法规和合规要求","推动企业本土化经营和品牌推广"],"education":"本科","salary_median_k":30,"est_employment_wan":30})

# 1-08 事业单位负责人
entries.append({"code":"1-08-01","name":"教育和科研事业单位负责人","major_category":MC1,"major_category_code":1,"mid_category":"事业单位负责人","description":"在学校、科研院所等教育科研事业单位中担任领导职务，负责教学科研和单位管理的负责人。","typical_tasks":["制定教育科研事业发展规划和工作计划","统筹学科建设和科研项目管理","推动人才引进和师资队伍建设","管理教学质量评估和学术成果评价","协调教育科研经费管理和资源配置"],"education":"本科","salary_median_k":15,"est_employment_wan":50})
entries.append({"code":"1-08-02","name":"卫生和文化事业单位负责人","major_category":MC1,"major_category_code":1,"mid_category":"事业单位负责人","description":"在医院、文化馆等卫生文化事业单位中担任领导职务，负责单位业务开展和运营管理的负责人。","typical_tasks":["制定卫生或文化事业单位发展规划","统筹业务开展和服务质量管理","推动人才培养和专业技术队伍建设","管理单位财务预算和资产运营","协调上级主管部门和社会资源对接"],"education":"本科","salary_median_k":14,"est_employment_wan":40})

# ═══════════════════════════════════════
# 大类2: 专业技术人员
# ═══════════════════════════════════════
MC2 = "专业技术人员"

# 2-01 工程技术人员 (CONFIRMED entries 01-11)
entries.append({"code":"2-01-01","name":"地质勘查工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"工程技术人员","description":"从事地质调查、矿产勘查、水文地质与工程地质勘查等工作的工程技术人员","typical_tasks":["地质勘查方案设计与实施","地质资料采集、整理与编录","矿产资源储量评估与报告编写","地质灾害调查与风险评价","地质数据分析与地质图编绘"],"education":"本科","salary_median_k":10,"est_employment_wan":35})
entries.append({"code":"2-01-02","name":"测绘工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"工程技术人员","description":"从事大地测量、工程测量、摄影测量与遥感、地图制图等工作的工程技术人员","typical_tasks":["控制测量与地形测量作业","遥感影像处理与解译","地理信息数据采集与处理","工程施工放样与变形监测","地图编制与空间数据建库"],"education":"本科","salary_median_k":10,"est_employment_wan":40})
entries.append({"code":"2-01-03","name":"矿山工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"工程技术人员","description":"从事矿山开采设计、施工组织、安全管理及矿山地质环境治理等工作的工程技术人员","typical_tasks":["矿山开采方案设计与优化","采矿工艺选择与施工组织","矿山安全技术管理与隐患排查","矿山地质环境保护与治理方案编制","矿山生产技术指标分析与统计"],"education":"本科","salary_median_k":12,"est_employment_wan":25})
entries.append({"code":"2-01-04","name":"石油天然气工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"工程技术人员","description":"从事石油天然气钻井、采油采气、油气集输及储运等工程技术工作的人员","typical_tasks":["钻井工程设计与施工技术管理","油气藏开发方案编制与实施","采油采气工艺优化与生产管理","油气集输管网设计与运行维护","油气田开发动态分析与调整"],"education":"本科","salary_median_k":15,"est_employment_wan":45})
entries.append({"code":"2-01-05","name":"冶金工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"工程技术人员","description":"从事冶金工艺设计、生产技术管理及金属材料冶炼等工作的工程技术人员","typical_tasks":["冶炼工艺流程设计与优化","冶金生产过程质量控制","冶金设备选型与技术改造","冶金产品性能检测与分析","节能减排技术研究与应用"],"education":"本科","salary_median_k":12,"est_employment_wan":30})
entries.append({"code":"2-01-06","name":"化工工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"工程技术人员","description":"从事化工产品研发、工艺设计、生产技术管理及化工安全等工作的工程技术人员","typical_tasks":["化工产品配方研发与工艺设计","化工生产装置操作规程编制","化工生产过程控制与质量管理","化工安全技术管理与应急预案编制","化工新材料与新技术应用研究"],"education":"本科","salary_median_k":12,"est_employment_wan":60})
entries.append({"code":"2-01-07","name":"机械工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"工程技术人员","description":"从事机械产品设计、制造工艺、设备维护及自动化技术等工作的工程技术人员","typical_tasks":["机械产品结构设计与三维建模","制造工艺规程编制与优化","机械设备安装调试与维护管理","机械加工精度检测与质量控制","自动化生产线规划与改造"],"education":"本科","salary_median_k":12,"est_employment_wan":180})
entries.append({"code":"2-01-08","name":"航空航天工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"工程技术人员","description":"从事飞行器设计、制造、试验及航天器系统研发等工作的工程技术人员","typical_tasks":["飞行器总体方案设计与论证","航空航天结构强度分析与试验","飞行控制系统设计与仿真","航空航天产品制造工艺研究","航天器在轨运行管理与故障分析"],"education":"硕士及以上","salary_median_k":20,"est_employment_wan":30})
entries.append({"code":"2-01-09","name":"电气工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"工程技术人员","description":"从事发电、输配电、电气设备制造及电力系统运行管理等工作的工程技术人员","typical_tasks":["电气系统设计与施工图绘制","电力设备选型、安装与调试","电力系统运行监控与故障诊断","配电网络规划与改造方案设计","电气安全技术管理与标准制定"],"education":"本科","salary_median_k":13,"est_employment_wan":120})
entries.append({"code":"2-01-10","name":"电子工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"工程技术人员","description":"从事电子元器件、电子产品及系统的研发、设计与制造等工作的工程技术人员","typical_tasks":["电路原理图设计与PCB布局","嵌入式系统硬件开发与调试","电子产品可靠性测试与分析","信号处理算法设计与实现","电子制造工艺改进与良率提升"],"education":"本科","salary_median_k":15,"est_employment_wan":150})
entries.append({"code":"2-01-11","name":"通信工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"工程技术人员","description":"从事通信网络规划、通信设备研发、通信系统建设与维护等工作的工程技术人员","typical_tasks":["通信网络规划设计与优化","通信设备安装调试与开通","无线通信基站选址与建设管理","通信协议开发与系统集成测试","网络性能监测与故障排除"],"education":"本科","salary_median_k":15,"est_employment_wan":100})

# 2-01 continued (NEW entries 12-19)
entries.append({"code":"2-01-12","name":"纺织工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"工程技术人员","description":"从事纺织纤维加工、纺纱织造、染整工艺设计及纺织品质量控制等工作的工程技术人员。","typical_tasks":["纺织工艺流程设计与参数优化","纤维原料性能检测与选配方案制定","织物结构设计与打样试织","印染工艺配方研发与色牢度控制","纺织产品质量检验与标准执行"],"education":"本科","salary_median_k":9,"est_employment_wan":40})
entries.append({"code":"2-01-13","name":"食品工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"工程技术人员","description":"从事食品加工工艺研发、生产技术管理、食品质量与安全控制等工作的工程技术人员。","typical_tasks":["食品加工工艺研发与配方优化","食品生产线设计与设备选型","食品安全检测与质量管理体系维护","食品营养成分分析与标签审核","新产品开发试验与中试放大"],"education":"本科","salary_median_k":10,"est_employment_wan":50})
entries.append({"code":"2-01-14","name":"环境保护工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"工程技术人员","description":"从事环境监测、污染治理、环境影响评价及生态修复等工作的工程技术人员。","typical_tasks":["环境影响评价报告编制与审查","废水废气处理工艺设计与调试","环境监测方案制定与数据采集分析","固体废物处理处置方案设计","生态环境修复技术研究与工程实施"],"education":"本科","salary_median_k":11,"est_employment_wan":35})
entries.append({"code":"2-01-15","name":"安全工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"工程技术人员","description":"从事安全生产技术管理、安全评价、职业健康防护及应急救援等工作的工程技术人员。","typical_tasks":["安全生产规章制度编制与执行监督","安全风险评估与隐患排查治理","安全生产应急预案编制与演练组织","职业危害因素检测与防护方案设计","安全生产事故调查分析与整改落实"],"education":"本科","salary_median_k":11,"est_employment_wan":45})
entries.append({"code":"2-01-16","name":"生物工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"工程技术人员","description":"从事生物技术研发、生物制品生产、基因工程及发酵工程等工作的工程技术人员。","typical_tasks":["生物制品研发与工艺路线设计","基因克隆表达与蛋白纯化实验","发酵工艺参数优化与放大生产","生物制品质量检测与工艺验证","生物安全管理与实验室规范运行"],"education":"本科","salary_median_k":14,"est_employment_wan":20})
entries.append({"code":"2-01-17","name":"材料工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"工程技术人员","description":"从事金属、高分子、陶瓷及复合材料的研发、制备工艺设计与性能检测等工作的工程技术人员。","typical_tasks":["新材料配方研发与制备工艺设计","材料力学性能与理化性能测试分析","材料微观结构表征与缺陷分析","材料应用方案设计与工程验证","材料标准制定与质量控制体系建设"],"education":"本科","salary_median_k":13,"est_employment_wan":40})
entries.append({"code":"2-01-18","name":"核工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"工程技术人员","description":"从事核反应堆设计、核燃料加工、辐射防护及核设施运行管理等工作的工程技术人员。","typical_tasks":["核反应堆系统设计与安全分析","核燃料元件制造工艺研究","辐射防护方案设计与剂量监测","核设施运行维护与技术管理","核废物处理处置技术研究与实施"],"education":"本科","salary_median_k":18,"est_employment_wan":8})
entries.append({"code":"2-01-19","name":"水利水电工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"工程技术人员","description":"从事水利水电工程规划、设计、施工及运行管理等工作的工程技术人员。","typical_tasks":["水利水电工程规划与可行性研究","水工建筑物结构设计与计算","水利工程施工组织与技术管理","水电站运行监控与设备维护","水资源调查评价与水文分析预报"],"education":"本科","salary_median_k":11,"est_employment_wan":30})

# 2-02 计算机与应用工程技术人员 (CONFIRMED entries 01-06)
entries.append({"code":"2-02-01","name":"软件工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"计算机与应用工程技术人员","description":"从事计算机软件的研究、设计、开发、测试及维护等工作的工程技术人员","typical_tasks":["软件系统架构设计与技术选型","程序编码、调试与单元测试","需求分析与技术方案编写","代码审查与性能优化","技术文档撰写与维护"],"education":"本科","salary_median_k":18,"est_employment_wan":700})
entries.append({"code":"2-02-02","name":"计算机硬件工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"计算机与应用工程技术人员","description":"从事计算机硬件系统及设备的研究、设计、开发与维护等工作的工程技术人员","typical_tasks":["计算机硬件系统架构设计","芯片选型与电路板设计验证","硬件产品原型制作与测试","服务器与存储设备运维管理","硬件故障诊断与维修"],"education":"本科","salary_median_k":16,"est_employment_wan":80})
entries.append({"code":"2-02-03","name":"计算机网络工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"计算机与应用工程技术人员","description":"从事计算机网络系统的规划、设计、实施、运维及安全管理等工作的工程技术人员","typical_tasks":["网络架构规划与方案设计","网络设备配置、部署与调试","网络安全策略制定与防护实施","网络性能优化与容量规划","网络故障排查与应急处置"],"education":"本科","salary_median_k":15,"est_employment_wan":90})
entries.append({"code":"2-02-04","name":"信息系统分析工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"计算机与应用工程技术人员","description":"从事信息系统需求分析、系统设计、项目管理及信息化规划等工作的工程技术人员","typical_tasks":["业务需求调研与分析建模","信息系统总体方案设计","系统集成方案编制与实施管理","信息化项目可行性研究与评估","企业数字化转型规划与咨询"],"education":"本科","salary_median_k":18,"est_employment_wan":60})
entries.append({"code":"2-02-05","name":"数据分析处理工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"计算机与应用工程技术人员","description":"从事数据采集、清洗、分析、挖掘及可视化等工作的工程技术人员","typical_tasks":["数据采集方案设计与ETL流程开发","数据清洗、转换与质量管理","数据统计分析与挖掘建模","数据可视化报表设计与开发","数据仓库与数据湖架构设计"],"education":"本科","salary_median_k":18,"est_employment_wan":80})
entries.append({"code":"2-02-06","name":"人工智能工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"计算机与应用工程技术人员","description":"从事人工智能算法研究、模型开发、系统设计及应用落地等工作的工程技术人员","typical_tasks":["机器学习与深度学习模型研发","训练数据集构建与标注管理","AI模型训练、调优与部署","自然语言处理与计算机视觉应用开发","AI系统性能评估与迭代优化"],"education":"硕士及以上","salary_median_k":25,"est_employment_wan":40})

# 2-02 continued (NEW entries 07-10)
entries.append({"code":"2-02-07","name":"信息安全工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"计算机与应用工程技术人员","description":"从事信息系统安全防护、漏洞检测、安全审计及应急响应等工作的工程技术人员。","typical_tasks":["信息安全风险评估与等级保护测评","网络安全漏洞扫描与渗透测试","安全事件监控分析与应急响应处置","信息安全管理制度编制与合规审查","安全防护体系设计与安全产品部署"],"education":"本科","salary_median_k":18,"est_employment_wan":30})
entries.append({"code":"2-02-08","name":"区块链工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"计算机与应用工程技术人员","description":"从事区块链底层平台研发、智能合约开发及分布式应用设计等工作的工程技术人员。","typical_tasks":["区块链底层架构设计与共识算法研发","智能合约编写、测试与安全审计","分布式应用DApp开发与部署","区块链网络节点部署与运维管理","区块链应用场景分析与解决方案设计"],"education":"本科","salary_median_k":22,"est_employment_wan":8})
entries.append({"code":"2-02-09","name":"云计算工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"计算机与应用工程技术人员","description":"从事云计算平台架构设计、云服务开发、云资源管理及运维等工作的工程技术人员。","typical_tasks":["云平台架构设计与技术选型","云计算资源编排与自动化部署","容器化应用开发与微服务治理","云平台性能优化与成本管理","云安全策略制定与灾备方案设计"],"education":"本科","salary_median_k":20,"est_employment_wan":25})
entries.append({"code":"2-02-10","name":"数字化解决方案设计师","major_category":MC2,"major_category_code":2,"mid_category":"计算机与应用工程技术人员","description":"从事企业数字化转型方案设计、数字化平台规划及技术架构咨询等工作的工程技术人员。","typical_tasks":["企业数字化现状诊断与需求分析","数字化转型整体解决方案设计","数字化平台技术选型与架构规划","数字化项目实施路径规划与管理","数字化运营效果评估与持续优化"],"education":"本科","salary_median_k":20,"est_employment_wan":15})

# 2-03 建筑工程技术人员 (CONFIRMED entries 01-03)
entries.append({"code":"2-03-01","name":"建筑设计工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"建筑工程技术人员","description":"从事民用与工业建筑设计、规划及建筑方案审查等工作的工程技术人员","typical_tasks":["建筑方案设计与效果图绘制","建筑施工图设计与审核","建筑规范与标准执行审查","绿色建筑与节能设计方案编制","建筑项目设计协调与管理"],"education":"本科","salary_median_k":14,"est_employment_wan":65})
entries.append({"code":"2-03-02","name":"土木工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"建筑工程技术人员","description":"从事道路、桥梁、隧道、房屋等土木工程的设计、施工与管理等工作的工程技术人员","typical_tasks":["土木工程结构设计与计算分析","施工组织设计与技术方案编制","工程质量检测与验收管理","工程造价预算编制与审核","施工现场技术指导与安全管理"],"education":"本科","salary_median_k":12,"est_employment_wan":200})
entries.append({"code":"2-03-03","name":"城市规划工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"建筑工程技术人员","description":"从事城乡规划编制、土地利用规划、城市设计及规划管理等工作的工程技术人员","typical_tasks":["城市总体规划与控制性详细规划编制","城市用地布局分析与优化","城市设计方案编制与评审","规划环境影响评价与论证","城市更新与历史文化保护规划"],"education":"本科","salary_median_k":13,"est_employment_wan":25})

# 2-03 continued (NEW entries 04-06)
entries.append({"code":"2-03-04","name":"建筑装饰工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"建筑工程技术人员","description":"从事建筑内外装饰设计、装饰施工技术管理及装饰材料选配等工作的工程技术人员。","typical_tasks":["建筑装饰方案设计与施工图绘制","装饰材料选型与造价预算编制","装饰工程施工组织与质量控制","装饰工程竣工验收与资料归档","装饰施工现场技术协调与安全管理"],"education":"本科","salary_median_k":10,"est_employment_wan":60})
entries.append({"code":"2-03-05","name":"市政工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"建筑工程技术人员","description":"从事城市道路、桥梁、给排水、燃气等市政基础设施的设计、施工与管理等工作的工程技术人员。","typical_tasks":["市政工程设计方案编制与审查","给排水管网设计与施工技术管理","市政道路与桥梁施工组织与监理","市政工程造价编制与竣工结算","城市地下管线综合规划与管理"],"education":"本科","salary_median_k":11,"est_employment_wan":40})
entries.append({"code":"2-03-06","name":"风景园林工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"建筑工程技术人员","description":"从事风景园林规划设计、园林绿化施工及园林植物养护管理等工作的工程技术人员。","typical_tasks":["风景园林规划方案设计与效果图制作","园林绿化施工组织与质量管理","园林植物配置方案设计与选苗","园林景观工程造价编制与审核","园林养护管理方案制定与实施"],"education":"本科","salary_median_k":10,"est_employment_wan":25})

# 2-04 交通运输工程技术人员
entries.append({"code":"2-04-01","name":"铁路工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"交通运输工程技术人员","description":"从事铁路线路、桥隧、站场等工程的设计、施工及运营维护等工作的工程技术人员。","typical_tasks":["铁路线路设计与线形优化","铁路桥梁隧道结构设计与施工管理","铁路轨道铺设与维护技术管理","铁路信号与通信系统设计调试","铁路工程质量检测与安全评估"],"education":"本科","salary_median_k":12,"est_employment_wan":35})
entries.append({"code":"2-04-02","name":"公路工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"交通运输工程技术人员","description":"从事公路路线设计、路面工程、交通工程及公路养护管理等工作的工程技术人员。","typical_tasks":["公路线路勘测设计与方案比选","路基路面工程施工组织与技术管理","公路桥涵结构设计与施工监控","公路养护技术方案制定与实施","交通安全设施设计与交通组织优化"],"education":"本科","salary_median_k":11,"est_employment_wan":50})
entries.append({"code":"2-04-03","name":"水运工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"交通运输工程技术人员","description":"从事港口、航道、船闸等水运工程的规划设计、施工与运行管理等工作的工程技术人员。","typical_tasks":["港口码头工程设计与施工管理","航道整治与疏浚工程技术管理","水运工程结构计算与安全评估","港口物流设施规划与优化","水运工程环境影响评价与生态保护"],"education":"本科","salary_median_k":12,"est_employment_wan":15})
entries.append({"code":"2-04-04","name":"民航工程技术人员","major_category":MC2,"major_category_code":2,"mid_category":"交通运输工程技术人员","description":"从事民用航空器维修、机场工程建设及空管系统技术保障等工作的工程技术人员。","typical_tasks":["民用航空器维修方案制定与实施","机场跑道和航站楼工程设计管理","空管通信导航监视设备维护保障","航空器适航审定与技术资料管理","机场运行安全评估与技术改造"],"education":"本科","salary_median_k":18,"est_employment_wan":12})

# 2-05 农业技术人员
entries.append({"code":"2-05-01","name":"农艺技术人员","major_category":MC2,"major_category_code":2,"mid_category":"农业技术人员","description":"从事农作物品种选育、栽培技术研究、田间管理及农业技术推广等工作的技术人员。","typical_tasks":["农作物品种试验与适应性评价","栽培技术方案制定与田间试验","农作物病虫害诊断与防治指导","农业生产技术培训与推广服务","农作物生长监测与产量预估"],"education":"本科","salary_median_k":7,"est_employment_wan":60})
entries.append({"code":"2-05-02","name":"园艺技术人员","major_category":MC2,"major_category_code":2,"mid_category":"农业技术人员","description":"从事果树、蔬菜、花卉等园艺作物的育种、栽培管理及技术推广等工作的技术人员。","typical_tasks":["园艺作物品种引进与选育试验","果蔬栽培技术方案设计与指导","设施园艺环境调控与管理","园艺产品采后处理与保鲜技术应用","园艺生产病虫害综合防治方案制定"],"education":"本科","salary_median_k":7,"est_employment_wan":30})
entries.append({"code":"2-05-03","name":"农业推广人员","major_category":MC2,"major_category_code":2,"mid_category":"农业技术人员","description":"从事农业新技术、新品种的试验示范和推广应用，为农民提供技术咨询服务的人员。","typical_tasks":["农业新技术新品种示范推广","农业技术培训与现场指导","农业生产技术咨询与信息服务","农业科技成果转化项目实施","农业生产调查统计与技术总结"],"education":"本科","salary_median_k":6,"est_employment_wan":50})
entries.append({"code":"2-05-04","name":"土壤肥料技术人员","major_category":MC2,"major_category_code":2,"mid_category":"农业技术人员","description":"从事土壤调查分析、肥料研发应用、测土配方施肥等工作的技术人员。","typical_tasks":["土壤采样与理化性质分析检测","测土配方施肥方案制定与推广","肥料产品质量检测与效果评价","土壤改良技术研究与方案实施","耕地质量监测与评价报告编写"],"education":"本科","salary_median_k":7,"est_employment_wan":20})

# 2-06 林业技术人员
entries.append({"code":"2-06-01","name":"营造林技术人员","major_category":MC2,"major_category_code":2,"mid_category":"林业技术人员","description":"从事造林绿化规划设计、林木育种育苗、森林经营管理等工作的技术人员。","typical_tasks":["造林规划设计与作业方案编制","林木种苗培育与良种选育推广","造林施工组织与技术指导","森林抚育经营方案制定与实施","造林成效检查验收与档案管理"],"education":"本科","salary_median_k":6,"est_employment_wan":25})
entries.append({"code":"2-06-02","name":"森林资源保护技术人员","major_category":MC2,"major_category_code":2,"mid_category":"林业技术人员","description":"从事森林资源调查监测、森林防火、林业有害生物防治等工作的技术人员。","typical_tasks":["森林资源调查与动态监测","森林防火预警监控与扑救技术指导","林业有害生物监测预报与防治","林地征占用审核与森林资源管理","森林生态效益评估与保护方案制定"],"education":"本科","salary_median_k":6,"est_employment_wan":15})
entries.append({"code":"2-06-03","name":"野生动植物保护技术人员","major_category":MC2,"major_category_code":2,"mid_category":"林业技术人员","description":"从事野生动植物资源调查、保护区管理及珍稀物种保护繁育等工作的技术人员。","typical_tasks":["野生动植物资源调查与种群监测","自然保护区巡护管理与生态监测","珍稀濒危物种保护与人工繁育","野生动物救护与疫源疫病监测","湿地生态保护与恢复技术实施"],"education":"本科","salary_median_k":7,"est_employment_wan":8})

# 2-07 畜牧兽医技术人员
entries.append({"code":"2-07-01","name":"畜牧技术人员","major_category":MC2,"major_category_code":2,"mid_category":"畜牧兽医技术人员","description":"从事畜禽品种选育、饲养管理技术研究及畜牧生产技术推广等工作的技术人员。","typical_tasks":["畜禽品种选育与繁殖技术指导","畜禽饲养管理方案制定与优化","饲料配方设计与营养评价","畜牧生产技术培训与推广服务","畜禽生产性能测定与数据分析"],"education":"本科","salary_median_k":6,"est_employment_wan":35})
entries.append({"code":"2-07-02","name":"兽医技术人员","major_category":MC2,"major_category_code":2,"mid_category":"畜牧兽医技术人员","description":"从事动物疫病诊断治疗、疫病防控、动物检疫及兽药管理等工作的技术人员。","typical_tasks":["动物疫病临床诊断与治疗","动物疫病监测采样与实验室检测","动物防疫免疫方案制定与实施","动物产品检疫检验与安全监管","重大动物疫情应急处置与流行病学调查"],"education":"本科","salary_median_k":7,"est_employment_wan":25})

# 2-08 水产技术人员
entries.append({"code":"2-08-01","name":"水产养殖技术人员","major_category":MC2,"major_category_code":2,"mid_category":"水产技术人员","description":"从事水产苗种繁育、养殖技术研究、水产病害防治及养殖水质管理等工作的技术人员。","typical_tasks":["水产苗种繁育与良种选育","养殖模式设计与饲养管理技术指导","水产养殖病害诊断与防治","养殖水质监测调控与环境管理","水产饲料配方设计与投喂管理"],"education":"本科","salary_median_k":6,"est_employment_wan":20})
entries.append({"code":"2-08-02","name":"水产资源保护技术人员","major_category":MC2,"major_category_code":2,"mid_category":"水产技术人员","description":"从事渔业资源调查评估、水生生物保护及渔业生态环境监测修复等工作的技术人员。","typical_tasks":["渔业资源调查与种群评估","水生生物多样性监测与保护","增殖放流方案设计与效果评估","渔业水域生态环境监测与修复","渔业资源保护管理与政策建议"],"education":"本科","salary_median_k":7,"est_employment_wan":5})

# 2-09 科学研究人员
entries.append({"code":"2-09-01","name":"自然科学研究人员","major_category":MC2,"major_category_code":2,"mid_category":"科学研究人员","description":"从事数学、物理、化学、生物、天文、地球科学等自然科学基础研究和应用研究的人员。","typical_tasks":["科研课题申请与研究方案设计","实验方案设计与实验数据采集分析","学术论文撰写与学术成果发表","科研项目结题验收与成果鉴定","学术交流合作与研究生培养指导"],"education":"硕士及以上","salary_median_k":15,"est_employment_wan":50})
entries.append({"code":"2-09-02","name":"社会科学研究人员","major_category":MC2,"major_category_code":2,"mid_category":"科学研究人员","description":"从事经济学、法学、社会学、政治学等社会科学领域研究工作的人员。","typical_tasks":["社会科学研究课题设计与立项申请","社会调查方案设计与数据采集","研究报告和学术论文撰写发表","政策咨询建议与决策参考报告编制","学术研讨会组织与学术成果交流"],"education":"硕士及以上","salary_median_k":12,"est_employment_wan":20})
entries.append({"code":"2-09-03","name":"人文科学研究人员","major_category":MC2,"major_category_code":2,"mid_category":"科学研究人员","description":"从事哲学、历史学、文学、语言学等人文科学领域研究工作的人员。","typical_tasks":["人文科学研究课题申报与方案设计","文献资料收集整理与考证分析","学术专著和论文撰写与出版","文化遗产研究与保护方案编制","学术讲座与研究生培养指导"],"education":"硕士及以上","salary_median_k":10,"est_employment_wan":10})

# 2-10 卫生专业技术人员
entries.append({"code":"2-10-01","name":"内科医师","major_category":MC2,"major_category_code":2,"mid_category":"卫生专业技术人员","description":"从事内科疾病的诊断、治疗、预防及健康管理等工作的执业医师。","typical_tasks":["患者病史采集与体格检查","内科疾病诊断与治疗方案制定","医嘱开具与治疗效果跟踪评估","住院患者查房与病情分析讨论","病历书写与医疗文书管理"],"education":"本科","salary_median_k":15,"est_employment_wan":80})
entries.append({"code":"2-10-02","name":"外科医师","major_category":MC2,"major_category_code":2,"mid_category":"卫生专业技术人员","description":"从事外科疾病的诊断和手术治疗，进行术前评估、手术操作及术后管理等工作的执业医师。","typical_tasks":["外科疾病诊断与手术适应症评估","手术方案设计与术前准备","外科手术操作与术中应急处理","术后患者管理与并发症防治","手术病例讨论与手术技术改进"],"education":"本科","salary_median_k":18,"est_employment_wan":50})
entries.append({"code":"2-10-03","name":"妇产科医师","major_category":MC2,"major_category_code":2,"mid_category":"卫生专业技术人员","description":"从事妇科疾病诊治、产前检查、分娩助产及生殖健康管理等工作的执业医师。","typical_tasks":["妇科疾病诊断与治疗方案制定","产前检查与高危妊娠监护管理","分娩接生与产科手术操作","围产期保健指导与产后康复","妇科手术操作与术后管理"],"education":"本科","salary_median_k":16,"est_employment_wan":30})
entries.append({"code":"2-10-04","name":"儿科医师","major_category":MC2,"major_category_code":2,"mid_category":"卫生专业技术人员","description":"从事儿童疾病的诊断治疗、生长发育监测及预防保健等工作的执业医师。","typical_tasks":["儿童常见病和多发病诊断治疗","新生儿疾病筛查与救治","儿童生长发育评估与健康指导","儿童预防接种与保健管理","儿科急危重症抢救与转运"],"education":"本科","salary_median_k":15,"est_employment_wan":25})
entries.append({"code":"2-10-05","name":"口腔科医师","major_category":MC2,"major_category_code":2,"mid_category":"卫生专业技术人员","description":"从事口腔疾病的预防、诊断、治疗及口腔修复等工作的执业医师。","typical_tasks":["口腔疾病检查诊断与治疗方案设计","龋齿充填与牙体牙髓治疗","口腔修复方案设计与义齿制作指导","口腔正畸方案制定与矫治器调整","口腔外科手术与种植牙手术操作"],"education":"本科","salary_median_k":16,"est_employment_wan":25})
entries.append({"code":"2-10-06","name":"中医医师","major_category":MC2,"major_category_code":2,"mid_category":"卫生专业技术人员","description":"运用中医理论和方法从事疾病诊断治疗、中药处方开具及中医养生保健指导等工作的执业医师。","typical_tasks":["中医四诊合参与辨证论治","中药处方开具与用药指导","针灸推拿等中医适宜技术操作","中医养生保健方案制定与指导","中医经典医案整理与临床经验总结"],"education":"本科","salary_median_k":12,"est_employment_wan":60})
entries.append({"code":"2-10-07","name":"影像诊断医师","major_category":MC2,"major_category_code":2,"mid_category":"卫生专业技术人员","description":"从事X线、CT、MRI、超声等医学影像的检查操作和诊断报告出具等工作的执业医师。","typical_tasks":["医学影像检查方案选择与操作","X线、CT和MRI影像阅片与诊断","超声检查操作与报告出具","介入放射学治疗操作与辅助","影像诊断质量控制与疑难病例会诊"],"education":"本科","salary_median_k":14,"est_employment_wan":30})
entries.append({"code":"2-10-08","name":"麻醉科医师","major_category":MC2,"major_category_code":2,"mid_category":"卫生专业技术人员","description":"从事手术麻醉、疼痛治疗、危重症患者生命功能监测与调控等工作的执业医师。","typical_tasks":["术前麻醉评估与麻醉方案制定","全身麻醉和区域麻醉操作实施","术中生命体征监测与麻醉深度调控","术后镇痛管理与麻醉复苏监护","急危重症患者心肺复苏与抢救"],"education":"本科","salary_median_k":18,"est_employment_wan":15})
entries.append({"code":"2-10-09","name":"全科医师","major_category":MC2,"major_category_code":2,"mid_category":"卫生专业技术人员","description":"在基层医疗卫生机构从事全科医疗服务，提供常见病诊治、慢病管理及健康教育等工作的执业医师。","typical_tasks":["社区常见病和多发病诊断治疗","慢性病患者健康管理与随访","居民健康档案建立与维护","健康教育与疾病预防指导","双向转诊与上级医院诊疗协调"],"education":"本科","salary_median_k":10,"est_employment_wan":80})
entries.append({"code":"2-10-10","name":"公共卫生医师","major_category":MC2,"major_category_code":2,"mid_category":"卫生专业技术人员","description":"从事传染病防控、卫生监督、健康教育及突发公共卫生事件应急处置等工作的执业医师。","typical_tasks":["传染病疫情监测与流行病学调查","计划免疫方案制定与预防接种管理","公共卫生应急预案编制与演练","卫生监测数据统计分析与报告","健康危害因素评价与干预措施制定"],"education":"本科","salary_median_k":10,"est_employment_wan":40})
entries.append({"code":"2-10-11","name":"精神科医师","major_category":MC2,"major_category_code":2,"mid_category":"卫生专业技术人员","description":"从事精神疾病和心理障碍的诊断治疗、心理危机干预及精神康复等工作的执业医师。","typical_tasks":["精神疾病临床诊断与鉴别诊断","精神药物治疗方案制定与调整","心理危机干预与自杀风险评估","精神障碍患者康复训练与管理","精神卫生健康教育与社区随访"],"education":"本科","salary_median_k":14,"est_employment_wan":10})
entries.append({"code":"2-10-12","name":"康复医学科医师","major_category":MC2,"major_category_code":2,"mid_category":"卫生专业技术人员","description":"从事伤病患者功能障碍评定、康复治疗方案制定及康复训练指导等工作的执业医师。","typical_tasks":["患者功能障碍评定与康复诊断","康复治疗方案制定与疗效评估","物理治疗与作业治疗技术指导","康复辅助器具适配与使用指导","康复训练计划调整与出院康复指导"],"education":"本科","salary_median_k":12,"est_employment_wan":15})

# 2-11 药学专业技术人员
entries.append({"code":"2-11-01","name":"药师","major_category":MC2,"major_category_code":2,"mid_category":"药学专业技术人员","description":"从事药品调配、药学服务、用药指导及药品质量管理等工作的药学专业技术人员。","typical_tasks":["处方审核与药品调配发放","患者用药咨询与合理用药指导","药品库存管理与效期监控","药物不良反应监测与报告","药品质量检查与药事管理"],"education":"本科","salary_median_k":10,"est_employment_wan":50})
entries.append({"code":"2-11-02","name":"中药师","major_category":MC2,"major_category_code":2,"mid_category":"药学专业技术人员","description":"从事中药鉴定、中药炮制、中药制剂配制及中药调剂等工作的药学专业技术人员。","typical_tasks":["中药饮片鉴别与质量验收","中药处方审核与调剂配发","中药炮制加工与制剂配制","中药材采购验收与仓储养护","中药用药咨询与合理用药指导"],"education":"本科","salary_median_k":9,"est_employment_wan":20})
entries.append({"code":"2-11-03","name":"药物研发人员","major_category":MC2,"major_category_code":2,"mid_category":"药学专业技术人员","description":"从事新药发现、药物合成、药效评价及临床前研究等工作的药学研发人员。","typical_tasks":["药物靶点筛选与先导化合物发现","药物合成路线设计与工艺研究","药物药理毒理学实验与评价","药物制剂处方研究与稳定性考察","新药注册申报资料撰写与审核"],"education":"硕士及以上","salary_median_k":18,"est_employment_wan":15})

# 2-12 护理人员
entries.append({"code":"2-12-01","name":"临床护理人员","major_category":MC2,"major_category_code":2,"mid_category":"护理人员","description":"在医疗卫生机构中从事临床护理、专科护理及危重症护理等工作的专业护理人员。","typical_tasks":["患者基础护理与生活照护","遵医嘱执行治疗操作与用药护理","患者病情观察与护理记录书写","急危重症患者抢救配合与监护","护理健康教育与出院指导"],"education":"大专","salary_median_k":8,"est_employment_wan":350})
entries.append({"code":"2-12-02","name":"社区护理人员","major_category":MC2,"major_category_code":2,"mid_category":"护理人员","description":"在社区卫生服务机构中从事社区护理、健康管理及家庭护理指导等工作的专业护理人员。","typical_tasks":["社区居民健康档案建立与管理","慢性病患者社区护理与随访","家庭护理技术指导与健康教育","社区预防保健与计划免疫护理","居家老年人护理评估与服务"],"education":"大专","salary_median_k":7,"est_employment_wan":50})
entries.append({"code":"2-12-03","name":"老年护理人员","major_category":MC2,"major_category_code":2,"mid_category":"护理人员","description":"在养老机构或居家环境中从事老年人日常护理、康复照护及健康管理等工作的专业护理人员。","typical_tasks":["老年人日常生活照护与安全管理","老年人健康评估与护理计划制定","老年慢性病护理与康复训练指导","老年人心理疏导与精神慰藉","老年人营养膳食指导与用药提醒"],"education":"大专","salary_median_k":6,"est_employment_wan":40})

# 2-13 经济专业人员
entries.append({"code":"2-13-01","name":"经济分析人员","major_category":MC2,"major_category_code":2,"mid_category":"经济专业人员","description":"从事宏观经济分析、行业研究、经济预测及政策评估等工作的专业人员。","typical_tasks":["宏观经济数据采集与统计分析","行业发展趋势研究与报告撰写","经济运行监测与预警预测","经济政策效果评估与建议","区域经济发展规划编制与论证"],"education":"本科","salary_median_k":15,"est_employment_wan":30})
entries.append({"code":"2-13-02","name":"投资分析人员","major_category":MC2,"major_category_code":2,"mid_category":"经济专业人员","description":"从事投资项目评估、投资策略研究、资产配置建议及投资风险分析等工作的专业人员。","typical_tasks":["投资项目可行性分析与估值建模","上市公司财务分析与投资研究","投资组合策略制定与业绩评估","行业投资机会挖掘与风险评估","投资研究报告撰写与路演汇报"],"education":"本科","salary_median_k":20,"est_employment_wan":20})
entries.append({"code":"2-13-03","name":"金融分析师","major_category":MC2,"major_category_code":2,"mid_category":"经济专业人员","description":"从事金融市场分析、金融产品设计、风险管理及量化交易策略研究等工作的专业人员。","typical_tasks":["金融市场数据分析与趋势研判","金融产品设计与定价模型构建","金融风险量化评估与管理策略制定","量化交易策略研发与回测验证","金融监管政策研究与合规分析"],"education":"本科","salary_median_k":25,"est_employment_wan":15})
entries.append({"code":"2-13-04","name":"保险精算师","major_category":MC2,"major_category_code":2,"mid_category":"经济专业人员","description":"运用数学、统计学和金融理论从事保险产品定价、准备金评估及风险管理等工作的专业人员。","typical_tasks":["保险产品费率厘定与定价模型设计","保险准备金评估与精算报告编制","保险公司偿付能力评估与分析","再保险方案设计与风险转移分析","保险精算模型开发与假设更新"],"education":"硕士及以上","salary_median_k":30,"est_employment_wan":3})

# 2-14 会计专业人员
entries.append({"code":"2-14-01","name":"会计师","major_category":MC2,"major_category_code":2,"mid_category":"会计专业人员","description":"从事会计核算、财务报告编制、税务申报及内部财务管理等工作的专业人员。","typical_tasks":["日常会计凭证编制与账务处理","财务报表编制与财务分析","税务申报与纳税筹划","成本核算与预算编制执行","内部控制制度建设与执行"],"education":"本科","salary_median_k":10,"est_employment_wan":200})
entries.append({"code":"2-14-02","name":"注册会计师","major_category":MC2,"major_category_code":2,"mid_category":"会计专业人员","description":"从事审计鉴证、财务咨询、税务筹划等专业服务的执业注册会计师。","typical_tasks":["企业财务报表审计与鉴证","内部控制审计与管理建议","企业并购尽职调查与估值","税务咨询与纳税规划服务","会计准则咨询与财务顾问"],"education":"本科","salary_median_k":18,"est_employment_wan":30})

# 2-15 审计人员
entries.append({"code":"2-15-01","name":"审计师","major_category":MC2,"major_category_code":2,"mid_category":"审计人员","description":"从事政府审计、内部审计及经济责任审计等工作的专业人员。","typical_tasks":["审计项目方案编制与审计实施","财务收支与预算执行审计","经济责任审计与绩效审计","审计证据采集与审计工作底稿编制","审计报告撰写与整改跟踪"],"education":"本科","salary_median_k":12,"est_employment_wan":40})

# 2-16 统计人员
entries.append({"code":"2-16-01","name":"统计师","major_category":MC2,"major_category_code":2,"mid_category":"统计人员","description":"从事统计调查设计、数据采集处理、统计分析及统计信息发布等工作的专业人员。","typical_tasks":["统计调查方案设计与组织实施","统计数据采集汇总与质量审核","统计分析报告撰写与数据解读","统计信息系统维护与数据管理","统计法规执行与统计台账建设"],"education":"本科","salary_median_k":10,"est_employment_wan":25})

# 2-17 法律专业人员
entries.append({"code":"2-17-01","name":"律师","major_category":MC2,"major_category_code":2,"mid_category":"法律专业人员","description":"取得律师执业证书，从事法律咨询、诉讼代理、非诉讼法律事务等工作的法律专业人员。","typical_tasks":["法律咨询与法律意见书出具","民事和刑事案件代理与辩护","合同审查与法律文书起草","企业合规审查与法律风险防控","调解谈判与争议解决方案设计"],"education":"本科","salary_median_k":15,"est_employment_wan":65})
entries.append({"code":"2-17-02","name":"公证员","major_category":MC2,"major_category_code":2,"mid_category":"法律专业人员","description":"在公证机构依法从事公证业务，对民事法律行为、事实和文书进行公证的法律专业人员。","typical_tasks":["民事法律行为公证办理与审查","合同协议公证与遗嘱公证","学历证书与资格证明公证","涉外公证事项办理与认证","公证档案管理与公证法律咨询"],"education":"本科","salary_median_k":12,"est_employment_wan":15})
entries.append({"code":"2-17-03","name":"法律顾问","major_category":MC2,"major_category_code":2,"mid_category":"法律专业人员","description":"在企事业单位或政府部门中从事法律事务管理、法律风险防范及法律咨询等工作的专业人员。","typical_tasks":["企业经营法律风险识别与评估","合同审核与法律条款拟定修改","知识产权保护与维权策略制定","劳动用工法律合规管理","企业重大决策法律论证与审查"],"education":"本科","salary_median_k":14,"est_employment_wan":30})

# 2-18 教学人员
entries.append({"code":"2-18-01","name":"高等学校教师","major_category":MC2,"major_category_code":2,"mid_category":"教学人员","description":"在普通高等学校中从事教学、科研及学生培养等工作的专业教学人员。","typical_tasks":["大学课程教学与教案编写","科研课题申请与学术论文发表","本科生与研究生培养指导","教学改革研究与课程建设","学科建设与学术交流活动"],"education":"硕士及以上","salary_median_k":14,"est_employment_wan":200})
entries.append({"code":"2-18-02","name":"中等职业教育教师","major_category":MC2,"major_category_code":2,"mid_category":"教学人员","description":"在中等职业学校中从事专业课程教学、实训指导及职业技能培养等工作的专业教学人员。","typical_tasks":["职业技术课程教学与实训指导","教学计划制定与教学资源开发","学生职业技能训练与竞赛辅导","校企合作联络与实习实训安排","专业课程标准制定与教材编写"],"education":"本科","salary_median_k":10,"est_employment_wan":80})
entries.append({"code":"2-18-03","name":"高中教师","major_category":MC2,"major_category_code":2,"mid_category":"教学人员","description":"在普通高中从事各学科教学、学生辅导及教育管理等工作的专业教学人员。","typical_tasks":["学科课程备课与课堂教学","学生作业批改与学业辅导","高考备考指导与模拟测试","教学研究与教学方法改进","班级管理与家校沟通协调"],"education":"本科","salary_median_k":10,"est_employment_wan":180})
entries.append({"code":"2-18-04","name":"初中教师","major_category":MC2,"major_category_code":2,"mid_category":"教学人员","description":"在初级中学从事各学科教学、学生管理及素质教育等工作的专业教学人员。","typical_tasks":["初中各学科课程备课与授课","学生作业批改与学习辅导","中考备考指导与考试分析","学生行为习惯培养与德育教育","教学质量分析与教研活动参与"],"education":"本科","salary_median_k":9,"est_employment_wan":380})
entries.append({"code":"2-18-05","name":"小学教师","major_category":MC2,"major_category_code":2,"mid_category":"教学人员","description":"在小学从事各学科教学、学生管理及课外活动组织等工作的专业教学人员。","typical_tasks":["小学课程备课与课堂教学","学生作业批改与学业评价","课外活动与兴趣小组组织辅导","学生行为习惯养成与心理辅导","家校联系沟通与家长会组织"],"education":"本科","salary_median_k":8,"est_employment_wan":650})
entries.append({"code":"2-18-06","name":"幼儿园教师","major_category":MC2,"major_category_code":2,"mid_category":"教学人员","description":"在幼儿园从事学前教育、游戏活动组织及幼儿生活照料指导等工作的专业教学人员。","typical_tasks":["幼儿教学活动设计与组织实施","游戏活动策划与玩教具制作","幼儿一日生活常规管理与照护","幼儿发展观察记录与评价","家园共育沟通与亲子活动组织"],"education":"大专","salary_median_k":6,"est_employment_wan":300})
entries.append({"code":"2-18-07","name":"特殊教育教师","major_category":MC2,"major_category_code":2,"mid_category":"教学人员","description":"在特殊教育学校或普通学校随班就读中从事残障学生教育教学和康复训练等工作的专业教学人员。","typical_tasks":["特殊学生个别化教育方案制定","特殊教育课程教学与康复训练","学生功能评估与教育干预","辅助技术设备选用与教学适配","特殊学生家庭教育指导与支持"],"education":"本科","salary_median_k":8,"est_employment_wan":20})

# 2-19 文学创作和编辑人员
entries.append({"code":"2-19-01","name":"作家和文学创作人员","major_category":MC2,"major_category_code":2,"mid_category":"文学创作和编辑人员","description":"从事小说、散文、诗歌、剧本等文学作品创作的专业人员。","typical_tasks":["文学作品构思与创作写作","文学素材采集与生活体验积累","作品修改润色与定稿","文学创作交流与作品研讨","版权授权与出版合作洽谈"],"education":"本科","salary_median_k":8,"est_employment_wan":10})
entries.append({"code":"2-19-02","name":"编辑","major_category":MC2,"major_category_code":2,"mid_category":"文学创作和编辑人员","description":"在出版社、杂志社、新闻网站等机构从事稿件审编、内容策划及出版管理等工作的专业人员。","typical_tasks":["稿件审读编辑与文字校对加工","选题策划与出版方案编制","作者联络与约稿组稿","图书版式设计与封面文案撰写","出版物质量审查与三审三校"],"education":"本科","salary_median_k":10,"est_employment_wan":30})
entries.append({"code":"2-19-03","name":"网络文学创作人员","major_category":MC2,"major_category_code":2,"mid_category":"文学创作和编辑人员","description":"在网络文学平台从事网络小说、网络文学作品创作和连载发表等工作的创作人员。","typical_tasks":["网络小说大纲设计与章节创作","作品日更连载与读者互动","故事情节构思与人物塑造","平台签约合作与版权运营","作品改编合作与IP开发"],"education":"本科","salary_median_k":8,"est_employment_wan":20})

# 2-20 记者
entries.append({"code":"2-20-01","name":"文字记者","major_category":MC2,"major_category_code":2,"mid_category":"记者","description":"从事新闻采访、调查报道、新闻写作及新闻评论等工作的新闻专业人员。","typical_tasks":["新闻线索采集与选题策划","新闻采访与调查取证","新闻稿件撰写与编辑","深度报道和专题报道制作","新闻评论与时事分析写作"],"education":"本科","salary_median_k":10,"est_employment_wan":20})
entries.append({"code":"2-20-02","name":"摄影摄像记者","major_category":MC2,"major_category_code":2,"mid_category":"记者","description":"从事新闻摄影、视频拍摄及新闻影像编辑等工作的新闻专业人员。","typical_tasks":["新闻现场摄影与视频拍摄","新闻图片与视频编辑处理","重大活动和突发事件影像记录","新闻专题纪录片拍摄制作","影像素材管理与图片库建设"],"education":"本科","salary_median_k":9,"est_employment_wan":10})

# 2-21 翻译人员
entries.append({"code":"2-21-01","name":"笔译人员","major_category":MC2,"major_category_code":2,"mid_category":"翻译人员","description":"从事各类文字翻译，包括文学翻译、科技翻译、商务翻译及本地化翻译等工作的专业人员。","typical_tasks":["中外文书面翻译与校审","专业术语查询与术语库维护","翻译项目管理与质量控制","机器翻译译后编辑与审校","翻译记忆库建设与翻译工具应用"],"education":"本科","salary_median_k":10,"est_employment_wan":15})
entries.append({"code":"2-21-02","name":"口译人员","major_category":MC2,"major_category_code":2,"mid_category":"翻译人员","description":"从事各类会议、商务谈判、外事接待中的同声传译和交替传译等工作的专业人员。","typical_tasks":["国际会议同声传译与交替传译","商务洽谈与外事活动口译","译前准备与专业术语研究","口译笔记技巧训练与提升","多语种翻译团队协作与协调"],"education":"本科","salary_median_k":15,"est_employment_wan":5})

# 2-22 图书资料与档案专业人员
entries.append({"code":"2-22-01","name":"图书资料专业人员","major_category":MC2,"major_category_code":2,"mid_category":"图书资料与档案专业人员","description":"在图书馆等机构从事图书采编、文献管理、读者服务及数字资源建设等工作的专业人员。","typical_tasks":["图书文献采购与编目分类","读者咨询与参考服务","数字资源建设与数据库管理","图书借阅管理与流通服务","阅读推广活动策划与组织"],"education":"本科","salary_median_k":7,"est_employment_wan":20})
entries.append({"code":"2-22-02","name":"档案专业人员","major_category":MC2,"major_category_code":2,"mid_category":"图书资料与档案专业人员","description":"在各级各类档案馆和机关企事业单位从事档案收集、整理、保管和利用等工作的专业人员。","typical_tasks":["档案资料收集整理与立卷归档","档案数字化扫描与电子档案管理","档案借阅利用与查询服务","档案保管条件维护与安全管理","档案编研与档案信息开发利用"],"education":"本科","salary_median_k":7,"est_employment_wan":25})

# 2-23 文化工作人员
entries.append({"code":"2-23-01","name":"博物馆工作人员","major_category":MC2,"major_category_code":2,"mid_category":"文化工作人员","description":"在各类博物馆从事藏品保管、陈列展览、社会教育及文博研究等工作的专业人员。","typical_tasks":["博物馆藏品登记保管与保护修复","陈列展览策划设计与布展实施","社会教育活动策划与讲解服务","文物鉴定与文博学术研究","博物馆数字化建设与线上展览"],"education":"本科","salary_median_k":8,"est_employment_wan":10})
entries.append({"code":"2-23-02","name":"文化馆群艺馆工作人员","major_category":MC2,"major_category_code":2,"mid_category":"文化工作人员","description":"在文化馆和群众艺术馆从事群众文化活动组织、文艺创作辅导及非遗保护传承等工作的专业人员。","typical_tasks":["群众文化活动策划组织与实施","文艺培训辅导与创作指导","群众文艺演出编排与舞台管理","基层公共文化服务指导与调研","民间文化艺术资源调查与整理"],"education":"本科","salary_median_k":7,"est_employment_wan":15})
entries.append({"code":"2-23-03","name":"非物质文化遗产保护人员","major_category":MC2,"major_category_code":2,"mid_category":"文化工作人员","description":"从事非物质文化遗产调查记录、保护传承及宣传推广等工作的专业人员。","typical_tasks":["非遗项目田野调查与资料采集","非遗代表性项目申报与评审","非遗传承人认定与传承活动组织","非遗数字化记录与数据库建设","非遗宣传展示与社会推广活动"],"education":"本科","salary_median_k":7,"est_employment_wan":5})

# 2-24 体育工作人员
entries.append({"code":"2-24-01","name":"运动员","major_category":MC2,"major_category_code":2,"mid_category":"体育工作人员","description":"从事各类竞技体育项目的专业训练和比赛竞技的专业人员。","typical_tasks":["日常体能训练与专项技术训练","国内外竞技比赛参赛与竞技","训练计划执行与体能恢复管理","比赛录像分析与技战术研讨","运动伤病预防与康复训练"],"education":"本科","salary_median_k":8,"est_employment_wan":10})
entries.append({"code":"2-24-02","name":"教练员","major_category":MC2,"major_category_code":2,"mid_category":"体育工作人员","description":"从事运动训练计划制定、技战术指导及运动员管理等工作的体育专业人员。","typical_tasks":["运动训练计划制定与实施","运动员技战术分析与指导","比赛战术布置与临场指挥","运动员选拔培养与梯队建设","训练效果评估与训练方法改进"],"education":"本科","salary_median_k":10,"est_employment_wan":15})
entries.append({"code":"2-24-03","name":"体育裁判员","major_category":MC2,"major_category_code":2,"mid_category":"体育工作人员","description":"在各类体育竞赛中从事执法裁判、成绩判定及竞赛规则执行等工作的专业人员。","typical_tasks":["竞赛规则学习与裁判法研究","比赛现场执法裁判与成绩判定","赛前技术会议参与与场地检查","裁判员培训与等级考核","比赛争议判罚处理与技术报告"],"education":"本科","salary_median_k":8,"est_employment_wan":5})

# 2-25 美术和设计专业人员
entries.append({"code":"2-25-01","name":"画家和雕塑家","major_category":MC2,"major_category_code":2,"mid_category":"美术和设计专业人员","description":"从事绘画、雕塑等视觉艺术创作的专业美术人员。","typical_tasks":["绘画和雕塑作品构思与创作","艺术展览参展与个人画展举办","艺术作品市场推广与销售","美术教学与艺术创作指导","艺术采风写生与创作素材积累"],"education":"本科","salary_median_k":8,"est_employment_wan":10})
entries.append({"code":"2-25-02","name":"平面设计师","major_category":MC2,"major_category_code":2,"mid_category":"美术和设计专业人员","description":"从事品牌视觉设计、广告设计、包装设计及印刷品设计等工作的专业设计人员。","typical_tasks":["品牌标识与视觉识别系统设计","广告宣传物料与海报设计制作","产品包装设计与印刷跟进","企业画册与宣传手册版式设计","网页与移动端界面视觉设计"],"education":"本科","salary_median_k":9,"est_employment_wan":60})
entries.append({"code":"2-25-03","name":"工业设计师","major_category":MC2,"major_category_code":2,"mid_category":"美术和设计专业人员","description":"从事工业产品外观造型设计、人机交互设计及产品创新设计等工作的专业设计人员。","typical_tasks":["产品外观造型设计与效果图绘制","产品用户研究与人机工程分析","产品原型制作与设计验证","产品CMF设计与工艺可行性分析","设计趋势研究与创新设计方案提出"],"education":"本科","salary_median_k":12,"est_employment_wan":20})
entries.append({"code":"2-25-04","name":"室内设计师","major_category":MC2,"major_category_code":2,"mid_category":"美术和设计专业人员","description":"从事室内空间功能规划、装饰风格设计及施工图绘制等工作的专业设计人员。","typical_tasks":["室内空间方案设计与效果图制作","施工图纸绘制与材料选配","室内装饰工程预算编制","施工现场技术交底与设计跟踪","客户需求沟通与设计方案汇报"],"education":"本科","salary_median_k":10,"est_employment_wan":50})
entries.append({"code":"2-25-05","name":"服装设计师","major_category":MC2,"major_category_code":2,"mid_category":"美术和设计专业人员","description":"从事服装款式设计、面料选配、样衣制作及服装流行趋势研究等工作的专业设计人员。","typical_tasks":["服装款式设计与效果图绘制","面料选配与服装辅料搭配","样衣打版制作与试穿修改","服装流行趋势分析与产品企划","服装发布会策划与品牌形象塑造"],"education":"本科","salary_median_k":10,"est_employment_wan":15})

# 2-26 音乐和表演艺术人员
entries.append({"code":"2-26-01","name":"音乐家","major_category":MC2,"major_category_code":2,"mid_category":"音乐和表演艺术人员","description":"从事音乐创作、演奏演唱及音乐教育等工作的专业音乐人员。","typical_tasks":["音乐作品创作与编曲","乐器演奏与声乐演唱训练","音乐会和演出排练与演出","音乐录音与后期制作","音乐教学与音乐理论研究"],"education":"本科","salary_median_k":8,"est_employment_wan":10})
entries.append({"code":"2-26-02","name":"演员","major_category":MC2,"major_category_code":2,"mid_category":"音乐和表演艺术人员","description":"从事戏剧、影视、曲艺等表演艺术创作和演出的专业表演人员。","typical_tasks":["角色分析研读与表演创作","影视剧和舞台剧排练与演出","台词与形体训练","试镜面试与角色竞选","艺术形象塑造与表演技巧提升"],"education":"本科","salary_median_k":10,"est_employment_wan":15})
entries.append({"code":"2-26-03","name":"导演和编剧","major_category":MC2,"major_category_code":2,"mid_category":"音乐和表演艺术人员","description":"从事影视剧、舞台剧的编剧创作和导演执导等工作的专业人员。","typical_tasks":["剧本创作与剧本修改打磨","影视和舞台剧导演与执导","演员指导与表演调度","拍摄计划制定与现场调度管理","作品后期制作监督与审核"],"education":"本科","salary_median_k":12,"est_employment_wan":8})
entries.append({"code":"2-26-04","name":"舞蹈家","major_category":MC2,"major_category_code":2,"mid_category":"音乐和表演艺术人员","description":"从事舞蹈表演、舞蹈编导及舞蹈教学等工作的专业舞蹈人员。","typical_tasks":["舞蹈作品排练与舞台演出","舞蹈编导与舞蹈动作设计","日常基本功训练与体能保持","舞蹈教学与学员培养","舞蹈比赛参赛与艺术交流"],"education":"本科","salary_median_k":7,"est_employment_wan":8})

# 2-27 广播电视和网络视听人员
entries.append({"code":"2-27-01","name":"广播电视编导","major_category":MC2,"major_category_code":2,"mid_category":"广播电视和网络视听人员","description":"从事广播电视节目策划、编导、制作及栏目管理等工作的专业人员。","typical_tasks":["电视节目选题策划与方案撰写","节目拍摄脚本编写与现场导播","节目后期剪辑与包装合成","节目播出审查与质量把控","栏目运营管理与收视分析"],"education":"本科","salary_median_k":10,"est_employment_wan":15})
entries.append({"code":"2-27-02","name":"播音员和节目主持人","major_category":MC2,"major_category_code":2,"mid_category":"广播电视和网络视听人员","description":"在广播电视媒体中从事新闻播报、节目主持及配音等工作的专业人员。","typical_tasks":["新闻节目播报与直播主持","综艺和访谈节目主持","播音稿件备稿与发声训练","配音和解说录制","媒体活动主持与形象管理"],"education":"本科","salary_median_k":12,"est_employment_wan":8})
entries.append({"code":"2-27-03","name":"影视后期制作人员","major_category":MC2,"major_category_code":2,"mid_category":"广播电视和网络视听人员","description":"从事影视作品剪辑、特效制作、调色合成及音效处理等后期制作工作的专业人员。","typical_tasks":["影视素材剪辑与叙事节奏把控","视觉特效制作与合成","画面调色与影调风格统一","音效编辑与声音混录","字幕制作与影片输出交付"],"education":"本科","salary_median_k":10,"est_employment_wan":25})
entries.append({"code":"2-27-04","name":"网络视听内容创作人员","major_category":MC2,"major_category_code":2,"mid_category":"广播电视和网络视听人员","description":"从事网络短视频、直播、播客等网络视听内容策划创作与运营的专业人员。","typical_tasks":["短视频选题策划与脚本创作","视频拍摄制作与后期剪辑","直播活动策划与在线互动","自媒体账号运营与粉丝维护","网络视听内容数据分析与优化"],"education":"本科","salary_median_k":8,"est_employment_wan":100})

# 2-28 文物保护和考古人员
entries.append({"code":"2-28-01","name":"文物保护修复人员","major_category":MC2,"major_category_code":2,"mid_category":"文物保护和考古人员","description":"从事文物保护修复方案设计、文物修复操作及预防性保护等工作的专业人员。","typical_tasks":["文物保存状况调查与病害评估","文物保护修复方案设计与实施","文物修复材料与工艺研究","文物保存环境监测与调控","文物保护修复档案建立与管理"],"education":"本科","salary_median_k":8,"est_employment_wan":5})
entries.append({"code":"2-28-02","name":"考古人员","major_category":MC2,"major_category_code":2,"mid_category":"文物保护和考古人员","description":"从事考古调查发掘、出土文物整理研究及考古报告编写等工作的专业人员。","typical_tasks":["考古遗址调查勘探与发掘","出土文物清理登记与分类整理","考古发掘记录与地层分析","考古报告编写与研究成果发表","考古现场文物保护与标本采集"],"education":"硕士及以上","salary_median_k":10,"est_employment_wan":3})


# ═══════════════════════════════════════
# Output
# ═══════════════════════════════════════
output_dir = "/Users/liuhongjie/software/project/china-ai-jobs/data"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "batch_1.json")

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(entries, f, ensure_ascii=False, indent=2)

# Count entries
mc1_count = sum(1 for e in entries if e["major_category_code"] == 1)
mc2_count = sum(1 for e in entries if e["major_category_code"] == 2)
print(f"Total entries: {len(entries)}")
print(f"  大类1 entries: {mc1_count}")
print(f"  大类2 entries: {mc2_count}")
print(f"Output written to: {output_path}")
