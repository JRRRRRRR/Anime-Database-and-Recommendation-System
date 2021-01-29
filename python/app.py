from flask import Flask, render_template, url_for, request, redirect
from forms import SearchForm
import numpy as np
import pandas as pd
import requests
import io
import PIL.Image
from IPython.display import display

import base64

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker


from surprise.prediction_algorithms import CoClustering
from surprise import Reader, Dataset
ratings = pd.read_csv('../cleaningData/clean_rating.csv', index_col=0)
df = pd.read_csv('../cleaningData/clean_basic.csv')
df.set_index('anime_id', inplace=True)

reader = Reader(rating_scale=(1, 10))
#data = Dataset.load_from_df(ratings,reader)
#dataset = data.build_full_trainset()
#coc = CoClustering(n_cltr_u= 3, n_cltr_i=5)
#coc.fit(dataset)



app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'



@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
	
	return render_template('home.html')

@app.route("/search", methods=['GET', 'POST'])
def search():
	form = SearchForm()
	anime_df = df.reset_index()
	if form.is_submitted():
		try:
			title = str(request.form['title'])
			if title:
				titles = anime_df.columns
				myresult = anime_df[anime_df['title'].str.contains(title)]
				return render_template('search.html', form=form, column_names=myresult.columns.values, row_data=list(myresult.values.tolist()),
                           	link_column="imageLink", zip=zip)
		except:
			print('error')

		try:
			animeID = int(request.form['animeID'])
			if animeID:
				myresult = anime_df.loc[df.index==animeID]
				titles = anime_df.columns
				return render_template('search.html', form=form, column_names=myresult.columns.values, row_data=list(myresult.values.tolist()),
                           link_column="imageLink", zip=zip)
		except:
			print('error')	
	return render_template('search.html', form=form)

@app.route("/sort", methods=['GET', 'POST'])
def sort():
	form = SearchForm()
	anime_df = df.reset_index()
	if form.is_submitted():
		ongoing = request.form['ongoing']
		sznOfRelease = request.form['sznOfRelease']
		animeType = request.form['animeType']
		genre = request.form['genre']

		sortBy = request.form['sortBy']
		orderBy = int(request.form['orderBy'])

		titles = anime_df.columns
		myresult = anime_df
		if ongoing != 'ALL':
			myresult = myresult.loc[myresult['ongoing']==bool(int(ongoing))]
		if sznOfRelease != 'ALL':
			myresult = myresult.loc[myresult['sznOfRelease']==sznOfRelease]
		if animeType != 'ALL':
			myresult = myresult.loc[myresult['type']==animeType]
		if genre != 'ALL':
			myresult = myresult.loc[myresult['genre'].str.contains(genre)]
		if sortBy != 'ALL':
			myresult = myresult.sort_values(sortBy, ascending=orderBy)
			
		return render_template('sort.html', form=form, column_names=myresult.columns.values, row_data=list(myresult.values.tolist()),
                           link_column="imageLink", zip=zip)
			
	return render_template('sort.html', form=form)

	

@app.route("/analyze", methods=['GET', 'POST'])
def analyze():
	form = SearchForm()
	anime_df = df.reset_index()
	continuous=['duration', 'watched', 'startYr', 'finishYr', 'watching', 'wantWatch', 'dropped', 'rating', 'members']
	cat = ['type', 'ongoing', 'genre', 'sznOfRelease']
	if form.is_submitted():
		animeID = int(request.form['animeID'])
		analyzeField = request.form['analyze']
		myresult = anime_df.loc[df.index==animeID]
		titles = anime_df.columns
		if analyzeField in continuous:
		    plt.figure(figsize=(12,8))
		    sns.distplot(df[analyzeField])
		    try:
		        plt.axvline(myresult[analyzeField].values[0], ls='--', c='red')
		    except:
		        print('no data here')
		    plt.savefig('../python/static/dist_{}.png'.format(analyzeField))
		    plt.close()

		if analyzeField in continuous:
		    plt.figure(figsize=(12,8))
		    sns.boxplot(df[analyzeField])
		    try:
		        plt.axvline(myresult[analyzeField].values[0], ls='--', c='red')
		    except:
		        print('no data here')
		    plt.savefig('../python/static/box_{}.png'.format(analyzeField))
		    plt.close()

		return render_template('analyze.html', form=form, column_names=myresult.columns.values, row_data=list(myresult.values.tolist()),
                link_column="imageLink", zip=zip, myresult=myresult, catField=[analyzeField, 'cat_{}.png'.format(analyzeField)], 
                cat=cat, contField=[analyzeField, 'dist_{}.png'.format(analyzeField), 'box_{}.png'.format(analyzeField)], 
                continuous=continuous)
			
	return render_template('empty.html', form=form)


@app.route("/recommendation", methods=['GET', 'POST'])
def recommendation():
	form = SearchForm()
	genre = 'ALL'
	anime_df = df.reset_index()
	num = 10
	userID = 88888
	rating_list = []
	ratings_form = [form.rating0, form.rating1, form.rating2, form.rating3, form.rating4, form.rating5, form.rating6, 
	form.rating7, form.rating8, form.rating9]
	if genre != 'ALL':
		animes = anime_df.loc[anime_df['genre'].str.contains(str(genre))].sample(num)[['anime_id', 'title', 'imageLink']]
	else:
		animes = anime_df.sample(num)[['anime_id', 'title', 'imageLink']]
	if form.is_submitted():
		rating0 = request.form.get('rating0', False)
		rating1 = request.form.get('rating1', False)
		rating2 = request.form.get('rating2', False)
		rating3 = request.form.get('rating3', False)
		rating4 = request.form.get('rating4', False)
		rating5 = request.form.get('rating5', False)
		rating6 = request.form.get('rating6', False)
		rating7 = request.form.get('rating7', False)
		rating8 = request.form.get('rating8', False)
		rating9 = request.form.get('rating9', False)
		for rating, anime in zip([rating0, rating1, rating2, rating3, rating4, rating5, rating6, rating7, rating8, rating9], animes.values):
			if rating == 0:
				continue
			else:
				rating_one_anime = {'user_id':userID,'anime_id':anime[0],'rating':rating}
				rating_list.append(rating_one_anime)
		ratings_df = ratings.append(rating_list,ignore_index=True)
		#reader = Reader(rating_scale=(1, 10))
		data = Dataset.load_from_df(ratings_df,reader)
		dataset = data.build_full_trainset()
		coc = CoClustering(n_cltr_u= 3, n_cltr_i=5)
		coc.fit(dataset)
		# Make predictions for the user
		# Create a list of tuples in the format (anime_id, predicted_score)
		list_of_animes = []
		for m_id in ratings['anime_id'].unique():
			list_of_animes.append( (m_id, coc.predict(1000,m_id)[3]))
		# Rank by rating
		ranked_animes = sorted(list_of_animes, key=lambda x:x[1], reverse=True)

		# Create some lists to store values
		id_list = []
		title_list = []
		image_list = []

		for i in range(5):
			id_ = ranked_animes[i][0]
			id_list.append(id_)
			title_list.append(anime_df.loc[anime_df['anime_id'] == int(id_)]['title'].values[0])
			image_list.append(anime_df.loc[anime_df['anime_id'] == int(id_)]['imageLink'].values[0])

		return render_template('display.html', column_names=['anime_id','title','poster'], link_column="anime_id",
			id_list=id_list, title_list=title_list, image_list=image_list, zip=zip)


	return render_template('recommendation.html', form=form, animes=animes, userID=userID, 
			column_names=['anime_id','title','rating'], row_data=list(animes.values.tolist()), link_column="anime_id", 
			image_column='rating', zip=zip, ratings_form=ratings_form)

@app.route("/mysuperplot", methods=["GET"])
def plotView():

    # Generate plot
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title("title")
    axis.set_xlabel("x-axis")
    axis.set_ylabel("y-axis")
    axis.grid()
    axis.plot(range(5), range(5), "ro-")
    
    # Convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    
    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    
    return render_template("image.html", image=pngImageB64String)





if __name__ == '__main__':
	app.run(debug=True)