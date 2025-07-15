# ZIMBABWE-ANALYSIS


# 📈 Zimbabwe GDP vs Life Expectancy Analysis (1950–2025)

This project explores the **relationship between GDP per capita** and **life expectancy** in Zimbabwe across multiple decades using **Python, Pandas, Matplotlib, and Seaborn**.

We visualize historical trends, observe patterns across decades, and investigate how economic conditions relate to public health outcomes.

---

## 📂 Dataset

- `LifeExpectency.csv`: Contains life expectancy values by year.
- `GDPperCapita.csv`: Contains GDP per capita values by year.
- Both datasets are merged on the `Year` column for analysis.

---

## 🛠️ Tools Used

- `pandas`: Data loading and manipulation
- `matplotlib.pyplot`: Basic plotting
- `seaborn`: Statistical plotting and boxplots

---

## 📊 Visualizations

### 1. Line Plot: Life Expectancy over Time

Shows how life expectancy in Zimbabwe has changed since 1950.

![Life Expectancy over Time](plots/LifeExpectency.png)

---

### 2. Line Plot: GDP per Capita over Time

Displays Zimbabwe's economic trends across decades.

![GDP per Capita over Time](plots/GDP.png)

---

### 3. Scatter Plot: GDP per Capita vs Life Expectancy

This scatter plot reveals a **positive, non-linear correlation** between GDP and life expectancy. GDP is shown on a **log scale** for better distribution clarity. Years are annotated.

📌 Blue labels highlight crisis years (1995–2005).

![Scatter Plot with Annotations](plots/GDP vs Life Expectency.png)

---

### 4. Histogram: Life Expectancy Distribution

Shows the distribution of life expectancy values across all years.

```python
plt.hist(merged_df['Life Expectency'], bins=10)


project/
│
├── data/
│   ├── LifeExpectency.csv
│   └── GDPperCapita.csv
│
├── plots/
│   ├── LifeExpectency.png
│   ├── GDP.png
│   ├── GDP vs Life Expectency.png
│   ├── Boxplot for GDP per Capita by Decade.png
│   └── Boxplot for Life Expectency per Capita by Decade.png
│
├── analysis.py  # Python script containing all visualizations
└── README.md
