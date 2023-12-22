import pymongo
from bson import ObjectId

class Database:

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["first_crud_database"]
    
    
    def __init__(self, collection) -> None:
        self.mycol = self.mydb[collection]


    def selectall(self):
        objects_list = list(self.mycol.find())
        for obj in objects_list:
            obj['_id'] = str(obj['_id'])
        return objects_list
    

    def select(self, _id):
        str_id = str(_id)
        obj = dict(self.mycol.find_one({'_id': ObjectId(str_id)}))
        obj['_id'] = str(obj['_id'])
        return obj


    def insert(self, obj):
        return self.mycol.insert_one(obj)


    def update(self, obj):
        obj['_id'] = ObjectId(obj['_id'])
        filter = {'_id': obj['_id']}
        update = {"$set": obj }
        lista = self.mycol.update_one(filter, update)
        return lista


    def delete(self, _id):
        _id = ObjectId(_id)
        lista = self.mycol.delete_one({'_id': _id})
        return lista


#Tasks: Criar as funções de update, insert e delete e deixa-las dinâmicas. 
#Descobrir como pegar informações do front (formulários) - Segunda/terça.
#1, 2 , 3 , 4, 5 
#Fazer os botões de input na mão, e enviar para o back-end.
#Colocar uma validação que só permita inserir um novo jogo se todos os campos estiverem preenchidos. Se não estiverem, colocar na URL um ?erro=emptyfields.

# create table games (
# 	id serial primary key,
# 	title varchar(60) not null,
# 	category varchar(60) not null,
# 	console varchar(60) not null
# );

# select * from games;

# insert into games
# 	(title, category, console)
# values (
# 	'COD',
# 	'First person shot game',
# 	'PS5'
# );