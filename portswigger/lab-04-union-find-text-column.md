# PortSwigger Lab: SQL injection UNION attack, finding a column containig text 

- **Category:** SQL INJECTION (UNION Attack)
- **Difficulty:** Apprentice

## 1. Objective

Identify which column returned by the vulnerable query is compatible with string data.

## 2. Exploitation Step-by-Step

1. Accessed the category filter in the shop.
2. Determined that the vulnerable query returns **3 columns**.
3. Used a `UNION SELECT` attack to test which column is compatible with string data.
4. Tested the provide random string in each of the three columns.
5. The injection succeeded when the string was placed in the **second column**, confirming that this column is compatible with string data.

## 3. Conclusion 

The original database query returns **3 colimns**. The **second column** is compatible with string data, allowing it to be used for retrieving text through a UNION-based SQL injection. 
