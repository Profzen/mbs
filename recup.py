# app/__init__.py

    from flask import Flask
    from flask_pymongo import PyMongo
    
    app = Flask(__name__)
    
    # Configurez votre URI MongoDB (remplacez par vos informations)
    app.config['MONGO_URI'] = 'mongodb+srv://profzzen:_Alazalaz_13@cluster0.erhtd.mongodb.net/mbs'
    
    # Initialisation de PyMongo avec l'application Flask
    mongo = PyMongo(app)
    
    print("Initialisation de l'application Flask")
    
    # Importer les routes de l'application (doit être fait après l'initialisation de mongo)
    from app import routes
    
    # Importer et exécuter l'initialisation de la base de données
    from app.init_db import create_indexes
    with app.app_context():
        create_indexes()

