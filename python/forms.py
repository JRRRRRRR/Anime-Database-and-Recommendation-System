import pandas as pd
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

df = pd.read_csv('/Users/jrchen/flatiron-ds-course/Milestones/capstone/cleaningData/clean_basic.csv')
df.set_index('anime_id', inplace=True)
genre_list=[] 
for i in df['genre']:
    for n in i.split(','):
        if n.strip() not in genre_list:
            genre_list.append(n.strip())
genre_list.sort()
for i in range(len(genre_list)):
    genre_list[i] = (genre_list[i],genre_list[i])
genre_list.insert(0, ('ALL','ALL'))


class SearchForm(FlaskForm):
		
	title = StringField('title')
	animeID = IntegerField('anime ID')
	sortBy = SelectField('sort by', 
		choices=[('ALL',''),('dropped','dropped'),('episodes','episodes'),('finishYr','finish year'),('members','members'),
		('rating','rating'),('startYr','start year'),('wantWatch','want watch'),('watched','watched'),('watching','watching'),
		('wantWatch','want watch')])
	ongoing = SelectField('on going', 
		choices=[('ALL','ALL'),('1','TRUE'),('0','FALSE')])
	orderBy = SelectField('order by', 
		choices=[(1,'ascending'),(0,'descending')])
	animeType = SelectField('anime type', 
		choices=[('ALL','ALL'),('Movie','movie'),('Music','music'),('ONA','original net animation'),('OVA','original video animation'),
		('Special','special'),('TV','TV')])
	sznOfRelease = SelectField('season of release', 
		choices=[('ALL','ALL'),('Spring','spring'),('Summer','summer'),('Fall','fall'),('Winter','winter')])
	genre = SelectField('genre', 
		choices=genre_list)
	num = IntegerField('numbers of evaluation')
	search = SubmitField('search')
	submit = SubmitField('submit')
	rating0 = FloatField('rating:')
	rating1 = FloatField('rating:')
	rating2 = FloatField('rating:')
	rating3 = FloatField('rating:')
	rating4 = FloatField('rating:')
	rating5 = FloatField('rating:')
	rating6 = FloatField('rating:')
	rating7 = FloatField('rating:')
	rating8 = FloatField('rating:')
	rating9 = FloatField('rating:')

	analyze = SelectField('analyze field', 
		choices=[('dropped','dropped'),('duration','duration'),('finishYr','finish year'),('genre','genre'),('members','members'),
		('ongoing','ongoing'),('rating','rating'),('sznOfRelease','season of release'),('startYr','start year'),('type','type'),
		('wantWatch','want watch'),('watched','watched'),('watching','watching'),('wantWatch','want watch')])
	










	


