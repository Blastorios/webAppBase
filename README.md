#webAppBase

A simple frame to build your own Web App, providing:

- Folder structure
- Basic Google Authentication
- A prefitted Mkdocs Materialize layout for documentation

> Overall folder structure

    .
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    ├── docker-compose.yml
    └── src
        ├── tests
        ├── containerSetup.sh
        ├── Dockerfile
        ├── requirements.txt
        └── app                            # The Actual Web Api Content
            ├── frontend                   # Potential folder to hold streamlit files
            │
            ├── backend                    # All backend modules to drive the web apps
            │   ├── __init__.py
            │   ├── videoConverter.py
            │   └── baseclasses            # All validation classes to use within the web apps
            │       ├── __init__.py
            │       └── responseBaseclass.py
            │
            ├── static                     # All static files to serve to Jinja2
            │   ├── css
            │   │   └── styles.css
            │   ├── images
            │   │   └── favicon.ico
            │   └── js
            │       └── someJSFile.js
            │
            ├── templates                  # All templates for Jinja2 to display on request
            │   └── index.html
            │
            ├── tmp                        # A temporary storage directory to store short-term data
            │   └── tmp_folder
            │
            ├──__init__.py
            └── main.py                    # The actual FastAPI server. Importing the backend modules through the APIRouter objects
