from application import app
from random import randrange


@app.route('/movies/randomise/generate/random_genre', methods=['GET'])
def generate_movie_genre():
    genre = Genre.query.all().genre
    ranger = len(genre)
    print(ranger)
    return genre[randrange(int(ranger))]

@app.route('movies/create/add/<filmID>', methods=['GET','POST'])
@login_required
def add_movie_genre(filmID, genre1, genre2, genre3, genre4, genre5):
    add = []
    movieData = Movies.query.filter_by(movie_title=title).first()
        for i in range(5):
            num = i + 1
            genre = 'genre' + str(num)
            check_genre = genre_check(genre)
            if check_genre == "":
                continue
            else:
                add.append(check_genre)
        for genres in add:
                genreData = Genre.query.filter_by(genre=genres).first()
                genrelinkData = GenreLink(
                    genre_id = genreData.id,
                    movie_id = movieData.id
                )
                db.session.add(genrelinkData)
    db.session.commit()
    return True

@app.route('movies/edit/<filmID>/update/genre', methods=['GET','POST'])
@login_required
def change_movie_genre(filmID, genre1, genre2, genre3, genre4, genre5):
    adding = []
    movieData = Movies.query.filter_by(movie_title=title).first()
        for i in range(5):
            num = i + 1
            genre = 'genre' + str(num)
            check_genre = genre_check(genre)
            if check_genre == "":
                continue
            else:
                adding.append(check_genre)
        own = GenreLink.query,filter_by(movie_id=filmID).all()
        for entry in own:
            db.session.delete(entry.id)
            db.session.commit()
        for genres in adding: 
            genreData = Genre.query.filter_by(genre=genres).first()
            genrelinkData = GenreLink(
                genre_id = genreData.id,
                movie_id = movieData.id
            )
            db.session.add(genrelinkData)
    db.session.commit()
    return True

@app.route('/movies/remove/<filmID>/genre', methods=['GET'])
def remove_movie_genre(filmID, remove):
    for link in remove:
        db.session.delete(link)
    db.session.commit()
    return True