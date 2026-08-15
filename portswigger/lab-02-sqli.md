# PortSwigger Lab 02: SQL injection vulnerability allowing login bypass

**Category:** SQL Injection  
**Difficulty:** Apprentice  
**Target:** Login Form (Username Parameter)  

---

## 1. Vulnerability Description
The application's login mechanism fails to sanitize user input in the username field, making it vulnerable to SQL injection. 

The backend query executes logic similar to:
SELECT * FROM users WHERE username = 'USER_INPUT' AND password = 'PASSWORD_INPUT'

---

## 2. Exploitation / Payload
By injecting a single quote (') to break out of the string literal and (--) to comment out the rest of the query, we can bypass password authentication entirely.

* **Target User:** administrator
* **Injected Username:** administrator'--
* **Password:** (Any random value)

### Resulting backend query:
SELECT * FROM users WHERE username = 'administrator'-- ' AND password = '1234'

* ' : Closes the string literal for the username.
* -- : Comments out the AND password = ... condition.

The database evaluates only: WHERE username = 'administrator' and authenticates the session successfully.

---

## 3. Impact
An attacker can log in as any user (including privileged users like administrator) without knowing their password.

---

## 4. Remediation
Use Parameterized Queries (Prepared Statements) so that user input is treated strictly as data rather than executable code.
