
# PortSwigger Lab: SQL injection UNION attack, retrieving multiple values in a single column

- **Category:** SQL Injection (UNION Attack)
- **Difficulty:** Apprentice

## 1. Objective

Retrieve multiple values within a single column using a SQL injection UNION attack.

## 2. Exploitation Step-by-Step

1. Accessed the product category filter.
2. Determined that the vulnerable query returns a single column.
3. The database contains a `users` table with `username` and `password` columns.
4. Used string concatenation to combine both values into a single column.
5. Used the following UNION-based SQL injection:

```sql
' UNION SELECT username || '~' || password FROM users--+

6. The application returned the usernames and passwords combined in a single column.
7. The lab was successfully solved.

## 3. Conclusion

The SQL injection UNION attack allowed multiple values to be concatenated and retrieved through a single column.
