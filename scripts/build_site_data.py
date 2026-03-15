#!/usr/bin/env python3
"""Transform data/scores.json → site/data.json with compressed field names."""

import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "scores.json")
DST = os.path.join(ROOT, "site", "data.json")

with open(SRC, "r", encoding="utf-8") as f:
    raw = json.load(f)

# --- Build compact jobs list ---
jobs = []
for j in raw:
    jobs.append({
        "c": j["code"],
        "n": j["name"],
        "cat": j["major_category"],
        "sub": j["mid_category"],
        "emp": j["est_employment_wan"],
        "sal": j["salary_median_k"],
        "edu": j["education"],
        "exp": j["ai_exposure"],
        "rt": j["replacement_type"],
        "tl": j["timeline"],
        "cf": j["china_factor"],
        "ra": j["rationale"],
    })

# --- Meta ---
total = len(jobs)
total_emp = sum(j["emp"] for j in jobs)
weighted_exp = sum(j["exp"] * j["emp"] for j in jobs) / total_emp
high_exp_emp = sum(j["emp"] for j in jobs if j["exp"] >= 7)

meta = {
    "total_jobs": total,
    "total_emp_wan": total_emp,
    "weighted_avg_exp": round(weighted_exp, 2),
    "high_exp_emp_wan": high_exp_emp,
    "high_exp_pct": round(high_exp_emp / total_emp * 100, 1),
}

# --- Categories summary ---
from collections import defaultdict

cat_data = defaultdict(lambda: {"count": 0, "emp": 0, "exp_sum": 0})
for j in jobs:
    c = cat_data[j["cat"]]
    c["count"] += 1
    c["emp"] += j["emp"]
    c["exp_sum"] += j["exp"] * j["emp"]

categories = []
for name, c in cat_data.items():
    categories.append({
        "name": name,
        "count": c["count"],
        "emp": c["emp"],
        "avg_exp": round(c["exp_sum"] / c["emp"], 2) if c["emp"] > 0 else 0,
    })
categories.sort(key=lambda x: x["avg_exp"], reverse=True)

# --- Write output ---
output = {"meta": meta, "categories": categories, "jobs": jobs}
os.makedirs(os.path.dirname(DST), exist_ok=True)
with open(DST, "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, separators=(",", ":"))

size_kb = os.path.getsize(DST) / 1024
print(f"✓ {DST}")
print(f"  {total} jobs, {size_kb:.1f} KB")
print(f"  Meta: {meta}")
