# clothestore
This is an ecommerce web platform built using django
## Language(s) And Technologies used
- Python
- Boostrap5
- Html
- css
- JavaScript
## Setup requirements and Installation
- Clone the repository 
- Navigate to the folder and create a virtualenv by running <virtualenv venv>
- Activate it ~ source venv/bin/activate and run pip freeze > requirements.txt
- Run pip install -r requirements.txt to install project requirements.
- Create a database in your postgres and change the development database      
  settings in settings.py
- Finally run python manage.py runserver to view the site
## BDD

| BEHAVIOUR    | INPUT   |  OUTPUT |
| :------------- | :------------- | :--------------- |
| Load website | Create user | View web app |

## Development

Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:
- Fork the repo
- Create a new branch (git checkout -b improve-feature)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (git commit -am 'Improve feature')
- Push to the branch (git push origin improve-feature)
- Create a Pull Request

## Known Bugs

If you find a bug (the website couldn't handle the query and or gave undesired results), kindly open an issue here by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue here. Please include sample queries and their corresponding results.
## Future releases
Further extend this web app tpo handle authentication using google and facebook and enable real time user following and unfollowing.
# Live version
- [Live version](https://ecommerce-project2.herokuapp.com/)

### Licence
You can use this application for personal use only.

*MIT*
Copyright (c) 2022**Patrick Mugambi**
