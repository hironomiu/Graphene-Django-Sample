# Graphene-Django-Sample

Django + Graphql(Graphene-Django)の実装例

![demo](./demo.png)

## SetUp

```
pipenv install
```

## Run

```
pipenv shell
python manage.py runserver
```

## DB(sqlite3)

事前にsqlite3を用意する

```
sqlite> insert into ingredients_usermodel(name,last_name)  values('hoge','fuga');
sqlite> insert into ingredients_usermodel(name,last_name)  values('piyo','gaoh');
```
