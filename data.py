# Importamos las librerias necesarias para acceder y limpiar los datos

import pandas as pd
import os
import datetime
import chardet



with open("./item.txt ", 'rb') as rawdata:
    result = chardet.detect(rawdata.read(100000))
result


item = pd.read_csv("./item.txt ", sep = "|", header=None, encoding='ISO-8859-1')
item = item.drop_duplicates()
item = item.set_axis(['itemid', 'movie_title', 'release_date', 'No_used',
               "url","unknown","action","adventure","animation","childens","comedy","crime","documentary","drama",
               "fantasi","film-noir","horror","musical","mystery","romance","sci-fi","thriller","war","western"], axis=1)
item = item.drop(['No_used'], axis=1)

users = pd.read_csv("./user.txt ", sep = "|", header=None, encoding='ISO-8859-1')
users = users.drop_duplicates()
users = users.set_axis(["userid","age","gender","occupation","zip code"], axis=1)

contenido = os.listdir('./movies_userdata')
combinado_csv = pd.concat([pd.read_csv("./movies_userdata/"+f) for f in contenido], ignore_index= True)
combinado_csv = combinado_csv.drop_duplicates()
combinado_csv.drop(combinado_csv[(combinado_csv['raiting'] > 5)].index, inplace=True)

combinado_csv['date'] = [datetime.datetime.fromtimestamp(s,datetime.timezone.utc) for s in combinado_csv['timestamp']] 
#print(combinado_csv)

#Pregunta 1 
print("-----------------------PREGUNTA 1--------------------------")
pregunta1 = combinado_csv.groupby(['itemid']).count().reset_index().sort_values('userid', ascending=False)
print(pregunta1)
movie1 = item.loc[item['itemid'] == 50]
movie2 = item.loc[item['itemid'] == 258]
movie3 = item.loc[item['itemid'] == 100]
movie4 = item.loc[item['itemid'] == 181]
print(movie1['movie_title'])
print(movie2['movie_title'])
print(movie3['movie_title'])
print(movie4['movie_title'])


#Pregunta2
print("-----------------------PREGUNTA 2--------------------------")
pregunta2 = combinado_csv.groupby(['itemid']).agg(
                                  {'raiting': 'sum',
                                  }).reset_index()

print(pregunta2.sort_values('raiting', ascending=False).head(10))
movie1 = item.loc[item['itemid'] == 50]
movie2 = item.loc[item['itemid'] == 100]
movie3 = item.loc[item['itemid'] == 181]
movie4 = item.loc[item['itemid'] == 258]
movie5 = item.loc[item['itemid'] == 174]
movie6 = item.loc[item['itemid'] == 127]
movie7 = item.loc[item['itemid'] == 286]
movie8 = item.loc[item['itemid'] == 1]
movie9 = item.loc[item['itemid'] == 98]
movie10 = item.loc[item['itemid'] == 288]
print(movie1['movie_title'])
print(movie2['movie_title'])
print(movie3['movie_title'])
print(movie4['movie_title'])
print(movie5['movie_title'])
print(movie6['movie_title'])
print(movie7['movie_title'])
print(movie8['movie_title'])
print(movie9['movie_title'])
print(movie10['movie_title'])
pregunta2 = combinado_csv.groupby(['itemid']).agg(
                                  {'raiting': 'mean',
                                  }).reset_index()

print(pregunta2.sort_values('raiting', ascending=False).head(10))
movie1 = item.loc[item['itemid'] == 814]
movie2 = item.loc[item['itemid'] == 1599]
movie3 = item.loc[item['itemid'] == 1201]
movie4 = item.loc[item['itemid'] == 1122]
movie5 = item.loc[item['itemid'] == 1653]
movie6 = item.loc[item['itemid'] == 1293]
movie7 = item.loc[item['itemid'] == 1500]
movie8 = item.loc[item['itemid'] == 1189]
movie9 = item.loc[item['itemid'] == 1536]
movie10 = item.loc[item['itemid'] == 1467]
print(movie1['movie_title'])
print(movie2['movie_title'])
print(movie3['movie_title'])
print(movie4['movie_title'])
print(movie5['movie_title'])
print(movie6['movie_title'])
print(movie7['movie_title'])
print(movie8['movie_title'])
print(movie9['movie_title'])
print(movie10['movie_title'])


#Pregunta 3
print("-----------------------PREGUNTA 3--------------------------")

print('Unknown', item['unknown'].sum())
print('action', item['action'].sum())
print('adventure', item['adventure'].sum())
print('animation', item['animation'].sum())
print('childens', item['childens'].sum())
print('comedy', item['comedy'].sum())
print('crime', item['crime'].sum())
print('documentary', item['documentary'].sum())
print('drama', item['drama'].sum())
print('fantasi', item['fantasi'].sum())
print('film-noir', item['film-noir'].sum())
print('horror', item['horror'].sum())
print('musical', item['musical'].sum())
print('mystery', item['mystery'].sum())
print('romance', item['romance'].sum())
print('sci-fi', item['sci-fi'].sum())
print('thriller', item['thriller'].sum())
print('war', item['war'].sum())
print('western', item['western'].sum())


#Pregunta 5
print("-----------------------PREGUNTA 4--------------------------")

pregunta4 = combinado_csv.merge(item, on='itemid', how='left')

unknown = pregunta4.groupby(['unknown']).agg({'raiting': 'sum',}).reset_index()
action = pregunta4.groupby(['action']).agg({'raiting': 'sum',}).reset_index()
adventure = pregunta4.groupby(['adventure']).agg({'raiting': 'sum',}).reset_index()
animation = pregunta4.groupby(['animation']).agg({'raiting': 'sum',}).reset_index()
childens = pregunta4.groupby(['childens']).agg({'raiting': 'sum',}).reset_index()
comedy = pregunta4.groupby(['comedy']).agg({'raiting': 'sum',}).reset_index()
crime = pregunta4.groupby(['crime']).agg({'raiting': 'sum',}).reset_index()
documentary = pregunta4.groupby(['documentary']).agg({'raiting': 'sum',}).reset_index()
drama = pregunta4.groupby(['drama']).agg({'raiting': 'sum',}).reset_index()
fantasi = pregunta4.groupby(['fantasi']).agg({'raiting': 'sum',}).reset_index()
film_noir = pregunta4.groupby(['film-noir']).agg({'raiting': 'sum',}).reset_index()
horror = pregunta4.groupby(['horror']).agg({'raiting': 'sum',}).reset_index()
musical = pregunta4.groupby(['musical']).agg({'raiting': 'sum',}).reset_index()
mystery = pregunta4.groupby(['mystery']).agg({'raiting': 'sum',}).reset_index()
romance = pregunta4.groupby(['romance']).agg({'raiting': 'sum',}).reset_index()
sci_fi = pregunta4.groupby(['sci-fi']).agg({'raiting': 'sum',}).reset_index()
thriller = pregunta4.groupby(['thriller']).agg({'raiting': 'sum',}).reset_index()
war = pregunta4.groupby(['war']).agg({'raiting': 'sum',}).reset_index()
western = pregunta4.groupby(['western']).agg({'raiting': 'sum',}).reset_index()


print(drama.loc[drama['drama'] == 1])
print(comedy.loc[comedy['comedy'] == 1])
print(action.loc[action['action'] == 1])
print(thriller.loc[thriller['thriller'] == 1])
print(romance.loc[romance['romance'] == 1])
print(adventure.loc[adventure['adventure'] == 1])
print(sci_fi.loc[sci_fi['sci-fi'] == 1])
print(war.loc[war['war'] == 1])
print(crime.loc[crime['crime'] == 1])
print(childens.loc[childens['childens'] == 1])
print(mystery.loc[mystery['mystery'] == 1])
print(horror.loc[horror['horror'] == 1])
print(musical.loc[musical['musical'] == 1])
print(animation.loc[animation['animation'] == 1])
print(film_noir.loc[film_noir['film-noir'] == 1])
print(western.loc[western['western'] == 1])
print(fantasi.loc[fantasi['fantasi'] == 1])
print(documentary.loc[documentary['documentary'] == 1])
print(unknown.loc[unknown['unknown'] == 1])


#Pregunta 5
print("-----------------------PREGUNTA 5--------------------------")
print('La media de edad de las personas es de:\n',users['age'].mean())


#pregunta 6
print("-----------------------PREGUNTA 6--------------------------")
pregunta6 = combinado_csv.merge(users, on='userid', how='left')
import matplotlib.pyplot as plt
scatter_plot = pregunta6.plot.scatter(x='age',y='raiting')
scatter_plot.plot()
plt.show()

#pregunta 7
print("-----------------------PREGUNTA 7--------------------------")
pregunta7 = combinado_csv.merge(users, on='userid', how='left')
pregunta7.drop(pregunta7[(pregunta7['age'] < 50)].index, inplace=True)
resultado = pregunta7.groupby(['itemid']).count().reset_index().sort_values('userid', ascending=False)
print(resultado)
movie1 = item.loc[item['itemid'] == 286]
movie2 = item.loc[item['itemid'] == 100]
movie3 = item.loc[item['itemid'] == 300]
movie4 = item.loc[item['itemid'] == 50]
print(movie1['movie_title'])
print(movie2['movie_title'])
print(movie3['movie_title'])
print(movie4['movie_title'])



#pregunta 8
print("-----------------------PREGUNTA 8--------------------------")
pregunta8 = combinado_csv.merge(users, on='userid', how='left')
pregunta8 = pregunta8.merge(item, on='itemid', how='left')
print('Unknown', item['unknown'].sum())
print('action', item['action'].sum())
print('adventure', item['adventure'].sum())
print('animation', item['animation'].sum())
print('childens', item['childens'].sum())
print('comedy', item['comedy'].sum())
print('crime', item['crime'].sum())
print('documentary', item['documentary'].sum())
print('drama', item['drama'].sum())
print('fantasi', item['fantasi'].sum())
print('film-noir', item['film-noir'].sum())
print('horror', item['horror'].sum())
print('musical', item['musical'].sum())
print('mystery', item['mystery'].sum())
print('romance', item['romance'].sum())
print('sci-fi', item['sci-fi'].sum())
print('thriller', item['thriller'].sum())
print('war', item['war'].sum())
print('western', item['western'].sum())
resultado8 = pregunta8.groupby(['gender']).agg(
                                  {'unknown': 'sum',
                                   'action': 'sum',
                                   'adventure': 'sum',
                                   'animation': 'sum',
                                   'childens': 'sum',
                                   'comedy': 'sum',
                                   'crime': 'sum',
                                   'documentary': 'sum',
                                   'drama': 'sum',
                                   'fantasi': 'sum',
                                   'film-noir': 'sum',
                                   'horror': 'sum',
                                   'musical': 'sum',
                                   'mystery': 'sum',
                                   'romance': 'sum',
                                   'sci-fi': 'sum',
                                   'thriller': 'sum',
                                   'war': 'sum',
                                   'western': 'sum'
                                  }).reset_index()
print(resultado8)


#pregunta 9
print("-----------------------PREGUNTA 9--------------------------")
combinado_csv["dia"] = combinado_csv["date"].dt.weekday
combinado_csv['hora'] = combinado_csv["date"].dt.hour
combinado_csv['minuto'] = combinado_csv["date"].dt.minute

combinado_csv.drop(combinado_csv[(combinado_csv["dia"] < 5)].index, inplace=True)
combinado_csv.drop(combinado_csv[(combinado_csv["hora"] < 8)].index, inplace=True)
combinado_csv.drop(combinado_csv[(combinado_csv["hora"] > 20)].index, inplace=True)
combinado_csv.drop(combinado_csv[(combinado_csv["hora"] == 20) & (combinado_csv["minuto"] > 0)].index, inplace=True)
print(combinado_csv)
resultado9 = combinado_csv.groupby(['itemid']).agg(
                                  {'raiting': 'sum',
                                  }).reset_index()

print(resultado9.sort_values('raiting', ascending=False).head(10))
movie1 = item.loc[item['itemid'] == 50]
movie2 = item.loc[item['itemid'] == 100]
movie3 = item.loc[item['itemid'] == 7]
print(movie1['movie_title'])
print(movie2['movie_title'])
print(movie3['movie_title'])

