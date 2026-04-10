# Address Book App

A RESTful Address Book API built using FastAPI.

## Setup

1. Clone repo
git clone https://github.com/ATHIRAKBHASKARAN/address-book-app.git
cd address-book-app

2. Create virtual env
python -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Environment Variables

Create a `.env` file in the root directory and add: 
    DATABASE_URL=sqlite:///./addresses.db
    DEBUG=True
    API_V1_PREFIX=/api/v1
    FEATURE_DISTANCE_SEARCH=True

5. Run server
uvicorn app.main:app --reload

6. Open
http://127.0.0.1:8000/docs