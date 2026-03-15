#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate batch_3.json for 大类5 and 大类6."""

import json
import os

data = []

# ═══════════════════════════════════════
# 大类5: 农、林、牧、渔业生产及辅助人员
# ═══════════════════════════════════════
MC5 = "农、林、牧、渔业生产及辅助人员"

# 5-01 粮食作物生产人员
mid = "粮食作物生产人员"
data.append({"code":"5-01-01","name":"水稻种植人员","major_category":MC5,"major_category_code":5,"mid_category":mid,"description":"从事水稻育秧、插秧、田间管理和收割等生产环节的农业劳动者。负责稻田从整地到收获全过程的种植管理工作。","typical_tasks":["水稻育秧和秧苗管理","稻田翻耕整地与插秧作业","稻田灌溉与水层管理","病虫草害防治与施肥管理","水稻收割与晾晒储存"],"education":"初中及以下","salary_median_k":3,"est_employment_wan":3500})
data.append({"code":"5-01-02","name":"小麦种植人员","major_category":MC5,"major_category_code":5,"mid_category":mid,"description":"从事小麦播种、田间管理和收获等工作的农业生产人员。承担小麦从种到收全过程的栽培管理任务。","typical_tasks":["小麦播种前整地与基肥施用","小麦播种与种子处理","冬春季麦田灌溉与追肥","小麦病虫害监测与防治","小麦机械收割与脱粒晾晒"],"education":"初中及以下","salary_median_k":3,"est_employment_wan":2000})
data.append({"code":"5-01-03","name":"玉米及杂粮种植人员","major_category":MC5,"major_category_code":5,"mid_category":mid,"description":"从事玉米、高粱、谷子等杂粮作物种植与管理的农业劳动者。负责杂粮作物的选种、播种、田间管理及收获工作。","typical_tasks":["玉米选种与种子包衣处理","玉米播种与合理密植","田间中耕除草与追肥","玉米螟等病虫害综合防治","杂粮作物收获与秸秆处理"],"education":"初中及以下","salary_median_k":3,"est_employment_wan":2500})

# 5-02 经济作物生产人员
mid = "经济作物生产人员"
data.append({"code":"5-02-01","name":"棉花种植人员","major_category":MC5,"major_category_code":5,"mid_category":mid,"description":"从事棉花种植、田间管理和采摘等工作的农业生产人员。负责棉花从播种到采收全过程的生产管理。","typical_tasks":["棉花播种与地膜覆盖作业","棉花打顶整枝与化学调控","棉田灌溉与肥料管理","棉铃虫等病虫害防治","棉花采摘与分级打包"],"education":"初中及以下","salary_median_k":3,"est_employment_wan":300})
data.append({"code":"5-02-02","name":"油料作物种植人员","major_category":MC5,"major_category_code":5,"mid_category":mid,"description":"从事花生、大豆、油菜等油料作物种植与管理的农业劳动者。承担油料作物田间栽培管理和收获工作。","typical_tasks":["油菜或花生播种与移栽","油料作物田间施肥与灌溉","菌核病等病虫害监测防治","油料作物收割与脱粒","油料作物种子晾晒与储藏"],"education":"初中及以下","salary_median_k":3,"est_employment_wan":500})
data.append({"code":"5-02-03","name":"蔬菜种植人员","major_category":MC5,"major_category_code":5,"mid_category":mid,"description":"从事各类蔬菜育苗、定植、田间管理和采收的农业生产人员。负责露地或设施蔬菜的全程栽培管理工作。","typical_tasks":["蔬菜育苗与苗期管理","大棚温湿度调控与通风管理","蔬菜定植与水肥一体化管理","蔬菜病虫害绿色防控","蔬菜采收分拣与保鲜包装"],"education":"初中及以下","salary_median_k":4,"est_employment_wan":2500})
data.append({"code":"5-02-04","name":"水果种植人员","major_category":MC5,"major_category_code":5,"mid_category":mid,"description":"从事苹果、柑橘、葡萄等水果种植与果园管理的农业生产人员。负责果树栽培、修剪、病虫害防治和果品采收工作。","typical_tasks":["果树整形修剪与树体管理","果园施肥灌溉与土壤改良","果树花期管理与疏花疏果","果树病虫害综合防治","水果采摘与分级包装"],"education":"初中及以下","salary_median_k":4,"est_employment_wan":1500})
data.append({"code":"5-02-05","name":"茶叶种植人员","major_category":MC5,"major_category_code":5,"mid_category":mid,"description":"从事茶树栽培、茶园管理和茶叶采摘的农业生产人员。负责茶园日常管护和鲜叶采摘工作。","typical_tasks":["茶树定植与幼龄茶园管理","茶园修剪与树冠培育","茶园施肥与土壤管理","茶小绿叶蝉等病虫害防治","茶叶按标准采摘与鲜叶保管"],"education":"初中及以下","salary_median_k":3,"est_employment_wan":300})
data.append({"code":"5-02-06","name":"中药材种植人员","major_category":MC5,"major_category_code":5,"mid_category":mid,"description":"从事中药材规范化种植与田间管理的农业生产人员。负责中药材从选种育苗到采收加工的全过程管理。","typical_tasks":["中药材种苗繁育与移栽","中药材田间水肥管理","中药材病虫害生物防治","中药材适时采收与产地初加工","中药材干燥分级与储藏"],"education":"初中及以下","salary_median_k":4,"est_employment_wan":200})
data.append({"code":"5-02-07","name":"花卉苗木种植人员","major_category":MC5,"major_category_code":5,"mid_category":mid,"description":"从事花卉和绿化苗木培育、种植与养护的农业生产人员。负责花卉苗木的繁殖、栽培管理和出圃销售工作。","typical_tasks":["花卉苗木扦插嫁接繁殖","花卉温室环境调控管理","苗木修剪造型与养护","花卉病虫害防治与营养管理","花卉苗木出圃包装与运输"],"education":"初中及以下","salary_median_k":4,"est_employment_wan":200})

# 5-03 林业生产人员
mid = "林业生产人员"
data.append({"code":"5-03-01","name":"营造林人员","major_category":MC5,"major_category_code":5,"mid_category":mid,"description":"从事植树造林、退耕还林和林木抚育等工作的林业生产人员。负责造林地整理、苗木栽植和幼林抚育管理。","typical_tasks":["造林地清理与整地挖穴","苗木栽植与浇水保活","幼林抚育与补植补造","林木修枝与间伐抚育","造林成活率调查与记录"],"education":"初中及以下","salary_median_k":3,"est_employment_wan":200})
data.append({"code":"5-03-02","name":"森林管护人员","major_category":MC5,"major_category_code":5,"mid_category":mid,"description":"从事森林资源巡护、防火防盗和林业有害生物防治的林业生产人员。负责管护区域内森林资源的日常巡查与保护工作。","typical_tasks":["林区日常巡护与资源监测","森林防火巡查与火源管控","森林病虫害监测与防治","制止乱砍滥伐等违法行为","林区基础设施维护与管理"],"education":"初中及以下","salary_median_k":3,"est_employment_wan":150})
data.append({"code":"5-03-03","name":"木材采运人员","major_category":MC5,"major_category_code":5,"mid_category":mid,"description":"从事林木采伐、木材集运和贮存等工作的林业生产人员。负责按采伐设计进行林木伐倒、造材和运输作业。","typical_tasks":["林木伐倒与安全作业","原木打枝造材与检尺","木材楞场归楞与装车","木材运输与中转贮存","采伐迹地清理与更新"],"education":"初中及以下","salary_median_k":4,"est_employment_wan":50})

# 5-04 畜牧业生产人员
mid = "畜牧业生产人员"
data.append({"code":"5-04-01","name":"生猪饲养人员","major_category":MC5,"major_category_code":5,"mid_category":mid,"description":"从事生猪繁殖、饲养管理和日常保健的畜牧业生产人员。负责种猪配种、仔猪保育和育肥猪饲养管理全过程。","typical_tasks":["种猪配种与母猪妊娠管理","仔猪接产护理与保育","生猪日粮配制与定时饲喂","猪舍环境清洁与消毒防疫","生猪出栏称重与转运"],"education":"初中及以下","salary_median_k":4,"est_employment_wan":800})
data.append({"code":"5-04-02","name":"牛羊饲养人员","major_category":MC5,"major_category_code":5,"mid_category":mid,"description":"从事牛、羊饲养管理和繁殖配种的畜牧业生产人员。负责牛羊的日常饲喂、放牧管理和疫病预防工作。","typical_tasks":["牛羊日粮搭配与饲喂管理","牛羊放牧与草场轮牧管理","母畜发情鉴定与配种","畜群防疫注射与驱虫","畜舍清洁消毒与粪污处理"],"education":"初中及以下","salary_median_k":4,"est_employment_wan":600})
data.append({"code":"5-04-03","name":"家禽饲养人员","major_category":MC5,"major_category_code":5,"mid_category":mid,"description":"从事鸡、鸭、鹅等家禽饲养管理的畜牧业生产人员。负责家禽的孵化育雏、饲养管理和蛋品收集工作。","typical_tasks":["家禽孵化与育雏温度管理","家禽日粮配制与自动饲喂","禽舍通风换气与光照调控","家禽疫苗接种与疫病防控","禽蛋收集分级与储存"],"education":"初中及以下","salary_median_k":3,"est_employment_wan":500})
data.append({"code":"5-04-04","name":"奶畜饲养人员","major_category":MC5,"major_category_code":5,"mid_category":mid,"description":"从事奶牛、奶山羊等奶畜饲养和挤奶管理的畜牧业生产人员。负责泌乳期奶畜的营养管理和机械化挤奶作业。","typical_tasks":["奶畜日粮营养配方调整","机械化挤奶操作与设备维护","奶畜乳房保健与乳质检测","奶畜繁殖配种与围产期管理","鲜奶冷却储存与质量记录"],"education":"高中/中专","salary_median_k":4,"est_employment_wan":80})

# 5-05 渔业生产人员
mid = "渔业生产人员"
data.append({"code":"5-05-01","name":"淡水养殖人员","major_category":MC5,"major_category_code":5,"mid_category":mid,"description":"从事鱼、虾、蟹等淡水水产品养殖的渔业生产人员。负责池塘或水库养殖的苗种投放、饲料投喂和水质管理工作。","typical_tasks":["养殖池塘清塘与肥水准备","鱼虾苗种投放与放养密度控制","饲料定时定量投喂管理","养殖水质监测与调控","水产品起捕与暂养销售"],"education":"初中及以下","salary_median_k":4,"est_employment_wan":400})
data.append({"code":"5-05-02","name":"海水养殖人员","major_category":MC5,"major_category_code":5,"mid_category":mid,"description":"从事海水鱼类、贝类、藻类等海产品养殖的渔业生产人员。负责近海网箱养殖或滩涂养殖的日常管理工作。","typical_tasks":["海水养殖网箱布设与维护","海产苗种投放与养殖管理","养殖海域水质监测与病害防治","贝类和藻类养殖筏架管理","海产品收获与保鲜运输"],"education":"初中及以下","salary_median_k":5,"est_employment_wan":200})
data.append({"code":"5-05-03","name":"海洋捕捞人员","major_category":MC5,"major_category_code":5,"mid_category":mid,"description":"从事海洋渔业捕捞作业的渔业生产人员。负责渔船出海作业、渔具操作和渔获物保鲜处理工作。","typical_tasks":["渔船出海前安全检查与物资准备","拖网或围网等渔具下放与起收","渔获物分拣与船上保鲜处理","航海设备操作与渔场定位","渔船靠港卸货与渔具修补"],"education":"初中及以下","salary_median_k":5,"est_employment_wan":150})

# 5-06 农林牧渔辅助人员
mid = "农林牧渔辅助人员"
data.append({"code":"5-06-01","name":"农业机械操作人员","major_category":MC5,"major_category_code":5,"mid_category":mid,"description":"从事农用拖拉机、收割机等农业机械驾驶与操作的辅助人员。负责农业机械化作业和机具日常维护保养。","typical_tasks":["拖拉机驾驶与农田耕整地作业","联合收割机操作与收获作业","播种施肥机械调试与作业","植保无人机或喷雾机操作","农业机械日常维护与故障排除"],"education":"初中及以下","salary_median_k":4,"est_employment_wan":200})
data.append({"code":"5-06-02","name":"农产品初加工人员","major_category":MC5,"major_category_code":5,"mid_category":mid,"description":"从事农产品清洗、分选、包装等初级加工的辅助人员。负责农产品采后处理和商品化加工作业。","typical_tasks":["农产品清洗与分级筛选","农产品烘干与脱水处理","农产品保鲜包装与贴标","初加工设备操作与清洁维护","农产品入库储存与出库管理"],"education":"初中及以下","salary_median_k":4,"est_employment_wan":500})
data.append({"code":"5-06-03","name":"灌溉排水人员","major_category":MC5,"major_category_code":5,"mid_category":mid,"description":"从事农田灌溉和排水设施运行管理的辅助人员。负责灌排渠系、泵站和节水灌溉设施的运行维护工作。","typical_tasks":["灌溉泵站设备启停与运行监控","灌排渠道闸门启闭与水量调配","滴灌喷灌系统运行与维护","灌排设施巡查与隐患排除","灌溉用水计量与记录"],"education":"初中及以下","salary_median_k":3,"est_employment_wan":100})

# ═══════════════════════════════════════
# 大类6: 生产制造及有关人员
# ═══════════════════════════════════════
MC6 = "生产制造及有关人员"

# 6-01 食品饮料生产加工人员
mid = "食品饮料生产加工人员"
data.append({"code":"6-01-01","name":"粮油加工人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事粮食碾磨、植物油脂压榨和精炼等加工的生产人员。负责面粉、大米、食用油等粮油产品的生产加工操作。","typical_tasks":["原粮清理筛选与润麦处理","碾米或制粉设备操作与调试","油脂浸出与精炼设备运行","粮油产品质量检测与记录","生产设备清洁维护与安全操作"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":80})
data.append({"code":"6-01-02","name":"肉类加工人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事畜禽屠宰、肉类分割和肉制品加工的生产人员。负责肉类产品从屠宰到包装的全流程加工操作。","typical_tasks":["畜禽屠宰与胴体检验","肉类分割与修整分级","腌腊灌肠等肉制品加工","肉类产品速冻与冷藏管理","加工车间卫生清洗与消毒"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":60})
data.append({"code":"6-01-03","name":"乳制品加工人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事牛奶巴氏杀菌、酸奶发酵和奶粉生产等加工的生产人员。负责乳制品生产线的操作与质量控制。","typical_tasks":["原料乳验收与预处理操作","巴氏杀菌或超高温灭菌设备操作","酸奶发酵与灌装封口作业","奶粉喷雾干燥与包装","乳制品生产过程质量检测"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":30})
data.append({"code":"6-01-04","name":"焙烤食品加工人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事面包、糕点、饼干等焙烤食品生产加工的生产人员。负责焙烤食品的配料、成型、烘烤和包装工作。","typical_tasks":["面团配料称量与搅拌和面","面包糕点成型与整形操作","烤炉温度控制与烘焙作业","焙烤产品冷却与装饰","成品包装与保质期标注"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":40})
data.append({"code":"6-01-05","name":"饮料制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事碳酸饮料、果汁、茶饮料等饮品生产加工的生产人员。负责饮料调配、灌装和包装生产线的操作运行。","typical_tasks":["饮料原料配比与调配操作","饮料杀菌与灌装封盖作业","碳酸化混合与充气操作","灌装生产线巡检与参数调整","饮料成品包装与码垛"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":30})
data.append({"code":"6-01-06","name":"酿酒人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事白酒、啤酒、葡萄酒等酒类酿造生产的生产人员。负责酿酒原料处理、发酵管理和蒸馏勾调等工序操作。","typical_tasks":["酿酒原料粉碎蒸煮与拌曲","发酵池或发酵罐温度监控管理","白酒蒸馏摘酒与分级储存","啤酒糖化过滤与发酵管理","成品酒勾调与灌装封口"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":25})

# 6-02 烟草制品生产人员
mid = "烟草制品生产人员"
data.append({"code":"6-02-01","name":"烟叶加工人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事烟叶复烤、分级和储存等加工处理的生产人员。负责烟叶原料的打叶复烤和醇化储存管理。","typical_tasks":["烟叶分级挑选与配方组模","打叶复烤生产线操作","烟叶含水率与温度监控","复烤烟叶包装与入库","烟叶醇化储存环境管理"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":15})
data.append({"code":"6-02-02","name":"卷烟制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事卷烟制丝、卷接和包装等生产工序的生产人员。负责卷烟生产设备的操作运行和产品质量控制。","typical_tasks":["制丝线投料与加工设备操作","卷接机组运行与参数调整","卷烟包装机操作与维护","卷烟产品外观与物理指标检测","生产线故障排除与设备保养"],"education":"高中/中专","salary_median_k":7,"est_employment_wan":10})

# 6-03 纺织品生产人员
mid = "纺织品生产人员"
data.append({"code":"6-03-01","name":"纺纱人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事棉、毛、麻等纤维纺纱生产的生产人员。负责开清棉、梳棉、并条、粗纱和细纱等工序的设备操作。","typical_tasks":["开清棉机组操作与杂质清除","梳棉机操作与棉网质量监控","并条和粗纱机操作调整","细纱机运行管理与接头操作","纱线质量检测与落纱管理"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":100})
data.append({"code":"6-03-02","name":"织造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事机织物或针织物织造生产的生产人员。负责织机的穿经、织造和布面质量监控等工作。","typical_tasks":["经纱整经穿综与织机上机","织机运行参数调整与监控","布面疵点巡检与停机处理","针织大圆机操作与织物检查","织造设备日常保养与维护"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":120})
data.append({"code":"6-03-03","name":"印染人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事纺织品染色、印花和后整理的生产人员。负责织物的前处理、染色印花和功能性整理工序操作。","typical_tasks":["坯布退浆煮练与漂白处理","染料配方调制与染色操作","织物印花制版与印花操作","织物定型与柔软整理","染色牢度和色差检测"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":60})

# 6-04 服装制作人员
mid = "服装制作人员"
data.append({"code":"6-04-01","name":"裁剪缝纫人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事服装面料裁剪和缝纫制作的生产人员。负责按照样板裁剪面料并进行缝纫拼接加工。","typical_tasks":["服装面料铺布与排料","电剪或自动裁床裁剪作业","缝纫机操作与部件缝合","缝制质量自检与返修","缝纫设备维护与换针调线"],"education":"初中及以下","salary_median_k":5,"est_employment_wan":400})
data.append({"code":"6-04-02","name":"制衣人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事成衣组装、整烫和成品检验的服装生产人员。负责服装缝制、锁钉、整烫和包装等工序的操作。","typical_tasks":["服装各部件组装与缝合","锁眼钉扣与商标缝制","成衣整烫与定型操作","成品尺寸和外观质量检验","服装折叠包装与装箱"],"education":"初中及以下","salary_median_k":5,"est_employment_wan":300})
data.append({"code":"6-04-03","name":"制鞋人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事皮鞋、运动鞋等鞋类产品制造的生产人员。负责鞋帮裁断、针车缝合和成型组装等工序。","typical_tasks":["鞋帮面料裁断与配料","鞋帮缝合与车缝操作","鞋底成型与帮底粘合","成鞋整理与质量检验","制鞋设备操作与维护"],"education":"初中及以下","salary_median_k":5,"est_employment_wan":150})

# 6-05 皮革毛皮制品加工人员
mid = "皮革毛皮制品加工人员"
data.append({"code":"6-05-01","name":"皮革鞣制加工人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事生皮鞣制和皮革涂饰等加工的生产人员。负责原料皮的浸泡脱毛、鞣制加脂和涂饰整理。","typical_tasks":["原料皮浸水脱毛与浸灰处理","铬鞣或植鞣工艺操作","皮革削匀与复鞣加脂","皮革涂饰与压花整理","鞣制废液处理与环保达标"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":30})
data.append({"code":"6-05-02","name":"皮革制品制作人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事皮包、皮带、皮衣等皮革制品制作的生产人员。负责皮革制品的裁切、缝制和成品组装。","typical_tasks":["皮革裁切与配件下料","皮革制品缝制与粘合","五金配件安装与铆接","皮革制品边油处理与抛光","成品质量检验与包装"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":50})

# 6-06 木材加工及家具制造人员
mid = "木材加工及家具制造人员"
data.append({"code":"6-06-01","name":"木材加工人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事原木锯解、木材干燥和木制品加工的生产人员。负责木材的开料、刨光和防腐处理等加工作业。","typical_tasks":["原木锯解与板材开料","木材干燥窑操作与含水率控制","木材刨光与砂光处理","木材防腐防虫药剂处理","木材分等与堆垛储存"],"education":"初中及以下","salary_median_k":5,"est_employment_wan":60})
data.append({"code":"6-06-02","name":"家具制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事木质家具、板式家具和软体家具制造的生产人员。负责家具的开料、组装、涂装和包装等工序操作。","typical_tasks":["家具部件开料与铣型加工","家具榫卯或五金连接组装","家具表面涂装与打磨","软体家具裁剪缝制与填充","成品家具检验与包装"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":100})
data.append({"code":"6-06-03","name":"人造板生产人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事胶合板、刨花板和纤维板等人造板生产的生产人员。负责人造板的原料制备、施胶热压和砂光等工序。","typical_tasks":["木片或刨花原料制备与干燥","调胶施胶与铺装组坯","热压机操作与工艺参数控制","人造板砂光与裁边处理","人造板质量检测与分等"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":20})

# 6-07 造纸和纸制品生产人员
mid = "造纸和纸制品生产人员"
data.append({"code":"6-07-01","name":"制浆造纸人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事木浆、纸浆制备和造纸机操作的生产人员。负责制浆蒸煮、纸浆漂白和纸机抄造等工序。","typical_tasks":["制浆原料蒸煮与洗涤","纸浆漂白与打浆调浆","造纸机上浆与抄造操作","纸页干燥与压光卷取","纸张定量厚度等质量检测"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":30})
data.append({"code":"6-07-02","name":"纸制品加工人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事纸箱、纸盒和卫生纸等纸制品加工的生产人员。负责纸制品的模切、折叠、粘合和成型加工。","typical_tasks":["瓦楞纸板制造与复合操作","纸箱模切与开槽操作","纸盒折叠粘合与成型","卫生纸复卷分切与包装","纸制品质量检验与计数"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":20})

# 6-08 印刷和包装人员
mid = "印刷和包装人员"
data.append({"code":"6-08-01","name":"印刷操作人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事书刊、包装和商业印刷品印刷生产的操作人员。负责印刷机的操作运行、墨色调整和印品质量控制。","typical_tasks":["印刷机上版与套准调整","油墨调配与墨色控制","印刷机运行监控与参数调整","印品质量抽检与色差比对","印刷机清洗保养与故障处理"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":50})
data.append({"code":"6-08-02","name":"包装人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事产品包装、封口和打包作业的生产人员。负责产品的装盒、封箱、贴标和码垛等包装工序。","typical_tasks":["产品装盒装箱与填充","封口机和打包机操作","产品贴标与喷码操作","包装成品码垛与入库","包装设备日常维护与调试"],"education":"初中及以下","salary_median_k":4,"est_employment_wan":100})

# 6-09 文教工美体育用品制造人员
mid = "文教工美体育用品制造人员"
data.append({"code":"6-09-01","name":"文教用品制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事笔、本、文具等文教用品生产制造的生产人员。负责文教用品的成型、装配和质量检验等工序。","typical_tasks":["笔类产品零件加工与组装","本册装订与裁切操作","文具塑料件注塑与组装","文教用品印刷与表面处理","成品质量检测与包装"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":30})
data.append({"code":"6-09-02","name":"工艺品制作人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事陶瓷、漆器、刺绣等工艺美术品制作的生产人员。负责工艺品的造型设计、手工制作和装饰加工。","typical_tasks":["工艺品造型设计与塑型","陶瓷拉坯修坯与施釉烧制","雕刻镂空与表面装饰","漆器髹涂或刺绣缝制","工艺品打磨抛光与包装"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":40})
data.append({"code":"6-09-03","name":"玩具制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事塑料玩具、毛绒玩具和电子玩具等制造的生产人员。负责玩具的注塑成型、缝制组装和功能检测。","typical_tasks":["玩具塑料件注塑与修边","毛绒玩具裁剪缝制与填充","玩具组装与功能调试","玩具安全性能检测","玩具喷涂装饰与包装"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":30})

# 6-10 石油加工和炼焦人员
mid = "石油加工和炼焦人员"
data.append({"code":"6-10-01","name":"石油炼制人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事原油蒸馏、催化裂化和产品精制等石油炼制的生产人员。负责炼油装置的操作运行和工艺参数控制。","typical_tasks":["常减压蒸馏装置操作","催化裂化装置运行与监控","加氢精制装置操作","炼油工艺参数调整与记录","炼油装置巡检与应急处理"],"education":"高中/中专","salary_median_k":7,"est_employment_wan":20})
data.append({"code":"6-10-02","name":"煤炭加工人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事煤炭洗选、炼焦和煤化工等加工的生产人员。负责选煤厂设备操作和焦炉生产运行管理。","typical_tasks":["原煤破碎筛分与洗选操作","焦炉装煤推焦与熄焦作业","煤气净化与副产品回收","焦炭质量检测与分级","煤化工设备运行与维护"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":30})

# 6-11 化学品制造人员
mid = "化学品制造人员"
data.append({"code":"6-11-01","name":"基本化学原料制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事酸、碱、盐等基本化学原料生产的生产人员。负责化工反应装置的操作运行和产品质量控制。","typical_tasks":["化工反应釜投料与反应操作","蒸馏精馏塔运行与调节","化工产品结晶与干燥","生产装置巡检与参数记录","化工原料储罐管理与出入库"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":50})
data.append({"code":"6-11-02","name":"化学肥料制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事氮肥、磷肥、复合肥等化学肥料生产的生产人员。负责合成氨、尿素和复混肥等生产装置的操作。","typical_tasks":["合成氨装置操作与气体净化","尿素合成塔运行与产品造粒","磷酸生产与磷肥加工操作","复合肥配料混合与造粒","化肥产品包装与质量检测"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":30})
data.append({"code":"6-11-03","name":"农药制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事杀虫剂、除草剂和杀菌剂等农药生产的生产人员。负责农药原药合成和制剂加工的生产操作。","typical_tasks":["农药原药合成反应操作","农药制剂配方调配","乳剂悬浮剂等剂型加工","农药产品灌装与包装","有毒废气废水处理操作"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":15})
data.append({"code":"6-11-04","name":"涂料油墨制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事涂料、油墨和颜料等产品生产的生产人员。负责涂料油墨的配方调制、研磨分散和灌装包装。","typical_tasks":["涂料配方原料称量与配料","高速分散机研磨操作","涂料调色与色差检测","油墨研磨与细度调整","涂料产品灌装与包装"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":20})
data.append({"code":"6-11-05","name":"合成材料制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事合成树脂、合成橡胶和合成纤维单体等生产的生产人员。负责聚合反应装置操作和产品后处理工序。","typical_tasks":["聚合反应釜投料与聚合操作","聚合物脱挥与造粒加工","合成橡胶凝聚与干燥","合成材料产品质量检测","聚合装置清洗与维护"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":40})
data.append({"code":"6-11-06","name":"日用化学品制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事洗涤用品、化妆品和日用化学品生产的生产人员。负责日化产品的配料乳化、灌装和包装操作。","typical_tasks":["日化产品原料称量与配制","乳化锅操作与均质乳化","洗涤液灌装与封口操作","化妆品灌装与外观检查","日化产品包装贴标与入库"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":25})

# 6-12 医药制造人员
mid = "医药制造人员"
data.append({"code":"6-12-01","name":"化学药品制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事化学原料药和制剂生产的医药制造人员。负责药品合成反应、制剂生产和GMP规范操作。","typical_tasks":["原料药合成反应与中间体纯化","片剂压片与胶囊充填操作","注射剂配液灌装与灭菌","药品生产批记录填写与复核","洁净区环境监测与GMP管理"],"education":"大专","salary_median_k":7,"est_employment_wan":40})
data.append({"code":"6-12-02","name":"中药制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事中药饮片加工和中成药制造的医药生产人员。负责中药材炮制、提取和中药制剂的生产操作。","typical_tasks":["中药材炮制与饮片加工","中药提取浓缩与纯化操作","中药丸散膏丹制剂生产","中药制剂包装与质量检查","中药生产设备清洁与验证"],"education":"大专","salary_median_k":6,"est_employment_wan":30})
data.append({"code":"6-12-03","name":"生物制药人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事生物制品和生物药物生产的医药制造人员。负责细胞培养、发酵和生物制品纯化等生产操作。","typical_tasks":["细胞培养与生物反应器操作","微生物发酵罐接种与发酵","蛋白质纯化与层析操作","生物制品分装与冻干","无菌环境监控与污染防控"],"education":"大专","salary_median_k":8,"est_employment_wan":20})
data.append({"code":"6-12-04","name":"医疗器械制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事医疗器械和医用耗材生产制造的生产人员。负责医疗器械的零部件加工、装配和灭菌包装。","typical_tasks":["医疗器械精密零件加工","医疗器械整机装配与调试","医用耗材注塑成型与组装","医疗器械灭菌与无菌包装","医疗器械性能检测与记录"],"education":"大专","salary_median_k":7,"est_employment_wan":25})

# 6-13 化学纤维制造人员
mid = "化学纤维制造人员"
data.append({"code":"6-13-01","name":"化学纤维生产人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事涤纶、锦纶、粘胶等化学纤维生产的生产人员。负责化纤纺丝、拉伸和卷绕等工序的设备操作。","typical_tasks":["化纤原料熔融挤出与纺丝操作","纤维拉伸定型与卷绕","化纤短纤维切断与打包","纺丝组件清洗与更换","化纤产品质量检测与分级"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":20})

# 6-14 橡胶和塑料制品制造人员
mid = "橡胶和塑料制品制造人员"
data.append({"code":"6-14-01","name":"橡胶制品制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事轮胎、胶管、密封件等橡胶制品生产的生产人员。负责橡胶的炼胶、成型和硫化等工序操作。","typical_tasks":["橡胶混炼与胶料制备","轮胎成型机操作与贴合","橡胶制品硫化与脱模","橡胶制品修边与外观检查","橡胶制品物理性能测试"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":40})
data.append({"code":"6-14-02","name":"塑料制品制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事塑料注塑、挤出和吹塑等成型加工的生产人员。负责塑料制品的注塑成型、修整和质量检验。","typical_tasks":["注塑机操作与模具安装调试","塑料管材挤出成型操作","吹塑机操作与中空制品成型","塑料制品修边与外观检查","注塑工艺参数调整与记录"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":80})

# 6-15 非金属矿物制品制造人员
mid = "非金属矿物制品制造人员"
data.append({"code":"6-15-01","name":"水泥制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事水泥熟料煅烧和水泥粉磨的生产人员。负责水泥回转窑和磨机等主要设备的操作运行。","typical_tasks":["生料磨操作与配料控制","回转窑点火与煅烧操作","水泥磨粉磨操作与细度控制","中控室DCS系统监控与调节","水泥质量检测与出厂管理"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":50})
data.append({"code":"6-15-02","name":"玻璃制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事平板玻璃和玻璃制品生产的生产人员。负责玻璃窑炉操作、成型和退火等工序的生产管理。","typical_tasks":["玻璃配料称量与混合","玻璃窑炉加料与温度控制","浮法玻璃成型与拉边操作","玻璃退火窑温度曲线控制","玻璃切割与质量等级检验"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":30})
data.append({"code":"6-15-03","name":"陶瓷制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事建筑陶瓷、卫生陶瓷和日用陶瓷生产的生产人员。负责陶瓷原料制备、成型、施釉和烧成等工序。","typical_tasks":["陶瓷泥料球磨与配制","陶瓷坯体压制或注浆成型","坯体施釉与装饰","隧道窑或辊道窑烧成操作","陶瓷产品分选与质量分等"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":40})
data.append({"code":"6-15-04","name":"耐火材料制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事耐火砖、浇注料等耐火材料生产的生产人员。负责耐火材料的配料成型、干燥烧成等生产操作。","typical_tasks":["耐火原料破碎筛分与配料","耐火砖机压成型操作","耐火材料干燥与烧成","不定形耐火材料搅拌与包装","耐火材料理化性能检测"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":15})

# 6-16 金属冶炼和压延加工人员
mid = "金属冶炼和压延加工人员"
data.append({"code":"6-16-01","name":"钢铁冶炼人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事高炉炼铁、转炉炼钢和连铸等钢铁冶炼的生产人员。负责冶金炉窑的操作运行和钢铁产品质量控制。","typical_tasks":["高炉上料与炉况判断调整","转炉吹炼与钢水成分控制","连铸机操作与铸坯质量监控","炉前取样与温度测量","冶金设备维护与耐材更换"],"education":"高中/中专","salary_median_k":7,"est_employment_wan":80})
data.append({"code":"6-16-02","name":"有色金属冶炼人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事铜、铝、锌等有色金属冶炼和精炼的生产人员。负责有色金属冶炼炉窑和电解槽等设备的操作。","typical_tasks":["矿石熔炼与粗金属冶炼操作","电解精炼槽操作与维护","有色金属铸锭与浇注","冶炼烟气收尘与环保处理","产品成分检测与品级判定"],"education":"高中/中专","salary_median_k":7,"est_employment_wan":30})
data.append({"code":"6-16-03","name":"金属压延加工人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事钢材和有色金属轧制加工的生产人员。负责热轧、冷轧生产线的轧机操作和产品质量控制。","typical_tasks":["加热炉操作与钢坯加热","轧机操作与轧制参数调整","冷轧机组运行与厚度控制","轧材精整与表面质量检查","轧钢产品切割与打包"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":50})

# 6-17 金属制品制造人员
mid = "金属制品制造人员"
data.append({"code":"6-17-01","name":"金属结构制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事钢结构件、金属构件制造和安装的生产人员。负责钢结构的下料、组装、焊接和防腐处理。","typical_tasks":["钢结构件放样与下料切割","钢构件组装与定位点焊","钢结构焊接与焊缝检测","钢结构除锈与防腐涂装","钢结构件出厂检验与编号"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":60})
data.append({"code":"6-17-02","name":"金属工具制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事刀具、量具和手工工具等金属工具制造的生产人员。负责金属工具的锻造、机加工和热处理。","typical_tasks":["工具毛坯锻造与退火","刀具机械加工与精密磨削","工具热处理淬火与回火","工具刃口研磨与精度检测","工具防锈包装与入库"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":30})
data.append({"code":"6-17-03","name":"集装箱和金属包装容器制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事集装箱、金属桶罐等金属包装容器制造的生产人员。负责金属容器的冲压、焊接和涂装等工序。","typical_tasks":["金属板材剪切与冲压成型","集装箱面板焊接与组装","金属容器封口与密封检测","容器内外涂装与烘干","集装箱水密性检测与整修"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":20})

# 6-18 通用设备制造人员
mid = "通用设备制造人员"
data.append({"code":"6-18-01","name":"锅炉及原动设备制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事锅炉、汽轮机和内燃机等原动设备制造的生产人员。负责锅炉和动力设备的零部件加工与装配。","typical_tasks":["锅炉受压元件加工与焊接","汽轮机叶片精密加工","锅炉部件组装与水压试验","原动设备整机装配与调试","压力容器焊缝无损检测"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":20})
data.append({"code":"6-18-02","name":"金属切削机床操作人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事各类金属切削机床操作加工的生产人员。负责普通车床、铣床和加工中心等机床设备的操作。","typical_tasks":["工件装夹与刀具选用安装","机床操作与切削参数设定","工件尺寸测量与精度检验","机床日常润滑与保养","加工工艺文件执行与记录"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":50})
data.append({"code":"6-18-03","name":"起重运输设备制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事起重机、输送机等起重运输设备制造的生产人员。负责起重设备的结构件加工、装配和试运转。","typical_tasks":["起重机结构件下料与焊接","起重设备机械部件装配","电气控制系统安装与接线","整机试运转与载荷试验","设备涂装与出厂检验"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":25})
data.append({"code":"6-18-04","name":"泵阀压缩机制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事泵、阀门和压缩机等通用机械制造的生产人员。负责泵阀零部件的精密加工和整机装配调试。","typical_tasks":["泵阀铸件机加工与精密配合","阀门密封面研磨与试压","压缩机转子动平衡校验","泵阀整机装配与性能测试","产品防腐包装与出厂"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":20})

# 6-19 专用设备制造人员
mid = "专用设备制造人员"
data.append({"code":"6-19-01","name":"采矿设备制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事矿山采掘设备和选矿设备制造的生产人员。负责采矿机械的零部件加工、装配和试运转。","typical_tasks":["采矿设备结构件焊接加工","矿山机械部件装配","采掘设备液压系统安装调试","选矿设备整机试运转","矿山设备耐磨件更换与检修"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":20})
data.append({"code":"6-19-02","name":"建筑工程设备制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事挖掘机、装载机和混凝土机械等建筑设备制造的生产人员。负责工程机械的零部件加工和整机装配。","typical_tasks":["工程机械结构件焊接","液压缸和液压马达装配","工程机械整机组装与调试","发动机和变速箱安装调校","建筑设备出厂检测与交付"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":30})
data.append({"code":"6-19-03","name":"纺织机械制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事纺纱机、织机等纺织机械制造的生产人员。负责纺织设备的精密零件加工和整机装配调试。","typical_tasks":["纺织机械精密零件加工","纺机传动系统装配","织机综框和打纬机构安装","纺织设备电气系统调试","整机空运转试验与出厂"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":15})
data.append({"code":"6-19-04","name":"农业机械制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事拖拉机、收割机等农业机械制造的生产人员。负责农机产品的零部件加工、装配和出厂调试。","typical_tasks":["农机结构件冲压与焊接","拖拉机变速箱装配","收割机割台与脱粒装置装配","农机整机装配与性能调试","农业机械涂装与出厂检验"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":25})
data.append({"code":"6-19-05","name":"食品加工机械制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事食品加工设备和包装机械制造的生产人员。负责食品机械的不锈钢部件加工和整机装配。","typical_tasks":["不锈钢部件切割与焊接抛光","食品机械传动系统装配","灌装封口设备组装与调试","食品机械电气控制系统安装","整机清洗试运行与出厂"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":15})

# 6-20 汽车制造人员
mid = "汽车制造人员"
data.append({"code":"6-20-01","name":"汽车整车制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事汽车冲压、焊装、涂装和总装等整车制造的生产人员。负责汽车生产线各工位的操作和质量控制。","typical_tasks":["车身冲压件操作与质检","车身焊装与点焊操作","车身涂装喷漆与烘干","汽车总装线部件安装","整车下线检测与路试"],"education":"高中/中专","salary_median_k":7,"est_employment_wan":200})
data.append({"code":"6-20-02","name":"汽车零部件制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事汽车发动机、变速箱和底盘等零部件制造的生产人员。负责汽车零部件的机加工、装配和质量检验。","typical_tasks":["汽车零部件精密机加工","发动机缸体缸盖加工","汽车零部件装配与力矩控制","零部件尺寸与性能检测","汽车线束制造与检测"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":300})
data.append({"code":"6-20-03","name":"新能源汽车制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事电动汽车动力电池、电驱系统和整车制造的生产人员。负责新能源汽车三电系统的装配和测试。","typical_tasks":["动力电池模组装配与检测","电驱动总成装配与调试","高压线束连接与绝缘检测","新能源整车电气系统联调","充电功能测试与整车标定"],"education":"大专","salary_median_k":7,"est_employment_wan":80})

# 6-21 铁路船舶航空设备制造人员
mid = "铁路船舶航空设备制造人员"
data.append({"code":"6-21-01","name":"铁路机车车辆制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事机车、客车和动车组等铁路车辆制造的生产人员。负责铁路车辆的车体焊接、装配和调试。","typical_tasks":["铁路车辆车体焊接与组装","转向架装配与调整","车辆内装饰施工与安装","牵引电气系统接线与调试","整车静态与动态调试试验"],"education":"高中/中专","salary_median_k":7,"est_employment_wan":40})
data.append({"code":"6-21-02","name":"船舶制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事各类船舶建造和舾装的生产人员。负责船体分段制作、合拢焊接和船舶舾装等工序。","typical_tasks":["船体钢板切割与分段制作","船体分段合拢与焊接","船舶管路和电缆敷设","船舶机电设备安装与调试","船舶下水前密性试验"],"education":"高中/中专","salary_median_k":7,"est_employment_wan":30})
data.append({"code":"6-21-03","name":"航空器部件制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事飞机机体结构件和发动机零部件制造的生产人员。负责航空零部件的精密加工、装配和质量检测。","typical_tasks":["航空零部件数控精密加工","飞机复合材料构件铺贴成型","航空部件装配与铆接","航空零部件表面处理与防护","航空产品检测与质量追溯"],"education":"大专","salary_median_k":8,"est_employment_wan":20})

# 6-22 电气机械和器材制造人员
mid = "电气机械和器材制造人员"
data.append({"code":"6-22-01","name":"电动机和发电机制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事电动机、发电机等旋转电机制造的生产人员。负责电机的铁芯冲片叠装、绕线嵌线和整机装配。","typical_tasks":["电机铁芯冲片与叠压","电机定子绕组嵌线与接线","电机转子动平衡校正","电机整机装配与气隙调整","电机性能试验与出厂检测"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":40})
data.append({"code":"6-22-02","name":"变压器和整流器制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事变压器、整流器等电力变换设备制造的生产人员。负责变压器的铁芯叠装、线圈绕制和整机装配。","typical_tasks":["变压器铁芯叠装与夹紧","变压器线圈绕制与绝缘处理","变压器器身装配与注油","变压器耐压与空载试验","整流设备组装与功能测试"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":25})
data.append({"code":"6-22-03","name":"电线电缆制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事电线、电缆和光缆生产制造的生产人员。负责导体拉丝、绝缘挤出和电缆成缆等工序操作。","typical_tasks":["铜铝导体拉丝与绞合","绝缘材料挤出与包覆","多芯电缆成缆与铠装","电线电缆耐压与电阻检测","电缆成圈包装与标识"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":30})
data.append({"code":"6-22-04","name":"电池制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事锂电池、铅酸电池等各类电池生产制造的生产人员。负责电池的极片制作、组装和化成检测。","typical_tasks":["电池正负极浆料涂布","极片辊压分切与叠片","电芯组装与注液封口","电池化成分容与分选","电池模组PACK组装与测试"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":60})

# 6-23 计算机通信和电子设备制造人员
mid = "计算机通信和电子设备制造人员"
data.append({"code":"6-23-01","name":"电子元器件制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事电阻、电容、电感等电子元器件生产的生产人员。负责电子元器件的成型、烧结和性能检测。","typical_tasks":["电子元器件原料配制与成型","陶瓷电容器烧结与端电极处理","电感线圈绕制与焊接","电子元器件参数测试与筛选","元器件编带包装与标识"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":200})
data.append({"code":"6-23-02","name":"半导体器件制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事二极管、三极管和功率器件等半导体器件制造的生产人员。负责半导体晶圆加工和器件封装测试。","typical_tasks":["晶圆清洗与光刻操作","半导体扩散与离子注入","芯片减薄与划片","半导体器件引线键合封装","器件电气参数测试与分选"],"education":"大专","salary_median_k":7,"est_employment_wan":60})
data.append({"code":"6-23-03","name":"集成电路制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事集成电路晶圆制造和芯片封装测试的生产人员。负责集成电路的光刻、刻蚀、薄膜沉积等前道工序和后道封测。","typical_tasks":["集成电路光刻与曝光操作","等离子刻蚀与薄膜沉积","化学机械抛光(CMP)操作","集成电路芯片封装","芯片功能测试与良率分析"],"education":"大专","salary_median_k":8,"est_employment_wan":40})
data.append({"code":"6-23-04","name":"电子终端产品装配人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事手机、电脑和平板等电子终端产品装配的生产人员。负责电子产品的SMT贴片、组装和功能测试。","typical_tasks":["SMT贴片机操作与回流焊接","电子产品主板组装与连接","屏幕模组与外壳装配","电子产品功能测试与调试","产品外观检查与包装"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":300})
data.append({"code":"6-23-05","name":"通信设备制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事基站、交换机和光通信设备等通信设备制造的生产人员。负责通信设备的电路板加工、整机装配和调测。","typical_tasks":["通信设备电路板SMT加工","通信设备整机组装与布线","射频模块调试与校准","通信设备整机联调与测试","设备老化筛选与出厂检验"],"education":"大专","salary_median_k":7,"est_employment_wan":50})
data.append({"code":"6-23-06","name":"光电子器件制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事LED、激光器和光探测器等光电子器件制造的生产人员。负责光电子芯片的外延生长、制造和封装。","typical_tasks":["光电子芯片外延片生长","LED芯片制造与测试分选","光电子器件封装与点胶","光纤耦合与光路对准","光电器件光电参数测试"],"education":"大专","salary_median_k":7,"est_employment_wan":20})

# 6-24 仪器仪表制造人员
mid = "仪器仪表制造人员"
data.append({"code":"6-24-01","name":"通用仪器仪表制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事温度、压力、流量等通用仪器仪表制造的生产人员。负责仪器仪表的零部件加工、装配和校准。","typical_tasks":["仪表精密零件加工与装配","仪表传感器安装与接线","仪器仪表功能调试与校准","仪表外壳组装与密封","仪器仪表检定与出厂检验"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":25})
data.append({"code":"6-24-02","name":"光学仪器制造人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事显微镜、望远镜和光学测量仪器等光学仪器制造的生产人员。负责光学零件加工和光学系统装调。","typical_tasks":["光学镜片研磨与抛光","光学零件镀膜操作","光学系统装配与调校","光学仪器性能测试与标定","光学零件清洁与防护包装"],"education":"大专","salary_median_k":7,"est_employment_wan":10})

# 6-25 建筑施工人员
mid = "建筑施工人员"
data.append({"code":"6-25-01","name":"砌筑工","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事砖石砌体施工的建筑施工人员。负责使用砖、石和砌块等材料砌筑墙体、柱子等建筑构件。","typical_tasks":["砌体放线与排砖撂底","砖墙砌筑与灰缝控制","砌体拉结筋和构造柱设置","砌体墙面勾缝处理","砌筑质量自检与垂直度校正"],"education":"初中及以下","salary_median_k":6,"est_employment_wan":200})
data.append({"code":"6-25-02","name":"混凝土工","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事混凝土搅拌、运输、浇筑和养护的建筑施工人员。负责混凝土工程的模板支设、浇筑振捣和拆模养护。","typical_tasks":["混凝土模板支设与加固","混凝土浇筑与振捣操作","混凝土表面收光与抹平","混凝土拆模与养护","混凝土试块制作与强度检测"],"education":"初中及以下","salary_median_k":6,"est_employment_wan":150})
data.append({"code":"6-25-03","name":"钢筋工","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事钢筋加工和绑扎安装的建筑施工人员。负责钢筋的下料加工、绑扎连接和预埋件安装。","typical_tasks":["钢筋下料切断与弯曲成型","钢筋绑扎与焊接连接","钢筋骨架制作与安装","预埋件定位与固定","钢筋保护层垫块设置"],"education":"初中及以下","salary_median_k":7,"est_employment_wan":120})
data.append({"code":"6-25-04","name":"架子工","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事脚手架搭设和拆除的建筑施工人员。负责各类脚手架、支撑架和卸料平台的搭设与维护。","typical_tasks":["脚手架搭设方案交底","扣件式脚手架搭设与连墙件设置","悬挑架与爬架安装操作","脚手架日常巡查与维护加固","脚手架安全拆除与材料归整"],"education":"初中及以下","salary_median_k":7,"est_employment_wan":80})
data.append({"code":"6-25-05","name":"防水工","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事建筑防水工程施工的建筑施工人员。负责屋面、地下室和卫生间等部位的防水材料铺贴和涂刷。","typical_tasks":["防水基层处理与找平","防水卷材热熔铺贴操作","防水涂料涂刷与节点加强","细部构造防水处理","防水层闭水试验与验收"],"education":"初中及以下","salary_median_k":6,"est_employment_wan":40})
data.append({"code":"6-25-06","name":"装饰装修工","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事建筑室内外装饰装修施工的建筑施工人员。负责墙面、地面和天棚的抹灰、贴砖、涂料等装修施工。","typical_tasks":["墙面抹灰与找平处理","地面铺贴瓷砖与石材","吊顶龙骨安装与面板固定","墙面乳胶漆或壁纸施工","木饰面安装与收口处理"],"education":"初中及以下","salary_median_k":6,"est_employment_wan":300})
data.append({"code":"6-25-07","name":"水电安装工","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事建筑给排水和电气管线安装的建筑施工人员。负责水管、电线管路的预埋布设和设备安装。","typical_tasks":["给排水管道切割与连接安装","电气线管预埋与穿线","配电箱安装与回路接线","卫浴设备和灯具安装","管线打压试验与通电调试"],"education":"初中及以下","salary_median_k":7,"est_employment_wan":200})

# 6-26 电力热力生产和供应人员
mid = "电力热力生产和供应人员"
data.append({"code":"6-26-01","name":"火力发电运行人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事火力发电厂锅炉、汽轮机和发电机组运行操作的生产人员。负责发电机组的启停操作和运行参数监控。","typical_tasks":["锅炉点火启动与运行调整","汽轮机组运行操作与监控","发电机并网与负荷调整","DCS集控系统操作与巡检","机组异常工况处理与应急操作"],"education":"大专","salary_median_k":7,"est_employment_wan":30})
data.append({"code":"6-26-02","name":"水力发电运行人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事水力发电站水轮发电机组运行操作的生产人员。负责水电站机组启停、运行监控和水库调度配合。","typical_tasks":["水轮发电机组启停操作","机组运行参数监控与调整","闸门启闭与水位调度配合","水电站设备巡回检查","机组故障判断与应急处理"],"education":"大专","salary_median_k":7,"est_employment_wan":10})
data.append({"code":"6-26-03","name":"风力和太阳能发电运行人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事风力发电和光伏发电设备运行维护的生产人员。负责风电机组和光伏电站的运行监控和日常维护。","typical_tasks":["风电机组远程监控与启停操作","风机定期巡检与叶片检查","光伏组件清洗与阵列巡检","逆变器和箱变运行监控","新能源发电设备故障诊断与处理"],"education":"大专","salary_median_k":7,"est_employment_wan":20})
data.append({"code":"6-26-04","name":"输配电线路工","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事输电和配电线路施工与运行维护的生产人员。负责高低压线路的架设、检修和带电作业。","typical_tasks":["输配电线路杆塔组立","导线架设与紧线操作","线路绝缘子和金具更换","配电线路故障巡查与抢修","高压线路带电检修作业"],"education":"高中/中专","salary_median_k":7,"est_employment_wan":40})

# 6-27 燃气和水生产供应人员
mid = "燃气和水生产供应人员"
data.append({"code":"6-27-01","name":"燃气生产和输配人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事天然气和液化气输配供应的生产人员。负责燃气管网运行维护、调压站管理和用户通气服务。","typical_tasks":["燃气管网巡线与泄漏检测","调压站设备运行与参数调整","燃气管道抢修与焊接","燃气用户通气点火服务","燃气输配SCADA系统监控"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":15})
data.append({"code":"6-27-02","name":"水处理人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事自来水净化和污水处理的生产人员。负责给水厂和污水处理厂工艺设备的操作运行和水质监测。","typical_tasks":["原水混凝沉淀与过滤操作","自来水消毒与出厂水质监测","污水处理生化池运行管理","污泥脱水与处置操作","水处理药剂投加与设备维护"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":20})

# 6-28 废弃资源综合利用人员
mid = "废弃资源综合利用人员"
data.append({"code":"6-28-01","name":"再生资源回收人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事废旧金属、废纸、废塑料等再生资源回收的生产人员。负责可回收废弃物的分类收集和初步处理。","typical_tasks":["废旧物资上门收购与称重","再生资源分类分拣","废旧金属和废纸打包压缩","回收物资登记与价格核算","再生资源暂存与转运"],"education":"初中及以下","salary_median_k":4,"est_employment_wan":100})
data.append({"code":"6-28-02","name":"废旧物资加工处理人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事废旧物资拆解和再利用加工的生产人员。负责废旧电器电子产品拆解和废旧材料的再生利用加工。","typical_tasks":["废旧家电拆解与有害物质分离","废塑料清洗破碎与造粒","废旧金属剪切与分选","电子废弃物贵金属提取","废旧轮胎破碎与橡胶再生"],"education":"初中及以下","salary_median_k":4,"est_employment_wan":50})

# 6-29 机械加工人员
mid = "机械加工人员"
data.append({"code":"6-29-01","name":"车工","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事车床操作加工的机械加工人员。负责使用普通车床或数控车床对工件进行车削加工。","typical_tasks":["工件装夹找正与刀具对刀","外圆和端面车削加工","内孔镗削与螺纹车削","锥面和成型面车削操作","工件尺寸测量与公差控制"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":80})
data.append({"code":"6-29-02","name":"铣工","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事铣床操作加工的机械加工人员。负责使用铣床对工件进行平面、沟槽和齿轮等铣削加工。","typical_tasks":["铣床工件装夹与铣刀安装","平面和台阶面铣削加工","键槽和T形槽铣削","齿轮和花键铣削操作","铣削工艺参数选择与调整"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":40})
data.append({"code":"6-29-03","name":"磨工","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事磨床操作加工的机械加工人员。负责使用平面磨床和外圆磨床对工件进行精密磨削。","typical_tasks":["砂轮选择安装与修整","外圆磨削与内圆磨削操作","平面精密磨削加工","工件表面粗糙度检测","磨削余量控制与尺寸精度保证"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":25})
data.append({"code":"6-29-04","name":"钳工","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事零件划线、锉削、钻孔和装配等手工加工的机械加工人员。负责机械零部件的手工精密加工和设备装配调试。","typical_tasks":["零件划线与锯切下料","锉削与刮研配合面加工","钻孔攻丝与铰孔操作","零部件装配与间隙调整","设备精度检测与故障排除"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":100})
data.append({"code":"6-29-05","name":"数控机床操作人员","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事数控机床编程和操作加工的机械加工人员。负责数控车床、加工中心等设备的程序编制和操作运行。","typical_tasks":["数控加工程序编制与调试","数控机床对刀与工件装夹","数控机床运行监控与参数修正","加工零件首件检验与批量生产","数控机床日常保养与刀具管理"],"education":"高中/中专","salary_median_k":7,"est_employment_wan":80})

# 6-30 焊接人员
mid = "焊接人员"
data.append({"code":"6-30-01","name":"电焊工","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事手工电弧焊、气体保护焊和埋弧焊等电焊操作的生产人员。负责金属结构和管道的焊接施工。","typical_tasks":["焊接接头坡口加工与组对","手工电弧焊和CO2气保焊操作","氩弧焊打底与多层多道焊","焊缝外观检查与缺陷返修","焊接设备维护与焊材管理"],"education":"高中/中专","salary_median_k":7,"est_employment_wan":150})
data.append({"code":"6-30-02","name":"气焊工","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事氧乙炔气焊、气割和钎焊等操作的生产人员。负责金属工件的气焊连接和气割下料。","typical_tasks":["氧乙炔火焰调节与气焊操作","金属构件气割下料","铜管和薄板气焊焊接","钎焊操作与焊后清理","气瓶安全使用与焊具维护"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":30})

# 6-31 金属热处理和表面处理人员
mid = "金属热处理和表面处理人员"
data.append({"code":"6-31-01","name":"热处理工","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事金属工件退火、淬火和回火等热处理操作的生产人员。负责金属零件的热处理工艺操作和质量控制。","typical_tasks":["热处理炉温度设定与预热","工件淬火与冷却介质选择","工件回火与消除应力处理","热处理后硬度和金相检测","热处理设备维护与炉温校验"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":30})
data.append({"code":"6-31-02","name":"电镀工","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事金属零件电镀和化学镀等表面处理的生产人员。负责镀前处理、电镀操作和镀后质量检测。","typical_tasks":["工件除油除锈等镀前处理","电镀槽液配制与维护","镀铬镀锌等电镀操作","镀层厚度与结合力检测","电镀废水处理与达标排放"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":25})
data.append({"code":"6-31-03","name":"涂装工","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事金属和非金属制品表面涂装的生产人员。负责工件的表面处理、喷涂和烘干等涂装工序操作。","typical_tasks":["工件表面打磨与底漆喷涂","面漆调配与喷枪喷涂操作","静电喷涂与粉末涂装","涂装件烘干与漆膜检测","喷漆房维护与废气处理"],"education":"高中/中专","salary_median_k":5,"est_employment_wan":40})

# 6-32 铸造和锻造人员
mid = "铸造和锻造人员"
data.append({"code":"6-32-01","name":"铸造工","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事金属铸造生产的生产人员。负责铸型制作、金属熔炼和浇注等铸造工序操作。","typical_tasks":["砂型造型与制芯操作","铸造合金熔炼与成分调整","金属液浇注与补缩","铸件落砂清理与打磨","铸件缺陷检查与质量检测"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":40})
data.append({"code":"6-32-02","name":"锻造工","major_category":MC6,"major_category_code":6,"mid_category":mid,"description":"从事金属锻造加工的生产人员。负责金属坯料的加热、锻打和模锻等锻造工序操作。","typical_tasks":["锻造坯料加热与温度控制","自由锻锤操作与锻件成型","模锻压力机操作与模具管理","锻件切边与热处理","锻件尺寸检测与缺陷探伤"],"education":"高中/中专","salary_median_k":6,"est_employment_wan":25})

# Write output
output_path = "/Users/liuhongjie/software/project/china-ai-jobs/data/batch_3.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Total entries: {len(data)}")

# Count by major category
mc5_count = sum(1 for d in data if d["major_category_code"] == 5)
mc6_count = sum(1 for d in data if d["major_category_code"] == 6)
print(f"大类5 entries: {mc5_count}")
print(f"大类6 entries: {mc6_count}")

mc5_emp = sum(d["est_employment_wan"] for d in data if d["major_category_code"] == 5)
mc6_emp = sum(d["est_employment_wan"] for d in data if d["major_category_code"] == 6)
print(f"大类5 total employment: {mc5_emp}万")
print(f"大类6 total employment: {mc6_emp}万")
