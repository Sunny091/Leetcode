# LeetCode Python 練習

## 目錄結構

```
python/
├── .gitignore              # 忽略 cache 檔案
├── requirements.txt        # pytest 依賴
├── conftest.py             # pytest 配置
├── new_problem.py          # 建立新題目的腳本
└── problems/
    └── _題號_題目名稱/
        ├── solution.py       # 解題程式
        └── test_solution.py  # 單元測試
```

## 安裝

```bash
cd python
pip install -r requirements.txt
```

## 使用方式

### 1. 建立新題目

```bash
cd python
python new_problem.py <題號> <題目名稱>
```

範例：
```bash
python new_problem.py 1 TwoSum
python new_problem.py 2799 CountCompleteSubarrayInAnArray
```

這會建立：
- `problems/_1_TwoSum/solution.py` - 解題程式模板
- `problems/_1_TwoSum/test_solution.py` - 測試程式模板

### 2. 撰寫解答

編輯 `problems/_題號_題名/solution.py`，實作 Solution class 中的方法。

### 3. 執行測試

單一題目測試：
```bash
cd python/problems/_1_TwoSum
pytest test_solution.py -v
```

執行所有題目測試：
```bash
cd python
pytest problems -v
```
