### MACINE LEARNING

### GITHUB

```git
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/edycoleee/ml2025.git
git push -u origin main
```

```py
#project-folder/
#│
#├── nature.ipynb.py
#└── README.md

# 1. Membuat Virtual Environtment
python -m venv venv
source venv/bin/activate  #Linux / Macbook
venv\Scripts\activate # Windows

#2. Install Flask
pip install matplotlib numpy
```

## 1. NORMALISASI DATA

## 2. PREDIKSI DENGAN GARIS LURUS (2 TITIK)

```py
# rumus awal
y = mx + b
# persamaan garis saat melewati titik (x1,y1) dengan gradient m
y1 = mx1 + b
# mecari nilai b
b = y1 – mx1
# masukkan persamaan awal
y = mx + (y1 – mx1)
y – y1 = mx - mx1
# rumus persamaan garis linear dengan gradient m dan melewati garis (x1,y1)
y – y1 = m(x – x1)


# Hitung slope (m) dan intercept (b)
m = (y2 - y1) / (x2 - x1)
b = y1 - m * x1

# Persamaan garis: y = m*x + b
y_pred = m * x_pred + b
```

## 3. BELAJAR SUM

## 4. BELAJAR TURUNAN

## 5. PREDIKSI DENGAN REGRESI LINEAR OLS

## 6. BELAJAR MATRIX

## 7. PREDIKSI DENGAN REGRESI LINEAR OLS MATRIX

## 8. GRADIEN DECENT

## 9. BATCH GRADIENT DECENT

## 10. MINI BATCH GRADIENT DECENT

## 11. SINGLE PERCEPTRON LINEAR

## 12. SINGLE PERCEPTRON SIGMOID >> KLASIFIKASI /DECISION BOUNDRY

## 13. SINGLE PERCEPTRON GERBANG LOGIKA AND

## 14. SINGLE PERCEPTRON GERBANG LOGIKA OR

## 15. DIAGRAM MLP (Multi-Layer Perceptron)
