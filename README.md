# 📊 YouTube Trending Video Analytics

**An end-to-end data analysis project using Python & Power BI to explore trends in YouTube videos across India 🇮🇳, Japan 🇯🇵, and South Korea 🇰🇷.**

---

## 🎯 Objective

To uncover regional patterns in YouTube trending content by analyzing video engagement, sentiment of titles, and category performance using Python-based EDA and Power BI dashboarding.

---

## 🛠 Tools & Technologies

- **Python** (Pandas, Seaborn, Matplotlib)
- **NLP**: NLTK (VADER Sentiment Analysis)
- **Power BI** (Dashboard & Visuals)
- **Jupyter Notebook**, **VS Code**
- **Dataset Source**: [Kaggle – YouTube Trending Videos](https://www.kaggle.com/datasets/datasnaek/youtube-new)

---

## 📂 Project Structure

📁 YouTube-Trending-Analytics/

├── data/ # Raw CSVs (INvideos, JPvideos, KRvideos)

├── visuals/ # Plots & heatmaps

├── output/ # Final insights and reports

├── Analyse.py & Merge.py/ #python codes

├── PowerBI_Dashboard.pdf

├── YouTube_Final_Insights.pdf

└── README.md

---

## 🔍 Steps Performed

### ✅ Data Cleaning & Merging
- Loaded CSVs for IN, JP, and KR
- Added `country` column and parsed dates
- Merged datasets and handled encoding issues

### ✅ Sentiment Analysis
- Used **VADER** to classify title sentiment as Positive / Neutral / Negative

### ✅ EDA & Correlation
- Analyzed relationships between views, likes, comments, and sentiment
- Generated heatmaps and scatter plots for insights

### ✅ Power BI Dashboard
- Visualized:
  - Category popularity by region
  - Sentiment distribution
  - KPI cards for video metrics
  - Region-wise trends using slicers

---

## 💡 Key Insights

- **Negative titles** received the highest average views (~1.58M)
- **Japan & Korea** had mostly neutral sentiment; **India** had more emotional variation
- **Music & Entertainment** performed best in India
- **Views strongly correlated** with likes and comments
- Sentiment-driven titles tend to attract more attention

---

## 📘 Report & Export Files

- `YouTube_Final_Insights.pdf` – summarized findings
- `PowerBI_Dashboard.pdf` – dashboard visual
- `YouTube_Trending_Project_Report.pdf` – full project summary

---

## 👤 Author

**Babi Pepakayala**  
📧 babipepakayala162129@gmail.com  
📅 June 2025

---

## 📌 License

This project is for educational and portfolio use. Attribution appreciated if reused.
