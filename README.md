# linked_in_scraper
LinkedIn Scraper with voyager API

- How to setup
1. Make sure you have python3 on your machine
2. Create virtual environtment python "python3 -m virtualenv env"
3. Activate virtual environment 
   . Windows: env\Scripts\activate
   . Unix : source env/bin/activate
4. Install python requirements "pip install -r requirements.txt 
5. Setup configuration apps 
   . Copy file .testing.env and rename to .env
   . Open file .env and adjust the value
   . To login this apps using SCRAPER_USERNAME and SCRAPER_PASSWORD, you can change this to whatever you want
6. Run the apps, cd to root folder apps run command "flask run" or "python run.py" and make sure you activate your virtual env before running this command.
7. Check collection folder, it hase postman collection.


This api just for testing to voyager api, voyager api that I use:
- /voyager/api/me
- /voyager/api/identity/profiles/%s/networkinfo
- /mob/sso/you


API Voyagaer endpoint configuration inside file config_routes.py

More detail about voyager api https://linkedin.api-docs.io/