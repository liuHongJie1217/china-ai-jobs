#!/usr/bin/env python3
"""
Update data/scores.json with official 2024 NBS salary and employment data.

Maps 394 occupations to:
  - 1 of 5 job position types (based on major_category_code)
  - 1 of 19 industry categories (based on mid_category)
Then updates salary_median_k and est_employment_wan using official data.
"""

import json
import os
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCORES = os.path.join(ROOT, "data", "scores.json")
OFFICIAL = os.path.join(ROOT, "data", "official_stats.json")

# ──────────────────────────────────────────────
# 1. major_category_code → job position type
# ──────────────────────────────────────────────
CATEGORY_TO_POSITION = {
    1: "management",   # 负责人 → 中层及以上管理人员
    2: "professional",  # 专业技术人员
    3: "clerical",     # 办事人员和有关人员
    4: "service",      # 社会生产服务和生活服务人员
    5: "production",   # 农林牧渔业生产人员 → 生产制造及有关人员
    6: "production",   # 生产制造及有关人员
    # 7: 军人 — no mapping
    # 8: 其他 — no mapping
}

# ──────────────────────────────────────────────
# 2. mid_category → industry_id mapping
# ──────────────────────────────────────────────
MID_CATEGORY_TO_INDUSTRY = {
    # === Major Category 1: 负责人 ===
    "中国共产党机关负责人": "public_admin",
    "国家机关负责人": "public_admin",
    "民主党派和工商联负责人": "public_admin",
    "人民团体和群众团体负责人": "public_admin",
    "基层群众自治组织负责人": "public_admin",
    "社会组织负责人": "leasing_business",  # NGO/社会组织 → 商务服务
    "事业单位负责人": "education",  # 事业单位多为教育/卫生，取教育
    "企业负责人": "manufacturing",  # 企业负责人跨行业，取制造业（最大雇主）

    # === Major Category 2: 专业技术人员 ===
    "工程技术人员": "manufacturing",
    "建筑工程技术人员": "construction",
    "交通运输工程技术人员": "transport",
    "计算机与应用工程技术人员": "ict",
    "科学研究人员": "research",
    "农业技术人员": "agriculture",
    "林业技术人员": "agriculture",
    "畜牧兽医技术人员": "agriculture",
    "水产技术人员": "agriculture",
    "卫生专业技术人员": "health",
    "护理人员": "health",
    "药学专业技术人员": "health",
    "教学人员": "education",
    "会计专业人员": "leasing_business",
    "审计人员": "leasing_business",
    "经济专业人员": "finance",
    "统计人员": "public_admin",
    "法律专业人员": "leasing_business",
    "翻译人员": "leasing_business",
    "图书资料与档案专业人员": "education",
    "广播电视和网络视听人员": "culture_sports",
    "文学创作和编辑人员": "culture_sports",
    "记者": "culture_sports",
    "文化工作人员": "culture_sports",
    "文物保护和考古人员": "culture_sports",
    "美术和设计专业人员": "culture_sports",
    "音乐和表演艺术人员": "culture_sports",
    "体育工作人员": "culture_sports",

    # === Major Category 3: 办事人员 ===
    "行政业务办理人员": "public_admin",
    "安全保卫和消防人员": "public_admin",
    "税务和社保经办人员": "public_admin",
    "海关和边防人员": "public_admin",
    "知识产权管理人员": "research",
    "质量管理和检验人员": "manufacturing",
    "环境和安全监测人员": "water_environment",
    "供应链和仓储管理人员": "transport",
    "邮政和电信业务人员": "ict",

    # === Major Category 4: 社会生产服务和生活服务人员 ===
    "批发与零售服务人员": "wholesale_retail",
    "交通运输服务人员": "transport",
    "仓储和快递服务人员": "transport",
    "住宿服务人员": "hospitality",
    "餐饮服务人员": "hospitality",
    "信息传输和软件服务人员": "ict",
    "金融服务人员": "finance",
    "房地产服务人员": "real_estate",
    "租赁和商务服务人员": "leasing_business",
    "修理服务人员": "resident_services",
    "居民生活服务人员": "resident_services",
    "健康服务人员": "health",
    "教育培训服务人员": "education",
    "文化、体育和娱乐服务人员": "culture_sports",
    "社会服务和公共管理人员": "public_admin",
    "环境卫生服务人员": "water_environment",
    "电力、燃气及水供应服务人员": "utilities",
    "宠物服务人员": "resident_services",
    "安保服务人员": "resident_services",

    # === Major Category 5: 农林牧渔业生产人员 ===
    "粮食作物生产人员": "agriculture",
    "经济作物生产人员": "agriculture",
    "畜牧业生产人员": "agriculture",
    "渔业生产人员": "agriculture",
    "林业生产人员": "agriculture",
    "农林牧渔辅助人员": "agriculture",

    # === Major Category 6: 生产制造及有关人员 ===
    "食品饮料生产加工人员": "manufacturing",
    "纺织品生产人员": "manufacturing",
    "服装制作人员": "manufacturing",
    "皮革毛皮制品加工人员": "manufacturing",
    "木材加工及家具制造人员": "manufacturing",
    "造纸和纸制品生产人员": "manufacturing",
    "印刷和包装人员": "manufacturing",
    "化学品制造人员": "manufacturing",
    "化学纤维制造人员": "manufacturing",
    "橡胶和塑料制品制造人员": "manufacturing",
    "非金属矿物制品制造人员": "manufacturing",
    "金属冶炼和压延加工人员": "mining",
    "金属制品制造人员": "manufacturing",
    "铸造和锻造人员": "manufacturing",
    "金属热处理和表面处理人员": "manufacturing",
    "焊接人员": "manufacturing",
    "机械加工人员": "manufacturing",
    "通用设备制造人员": "manufacturing",
    "专用设备制造人员": "manufacturing",
    "汽车制造人员": "manufacturing",
    "铁路船舶航空设备制造人员": "manufacturing",
    "电气机械和器材制造人员": "manufacturing",
    "计算机通信和电子设备制造人员": "manufacturing",
    "仪器仪表制造人员": "manufacturing",
    "文教工美体育用品制造人员": "manufacturing",
    "医药制造人员": "manufacturing",
    "石油加工和炼焦人员": "mining",
    "烟草制品生产人员": "manufacturing",
    "电力热力生产和供应人员": "utilities",
    "燃气和水生产供应人员": "utilities",
    "建筑施工人员": "construction",
    "废弃资源综合利用人员": "water_environment",

    # === Major Category 7: 军人 ===
    "中国人民解放军": None,  # 不映射

    # === Major Category 8: 其他 ===
    "其他从业人员": None,  # 不映射
}


def main():
    # Load data
    with open(SCORES, "r", encoding="utf-8") as f:
        jobs = json.load(f)
    with open(OFFICIAL, "r", encoding="utf-8") as f:
        official = json.load(f)

    # Build industry lookup: id → {salary, employment_wan}
    industry_map = {}
    for ind in official["industries"]:
        industry_map[ind["id"]] = ind

    # ──────────────────────────────────────────
    # Phase 1: Map each job to industry + position
    # ──────────────────────────────────────────
    for job in jobs:
        mid = job["mid_category"]
        cat_code = job["major_category_code"]
        job["_industry_id"] = MID_CATEGORY_TO_INDUSTRY.get(mid)
        job["_position"] = CATEGORY_TO_POSITION.get(cat_code)

    # Check for unmapped mid_categories
    unmapped = set()
    for job in jobs:
        if job["_industry_id"] is None and job["_position"] is not None:
            unmapped.add(job["mid_category"])
    if unmapped:
        print(f"⚠ Unmapped mid_categories (kept original data): {unmapped}")

    # ──────────────────────────────────────────
    # Phase 2: Update salaries
    # ──────────────────────────────────────────
    salary_updated = 0
    salary_skipped = 0
    for job in jobs:
        ind_id = job["_industry_id"]
        pos = job["_position"]
        if ind_id and pos and ind_id in industry_map:
            annual_salary = industry_map[ind_id]["salary"][pos]
            monthly_k = round(annual_salary / 12 / 1000, 1)
            # Clamp to reasonable range
            monthly_k = max(3.0, min(monthly_k, 40.0))
            job["salary_median_k"] = monthly_k
            salary_updated += 1
        else:
            salary_skipped += 1

    print(f"✓ Salary: {salary_updated} updated, {salary_skipped} skipped")

    # ──────────────────────────────────────────
    # Phase 3: Update employment
    # ──────────────────────────────────────────
    # Group jobs by industry
    industry_jobs = defaultdict(list)
    no_industry_jobs = []
    for job in jobs:
        ind_id = job["_industry_id"]
        if ind_id and ind_id in industry_map:
            industry_jobs[ind_id].append(job)
        else:
            no_industry_jobs.append(job)

    # For each industry, distribute official employment proportionally
    emp_updated = 0
    for ind_id, ind_jobs in industry_jobs.items():
        official_emp = industry_map[ind_id]["employment_wan"]
        # Use existing employment as weights for proportional distribution
        total_existing = sum(j["est_employment_wan"] for j in ind_jobs)
        if total_existing == 0:
            # Equal distribution if no existing data
            per_job = round(official_emp / len(ind_jobs))
            for j in ind_jobs:
                j["est_employment_wan"] = per_job
        else:
            for j in ind_jobs:
                share = j["est_employment_wan"] / total_existing
                j["est_employment_wan"] = max(1, round(official_emp * share))
        emp_updated += len(ind_jobs)

    # Adjust rounding to match official total for mapped industries
    for ind_id, ind_jobs in industry_jobs.items():
        official_emp = industry_map[ind_id]["employment_wan"]
        current_sum = sum(j["est_employment_wan"] for j in ind_jobs)
        diff = official_emp - current_sum
        if diff != 0 and ind_jobs:
            # Add/subtract from the largest job
            largest = max(ind_jobs, key=lambda j: j["est_employment_wan"])
            largest["est_employment_wan"] += diff

    # For unmapped jobs (military, other), keep existing values
    print(f"✓ Employment: {emp_updated} updated, {len(no_industry_jobs)} skipped")
    print(f"  Unmapped jobs: {[j['name'] for j in no_industry_jobs]}")

    # ──────────────────────────────────────────
    # Phase 4: Verify totals
    # ──────────────────────────────────────────
    total_emp = sum(j["est_employment_wan"] for j in jobs)
    mapped_emp = sum(j["est_employment_wan"] for j in jobs if j["_industry_id"])
    unmapped_emp = sum(j["est_employment_wan"] for j in jobs if not j["_industry_id"])
    print(f"\n  Total employment: {total_emp}万人 ({total_emp/10000:.2f}亿)")
    print(f"  Mapped: {mapped_emp}万人, Unmapped: {unmapped_emp}万人")

    # Industry-level summary
    print("\n  Industry employment summary:")
    for ind in official["industries"]:
        ind_id = ind["id"]
        actual = sum(j["est_employment_wan"] for j in industry_jobs.get(ind_id, []))
        target = ind["employment_wan"]
        n_jobs = len(industry_jobs.get(ind_id, []))
        marker = "✓" if actual == target else "✗"
        print(f"    {marker} {ind['name'][:12]:　<12} target={target:>6} actual={actual:>6} ({n_jobs} jobs)")

    # ──────────────────────────────────────────
    # Phase 5: Clean up temp fields and write
    # ──────────────────────────────────────────
    for job in jobs:
        del job["_industry_id"]
        del job["_position"]

    with open(SCORES, "w", encoding="utf-8") as f:
        json.dump(jobs, f, ensure_ascii=False, indent=2)

    print(f"\n✓ Written to {SCORES}")
    print(f"  {len(jobs)} jobs, total employment: {total_emp}万人")


if __name__ == "__main__":
    main()
