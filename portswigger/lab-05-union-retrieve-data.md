# PortSwigger Lab: SQL injection UNION attack, retrieving data from other tables

- **Category:** SQL Injection (UNION Attack)
- **Difficulty:** Apprentice

## 1. Objective

Retrieve username and password from another database table using a SQL injection UNION attack, then use the administrator credentials to log in.

## 2. Exploitation Step-by-Step

1. Accessed the category filter in the shop.
2. Determined that the vulnerable query returns **2 columns**.
3. Confirmed that both columns are compatible with string data.
4. Identified the `users` table containing the `username` and `password` columns.
5. Used the following UNION-based SQL injection:

```sql
' UNION SELECT username, password FROM users--

6. The application returned the usernames and passwords stored in the users table.
7. Retrieved the credentials for the administrator user.
8. Used the administrator credentials to log in through the My account page.
9. The lab was successfully solved.

## 3. Conclusion

The SQL injection vulnerability allowed dara to be retrieved from another database table using a UNION attack. By recoverign the administrator credentials, it was possible to authenticate as the administrator and successfully complete the lab.
