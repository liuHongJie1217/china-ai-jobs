#!/usr/bin/env python3
"""Merge all batch files + categories 7-8 into final occupations.json"""
import json, os

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Load batches
all_data = []
for i in range(1, 4):
    with open(f"data/batch_{i}.json", encoding="utf-8") as f:
        batch = json.load(f)
        all_data.extend(batch)
        print(f"batch_{i}.json: {len(batch)} entries")

# Add Category 7: 军人
cat7 = [
    {
        "code": "7-01-01", "name": "军官",
        "major_category": "军人", "major_category_code": 7,
        "mid_category": "中国人民解放军",
        "description": "在中国人民解放军中担任排级以上职务或者初级以上专业技术职务的现役军人",
        "typical_tasks": ["部队日常管理与训练组织", "作战方案拟制与战术演练", "军事理论学习与研究", "武器装备使用与管理", "部队政治教育与思想工作"],
        "education": "本科", "salary_median_k": 12, "est_employment_wan": 90
    },
    {
        "code": "7-01-02", "name": "军士",
        "major_category": "军人", "major_category_code": 7,
        "mid_category": "中国人民解放军",
        "description": "在中国人民解放军中服现役并被授予军士军衔的士兵，是军队专业技术和作战骨干",
        "typical_tasks": ["专业技术装备操作与维护", "班组战术训练与体能训练", "新兵传帮带与技能培训", "装备日常保养与故障排除", "战备值班与执勤任务执行"],
        "education": "高中/中专", "salary_median_k": 7, "est_employment_wan": 80
    },
    {
        "code": "7-01-03", "name": "义务兵",
        "major_category": "军人", "major_category_code": 7,
        "mid_category": "中国人民解放军",
        "description": "依照法律规定在中国人民解放军中服义务兵役的现役军人",
        "typical_tasks": ["军事基础训练与体能达标", "武器装备基本操作学习", "营区警卫与日常执勤", "军事科目考核与演练", "内务整理与条令条例学习"],
        "education": "高中/中专", "salary_median_k": 4, "est_employment_wan": 40
    },
    {
        "code": "7-01-04", "name": "军队文职人员",
        "major_category": "军人", "major_category_code": 7,
        "mid_category": "中国人民解放军",
        "description": "在军队编制岗位从事管理和专业技术工作的非现役人员",
        "typical_tasks": ["军队院校教学与科研工作", "军队医疗卫生保障服务", "军事科技研发与技术支持", "军队机关行政与后勤管理", "军事训练保障与装备管理"],
        "education": "本科", "salary_median_k": 10, "est_employment_wan": 20
    }
]
all_data.extend(cat7)
print(f"大类7 军人: 4 entries")

# Add Category 8: 不便分类的其他从业人员
cat8 = [
    {
        "code": "8-01-01", "name": "自由职业者",
        "major_category": "不便分类的其他从业人员", "major_category_code": 8,
        "mid_category": "其他从业人员",
        "description": "不隶属于任何组织，自主安排工作的独立从业人员，涵盖自媒体人、独立咨询师等",
        "typical_tasks": ["自主承接项目与商务洽谈", "专业技能服务交付与质量把控", "个人品牌建设与客户关系维护", "财务收支管理与税务申报", "持续学习与专业技能更新"],
        "education": "大专", "salary_median_k": 8, "est_employment_wan": 300
    },
    {
        "code": "8-01-02", "name": "平台经济从业人员",
        "major_category": "不便分类的其他从业人员", "major_category_code": 8,
        "mid_category": "其他从业人员",
        "description": "依托互联网平台从事各类灵活就业的从业人员，如直播带货、共享经济服务等",
        "typical_tasks": ["平台接单与任务执行", "线上内容创作与粉丝运营", "平台规则学习与账号管理", "客户沟通与售后服务处理", "收入结算与数据复盘分析"],
        "education": "高中/中专", "salary_median_k": 6, "est_employment_wan": 400
    },
    {
        "code": "8-01-03", "name": "其他未分类从业人员",
        "major_category": "不便分类的其他从业人员", "major_category_code": 8,
        "mid_category": "其他从业人员",
        "description": "从事难以归入上述各大类职业的其他各类工作的从业人员",
        "typical_tasks": ["日常工作任务执行与完成", "工作场所整理与物料准备", "工作记录与信息报告", "安全规程遵守与劳动保护", "岗位技能学习与适应性调整"],
        "education": "初中及以下", "salary_median_k": 4, "est_employment_wan": 100
    }
]
all_data.extend(cat8)
print(f"大类8 其他: 3 entries")

# Sort by code
all_data.sort(key=lambda x: x["code"])

# Validate
errors = []
codes = set()
for i, entry in enumerate(all_data):
    # Check required fields
    required = ["code","name","major_category","major_category_code","mid_category","description","typical_tasks","education","salary_median_k","est_employment_wan"]
    for f in required:
        if f not in entry:
            errors.append(f"Entry {i}: missing field '{f}'")
    # Check typical_tasks count
    if len(entry.get("typical_tasks", [])) != 5:
        errors.append(f"Entry {i} ({entry['code']}): has {len(entry.get('typical_tasks',[]))} tasks, expected 5")
    # Check education values
    valid_edu = ["初中及以下", "高中/中专", "大专", "本科", "硕士及以上"]
    if entry.get("education") not in valid_edu:
        errors.append(f"Entry {i} ({entry['code']}): invalid education '{entry.get('education')}'")
    # Check duplicate codes
    if entry["code"] in codes:
        errors.append(f"Entry {i}: duplicate code '{entry['code']}'")
    codes.add(entry["code"])

if errors:
    print(f"\n⚠ {len(errors)} validation errors:")
    for e in errors[:20]:
        print(f"  {e}")
else:
    print(f"\n✓ All entries validated successfully")

# Write output
with open("data/occupations.json", "w", encoding="utf-8") as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)

# Statistics
print(f"\n{'='*60}")
print(f"总条目数: {len(all_data)}")
print(f"{'='*60}")
print(f"{'大类':<40s} {'条目':>5s} {'就业(万)':>10s} {'平均薪资(k)':>12s}")
print(f"{'-'*40} {'-'*5} {'-'*10} {'-'*12}")

total_emp = 0
for mc in sorted(set(d["major_category_code"] for d in all_data)):
    cat_data = [d for d in all_data if d["major_category_code"] == mc]
    name = cat_data[0]["major_category"]
    count = len(cat_data)
    emp = sum(d["est_employment_wan"] for d in cat_data)
    avg_sal = sum(d["salary_median_k"] for d in cat_data) / count
    total_emp += emp
    # Truncate name for display
    display_name = f"{mc}. {name}"
    if len(display_name) > 38:
        display_name = display_name[:38]
    print(f"{display_name:<40s} {count:>5d} {emp:>10d} {avg_sal:>12.1f}")

print(f"{'-'*40} {'-'*5} {'-'*10} {'-'*12}")
print(f"{'合计':<40s} {len(all_data):>5d} {total_emp:>10d}")
print(f"\n预估总就业人数: {total_emp}万 = {total_emp/10000:.2f}亿")
print(f"输出文件: data/occupations.json")
