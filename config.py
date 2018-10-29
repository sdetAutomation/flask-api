import os
import connexion

# create an application instance

my_app = connexion.App(__name__, specification_dir='./swagger')

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(my_app.root_path, 'database/database.db')

my_app.app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
my_app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

my_app.add_api('swagger.yml')
