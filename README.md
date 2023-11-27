# Recipe Recommender

## Design
[Figma link](https://www.figma.com/file/Zl5fEh2x30VyPhi3T9jItj/Food-recipes-website-UI---Del%C3%ADcias-%C3%A0-Mesa-(Community)?type=design&node-id=0%3A1&mode=design&t=4z9xTQ2vTItuTz8D-1)

<img width="604" alt="main page" src="https://github.com/kseniia-grishchenko/RecipeRecommender/assets/152200130/58012b27-2df9-4398-a614-e0ccb1839e0f">

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
    * On Windows: `venv\Scripts\activate`
    * On Linux or MacOS: `source venv/bin/activate`
5. Go to the `backend` folder: 
`cd backend`
6. And mark it as the source root 
7. Install requirements: `pip install -r requirements.txt`
8. Make migrations: `python manage.py migrate`  
9. Now you can run it: `python manage.py runserver`
