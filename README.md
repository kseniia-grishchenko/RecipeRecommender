<img width="604" alt="main page" src="https://github.com/kseniia-grishchenko/RecipeRecommender/assets/152200130/7d7bf8e3-77d1-48dc-bd92-242ce263fa84"># Recipe Recommender

## Design

[Filma link](<https://www.figma.com/file/Zl5fEh2x30VyPhi3T9jItj/Food-recipes-website-UI---Del%C3%ADcias-%C3%A0-Mesa-(Community)?type=design&node-id=0%3A1&mode=design&t=4z9xTQ2vTItuTz8D-1>)
<img width="604" alt="main page" src="https://github.com/kseniia-grishchenko/RecipeRecommender/assets/152200130/7256a1fa-0c41-45cc-a4b2-4caa252d79dd">

## Backend

### Installing using Github

Python 3.10+ is a must

1. Clone the repository in the terminal:
   `git clone https://github.com/ArkadyBIG/RecipeRecommender.git`
2. Make the following command and populate it with required data:
   `cp .env.example .env`
3. Create virtual env:
   `python -m venv venv`
4. Setup virtual env:
   - On Windows: `venv\Scripts\activate`
   - On Linux or MacOS: `source venv/bin/activate`
5. Go to the `backend` folder:
   `cd backend`
6. And mark it as the source root
7. Install requirements: `pip install -r requirements.txt`
8. Make migrations: `python manage.py migrate`
9. Now you can run it: `python manage.py runserver`
