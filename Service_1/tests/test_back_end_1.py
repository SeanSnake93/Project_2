import unittest
from flask import abort, url_for
from flask_testing import TestCase
from application import app, db
from application.models import Genres, Movies, Generated
from os import getenv
import requests

# ---------- Base-SetUp-Testing ----------

class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        app.config.update(
            SQLALCHEMY_DATABASE_URI=getenv('TEST_PROJECT_URI'),
            SECRET_KEY=getenv('TEST_SECRET_KEY'),
            WTF_CSRF_ENABLED=False,
            DEBUG=True
            )
        return app
 
    def setUp(self):
        """Will be called before every test"""
        db.drop_all()
        db.create_all()
        db.session.commit()
        g1=Genres(genre="Action")
        g2=Genres(genre="Adventure")
        g3=Genres(genre="Animated")
        g4=Genres(genre="Comedy")
        g5=Genres(genre="Documentary")
        g6=Genres(genre="Drama")
        g7=Genres(genre="Fantasy")
        g8=Genres(genre="Horror")
        g9=Genres(genre="Musical")
        g10=Genres(genre="Romance")
        g11=Genres(genre="Science Fiction")
        g12=Genres(genre="War")
        g13=Genres(genre="Western")
        film01=Movies(movie_title="007: Casino Royal", year=2006, rating="15", genre1="Action", genre2="Adventure", genre3="Drama", genre4="", genre5="")
        film02=Movies(movie_title="007: Spectre", year=2015, rating="12A", genre1="Adventure", genre2="Action", genre3="Drama", genre4="", genre5="")
        film03=Movies(movie_title="300", year=2007, rating="15", genre1="Action", genre2="Drama", genre3="War", genre4="", genre5="")
        film04=Movies(movie_title="AdULTHOOD", year=2008, rating="15", genre1="Action", genre2="Drama", genre3="", genre4="", genre5="")
        film05=Movies(movie_title="Bad Boys", year=1995, rating="18", genre1="Action", genre2="Comedy", genre3="Drama", genre4="", genre5="")
        film06=Movies(movie_title="Blade Runner", year=1982, rating="15", genre1="Action", genre2="Drama", genre3="Science Fiction", genre4="", genre5="")
        film07=Movies(movie_title="Down to Earth", year=2001, rating="12", genre1="Comedy", genre2="", genre3="", genre4="", genre5="")
        film08=Movies(movie_title="Fast & Furious", year=2009, rating="12", genre1="Action", genre2="Adventure", genre3="Drama", genre4="", genre5="")
        film09=Movies(movie_title="Final Fantasy VII: Advent Children Complete", year=2005, rating="PG", genre1="Action", genre2="Animated", genre3="Fantasy", genre4="", genre5="")
        film10=Movies(movie_title="Fist Fill of Dollars", year=1964, rating="15", genre1="Action", genre2="Adventure", genre3="Drama", genre4="Western", genre5="")
        film11=Movies(movie_title="From Paris with Love", year=2010, rating="15", genre1="Action", genre2="Drama", genre3="Romance", genre4="", genre5="")
        film12=Movies(movie_title="Gamer", year=2009, rating="18", genre1="Action", genre2="Drama", genre3="Science Fiction", genre4="", genre5="")
        film13=Movies(movie_title="Grown Ups", year=2010, rating="12A", genre1="Adventure", genre2="Comedy", genre3="Drama", genre4="", genre5="")
        film14=Movies(movie_title="Hall Pass", year=2011, rating="15", genre1="Comedy", genre2="Drama", genre3="Romance", genre4="", genre5="")
        film15=Movies(movie_title="I Love You Man", year=2009, rating="15", genre1="Comedy", genre2="Drama", genre3="Romance", genre4="", genre5="")
        film16=Movies(movie_title="Indiana Jones and the Kingdom of the Crysral Skull", year=2008, rating="12", genre1="Action", genre2="Adventure", genre3="Drama", genre4="Science Fiction", genre5="")
        film17=Movies(movie_title="Indiana Jones and the Last Crusade", year=1989, rating="PG", genre1="Action", genre2="Adventure", genre3="Drama", genre4="", genre5="")
        film18=Movies(movie_title="Indiana Jones and the Raiders of the Lost Ark", year=1981, rating="PG", genre1="Action", genre2="Adventure", genre3="Drama", genre4="", genre5="")
        film19=Movies(movie_title="Indiana Jones and the Temple of Doom", year=1984, rating="12", genre1="Action", genre2="Adventure", genre3="Drama", genre4="", genre5="")
        film20=Movies(movie_title="KiDULTHOOD", year=2006, rating="15", genre1="Action", genre2="Drama", genre3="", genre4="", genre5="")
        film21=Movies(movie_title="Man of Steel", year=2013, rating="12", genre1="Action", genre2="Adventure", genre3="Drama", genre4="Romance", genre5="Science Fiction")
        film22=Movies(movie_title="Repo! The Genetic Opera", year=2008, rating="18", genre1="Drama", genre2="Musical", genre3="Science Fiction", genre4="", genre5="")
        film23=Movies(movie_title="Saving Private Ryan", year=1998, rating="15", genre1="Action", genre2="Adventure", genre3="Drama", genre4="War", genre5="")
        film24=Movies(movie_title="Scott Pilgrim vs. The World", year=2010, rating="12", genre1="Action", genre2="Comedy", genre3="Fantasy", genre4="Romance", genre5="Science Fiction")
        film25=Movies(movie_title="Shaun of the Dead", year=2004, rating="15", genre1="Action", genre2="Comedy", genre3="Romance", genre4="Science Fiction", genre5="")
        film26=Movies(movie_title="Shrek", year=2001, rating="U", genre1="Adventure", genre2="Animated", genre3="Childrens", genre4="Comedy", genre5="Fantasy")
        film27=Movies(movie_title="Shrek 2", year=2004, rating="U", genre1="Adventure", genre2="Animated", genre3="Childrens", genre4="Comedy", genre5="Fantasy")
        film28=Movies(movie_title="Shrek: Forever After", year=2010, rating="U", genre1="Adventure", genre2="Animated", genre3="Childrens", genre4="Comedy", genre5="Fantasy")
        film29=Movies(movie_title="Shrek: The Third", year=2007, rating="U", genre1="Adventure", genre2="Animated", genre3="Childrens", genre4="Comedy", genre5="Fantasy")
        film30=Movies(movie_title="Sinister", year=2012, rating="15", genre1="Drama", genre2="Horror", genre3="", genre4="", genre5="")
        film31=Movies(movie_title="Straight outta Compton", year=2015, rating="15", genre1="Adventutre", genre2="Documentry", genre3="Drama", genre4="Musical", genre5="")
        film32=Movies(movie_title="Superbad", year=2007, rating="15", genre1="Comedy", genre2="Drama", genre3="Romance", genre4="", genre5="")
        film33=Movies(movie_title="T2: Trainspotting", year=2017, rating="18", genre1="Action", genre2="Adventure", genre3="Drama", genre4="", genre5="")
        film34=Movies(movie_title="Team America World Police", year=2004, rating="15", genre1="Action", genre2="Comedy", genre3="", genre4="", genre5="")
        film35=Movies(movie_title="Ted", year=2012, rating="15", genre1="Adventure", genre2="Comedy", genre3="Drama", genre4="Romance", genre5="")
        film36=Movies(movie_title="The Campaign", year=2012, rating="15", genre1="Comedy", genre2="Drama", genre3="", genre4="", genre5="")
        film37=Movies(movie_title="The Good the Bad and the Ugly", year=1966, rating="18", genre1="Action", genre2="Western", genre3="", genre4="", genre5="")
        film38=Movies(movie_title="The Greatest Showman", year=2017, rating="PG", genre1="Adventure", genre2="Drama", genre3="genre3=Musical", genre4="Romance", genre5="")
        film39=Movies(movie_title="The Fault in our Stars", year=2014, rating="12", genre1="Adventure", genre2="Drama", genre3="Romance", genre4="", genre5="")
        film40=Movies(movie_title="The Raid: Redemption", year=2012, rating="18", genre1="Action", genre2="Drama", genre3="War", genre4="", genre5="")
        film41=Movies(movie_title="The Raid 2", year=2014, rating="18", genre1="Action", genre2="Drama", genre3="War", genre4="", genre5="")
        film42=Movies(movie_title="The Social Network", year=2010, rating="12", genre1="Documentry", genre2="Drama", genre3="", genre4="", genre5="")
        film43=Movies(movie_title="The Ugly Truth", year=2009, rating="15", genre1="Comedy", genre2="Drama", genre3="Romance", genre4="", genre5="")
        film44=Movies(movie_title="This is the End", year=2013, rating="15", genre1="Adventure", genre2="Comedy", genre3="Drama", genre4="Horror", genre5="")
        film45=Movies(movie_title="Thor: The Dark World", year=2013, rating="12A", genre1="Action", genre2="Adventure", genre3="Fantacy", genre4="Science Fiction", genre5="")
        film46=Movies(movie_title="Tower Heist", year=2011, rating="12A", genre1="Comedy", genre2="Drama", genre3="", genre4="", genre5="")
        film47=Movies(movie_title="Training Day", year=2001, rating="18", genre1="Action", genre2="Adventure", genre3="Drama", genre4="", genre5="")
        film48=Movies(movie_title="Trainspotting", year=1996, rating="18", genre1="Adventure", genre2="Drama", genre3="", genre4="", genre5="")
        film49=Movies(movie_title="Wolf of Wall street", year=2013, rating="18", genre1="Adventure", genre2="Comedy", genre3="Drama", genre4="", genre5="")
        film50=Movies(movie_title="World War Z", year=2013, rating="15", genre1="Action", genre2="Adventure", genre3="Horror", genre4="Science Fiction", genre5="")
        film51=Movies(movie_title="Whiplash", year=2014, rating="15", genre1="Drama", genre2="Musical", genre3="", genre4="", genre5="")
        film52=Movies(movie_title="Wreck-it Ralph", year=2012, rating="PG", genre1="Adventure", genre2="Animated", genre3="Childrens", genre4="", genre5="")
        db.session.add(g1)
        db.session.add(g2)
        db.session.add(g3)
        db.session.add(g4)
        db.session.add(g5)
        db.session.add(g6)
        db.session.add(g7)
        db.session.add(g8)
        db.session.add(g9)
        db.session.add(g10)
        db.session.add(g11)
        db.session.add(g12)
        db.session.add(g13)
        db.session.add(film01)
        db.session.add(film02)
        db.session.add(film03)
        db.session.add(film04)
        db.session.add(film05)
        db.session.add(film06)
        db.session.add(film07)
        db.session.add(film08)
        db.session.add(film09)
        db.session.add(film10)
        db.session.add(film11)
        db.session.add(film12)
        db.session.add(film13)
        db.session.add(film14)
        db.session.add(film15)
        db.session.add(film16)
        db.session.add(film17)
        db.session.add(film18)
        db.session.add(film19)
        db.session.add(film20)
        db.session.add(film21)
        db.session.add(film22)
        db.session.add(film23)
        db.session.add(film24)
        db.session.add(film25)
        db.session.add(film26)
        db.session.add(film27)
        db.session.add(film28)
        db.session.add(film29)
        db.session.add(film30)
        db.session.add(film31)
        db.session.add(film32)
        db.session.add(film33)
        db.session.add(film34)
        db.session.add(film35)
        db.session.add(film36)
        db.session.add(film37)
        db.session.add(film38)
        db.session.add(film39)
        db.session.add(film40)
        db.session.add(film41)
        db.session.add(film42)
        db.session.add(film43)
        db.session.add(film44)
        db.session.add(film45)
        db.session.add(film46)
        db.session.add(film47)
        db.session.add(film49)
        db.session.add(film50)
        db.session.add(film51)
        db.session.add(film52)
        db.session.add(film48)
        db.session.commit()

    def tearDown(self):
        """Will be called after every test"""
        db.session.remove()
        db.drop_all()

# -------- END-Base-SetUp-Testing --------

# ____________________________________________________________________

# ---------- Visit-Testing ----------

class TestViews(TestBase):
    def test_homepage_view(self):
        """This is the server getting a status code 200 on Home page"""
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

class TestViews(TestBase):
    def test_about_view(self):
        """This is the server getting a status code 200 on about page"""
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)

class TestViews(TestBase):
    def test_history_view(self):
        """This is the server getting a status code 200 on logs page"""
        response = self.client.get(url_for('history'))
        self.assertEqual(response.status_code, 200)

class TestViews(TestBase):
    def test_sql_data_view(self):
        """This is the server getting a status code 200 on movies and genres page"""
        response = self.client.get(url_for('sql_data'))
        self.assertEqual(response.status_code, 200)

# -------- END-Visit-Testing --------

# ____________________________________________________________________

# ---------- Create-Function-Testing ----------

class TestHistory(TestBase):
    """Testing to see if Generated content is infact added"""
    def test_own_film(self):
        with self.client:
            response = self.client.post(
                url_for('home'),
                follow_redirects=True
            )
            self.assertEqual(response.status_code, 200)
        self.assertEqual(Generated.query.count(), 1)

# -------- END-Create-Function-Testing --------

# ____________________________________________________________________

# ---------- Read-Function-Testing ----------


class TestUpload(TestBase):
    """Testing to see if content is added"""
    def test_own_film(self):
        with self.client:
            self.assertEqual(Movies.query.count(), 52)
            self.assertEqual(Genres.query.count(), 13)

# -------- Read-Function-Limitations --------

# -------- END-Read-Function-Testing --------

# ____________________________________________________________________

# ---------- Update-Function-Testing ----------

# -------- Update-Function-Limitations --------

# -------- END-Update-Function-Testing --------

# ____________________________________________________________________

# ---------- Delete-Function-Testing ----------

# -------- Delete-Function-Limitations --------

# -------- END-Delete-Function-Testing --------