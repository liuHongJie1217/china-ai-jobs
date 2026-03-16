# AI Exposure of the Chinese Job Market

How exposed is every occupation in China's economy to AI and automation?

This project scores **394 occupations** from China's National Occupational Classification Dictionary (2022 edition) on their AI exposure (0–10), and visualizes the results as an interactive treemap where **area = employment** and **color = AI exposure**.

**[Live Demo →](https://china-ai-jobs.pages.dev/)** · Inspired by [@karpathy/jobs](https://github.com/karpathy/jobs)

---

## What's Here

- **394 occupations** from 《中华人民共和国职业分类大典》(2022), spanning 8 major categories
- Each occupation scored by **Claude (Anthropic)** on AI exposure (0–10), with rationale, replacement type, timeline, and China-specific factors
- **Interactive treemap** visualization built with D3.js
- Salary vs. exposure scatter plot, education vs. exposure box plot, category ranking table

## Key Findings

All numbers computed from `data/scores.json` across 394 occupations covering ~745 million workers:

| Metric | Value |
|--------|-------|
| Weighted average AI exposure | **4.76 / 10** |
| Workforce in high-exposure jobs (≥7) | **15.4%** (~114 million) |
| Workforce in medium-exposure jobs (4–6) | **62.6%** (~466 million) |
| Jobs facing full replacement | **7** (32.2 million workers) |
| Jobs on 1–3 year timeline | **32** |

### Most Exposed Occupations

| Rank | Occupation | Score | Employment |
|------|-----------|-------|------------|
| 1 | Call center workers (呼叫中心服务人员) | 10 | 580K |
| 2 | Translators (笔译人员) | 10 | 450K |
| 3 | Cashiers (收银员) | 9 | 22.95M |
| 4 | Financial clerks (财务出纳人员) | 9 | 3.07M |
| 5 | Administrative assistants (行政文员) | 9 | 2.34M |

### Least Exposed Occupations

| Rank | Occupation | Score | Employment |
|------|-----------|-------|------------|
| 1 | Athletes (运动员) | 1 | 60K |
| 2 | Chinese cuisine chefs (中式烹调师) | 2 | 13.50M |
| 3 | Domestic workers (家政服务人员) | 2 | 13.32M |
| 4 | Interior renovation workers (装饰装修工) | 2 | 12.12M |
| 5 | Bricklayers (砌筑工) | 2 | 8.07M |

### Category Rankings (by weighted average exposure)

| Category | Avg Exposure | Jobs | Employment |
|----------|-------------|------|------------|
| Clerical workers (办事人员) | **6.41** | 28 | 29M |
| Professionals (专业技术人员) | **5.64** | 119 | 84M |
| Service workers (社会生产服务和生活服务人员) | **5.14** | 90 | 270M |
| Agriculture workers (农林牧渔业生产人员) | **4.18** | 23 | 158M |
| Manufacturing workers (生产制造及有关人员) | **4.10** | 105 | 177M |
| Government & Party officials (负责人) | **3.65** | 22 | 15M |
| Military (军人) | **3.39** | 4 | 2.3M |

### Surprising Findings

1. **Software engineers score 8/10** — facing partial replacement on a 1–3 year timeline
2. **Clerical workers are the most endangered category**, not factory workers — office automation hits harder than industrial automation
3. **Service workers moved up to 3rd most exposed** (5.14) — AI chatbots, self-checkout, and robo-advisory reshaping the service sector
4. **Higher education correlates with higher exposure** — bachelor's degree holders average 6.0 vs. 3.8 for those without high school diplomas

## Data Pipeline

```
1. Compile occupations              → data/occupations.json (394 occupations from 职业分类大典 2022)
2. Score with Claude Sonnet         → data/scores.json (temperature=0, batch processing)
3. Update with official NBS data    → data/scores.json (salary & employment from 国家统计局 2024)
4. Build site data                  → site/data.json (compressed format)
5. D3.js visualization              → site/index.html (treemap + charts)
```

## Scoring Methodology

Each occupation is scored on a 0–10 scale across multiple dimensions:

| Dimension | Description |
|-----------|-------------|
| Task automability | What % of core tasks can current AI handle? |
| Digital vs. physical | Is the work primarily digital (higher exposure) or physical? |
| Creativity & judgment | Does the job require novel problem-solving? |
| Human interaction | Is face-to-face interaction essential? |
| China-specific factors | Regulatory, institutional, and cultural constraints |

**Calibration examples:**

| Occupation | Score | Rationale |
|-----------|-------|-----------|
| Translator (笔译人员) | 10 | Pure text transformation; LLMs already match human quality |
| Software engineer (软件工程技术人员) | 8 | Core coding highly automatable; architecture/design less so |
| Teacher (中小学教师) | 4 | Content delivery automatable; mentoring and classroom management not |
| Chinese chef (中式烹调师) | 2 | Physical skill, sensory judgment, cultural artistry |
| Athlete (运动员) | 1 | Irreducibly physical performance |

**Replacement types:**
- `full` — AI can fully replace the role (7 occupations, 32.2M workers)
- `partial` — significant task replacement but human still needed (180 occupations)
- `augment` — AI primarily enhances productivity (207 occupations)

## Key Files

| File | Description |
|------|-------------|
| `data/occupations.json` | Raw occupation data from 职业分类大典 2022 |
| `data/scores.json` | Full scored dataset (394 occupations, 15 fields each) |
| `site/data.json` | Compressed site data |
| `site/index.html` | Interactive visualization (single-file, D3.js) |
| `scripts/generate_batch*.py` | Claude API scoring scripts |
| `scripts/merge_batches.py` | Merge batch results |
| `scripts/build_site_data.py` | Transform scores → site data |
| `scripts/adjust_employment.py` | Employment estimation adjustments |
| `scripts/update_with_official_data.py` | Update salary & employment with NBS 2024 data |
| `data/official_stats.json` | Official NBS 2024 statistics (19 industries × 5 job types) |

## Setup

```bash
cd site && python3 -m http.server 8000
# Open http://localhost:8000
```

No build step required — the site is a single HTML file with inline CSS/JS.

## Credits

- Inspired by [Andrej Karpathy — AI Exposure of the US Job Market](https://github.com/karpathy/jobs)
- Occupation data: 《中华人民共和国职业分类大典》(2022 edition)
- Salary & employment data: [国家统计局 2024年数据](https://www.stats.gov.cn/sj/zxfb/202505/t20250516_1959826.html) — 城镇单位就业人员年平均工资 + 统计年鉴分行业就业人员数
- AI exposure scoring: [Claude](https://www.anthropic.com/) by Anthropic
- Visualization: [D3.js](https://d3js.org/)

## License

MIT
