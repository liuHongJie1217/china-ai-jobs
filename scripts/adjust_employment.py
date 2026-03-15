#!/usr/bin/env python3
"""Adjust employment numbers to match realistic totals (~7.4亿)"""
import json, os

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

with open("data/occupations.json", encoding="utf-8") as f:
    data = json.load(f)

# Target employment by major category (万人)
targets = {
    1: 2000,
    2: 10000,
    3: 5500,
    4: 17000,
    5: 17000,
    6: 20000,
    7: 230,
    8: 800
}

for mc, target in targets.items():
    cat_data = [d for d in data if d["major_category_code"] == mc]
    current = sum(d["est_employment_wan"] for d in cat_data)
    if current == 0:
        continue
    ratio = target / current
    if abs(ratio - 1.0) < 0.05:  # within 5%, skip
        print(f"大类{mc}: {current}万 → 保持不变 (目标{target}万)")
        continue
    # Scale proportionally, round to nearest integer
    for d in cat_data:
        d["est_employment_wan"] = max(1, round(d["est_employment_wan"] * ratio))
    new_total = sum(d["est_employment_wan"] for d in cat_data)
    print(f"大类{mc}: {current}万 → {new_total}万 (目标{target}万, 缩放{ratio:.2f}x)")

# Write back
with open("data/occupations.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Print final stats
print(f"\n{'='*60}")
print(f"{'大类':<6s} {'名称':<28s} {'条目':>5s} {'就业(万)':>10s} {'平均薪资(k)':>12s}")
print(f"{'-'*6} {'-'*28} {'-'*5} {'-'*10} {'-'*12}")
total_emp = 0
for mc in sorted(set(d["major_category_code"] for d in data)):
    cat_data = [d for d in data if d["major_category_code"] == mc]
    name = cat_data[0]["major_category"]
    count = len(cat_data)
    emp = sum(d["est_employment_wan"] for d in cat_data)
    avg_sal = sum(d["salary_median_k"] for d in cat_data) / count
    total_emp += emp
    short_name = name[:14] if len(name) > 14 else name
    print(f"  {mc:<4d} {short_name:<28s} {count:>5d} {emp:>10d} {avg_sal:>12.1f}")
print(f"{'-'*6} {'-'*28} {'-'*5} {'-'*10} {'-'*12}")
print(f"{'':6s} {'合计':<28s} {len(data):>5d} {total_emp:>10d}")
print(f"\n总就业人数: {total_emp}万 = {total_emp/10000:.2f}亿")
