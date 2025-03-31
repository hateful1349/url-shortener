# **URL Shortener Service**

🚀 FastAPI, a service for URL shortening with asynchronous processing

---

## **Functionality**

✅ **URL shortening** – POST `/` → returns a short ID

✅ **Redirect** – GET `/{short_id}` → redirects to the source URL (307)

✅ **Asynchronous endpoint** – GET `/async-data` → asynchrony test

---

## **Technologies**

- Python 3.9+
    
- FastAPI (web framework)
    
- Uvicorn (ASGI server)
    
- HTTP-client (curl, Postman, browser)
    

---

## **How do I launch it?**

### 1. Clone the repository

```
git clone https://github.com/hateful1349/url-shortener.git
cd url-shortener
```
### 2. Create a virtual environment

```
python -m venv .venv
source .venv/bin/activate  # Linux/MacOS
.\.venv\Scripts\activate   # Windows
```

### 3. Install the dependencies

```
pip install -r requirements.txt
```

###4. Start the server

```
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
The server will be available at:
👉 **[http://127.0.0.1:8000](http://127.0.0.1:8000/)**

---

## **Query examples**

### 1. Shorten URL

```
curl -X POST -H "Content-Type: application/json" -d "{\"url\":\"https://example.com\"}" http://127.0.0.1:8000/
```
**Response:**
```
{"short_id":"100680"}
```
### 2. Follow the short link
```
curl -v http://127.0.0.1:8000/100680
```
**Response:**

- Code `307 Temporary Redirect`
    
- The `Location' header: https://example.com `
    

### 3. Check the asynchronous endpoint
```
curl http://127.0.0.1:8000/async-data
```
**Response:**
```
{"status":"done"}
```
