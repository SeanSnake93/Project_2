from application import app
from flask import request, Responce
from random import randrange
import requests


@app.route('/old/<genre>', methods=['GET', 'POST'])
def old_generatemovie(genre):
    filt = []
    films = ['007: Casino Royal, Action, Adventure, Drama.', '007: Spectre, Action, Adventure, Drama.', '300, Action, Drama, War.', 'AdULTHOOD, Action, Drama.', 'Bad Boys, Action, Comedy, Drama.', 'Blade Runner, Action, Drama, Science Fiction.', 'Down to Earth, Comedy.', 'Fast & Furious, Action, Adventure, Drama.', 'Final Fantasy VII: Advent Children Complete, Action, Animated, Fantasy.', 'Fist Fill of Dollars, Action, Adventure, Drama, Western.', 'From Paris with Love, Action, Drama, Romance.', 'Gamer, Action, Drama, Science Fiction.', 'Grown Ups, Adventure, Comedy, Drama.', 'Hall Pass, Comedy, Drama, Romance.', 'I Love You Man, Comedy, Drama, Romance.', 'Indiana Jones and the Kingdom of the Crysral Skull, Action, Adventure, Drama, Science Fiction.', 'Indiana Jones and the Last Crusade, Action, Adventure, Drama.', 'Indiana Jones and the Raiders of the Lost Ark, Action, Adventure, Drama.', 'Indiana Jones and the Temple of Doom, Action, Adventure, Drama.', 'KiDULTHOOD, Action, Drama.', 'Man of Steel, Action, Adventure, Drama, Romance, Science Fiction.', 'Repo! The Genetic Opera, Drama, Musical, Science Fiction', 'Saving Private Ryan, Action, Adventure, Drama, War.', 'Scott Pilgrim vs. The World, Action, Adventure, Comedy, Fantasy, Romance, Science Fiction.', 'Shaun of the Dead, Actin, Comedy, Romance, Science Fiction.', 'Shrek, Adventure, Animated, Childrens, Comedy, Fantasy.', 'Shrek 2, Adventure, Animated, Childrens, Comedy, Fantasy.', 'Shrek: Forever After, Adventure, Animated, Childrens, Comedy, Fantasy.', 'Shrek: The Third, Adventure, Animated, Childrens, Comedy, Fantasy.', 'Sinister, Drama, Horror.', 'Straight outta Compton, Adventutre, Documentry, Drama, Musical.', 'Superbad, Comedy, Drama, Romance.', 'T2: Trainspotting, Action, Adventure, Drama.', 'Team America World Police, Action, Comedy.', 'Ted, Adventure, Comedy, Drama, Romance.', 'The Campaign, Comedy, Drama.', 'The Good the Bad and the Ugly, Action, Western.', 'The Greatest Showman, Adventure, Drama, Musical, Romance.', 'The Fault in our Stars, Adventure, Drama, Romance.', 'The Raid: Redemption, Action, Drama, War.', 'The Raid 2, Action, Drama, War.', 'The Social Network, Documentry, Drama.', 'The Ugly Truth, Adventure, Comedy Drama, Romance.', 'This is the End, Adventure, Comedy, Drama, Horror.', 'Thor: The Dark World, Action, Adventure, Fantacy, Science Fiction.', 'Tower Heist, Comedy, Drama.', 'Training Day, Action, Adventure, Drama.', 'Trainspotting, Adventure, Drama.', 'Wolf of Wall street, Adventure, Comedy, Drama.', 'World War Z, Action, Adventure, Horror, Science Fiction.', 'Whiplash, Drama, Musical.', 'Wreck-it Ralph, Adventure, Animated, Childrens.']
    for movie in films:
        if genre in movie:
            attributes = movie.split(",")
            title = attributes[0]
            print(title, "has been appended.")
            filt.append(title)
        else:
            continue
    ranger = len(filt)
    return Responce(filt[randrange(ranger)], mimetype='text/plain')

@app.route('/movie', methods=['GET', 'POST'])
def generatemovie():
    genre = request.data.decode('utf-8')
    movies = Movies.query.filter_by(genre1=genre or genre2=genre).all()
    movie = movies[randrange(len(movies))
    movieDict = {"title":movie.title, "year":movie.year, "rating":movie.rating, "description":movie.description, "genre1":movie.genre1, "genre2":movie.genre2}
    return jsonify{movieDict}