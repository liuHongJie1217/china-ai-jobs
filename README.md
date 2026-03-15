# AI Exposure of the Chinese Job Market

How exposed is every occupation in China's economy to AI and automation?

This project scores **394 occupations** from China's National Occupational Classification Dictionary (2022 edition) on their AI exposure (0–10), and visualizes the results as an interactive treemap where **area = employment** and **color = AI exposure**.

**[Live Demo →](TODO)** · Inspired by [@karpathy/jobs](https://github.com/karpathy/jobs)

---

## What's Here

- **394 occupations** from 《中华人民共和国职业分类大典》(2022), spanning 8 major categories
- Each occupation scored by **Claude (Anthropic)** on AI exposure (0–10), with rationale, replacement type, timeline, and China-specific factors
- **Interactive treemap** visualization built with D3.js
- Salary vs. exposure scatter plot, education vs. exposure box plot, category ranking table

## Key Findings

All numbers computed from `data/scores.json` across 394 occupations covering ~730 million workers:

| Metric | Value |
|--------|-------|
| Weighted average AI exposure | **4.62 / 10** |
| Workforce in high-exposure jobs (≥7) | **10.6%** (~77 million) |
| Workforce in medium-exposure jobs (4–6) | **67.1%** (~490 million) |
| Jobs facing full replacement | **7** (18.6 million workers) |
| Jobs on 1–3 year timeline | **32** |

### Most Exposed Occupations

| Rank | Occupation | Score | Employment |
|------|-----------|-------|------------|
| 1 | Translators (笔译人员) | 10 | 220K |
| 2 | Call center workers (呼叫中心服务人员) | 10 | 1.39M |
| 3 | Financial clerks (财务出纳人员) | 9 | 6.21M |
| 4 | Administrative assistants (行政文员) | 9 | 4.66M |
| 5 | Cashiers (收银员) | 9 | 2.77M |

### Least Exposed Occupations

| Rank | Occupation | Score | Employment |
|------|-----------|-------|------------|
| 1 | Athletes (运动员) | 1 | 140K |
| 2 | Interior renovation workers (装饰装修工) | 2 | 9.01M |
| 3 | Chinese cuisine chefs (中式烹调师) | 2 | 8.32M |
| 4 | Domestic workers (家政服务人员) | 2 | 8.32M |
| 5 | Bricklayers (砌筑工) | 2 | 6.01M |

### Category Rankings (by weighted average exposure)

| Category | Avg Exposure | Jobs | Employment |
|----------|-------------|------|------------|
| Clerical workers (办事人员) | **6.37** | 28 | 55M |
| Professionals (专业技术人员) | **5.61** | 119 | 100M |
| Service workers (社会生产服务和生活服务人员) | **4.42** | 90 | 170M |
| Manufacturing workers (生产制造及有关人员) | **4.29** | 105 | 200M |
| Agriculture workers (农林牧渔业生产人员) | **4.18** | 23 | 174M |
| Government & Party officials (负责人) | **3.49** | 22 | 20M |
| Military (军人) | **3.39** | 4 | 2.3M |

### Surprising Findings

1. **Software engineers score 8/10** — the single largest high-exposure job with 10 million workers, facing partial replacement on a 1–3 year timeline
2. **Clerical workers are the most endangered category**, not factory workers — office automation hits harder than industrial automation
3. **Higher education correlates with higher exposure** — bachelor's degree holders average 6.0 vs. 3.8 for those without high school diplomas
4. **Salary weakly correlates with exposure** (r=0.29) — high-paying knowledge jobs (blockchain engineers at 22K/month, investment analysts at 20K/month) sit alongside low-wage data entry in the danger zone

## Data Pipeline

```
1. Compile occupations      → data/occupations.json (394 occupations from 职业分类大典 2022)
2. Score with Claude Sonnet  → data/scores.json (temperature=0, batch processing)
3. Build site data           → site/data.json (compressed format)
4. D3.js visualization       → site/index.html (treemap + charts)
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
- `full` — AI can fully replace the role (7 occupations, 18.6M workers)
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

## Setup

```bash
cd site && python3 -m http.server 8000
# Open http://localhost:8000
```

No build step required — the site is a single HTML file with inline CSS/JS.

## Credits

- Inspired by [Andrej Karpathy — AI Exposure of the US Job Market](https://github.com/karpathy/jobs)
- Data source: 《中华人民共和国职业分类大典》(2022 edition)
- Scoring: [Claude](https://www.anthropic.com/) by Anthropic
- Visualization: [D3.js](https://d3js.org/)

## License

MIT
