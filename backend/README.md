# Backend

## Installing using Github

Python 3.10+ is a must

1. Clone the repository in the terminal:
`git clone https://github.com/kseniia-grishchenko/RecipeRecommender.git`
2. Go to the `backend` folder: 
`cd backend`
3. Make the following command and populate it with required data:
`cp .env.example .env`
4. Create virtual env:
`python -m venv venv`
5. Setup virtual env:
    * On Windows: `venv\Scripts\activate`
    * On Linux or MacOS: `source venv/bin/activate`
6. And mark it as the source root 
7. Install requirements: `pip install -r requirements.txt`
8. Make migrations: `python manage.py migrate`  
9. Now you can run it: `python manage.py runserver`
