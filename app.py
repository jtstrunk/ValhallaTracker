from flask import Flask, render_template, flash, redirect, url_for, request, jsonify
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import and_, or_, Date, text, literal
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length, Email
from datetime import date, datetime
import os
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = '1145'
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\Users\Josh Strunk\Desktop\ValhallaTracker\db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    email = StringField('email', validators=[InputRequired(), Email(message='Invald Email'), Length(max=50)])
    fullname = StringField('fullname', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

friends = db.Table('friends',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('friend_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)

userFavorites = db.Table('userFavorites',
        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
        db.Column('game_id', db.Integer, db.ForeignKey('supported_games.id'))
    )

playedUsers = db.Table('playedUsers',
        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
        db.Column('player_id', db.Integer, db.ForeignKey('supported_names.id'))
    )

class User(UserMixin, db.Model):
        id = db.Column(db.Integer, primary_key=True)
        fullname = db.Column(db.String(50), nullable=False)
        username = db.Column(db.String(15), nullable=False, unique=True)
        email = db.Column(db.String(50), nullable=False, unique=True)
        password = db.Column(db.String(80), nullable=False)

        favorites = db.relationship('SupportedGames', secondary=userFavorites, backref='favoritedby')
        played = db.relationship('SupportedNames', secondary=playedUsers, backref='playedwith')

        friends = db.relationship('User', secondary=friends,
                                primaryjoin=(friends.c.user_id == id),
                                secondaryjoin=(friends.c.friend_id == id),
                                backref=db.backref('friend_of', lazy='dynamic'),
                                lazy='dynamic')
        
class SupportedGames(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        gameName = db.Column(db.String(50))
        numPlayers = db.Column(db.String(50))

class SupportedNames(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        playerID = db.Column(db.Integer)
        playerName = db.Column(db.String(50))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class DominionGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, nullable=False)
    poster_id = db.Column(db.Integer)
    winnerName = db.Column(db.String(50), nullable=False)
    winnerScore = db.Column(db.Integer, nullable=False)
    secondName = db.Column(db.String(50), nullable=False)
    secondScore = db.Column(db.Integer, nullable=False)
    thirdName = db.Column(db.String(50))
    thirdScore = db.Column(db.Integer)
    fourthName = db.Column(db.String(50))
    fourthScore = db.Column(db.Integer)
    date = db.Column(db.Date)

class CatanGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, nullable=False)
    poster_id = db.Column(db.Integer)
    winnerName = db.Column(db.String(50), nullable=False)
    winnerScore = db.Column(db.Integer, nullable=False)
    secondName = db.Column(db.String(50), nullable=False)
    secondScore = db.Column(db.Integer, nullable=False)
    thirdName = db.Column(db.String(50))
    thirdScore = db.Column(db.Integer)
    fourthName = db.Column(db.String(50))
    fourthScore = db.Column(db.Integer)
    date = db.Column(db.Date)

class LordsofWaterdeepGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, nullable=False)
    poster_id = db.Column(db.Integer)
    winnerName = db.Column(db.String(50), nullable=False)
    winnerScore = db.Column(db.Integer, nullable=False)
    secondName = db.Column(db.String(50), nullable=False)
    secondScore = db.Column(db.Integer, nullable=False)
    thirdName = db.Column(db.String(50))
    thirdScore = db.Column(db.Integer)
    fourthName = db.Column(db.String(50))
    fourthScore = db.Column(db.Integer)
    fifthName = db.Column(db.String(50))
    fifthScore = db.Column(db.Integer)
    date = db.Column(db.Date)

class MagicTheGatheringGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, nullable=False)
    poster_id = db.Column(db.Integer)
    winnerName = db.Column(db.String(50), nullable=False)
    winnerColor = db.Column(db.String(50), nullable=False)
    winnerKills = db.Column(db.Integer)
    winnerDeck = db.Column(db.String(50))
    secondName = db.Column(db.String(50), nullable=False)
    secondColor = db.Column(db.String(50), nullable=False)
    secondKills = db.Column(db.Integer)
    secondDeck = db.Column(db.String(50))
    thirdName = db.Column(db.String(50))
    thirdColor = db.Column(db.String(50))
    thirdKills = db.Column(db.Integer)
    thirdDeck = db.Column(db.String(50))
    fourthName = db.Column(db.String(50))
    fourthColor = db.Column(db.String(50))
    fourthKills = db.Column(db.Integer)
    fourthDeck = db.Column(db.String(50))
    fifthName = db.Column(db.String(50))
    fifthColor = db.Column(db.String(50))
    fifthKills = db.Column(db.Integer)
    fifthDeck = db.Column(db.String(50))
    date = db.Column(db.Date)

class CoupGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, nullable=False)
    poster_id = db.Column(db.Integer)
    winnerName = db.Column(db.String(50), nullable=False)
    secondName = db.Column(db.String(50), nullable=False)
    thirdName = db.Column(db.String(50))
    fourthName = db.Column(db.String(50))
    fifthName = db.Column(db.String(50))
    sixthName = db.Column(db.String(50))
    date = db.Column(db.Date)

class LoveLetterGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, nullable=False)
    poster_id = db.Column(db.Integer)
    winnerName = db.Column(db.String(50), nullable=False)
    secondName = db.Column(db.String(50), nullable=False)
    thirdName = db.Column(db.String(50))
    fourthName = db.Column(db.String(50))
    fifthName = db.Column(db.String(50))
    sixthName = db.Column(db.String(50))
    date = db.Column(db.Date)

class MunchkinGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, nullable=False)
    poster_id = db.Column(db.Integer)
    winnerName = db.Column(db.String(50), nullable=False)
    winnerScore = db.Column(db.Integer, nullable=False)
    secondName = db.Column(db.String(50), nullable=False)
    secondScore = db.Column(db.Integer, nullable=False)
    thirdName = db.Column(db.String(50), nullable=False)
    thirdScore = db.Column(db.Integer, nullable=False)
    fourthName = db.Column(db.String(50))
    fourthScore = db.Column(db.Integer)
    fifthName = db.Column(db.String(50))
    fifthScore = db.Column(db.Integer)
    sixthName = db.Column(db.String(50))
    sixthScore = db.Column(db.Integer)
    date = db.Column(db.Date)

class TheMindGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, nullable=False)
    poster_id = db.Column(db.Integer)
    playerone = db.Column(db.String(50), nullable=False)
    playertwo = db.Column(db.String(50), nullable=False)
    playerthree = db.Column(db.String(50))
    playerfour = db.Column(db.String(50))
    victory = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date)
    
class JustOneGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, nullable=False)
    poster_id = db.Column(db.Integer)
    playerone = db.Column(db.String(50), nullable=False)
    playertwo = db.Column(db.String(50), nullable=False)
    playerthree = db.Column(db.String(50))
    playerfour = db.Column(db.String(50))
    playerfive = db.Column(db.String(50))
    playersix = db.Column(db.String(50))
    playerseven = db.Column(db.String(50))
    victory = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date)

class CosmicEncounterGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, nullable=False)
    poster_id = db.Column(db.Integer)
    winnerName = db.Column(db.String(50), nullable=False)
    winnerScore = db.Column(db.Integer, nullable=False)
    secondName = db.Column(db.String(50), nullable=False)
    secondScore = db.Column(db.Integer, nullable=False)
    thirdName = db.Column(db.String(50), nullable=False)
    thirdScore = db.Column(db.Integer, nullable=False)
    fourthName = db.Column(db.String(50))
    fourthScore = db.Column(db.Integer)
    fourthName = db.Column(db.String(50))
    fourthScore = db.Column(db.Integer)
    fifthName = db.Column(db.String(50))
    fifthScore = db.Column(db.Integer)
    date = db.Column(db.Date)

class MoonrakersGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, nullable=False)
    poster_id = db.Column(db.Integer)
    winnerName = db.Column(db.String(50), nullable=False)
    winnerScore = db.Column(db.Integer, nullable=False)
    secondName = db.Column(db.String(50))
    secondScore = db.Column(db.Integer)
    thirdName = db.Column(db.String(50))
    thirdScore = db.Column(db.Integer)
    fourthName = db.Column(db.String(50))
    fourthScore = db.Column(db.Integer)
    fourthName = db.Column(db.String(50))
    fourthScore = db.Column(db.Integer)
    fifthName = db.Column(db.String(50))
    fifthScore = db.Column(db.Integer)
    date = db.Column(db.Date)

class ClankGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, nullable=False)
    poster_id = db.Column(db.Integer)
    winnerName = db.Column(db.String(50), nullable=False)
    winnerScore = db.Column(db.Integer, nullable=False)
    secondName = db.Column(db.String(50), nullable=False)
    secondScore = db.Column(db.Integer, nullable=False)
    thirdName = db.Column(db.String(50))
    thirdScore = db.Column(db.Integer)
    fourthName = db.Column(db.String(50))
    fourthScore = db.Column(db.Integer)
    date = db.Column(db.Date)

class HeatGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, nullable=False)
    poster_id = db.Column(db.Integer)
    winnerName = db.Column(db.String(50), nullable=False)
    secondName = db.Column(db.String(50))
    thirdName = db.Column(db.String(50))
    fourthName = db.Column(db.String(50))
    fifthName = db.Column(db.String(50))
    sixthName = db.Column(db.String(50))
    date = db.Column(db.Date)

class SpaceBaseGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, nullable=False)
    poster_id = db.Column(db.Integer)
    winnerName = db.Column(db.String(50), nullable=False)
    winnerScore = db.Column(db.Integer, nullable=False)
    secondName = db.Column(db.String(50), nullable=False)
    secondScore = db.Column(db.Integer, nullable=False)
    thirdName = db.Column(db.String(50))
    thirdScore = db.Column(db.Integer)
    fourthName = db.Column(db.String(50))
    fourthScore = db.Column(db.Integer)
    fifthName = db.Column(db.String(50))
    fifthScore = db.Column(db.Integer)
    date = db.Column(db.Date)

class SushiGoPartyGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, nullable=False)
    poster_id = db.Column(db.Integer)
    winnerName = db.Column(db.String(50), nullable=False)
    winnerScore = db.Column(db.Integer, nullable=False)
    secondName = db.Column(db.String(50), nullable=False)
    secondScore = db.Column(db.Integer, nullable=False)
    thirdName = db.Column(db.String(50))
    thirdScore = db.Column(db.Integer)
    fourthName = db.Column(db.String(50))
    fourthScore = db.Column(db.Integer)
    fifthName = db.Column(db.String(50))
    fifthScore = db.Column(db.Integer)
    sixthName = db.Column(db.String(50))
    sixthScore = db.Column(db.Integer)
    seventhName = db.Column(db.String(50))
    seventhScore = db.Column(db.Integer)
    eighthName = db.Column(db.String(50))
    eighthScore = db.Column(db.Integer)
    date = db.Column(db.Date)

class ExplodingKittensGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, nullable=False)
    poster_id = db.Column(db.Integer)
    winnerName = db.Column(db.String(50), nullable=False)
    secondName = db.Column(db.String(50), nullable=False)
    thirdName = db.Column(db.String(50))
    fourthName = db.Column(db.String(50))
    fifthName = db.Column(db.String(50))
    sixthName = db.Column(db.String(50))
    seventhName = db.Column(db.String(50))
    eighthName = db.Column(db.String(50))
    ninthName = db.Column(db.String(50))
    tenthName = db.Column(db.String(50))
    date = db.Column(db.Date)

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    email = StringField('email', validators=[InputRequired(), Email(message='Invald Email'), Length(max=50)])
    fullname = StringField('display name', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

class Cards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cardName = db.Column(db.String(50), nullable=False)
    cardSet = db.Column(db.String(50), nullable=False)
class Village(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cardName = db.Column(db.String(50), db.ForeignKey('cards.cardName'), nullable=False)
    card = db.relationship('Cards', backref='village')
class Cantrip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cardName = db.Column(db.String(50), db.ForeignKey('cards.cardName'), nullable=False)
    card = db.relationship('Cards', backref='cantrip')
class Gainer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cardName = db.Column(db.String(50), db.ForeignKey('cards.cardName'), nullable=False)
    card = db.relationship('Cards', backref='gainer')
class Sifter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cardName = db.Column(db.String(50), db.ForeignKey('cards.cardName'), nullable=False)
    card = db.relationship('Cards', backref='sifter')
class Trasher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cardName = db.Column(db.String(50), db.ForeignKey('cards.cardName'), nullable=False)
    card = db.relationship('Cards', backref='trasher')
class NonterminalDraw(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cardName = db.Column(db.String(50), db.ForeignKey('cards.cardName'), nullable=False)
    card = db.relationship('Cards', backref='nonterminalDraw')
class TerminalDraw(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cardName = db.Column(db.String(50), db.ForeignKey('cards.cardName'), nullable=False)
    card = db.relationship('Cards', backref='terminalDraw')
class TerminalSilver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cardName = db.Column(db.String(50), db.ForeignKey('cards.cardName'), nullable=False)
    card = db.relationship('Cards', backref='terminalSilver')
class Action(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cardName = db.Column(db.String(50), db.ForeignKey('cards.cardName'), nullable=False)
    card = db.relationship('Cards', backref='action')
class Attack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cardName = db.Column(db.String(50), db.ForeignKey('cards.cardName'), nullable=False)
    card = db.relationship('Cards', backref='attack')
class Victory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cardName = db.Column(db.String(50), db.ForeignKey('cards.cardName'), nullable=False)
    card = db.relationship('Cards', backref='victory')
class Treasure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cardName = db.Column(db.String(50), db.ForeignKey('cards.cardName'), nullable=False)
    card = db.relationship('Cards', backref='treasure')
class Reaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cardName = db.Column(db.String(50), db.ForeignKey('cards.cardName'), nullable=False)
    card = db.relationship('Cards', backref='reaction')
class Duration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cardName = db.Column(db.String(50), db.ForeignKey('cards.cardName'), nullable=False)
    card = db.relationship('Cards', backref='duration')

class Expansions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, nullable=False)
    expansionList = db.Column(db.Text, nullable=False)   

@app.route('/')
@app.route('/home')
@login_required
def home():

    user = User.query.filter_by(username=current_user.username).first()
    user_friends = user.friends.limit(5).all()

    topGames = findRecentGames(user)
    friendsGames = findFriendsGames(current_user)

    combinedGames = topGames + friendsGames
    combinedGames = sorted(combinedGames, key=lambda x: x['game_id'], reverse=True)

    print("combinedGames")
    print(combinedGames)
    
    combinedGames = combinedGames[:12]



    gamesWon = calcGamesWon(user)
    gamesPlayed = calcGamesPlayed(user)
    mostPlayed = calcMostPlayed(user)
    mostWon = calcMostWon(user)
    bestFriend = calcBestFriend(user)

    games = user.favorites

    favoriteGames = []
    for game in games:
        game_name = game.gameName
        num_players = game.numPlayers
        favoriteGames.append((game_name, num_players))

    profileStats = [gamesPlayed, gamesWon, mostPlayed, mostWon, bestFriend]

    return render_template('home.html', title='Home', name=current_user.fullname, friends=user_friends, recentGames=combinedGames, profileStats=profileStats, favoriteGames=favoriteGames)

@app.route('/dominion', methods=['GET'])
def dominion():
    return render_template('dominion.html')

@app.route('/login', methods=['GET','POST'])
def login():
    form= LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if user is not None and user.password == password:
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))

    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET','POST'])
def register():
    form=RegisterForm()
    if form.validate_on_submit():
        new_user = User(username = form.username.data, email = form.email.data, password = form.password.data, fullname = form.fullname.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')
    
    return render_template('register.html', title='Register', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/profile')
@login_required
def profile():
    userName = request.args.get('name')

    if userName != 'current':
        user = User.query.filter_by(username=userName).first()
    else:
        user = current_user

    user_friends = user.friends.limit(5).all()
    print("user_friends")
    print(user_friends)
    topGames = findRecentGames(user)
    topGames = sorted(topGames, key=lambda x: x['game_id'], reverse=True)
    games = user.favorites

    gameResults = []
    for game in games:
        #fullname = user.fullname
        game_name = game.gameName
        num_players = game.numPlayers
        gameResults.append((game_name, num_players))

    print("gameResults")
    print(gameResults)

    for game_name, num_players in gameResults:
        print(f"{game_name} has {num_players}")

    gamesWon = calcGamesWon(user)
    gamesPlayed = calcGamesPlayed(user)
    mostPlayed = calcMostPlayed(user)
    mostWon = calcMostWon(user)
    bestFriend = calcBestFriend(user)
    
    profileStats = [gamesPlayed, gamesWon, mostPlayed, mostWon, bestFriend]

    games = SupportedGames.query.with_entities(SupportedGames.gameName).all()
    game_list = [game[0] for game in games]
    
    return render_template('profile.html', user=user, friends=user_friends, recentGames = topGames, favoriteGames=gameResults, profileStats = profileStats, profileName=userName, currUser = current_user, game_list=game_list)

@app.route('/friend', methods = ['GET'])
@login_required
def friend():
    user = current_user
    user_friends = user.friends.all()
    return render_template('friends.html', friends=user_friends)

@app.route('/addfriend', methods=['POST'])
@login_required
def addFriend():
    user1 = current_user
    username = request.form.get('addAccount')
    user2 = User.query.filter_by(username=username).first()

    if user2:
        user1.friends.append(user2)
        user2.friends.append(user1)
        db.session.commit()
        flash('Friend added successfully!', 'success')
    else:
        flash('User not found.', 'danger')

    return redirect(url_for('home'))
        
@app.route('/removefriend', methods=['POST'])
@login_required
def removefriend():
    user1 = current_user
    username = request.form.get('removeAccount')
    user2 = User.query.filter_by(username=username).first()

    if user2:
        user1.friends.remove(user2)
        user2.friends.remove(user1)
        db.session.commit()
        print("removingdasdsadsadsa")

    print("removing")
    return redirect(url_for('friend'))

@app.route('/returnFriends', methods=['GET'])
def returnFriends():
    user_playedwith = SupportedNames.query.filter(SupportedNames.playerID == current_user.id)

    friends_list = [friend.playerName for friend in user_playedwith]
    print(friends_list)
    return jsonify(friends_list)

@app.route('/addFavorite', methods=['POST'])
def addFavorite():
    game = request.args.get('game')
    print(game)
    user = User.query.get(current_user.id)
    # gameID = 4
    game_obj = SupportedGames.query.filter_by(gameName=game).first()
    user.favorites.append(game_obj)

    # favorite = userFavorites(user_id=userID, game_id=gameID)
    # userID.favorites.append(favorite)
    db.session.commit()
    return 'Game Added'


@app.route('/showGames', methods=['GET'])
@login_required
def showGames():

    games = current_user.favorites

    favoriteGames = []
    for game in games:
        #fullname = user.fullname
        game_name = game.gameName
        num_players = game.numPlayers
        favoriteGames.append((game_name, num_players))

    print("favoriteGames")
    print(favoriteGames)

    sortedGames = findRecentGames(current_user)
    sortedGames = sorted(sortedGames, key=lambda x: x['game_id'], reverse=True)
    
    return render_template('GameRecords.html', title='Show Games', sortedGames=sortedGames, favoriteGames=favoriteGames)

@app.route('/addGame', methods=['GET'])
@login_required
def addGame():
    return render_template("addGame.html", title='Home')

@app.route('/displayGame', methods=['GET'])
@login_required
def displayGame():
    game = request.args.get('game')
    game = game.replace(" ", "")
    gameid = request.args.get('id')

    fullGameName = f'{game}Game'
    gameModel = globals()[fullGameName]
    gameInfo = gameModel.query.filter_by(game_id=gameid).first()

    fields_to_return = ['winnerName', 'winnerScore', 'secondName', 'secondScore', 'thirdName', 'thirdScore', 'fourthName', 'fourthScore', 'fifthName', 'fifthScore', 'sixthName', 'sixthScore', 'date']
    response_data = {key: getattr(gameInfo, key) for key in fields_to_return if hasattr(gameInfo, key)}
    return jsonify(response_data)

@app.route('/updategame', methods=['POST'])
def updategame():
    if request.method == 'POST':
        game = request.form['game']
        game = game.replace(" ", "")
        print(game)
        game_id = request.form['game_id']
        date_str = request.form['datepicker']
        newdate = datetime.strptime(date_str, '%Y-%m-%d').date()

        full_game_name = f'{game}Game'
        game_model = globals().get(full_game_name)
        
        if game_model:
            existing_game = game_model.query.filter_by(game_id=game_id).first()

            if existing_game:
                # Update the existing record with new data
                existing_game.winnerName = request.form['winnerName']
                existing_game.winnerScore = request.form['winnerScore']
                existing_game.secondName = request.form['secondName']
                existing_game.secondScore = request.form['secondScore']
                existing_game.thirdName = request.form['thirdName']
                existing_game.thirdScore = request.form['thirdScore']
                existing_game.fourthName = request.form['fourthName']
                existing_game.fourthScore = request.form['fourthScore']

                if hasattr(existing_game, 'fifthName'):
                    existing_game.fifthName = request.form.get('fifthName', None)
                if hasattr(existing_game, 'fifthScore'):
                    existing_game.fifthScore = request.form.get('fifthScore', None)

                if hasattr(existing_game, 'sixthName'):
                    existing_game.sixthName = request.form.get('sixthName', None)
                if hasattr(existing_game, 'sixthScore'):
                    existing_game.sixthScore = request.form.get('sixthScore', None)

                existing_game.date = newdate

                db.session.commit()

    return redirect(url_for('home'))

@app.route('/DominionSelect', methods=['GET'])
@login_required
def DominionSelect():
    return render_template("DominionSelect.html", title='Home')

@app.route('/retrieveExpansion', methods=['GET'])
@login_required
def retrieveExpansion():
    gameid = request.args.get('gameid')
    
    if not gameid:
        return jsonify({"error": "No game ID provided"}), 400

    expansion = Expansions.query.filter_by(game_id=gameid).first()

    if expansion:
        # Assuming expansionList is stored as a comma-separated string
        expansion_list = expansion.expansionList.split(',') if expansion.expansionList else []
        return jsonify({"expansions": expansion_list})
    else:
        return jsonify({"expansions": []})

@app.route('/addDominionRecord', methods=['POST', 'GET'])
@login_required
def addDominionRecord():
    if request.method == 'POST':
        player1 = request.form['Player1']
        player1Score = request.form['Score1']
        player2 = request.form['Player2']
        player2Score = request.form['Score2']
        player3 = request.form['Player3']
        player3Score = request.form['Score3']
        player4 = request.form['Player4']
        player4Score = request.form['Score4']
        newGameID = findID()

        dominion_game = DominionGame(
            game_id=newGameID,
            poster_id=current_user.id, 
            winnerName=player1, 
            winnerScore=player1Score, 
            secondName=player2, 
            secondScore=player2Score, 
            thirdName=player3, 
            thirdScore=player3Score, 
            fourthName=player4, 
            fourthScore=player4Score,
            date=date.today()),
        db.session.add(dominion_game)
        db.session.commit()

        return render_template("home.html", title='Home')

@app.route('/cards')
def cards():

    cardType = request.args.get('cardType')

    table_map = {
        'village': Village,
        'cantrip': Cantrip,
        'sifter': Sifter,
        'gainer': Gainer,
        'trasher': Trasher,
        'terminalDraw': TerminalDraw,
        'terminalSilver': TerminalSilver,
        'action': Action,
        'victory': Victory,
        'treasure': Treasure,
        'attack': Attack,
        'reaction': Reaction,
        'duration': Duration
    }

    if cardType in table_map:
        records = table_map[cardType].query.all()
        data = [card.cardName for card in records]

    return jsonify(data)

@app.route('/addDominion', methods = ['POST', 'GET'])
@login_required
def addDominion():
    if request.method == 'POST':
        try:
            print('request.form')
            print(request.form)
            player1 = request.form['Player1']
            player1Score = request.form['Score1']
            player2 = request.form['Player2']
            player2Score = request.form['Score2']
            player3 = request.form['Player3']
            player3Score = request.form['Score3']
            player4 = request.form['Player4']
            player4Score = request.form['Score4']
            newGameID = findID()
            numPlayers = 4
            game = "dominion"
            for i in range(1, numPlayers):
                player = request.form[f'Player{i}']
                if not SupportedNames.query.filter_by(playerID=current_user.id, playerName=player).first():
                    new_played_user = SupportedNames(playerID=current_user.id, playerName=player)
                    db.session.add(new_played_user)

            dominion_game = DominionGame(
                game_id=newGameID,
                poster_id=current_user.id,  
                winnerName=player1, 
                winnerScore=player1Score, 
                secondName=player2, 
                secondScore=player2Score, 
                thirdName=player3, 
                thirdScore=player3Score, 
                fourthName=player4, 
                fourthScore=player4Score,
                date=date.today())
            db.session.add(dominion_game)
            addExpansion(newGameID)
            db.session.commit()
            print("DominionGame added successfully!")

        except Exception as e:
            print(f"An error occurred while adding the DominionGame: {e}")

        finally:
            print("Record Added")
            return redirect('/home')
        
@app.route('/addMoonrakers', methods = ['POST', 'GET'])
@login_required
def addMoonrakers():
    if request.method == 'POST':
        try:
            player1 = request.form['Player1']
            player1Score = request.form['Score1']
            player2 = request.form['Player2']
            player2Score = request.form['Score2']
            player3 = request.form['Player3']
            player3Score = request.form['Score3']
            player4 = request.form['Player4']
            player4Score = request.form['Score4']
            player5 = request.form['Player5']
            player5Score = request.form['Score5']
            newGameID = findID()

            numPlayers = 5
            game = "moonrakers"
            for i in range(1, numPlayers):
                player = request.form[f'Player{i}']
                if not SupportedNames.query.filter_by(playerID=current_user.id, playerName=player).first():
                    new_played_user = SupportedNames(playerID=current_user.id, playerName=player)
                    db.session.add(new_played_user)

            new_game = MoonrakersGame(
                game_id=newGameID,
                poster_id=current_user.id,   
                winnerName=player1, 
                winnerScore=player1Score, 
                secondName=player2, 
                secondScore=player2Score, 
                thirdName=player3, 
                thirdScore=player3Score, 
                fourthName=player4, 
                fourthScore=player4Score, 
                fifthName=player5, 
                fifthScore=player5Score,
                date=date.today())
            db.session.add(new_game)
            db.session.commit()

        except Exception as e:
            print(f"An error occurred while adding the MoonrakersGame: {e}")

        finally:
            print("Record Added")
            return redirect('/home')

@app.route('/addClank', methods = ['POST', 'GET'])
@login_required
def addClank():
    if request.method == 'POST':
        try:
            player1 = request.form['Player1']
            player1Score = request.form['Score1']
            player2 = request.form['Player2']
            player2Score = request.form['Score2']
            player3 = request.form['Player3']
            player3Score = request.form['Score3']
            player4 = request.form['Player4']
            player4Score = request.form['Score4']
            newGameID = findID()
            numPlayers = 4
            game = "clank"
            for i in range(1, numPlayers):
                player = request.form[f'Player{i}']
                if not SupportedNames.query.filter_by(playerID=current_user.id, playerName=player).first():
                    new_played_user = SupportedNames(playerID=current_user.id, playerName=player)
                    db.session.add(new_played_user)

            clank_game = ClankGame(
                game_id=newGameID,
                poster_id=current_user.id,   
                winnerName=player1, 
                winnerScore=player1Score, 
                secondName=player2, 
                secondScore=player2Score, 
                thirdName=player3, 
                thirdScore=player3Score, 
                fourthName=player4, 
                fourthScore=player4Score,
                date=date.today())
            db.session.add(clank_game)
            addExpansion(newGameID)
            db.session.commit()
            print("ClankGame added successfully!")

        except Exception as e:
            print(f"An error occurred while adding the ClankGame: {e}")

        finally:
            print("Record Added")
            return redirect('/home')

@app.route('/addLordsofWaterdeep', methods = ['POST', 'GET'])
@login_required
def addLordsofWaterdeep():
    if request.method == 'POST':
        try:
            player1 = request.form['Player1']
            player1Score = request.form['Score1']
            player2 = request.form['Player2']
            player2Score = request.form['Score2']
            player3 = request.form['Player3']
            player3Score = request.form['Score3']
            player4 = request.form['Player4']
            player4Score = request.form['Score4']
            player5 = request.form['Player5']
            player5Score = request.form['Score5']
            newGameID = findID()

            numPlayers = 5
            game = "lordsofwaterdeep"
            for i in range(1, numPlayers):
                player = request.form[f'Player{i}']
                if not SupportedNames.query.filter_by(playerID=current_user.id, playerName=player).first():
                    new_played_user = SupportedNames(playerID=current_user.id, playerName=player)
                    db.session.add(new_played_user)

            new_game = LordsofWaterdeepGame(
                game_id=newGameID,
                poster_id=current_user.id,   
                winnerName=player1, 
                winnerScore=player1Score, 
                secondName=player2, 
                secondScore=player2Score, 
                thirdName=player3, 
                thirdScore=player3Score, 
                fourthName=player4, 
                fourthScore=player4Score, 
                fifthName=player5, 
                fifthScore=player5Score,
                date=date.today())
            db.session.add(new_game)
            addExpansion(newGameID)
            db.session.commit()

        except Exception as e:
            print(f"An error occurred while adding the LordsofWaterdeepGame: {e}")

        finally:
            print("Record Added")
            return redirect('/home')
        
@app.route('/addHeat', methods = ['POST', 'GET'])
@login_required
def addHeat():
    if request.method == 'POST':
        try:
            player1 = request.form['Player1']
            player2 = request.form['Player2']
            player3 = request.form['Player3']
            player4 = request.form['Player4']
            player5 = request.form['Player5']
            player6 = request.form['Player6']
            newGameID = findID()

            numPlayers = 5
            game = "heat"
            for i in range(1, numPlayers):
                player = request.form[f'Player{i}']
                if not SupportedNames.query.filter_by(playerID=current_user.id, playerName=player).first():
                    new_played_user = SupportedNames(playerID=current_user.id, playerName=player)
                    db.session.add(new_played_user)

            new_game = HeatGame(
                game_id=newGameID,
                poster_id=current_user.id,   
                winnerName=player1, 
                secondName=player2, 
                thirdName=player3, 
                fourthName=player4, 
                fifthName=player5, 
                sixthName=player6, 
                date=date.today())
            db.session.add(new_game)
            db.session.commit()

        except Exception as e:
            print(f"An error occurred while adding the HeatGame: {e}")

        finally:
            print("Record Added")
            return redirect('/home')
        
@app.route('/addSpaceBase', methods = ['POST', 'GET'])
@login_required
def addSpaceBase():
    if request.method == 'POST':
        try:
            player1 = request.form['Player1']
            player1Score = request.form['Score1']
            player2 = request.form['Player2']
            player2Score = request.form['Score2']
            player3 = request.form['Player3']
            player3Score = request.form['Score3']
            player4 = request.form['Player4']
            player4Score = request.form['Score4']
            player5 = request.form['Player5']
            player5Score = request.form['Score5']
            newGameID = findID()

            numPlayers = 5
            game = "spacebase"
            for i in range(1, numPlayers):
                player = request.form[f'Player{i}']
                if not SupportedNames.query.filter_by(playerID=current_user.id, playerName=player).first():
                    new_played_user = SupportedNames(playerID=current_user.id, playerName=player)
                    db.session.add(new_played_user)

            new_game = SpaceBaseGame(
                game_id=newGameID,
                poster_id=current_user.id,   
                winnerName=player1, 
                winnerScore=player1Score, 
                secondName=player2, 
                secondScore=player2Score, 
                thirdName=player3, 
                thirdScore=player3Score, 
                fourthName=player4, 
                fourthScore=player4Score, 
                fifthName=player5, 
                fifthScore=player5Score,
                date=date.today())
            db.session.add(new_game)
            addExpansion(newGameID)
            db.session.commit()

        except Exception as e:
            print(f"An error occurred while adding the SpaceBaseGame: {e}")

        finally:
            print("Record Added")
            return redirect('/home')
        
@app.route('/addCosmicEncounter', methods = ['POST', 'GET'])
@login_required
def addCosmicEncounter():
    if request.method == 'POST':
        try:
            player1 = request.form['Player1']
            player1Score = request.form['Score1']
            player2 = request.form['Player2']
            player2Score = request.form['Score2']
            player3 = request.form['Player3']
            player3Score = request.form['Score3']
            player4 = request.form['Player4']
            player4Score = request.form['Score4']
            player5 = request.form['Player5']
            player5Score = request.form['Score5']
            newGameID = findID()

            numPlayers = 5
            game = "cosmicencounter"
            for i in range(1, numPlayers):
                player = request.form[f'Player{i}']
                if not SupportedNames.query.filter_by(playerID=current_user.id, playerName=player).first():
                    new_played_user = SupportedNames(playerID=current_user.id, playerName=player)
                    db.session.add(new_played_user)

            new_game = CosmicEncounterGame(
                game_id=newGameID,
                poster_id=current_user.id,   
                winnerName=player1, 
                winnerScore=player1Score, 
                secondName=player2, 
                secondScore=player2Score, 
                thirdName=player3, 
                thirdScore=player3Score, 
                fourthName=player4, 
                fourthScore=player4Score, 
                fifthName=player5, 
                fifthScore=player5Score,
                date=date.today())
            db.session.add(new_game)
            db.session.commit()

        except Exception as e:
            print(f"An error occurred while adding the CosmicEncounterGame: {e}")

        finally:
            print("Record Added")
            return redirect('/home')

@app.route('/addCatan', methods = ['POST', 'GET'])
@login_required
def addCatan():
    if request.method == 'POST':
        try:
            player1 = request.form['Player1']
            player1Score = request.form['Score1']
            player2 = request.form['Player2']
            player2Score = request.form['Score2']
            player3 = request.form['Player3']
            player3Score = request.form['Score3']
            player4 = request.form['Player4']
            player4Score = request.form['Score4']
            newGameID = findID()

            numPlayers = 4
            game = "catan"
            for i in range(1, numPlayers):
                player = request.form[f'Player{i}']
                if not SupportedNames.query.filter_by(playerID=current_user.id, playerName=player).first():
                    new_played_user = SupportedNames(playerID=current_user.id, playerName=player)
                    db.session.add(new_played_user)

            catan_game = CatanGame(
                game_id=newGameID,
                poster_id=current_user.id,   
                winnerName=player1, 
                winnerScore=player1Score, 
                secondName=player2, 
                secondScore=player2Score, 
                thirdName=player3, 
                thirdScore=player3Score, 
                fourthName=player4, 
                fourthScore=player4Score,
                date=date.today())
            db.session.add(catan_game)
            addExpansion(newGameID)
            db.session.commit()

        except Exception as e:
            print(f"An error occurred while adding the CatanGame: {e}")

        finally:
            print("Record Added")
            return redirect('/home')
        
@app.route('/addSushiGoParty', methods = ['POST', 'GET'])
@login_required
def addSushiGoParty():
    if request.method == 'POST':
        try:
            player1 = request.form['Player1']
            player1Score = request.form['Score1']
            player2 = request.form['Player2']
            player2Score = request.form['Score2']
            player3 = request.form['Player3']
            player3Score = request.form['Score3']
            player4 = request.form['Player4']
            player4Score = request.form['Score4']
            player5 = request.form['Player5']
            player5Score = request.form['Score5']
            player6 = request.form['Player6']
            player6Score = request.form['Score6']
            player7 = request.form['Player7']
            player7Score = request.form['Score7']
            player8 = request.form['Player8']
            player8Score = request.form['Score8']
            newGameID = findID()

            numPlayers = 4
            game = "sushigoparty"
            for i in range(1, numPlayers):
                player = request.form[f'Player{i}']
                if not SupportedNames.query.filter_by(playerID=current_user.id, playerName=player).first():
                    new_played_user = SupportedNames(playerID=current_user.id, playerName=player)
                    db.session.add(new_played_user)

            sushigoparty_game = SushiGoPartyGame(
                game_id=newGameID,
                poster_id=current_user.id,   
                winnerName=player1, 
                winnerScore=player1Score, 
                secondName=player2, 
                secondScore=player2Score, 
                thirdName=player3, 
                thirdScore=player3Score, 
                fourthName=player4, 
                fourthScore=player4Score,
                fifthName=player5,
                fifthScore=player5Score,
                sixthName=player6,
                sixthScore=player6Score,
                seventhName=player7,
                seventhScore=player7Score,
                eighthName=player8,
                eighthScore=player8Score,
                date=date.today())
            db.session.add(sushigoparty_game)
            db.session.commit()

        except Exception as e:
            print(f"An error occurred while adding the SushiGoPartyGame: {e}")

        finally:
            print("Record Added")
            return redirect('/home')
        
@app.route('/addExplodingKittens', methods = ['POST', 'GET'])
@login_required
def addExplodingKittens():
    if request.method == 'POST':
        try:
            player1 = request.form['Player1']
            player2 = request.form['Player2']
            player3 = request.form['Player3']
            player4 = request.form['Player4']
            player5 = request.form['Player5']
            player6 = request.form['Player6']
            player7 = request.form['Player7']
            player8 = request.form['Player8']
            player9 = request.form['Player9']
            player10 = request.form['Player10']
            newGameID = findID()

            numPlayers = 4
            game = "explodingkittens"
            for i in range(1, numPlayers):
                player = request.form[f'Player{i}']
                if not SupportedNames.query.filter_by(playerID=current_user.id, playerName=player).first():
                    new_played_user = SupportedNames(playerID=current_user.id, playerName=player)
                    db.session.add(new_played_user)

            explodingkittens_game = ExplodingKittensGame(
                game_id=newGameID,
                poster_id=current_user.id,   
                winnerName=player1, 
                secondName=player2, 
                thirdName=player3, 
                fourthName=player4, 
                fifthName=player5,
                sixthName=player6,
                seventhName=player7,
                eighthName=player8,
                ninthName=player9,
                tenthName=player10,
                date=date.today())
            db.session.add(explodingkittens_game)
            db.session.commit()

        except Exception as e:
            print(f"An error occurred while adding the ExplodingKittensGame: {e}")

        finally:
            print("Record Added")
            return redirect('/home')
        
@app.route('/addMagicTheGathering', methods = ['POST', 'GET'])
@login_required
def addMagicTheGathering():
    if request.method == 'POST':
        try:
            player1 = request.form['magicthegatheringPlayer1']
            player1Deck = request.form['Player1_Deck']
            player1Kills = request.form['Player1_Kills']
            player1Color = request.form['Player1_Color']
            player2 = request.form['magicthegatheringPlayer2']
            player2Deck = request.form['Player2_Deck']
            player2Kills = request.form['Player2_Kills']
            player2Color = request.form['Player2_Color']
            player3 = request.form['magicthegatheringPlayer3']
            player3Deck = request.form['Player3_Deck']
            player3Kills = request.form['Player3_Kills']
            player3Color = request.form['Player3_Color']
            player4 = request.form['magicthegatheringPlayer4']
            player4Deck = request.form['Player4_Deck']
            player4Kills = request.form['Player4_Kills']
            player4Color = request.form['Player4_Color']
            player5 = request.form['magicthegatheringPlayer5']
            player5Deck = request.form['Player5_Deck']
            player5Kills = request.form['Player5_Kills']
            player5Color = request.form['Player5_Color']
            newGameID = findID()

            numPlayers = 5
            game = "magicthegathering"
            for i in range(1, numPlayers):
                player = request.form[f'{game}Player{i}']
                if not SupportedNames.query.filter_by(playerID=current_user.id, playerName=player).first():
                    new_played_user = SupportedNames(playerID=current_user.id, playerName=player)
                    db.session.add(new_played_user)

            new_game = MagicTheGatheringGame(
                game_id=newGameID,
                poster_id=current_user.id,   
                winnerName = player1, 
                winnerColor = player1Color,
                winnerKills = player1Kills,
                winnerDeck = player1Deck,
                secondName = player2, 
                secondColor = player2Color,
                secondKills = player2Kills,
                secondDeck = player2Deck,
                thirdName = player3, 
                thirdColor = player3Color, 
                thirdKills = player3Kills, 
                thirdDeck = player3Deck,
                fourthName = player4,
                fourthColor = player4Color, 
                fourthKills = player4Kills, 
                fourthDeck = player4Deck,
                fifthName = player5, 
                fifthColor = player5Color,
                fifthKills = player5Kills,
                fifthDeck = player5Deck,
                date=date.today())
            db.session.add(new_game)
            db.session.commit()

        except Exception as e:
            print(f"An error occurred while adding the MagicTheGatheringGame: {e}")

        finally:
            print("Record Added")
            return redirect('/home')

@app.route('/addCoup', methods = ['POST', 'GET'])
@login_required
def addCoup():
    if request.method == 'POST':
        try:
            player1 = request.form['coupPlayer1']
            player2 = request.form['coupPlayer2']
            player3 = request.form['coupPlayer3']
            player4 = request.form['coupPlayer4']
            player5 = request.form['coupPlayer5']
            player6 = request.form['coupPlayer6']
            newGameID = findID()

            numPlayers = 6
            game = "coup"
            for i in range(1, numPlayers):
                player = request.form[f'{game}Player{i}']
                if not SupportedNames.query.filter_by(playerID=current_user.id, playerName=player).first():
                    new_played_user = SupportedNames(playerID=current_user.id, playerName=player)
                    db.session.add(new_played_user)

            new_game = CoupGame(
                game_id=newGameID,
                poster_id=current_user.id,   
                winnerName=player1, 
                secondName=player2, 
                thirdName=player3, 
                fourthName=player4, 
                fifthName=player5, 
                sixthName=player6,
                date=date.today())
            db.session.add(new_game)
            db.session.commit()

        except Exception as e:
            print(f"An error occurred while adding the CoupGame: {e}")

        finally:
            print("Record Added")
            return redirect('/home')
        
@app.route('/addLoveLetter', methods=['POST', 'GET'])
def addLoveLetter():
    if request.method == 'POST':
        try:
            player1 = request.form['loveletterPlayer1']
            player2 = request.form['loveletterPlayer2']
            player3 = request.form['loveletterPlayer3']
            player4 = request.form['loveletterPlayer4']
            player5 = request.form['loveletterPlayer5']
            player6 = request.form['loveletterPlayer6']
            newGameID = findID()

            numPlayers = 6
            game = "loveletter"
            for i in range(1, numPlayers):
                player = request.form[f'{game}Player{i}']
                if not SupportedNames.query.filter_by(playerID=current_user.id, playerName=player).first():
                    new_played_user = SupportedNames(playerID=current_user.id, playerName=player)
                    db.session.add(new_played_user)
            
            new_game = LoveLetterGame(
                game_id=newGameID,
                poster_id=current_user.id,   
                winnerName=player1, 
                secondName=player2, 
                thirdName=player3, 
                fourthName=player4, 
                fifthName=player5, 
                sixthName=player6,
                date=date.today())
            db.session.add(new_game)
            db.session.commit()

        finally:
            print("Record Added")
            return redirect('/home')
        
@app.route('/addMunchkin', methods = ['POST', 'GET'])
@login_required
def addMunchkin():
    if request.method == 'POST':
        try:
            player1 = request.form['munchkinPlayer1']
            player1Score = request.form['Player1_Score']
            player2 = request.form['munchkinPlayer2']
            player2Score = request.form['Player2_Score']
            player3 = request.form['munchkinPlayer3']
            player3Score = request.form['Player3_Score']
            player4 = request.form['munchkinPlayer4']
            player4Score = request.form['Player4_Score']
            player5 = request.form['munchkinPlayer5']
            player5Score = request.form['Player5_Score']
            player6 = request.form['munchkinPlayer6']
            player6Score = request.form['Player6_Score']
            newGameID = findID()

            numPlayers = 6
            game = "munchkin"
            for i in range(1, numPlayers):
                player = request.form[f'{game}Player{i}']
                if not SupportedNames.query.filter_by(playerID=current_user.id, playerName=player).first():
                    new_played_user = SupportedNames(playerID=current_user.id, playerName=player)
                    db.session.add(new_played_user)

            new_game = MunchkinGame(
                game_id=newGameID,
                poster_id=current_user.id,   
                winnerName=player1, 
                winnerScore=player1Score, 
                secondName=player2, 
                secondScore=player2Score, 
                thirdName=player3, 
                thirdScore=player3Score, 
                fourthName=player4, 
                fourthScore=player4Score, 
                fifthName=player5, 
                fifthScore=player5Score,
                sixthName=player6, 
                sixthScore=player6Score,
                date=date.today())
            db.session.add(new_game)
            db.session.commit()

        except Exception as e:
            print(f"An error occurred while adding the MunchkinGame: {e}")

        finally:
            print("Record Added")
            return redirect('/home')
        
@app.route('/addJustOne', methods = ['POST', 'GET'])
@login_required
def addJustOne():
    if request.method == 'POST':
        try:
            player1 = request.form['justonePlayer1']
            player2 = request.form['justonePlayer2']
            player3 = request.form['justonePlayer3']
            player4 = request.form['justonePlayer4']
            player5 = request.form['justonePlayer5']
            player6 = request.form['justonePlayer6']
            player7 = request.form['justonePlayer7']
            gamevictory = request.form['win']
            newGameID = findID()

            numPlayers = 7
            game = "justone"
            for i in range(1, numPlayers):
                player = request.form[f'{game}Player{i}']
                if not SupportedNames.query.filter_by(playerID=current_user.id, playerName=player).first():
                    new_played_user = SupportedNames(playerID=current_user.id, playerName=player)
                    db.session.add(new_played_user)

            new_game = JustOneGame(
                game_id=newGameID,
                poster_id=current_user.id,   
                playerone=player1, 
                playertwo=player2,  
                playerthree=player3, 
                playerfour=player4,
                playerfive=player5,  
                playersix=player6, 
                playerseven=player7,  
                victory = gamevictory,
                date=date.today())
            db.session.add(new_game)
            db.session.commit()
            print("JustOneGame added successfully!")

        except Exception as e:
            print(f"An error occurred while adding the JustOneGame: {e}")

        finally:
            print("Record Added")
            return redirect('/home')
        
@app.route('/addTheMind', methods = ['POST', 'GET'])
@login_required
def addTheMind():
    if request.method == 'POST':
        try:
            player1 = request.form['themindPlayer1']
            player2 = request.form['themindPlayer2']
            player3 = request.form['themindPlayer3']
            player4 = request.form['themindPlayer4']
            gamevictory = request.form['win']
            newGameID = findID()

            numPlayers = 4
            game = "themind"
            for i in range(1, numPlayers):
                player = request.form[f'{game}Player{i}']
                if not SupportedNames.query.filter_by(playerID=current_user.id, playerName=player).first():
                    new_played_user = SupportedNames(playerID=current_user.id, playerName=player)
                    db.session.add(new_played_user)

            new_game = TheMindGame(
                game_id=newGameID,
                poster_id=current_user.id,   
                playerone=player1, 
                playertwo=player2,  
                playerthree=player3, 
                playerfour=player4, 
                victory = gamevictory,
                date=date.today())
            db.session.add(new_game)
            db.session.commit()
            print("TheMindGame added successfully!")

        except Exception as e:
            print(f"An error occurred while adding the TheMindGame: {e}")

        finally:
            print("Record Added")
            return redirect('/home')
        
def addExpansion(newGameID):
    expansionnames = request.form.get('expansionnames')
    if expansionnames:
        print(f"Expansion names: {expansionnames}")
        expansion = Expansions(
        game_id=newGameID, 
        expansionList=expansionnames)
        db.session.add(expansion)
        db.session.commit()
        return print("added expansions")

    else:
        return print("No expansion names provided")

def findID():
    dom_id = db.session.query(db.func.max(DominionGame.game_id)).scalar() or 0
    moo_id = db.session.query(db.func.max(MoonrakersGame.game_id)).scalar() or 0
    cla_id = db.session.query(db.func.max(ClankGame.game_id)).scalar() or 0
    lor_id = db.session.query(db.func.max(LordsofWaterdeepGame.game_id)).scalar() or 0
    hea_id = db.session.query(db.func.max(HeatGame.game_id)).scalar() or 0
    spa_id = db.session.query(db.func.max(SpaceBaseGame.game_id)).scalar() or 0
    cos_id = db.session.query(db.func.max(CosmicEncounterGame.game_id)).scalar() or 0
    cat_id = db.session.query(db.func.max(CatanGame.game_id)).scalar() or 0
    cou_id = db.session.query(db.func.max(CoupGame.game_id)).scalar() or 0
    lov_id = db.session.query(db.func.max(LoveLetterGame.game_id)).scalar() or 0
    mag_id = db.session.query(db.func.max(MagicTheGatheringGame.game_id)).scalar() or 0
    mun_id = db.session.query(db.func.max(MunchkinGame.game_id)).scalar() or 0
    jus_id = db.session.query(db.func.max(JustOneGame.game_id)).scalar() or 0
    min_id = db.session.query(db.func.max(TheMindGame.game_id)).scalar() or 0
    sus_id = db.session.query(db.func.max(SushiGoPartyGame.game_id)).scalar() or 0
    exp_id = db.session.query(db.func.max(ExplodingKittensGame.game_id)).scalar() or 0
    max_id = max(dom_id, hea_id, spa_id, cat_id, lor_id, cou_id, lov_id, mun_id, jus_id, min_id, mag_id, moo_id, cos_id, cla_id, sus_id, exp_id)

    return max_id + 1

def calcGamesWon(user):
    gamesWon = 0
    gamesWon += db.session.query(DominionGame).filter(or_(DominionGame.winnerName == user.username, DominionGame.winnerName == user.fullname)).count()
    gamesWon += db.session.query(MoonrakersGame).filter(or_(MoonrakersGame.winnerName == user.username, MoonrakersGame.winnerName == user.fullname)).count()
    gamesWon += db.session.query(ClankGame).filter(or_(ClankGame.winnerName == user.username, ClankGame.winnerName == user.fullname)).count()
    gamesWon += db.session.query(LordsofWaterdeepGame).filter(or_(LordsofWaterdeepGame.winnerName == user.username, LordsofWaterdeepGame.winnerName == user.fullname)).count()
    gamesWon += db.session.query(HeatGame).filter(or_(HeatGame.winnerName == user.username, HeatGame.winnerName == user.fullname)).count()
    gamesWon += db.session.query(SpaceBaseGame).filter(or_(SpaceBaseGame.winnerName == user.username, SpaceBaseGame.winnerName == user.fullname)).count()
    gamesWon += db.session.query(CosmicEncounterGame).filter(or_(CosmicEncounterGame.winnerName == user.username, CosmicEncounterGame.winnerName == user.fullname)).count()
    gamesWon += db.session.query(CatanGame).filter(or_(CatanGame.winnerName == user.username, CatanGame.winnerName == user.fullname)).count()
    gamesWon += db.session.query(ExplodingKittensGame).filter(or_(ExplodingKittensGame.winnerName == user.username, ExplodingKittensGame.winnerName == user.fullname)).count()
    gamesWon += db.session.query(SushiGoPartyGame).filter(or_(SushiGoPartyGame.winnerName == user.username, SushiGoPartyGame.winnerName == user.fullname)).count()
    gamesWon += db.session.query(CoupGame).filter(or_(CoupGame.winnerName == user.username, CoupGame.winnerName == user.fullname)).count()
    gamesWon += db.session.query(LoveLetterGame).filter(or_(LoveLetterGame.winnerName == user.username, LoveLetterGame.winnerName == user.fullname)).count()
    gamesWon += db.session.query(MunchkinGame).filter(or_(MunchkinGame.winnerName == user.username, MunchkinGame.winnerName == user.fullname)).count()
    gamesWon += db.session.query(TheMindGame).filter(
        and_(
            TheMindGame.victory == 'Victory',
            or_(
                TheMindGame.playerone == user.username,
                TheMindGame.playerone == user.fullname,
                TheMindGame.playertwo == user.username,
                TheMindGame.playertwo == user.fullname,
                TheMindGame.playerthree == user.username,
                TheMindGame.playerthree == user.fullname,
                TheMindGame.playerfour == user.username,
                TheMindGame.playerfour == user.fullname,
            )
        )
    ).count()

    return gamesWon

def calcGamesPlayed(user):
    gamesPlayed = 0
    gamesPlayed += db.session.query(DominionGame).filter(or_(
        DominionGame.winnerName.in_([user.fullname, user.username]),
        DominionGame.secondName.in_([user.fullname, user.username]),
        DominionGame.thirdName.in_([user.fullname, user.username]),
        DominionGame.fourthName.in_([user.fullname, user.username]),)).count()
    gamesPlayed += db.session.query(MoonrakersGame).filter(or_(
        MoonrakersGame.winnerName.in_([user.fullname, user.username]),
        MoonrakersGame.secondName.in_([user.fullname, user.username]),
        MoonrakersGame.thirdName.in_([user.fullname, user.username]),
        MoonrakersGame.fourthName.in_([user.fullname, user.username]),
        MoonrakersGame.fifthName.in_([user.fullname, user.username]),)).count()
    gamesPlayed += db.session.query(ClankGame).filter(or_(
        ClankGame.winnerName.in_([user.fullname, user.username]),
        ClankGame.secondName.in_([user.fullname, user.username]),
        ClankGame.thirdName.in_([user.fullname, user.username]),
        ClankGame.fourthName.in_([user.fullname, user.username]),)).count()
    gamesPlayed += db.session.query(LordsofWaterdeepGame).filter(or_(
        LordsofWaterdeepGame.winnerName.in_([user.fullname, user.username]),
        LordsofWaterdeepGame.secondName.in_([user.fullname, user.username]),
        LordsofWaterdeepGame.thirdName.in_([user.fullname, user.username]),
        LordsofWaterdeepGame.fourthName.in_([user.fullname, user.username]),
        LordsofWaterdeepGame.fifthName.in_([user.fullname, user.username]),)).count()
    gamesPlayed += db.session.query(HeatGame).filter(or_(
        HeatGame.winnerName.in_([user.fullname, user.username]),
        HeatGame.secondName.in_([user.fullname, user.username]),
        HeatGame.thirdName.in_([user.fullname, user.username]),
        HeatGame.fourthName.in_([user.fullname, user.username]),
        HeatGame.fifthName.in_([user.fullname, user.username]),
        HeatGame.sixthName.in_([user.fullname, user.username]),)).count()
    gamesPlayed += db.session.query(SpaceBaseGame).filter(or_(
        SpaceBaseGame.winnerName.in_([user.fullname, user.username]),
        SpaceBaseGame.secondName.in_([user.fullname, user.username]),
        SpaceBaseGame.thirdName.in_([user.fullname, user.username]),
        SpaceBaseGame.fourthName.in_([user.fullname, user.username]),
        SpaceBaseGame.fifthName.in_([user.fullname, user.username]),)).count()
    gamesPlayed += db.session.query(CatanGame).filter(or_(
        CatanGame.winnerName.in_([user.fullname, user.username]),
        CatanGame.secondName.in_([user.fullname, user.username]),
        CatanGame.thirdName.in_([user.fullname, user.username]),
        CatanGame.fourthName.in_([user.fullname, user.username]),)).count()
    gamesPlayed += db.session.query(ExplodingKittensGame).filter(or_(
        ExplodingKittensGame.winnerName.in_([user.fullname, user.username]),
        ExplodingKittensGame.secondName.in_([user.fullname, user.username]),
        ExplodingKittensGame.thirdName.in_([user.fullname, user.username]),
        ExplodingKittensGame.fourthName.in_([user.fullname, user.username]),
        ExplodingKittensGame.fifthName.in_([user.fullname, user.username]),
        ExplodingKittensGame.sixthName.in_([user.fullname, user.username]),
        ExplodingKittensGame.seventhName.in_([user.fullname, user.username]),
        ExplodingKittensGame.eighthName.in_([user.fullname, user.username]),
        ExplodingKittensGame.ninthName.in_([user.fullname, user.username]),
        ExplodingKittensGame.tenthName.in_([user.fullname, user.username])
    )).count()
    gamesPlayed += db.session.query(SushiGoPartyGame).filter(or_(
        SushiGoPartyGame.winnerName.in_([user.fullname, user.username]),
        SushiGoPartyGame.secondName.in_([user.fullname, user.username]),
        SushiGoPartyGame.thirdName.in_([user.fullname, user.username]),
        SushiGoPartyGame.fourthName.in_([user.fullname, user.username]),
        SushiGoPartyGame.fifthName.in_([user.fullname, user.username]),
        SushiGoPartyGame.sixthName.in_([user.fullname, user.username]),
        SushiGoPartyGame.seventhName.in_([user.fullname, user.username]),
        SushiGoPartyGame.eighthName.in_([user.fullname, user.username])
    )).count()
    gamesPlayed += db.session.query(MagicTheGatheringGame).filter(or_(
        MagicTheGatheringGame.winnerName == user.fullname,
        MagicTheGatheringGame.secondName == user.fullname,
        MagicTheGatheringGame.thirdName == user.fullname,
        MagicTheGatheringGame.fourthName == user.fullname,
        MagicTheGatheringGame.fifthName == user.fullname,
        MagicTheGatheringGame.winnerName == user.username,
        MagicTheGatheringGame.secondName == user.username,
        MagicTheGatheringGame.thirdName == user.username,
        MagicTheGatheringGame.fourthName == user.username,
        MagicTheGatheringGame.fifthName == user.username)).count()
    gamesPlayed += db.session.query(CoupGame).filter(or_(
        CoupGame.winnerName == user.fullname,
        CoupGame.secondName == user.fullname,
        CoupGame.thirdName == user.fullname,
        CoupGame.fourthName == user.fullname,
        CoupGame.fifthName == user.fullname,
        CoupGame.sixthName == user.fullname,
        CoupGame.winnerName == user.username,
        CoupGame.secondName == user.username,
        CoupGame.thirdName == user.username,
        CoupGame.fourthName == user.username,
        CoupGame.fifthName == user.username,
        CoupGame.sixthName == user.username)).count()
    gamesPlayed += db.session.query(LoveLetterGame).filter(or_(
        LoveLetterGame.winnerName == user.fullname,
        LoveLetterGame.secondName == user.fullname,
        LoveLetterGame.thirdName == user.fullname,
        LoveLetterGame.fourthName == user.fullname,
        LoveLetterGame.fifthName == user.fullname,
        LoveLetterGame.sixthName == user.fullname,
        LoveLetterGame.winnerName == user.username,
        LoveLetterGame.secondName == user.username,
        LoveLetterGame.thirdName == user.username,
        LoveLetterGame.fourthName == user.username,
        LoveLetterGame.fifthName == user.username,
        LoveLetterGame.sixthName == user.username)).count()
    gamesPlayed += db.session.query(MunchkinGame).filter(or_(
        MunchkinGame.winnerName == user.fullname,
        MunchkinGame.secondName == user.fullname,
        MunchkinGame.thirdName == user.fullname,
        MunchkinGame.fourthName == user.fullname,
        MunchkinGame.fifthName == user.fullname,
        MunchkinGame.sixthName == user.fullname,
        MunchkinGame.winnerName == user.username,
        MunchkinGame.secondName == user.username,
        MunchkinGame.thirdName == user.username,
        MunchkinGame.fourthName == user.username,
        MunchkinGame.fifthName == user.username,
        MunchkinGame.sixthName == user.username)).count()
    gamesPlayed += db.session.query(TheMindGame).filter(or_(
        TheMindGame.playerone == user.fullname,
        TheMindGame.playertwo == user.fullname,
        TheMindGame.playerthree == user.fullname,
        TheMindGame.playerfour == user.fullname,
        TheMindGame.playerone == user.username,
        TheMindGame.playertwo == user.username,
        TheMindGame.playerthree == user.username,
        TheMindGame.playerfour == user.username)).count()
    gamesPlayed += db.session.query(JustOneGame).filter(or_(
        JustOneGame.playerone == user.fullname,
        JustOneGame.playertwo == user.fullname,
        JustOneGame.playerthree == user.fullname,
        JustOneGame.playerfour == user.fullname,
        JustOneGame.playerfive == user.fullname,
        JustOneGame.playersix == user.fullname,
        JustOneGame.playerseven == user.fullname,
        JustOneGame.playerone == user.username,
        JustOneGame.playertwo == user.username,
        JustOneGame.playerthree == user.username,
        JustOneGame.playerfour == user.username,
        JustOneGame.playerfive == user.username,
        JustOneGame.playersix == user.username,
        JustOneGame.playerseven == user.username)).count()

    return gamesPlayed

def calcMostPlayed(user):
    mostPlayed = ""

    DominionCount = db.session.query(DominionGame).filter(or_(
        DominionGame.winnerName.in_([user.fullname, user.username]),
        DominionGame.secondName.in_([user.fullname, user.username]),
        DominionGame.thirdName.in_([user.fullname, user.username]),
        DominionGame.fourthName.in_([user.fullname, user.username]))).count()
    MoonrakersCount = db.session.query(MoonrakersGame).filter(or_(
        MoonrakersGame.winnerName.in_([user.fullname, user.username]),
        MoonrakersGame.secondName.in_([user.fullname, user.username]),
        MoonrakersGame.thirdName.in_([user.fullname, user.username]),
        MoonrakersGame.fourthName.in_([user.fullname, user.username]))).count()
    ClankCount = db.session.query(ClankGame).filter(or_(
        ClankGame.winnerName.in_([user.fullname, user.username]),
        ClankGame.secondName.in_([user.fullname, user.username]),
        ClankGame.thirdName.in_([user.fullname, user.username]),
        ClankGame.fourthName.in_([user.fullname, user.username]))).count()
    LordsofWaterdeepCount = db.session.query(LordsofWaterdeepGame).filter(or_(
        LordsofWaterdeepGame.winnerName.in_([user.fullname, user.username]),
        LordsofWaterdeepGame.secondName.in_([user.fullname, user.username]),
        LordsofWaterdeepGame.thirdName.in_([user.fullname, user.username]),
        LordsofWaterdeepGame.fourthName.in_([user.fullname, user.username]),
        LordsofWaterdeepGame.fifthName.in_([user.fullname, user.username]),)).count()
    HeatCount = db.session.query(HeatGame).filter(or_(
        HeatGame.winnerName.in_([user.fullname, user.username]),
        HeatGame.secondName.in_([user.fullname, user.username]),
        HeatGame.thirdName.in_([user.fullname, user.username]),
        HeatGame.fourthName.in_([user.fullname, user.username]),
        HeatGame.fifthName.in_([user.fullname, user.username]),)).count()
    SpaceBaseCount = db.session.query(SpaceBaseGame).filter(or_(
        SpaceBaseGame.winnerName.in_([user.fullname, user.username]),
        SpaceBaseGame.secondName.in_([user.fullname, user.username]),
        SpaceBaseGame.thirdName.in_([user.fullname, user.username]),
        SpaceBaseGame.fourthName.in_([user.fullname, user.username]),
        SpaceBaseGame.fifthName.in_([user.fullname, user.username]),)).count()
    CosmicEncounterCount = db.session.query(CosmicEncounterGame).filter(or_(
        CosmicEncounterGame.winnerName.in_([user.fullname, user.username]),
        CosmicEncounterGame.secondName.in_([user.fullname, user.username]),
        CosmicEncounterGame.thirdName.in_([user.fullname, user.username]),
        CosmicEncounterGame.fourthName.in_([user.fullname, user.username]),
        CosmicEncounterGame.fifthName.in_([user.fullname, user.username]),)).count()
    CatanCount = db.session.query(CatanGame).filter(or_(
        CatanGame.winnerName.in_([user.fullname, user.username]),
        CatanGame.secondName.in_([user.fullname, user.username]),
        CatanGame.thirdName.in_([user.fullname, user.username]),
        CatanGame.fourthName.in_([user.fullname, user.username]),)).count()
    SushiGoPartyCount = db.session.query(SushiGoPartyGame).filter(or_(
        SushiGoPartyGame.winnerName.in_([user.fullname, user.username]),
        SushiGoPartyGame.secondName.in_([user.fullname, user.username]),
        SushiGoPartyGame.thirdName.in_([user.fullname, user.username]),
        SushiGoPartyGame.fourthName.in_([user.fullname, user.username]),
        SushiGoPartyGame.fifthName.in_([user.fullname, user.username]),
        SushiGoPartyGame.sixthName.in_([user.fullname, user.username]),
        SushiGoPartyGame.seventhName.in_([user.fullname, user.username]),
        SushiGoPartyGame.eighthName.in_([user.fullname, user.username]),)).count()
    ExplodingKittensCount = db.session.query(ExplodingKittensGame).filter(or_(
        ExplodingKittensGame.winnerName.in_([user.fullname, user.username]),
        ExplodingKittensGame.secondName.in_([user.fullname, user.username]),
        ExplodingKittensGame.thirdName.in_([user.fullname, user.username]),
        ExplodingKittensGame.fourthName.in_([user.fullname, user.username]),
        ExplodingKittensGame.fifthName.in_([user.fullname, user.username]),
        ExplodingKittensGame.sixthName.in_([user.fullname, user.username]),
        ExplodingKittensGame.seventhName.in_([user.fullname, user.username]),
        ExplodingKittensGame.eighthName.in_([user.fullname, user.username]),
        ExplodingKittensGame.ninthName.in_([user.fullname, user.username]),
        ExplodingKittensGame.tenthName.in_([user.fullname, user.username]),)).count()
    MagicTheGatheringCount = db.session.query(MagicTheGatheringGame).filter(or_(
        MagicTheGatheringGame.winnerName == user.fullname,
        MagicTheGatheringGame.secondName == user.fullname,
        MagicTheGatheringGame.thirdName == user.fullname,
        MagicTheGatheringGame.fourthName == user.fullname,
        MagicTheGatheringGame.fifthName == user.fullname,
        MagicTheGatheringGame.winnerName == user.username,
        MagicTheGatheringGame.secondName == user.username,
        MagicTheGatheringGame.thirdName == user.username,
        MagicTheGatheringGame.fourthName == user.username,
        MagicTheGatheringGame.fifthName == user.username)).count()
    CoupCount = db.session.query(CoupGame).filter(or_(
        CoupGame.winnerName == user.fullname,
        CoupGame.secondName == user.fullname,
        CoupGame.thirdName == user.fullname,
        CoupGame.fourthName == user.fullname,
        CoupGame.fifthName == user.fullname,
        CoupGame.sixthName == user.fullname,
        CoupGame.winnerName == user.username,
        CoupGame.secondName == user.username,
        CoupGame.thirdName == user.username,
        CoupGame.fourthName == user.username,
        CoupGame.fifthName == user.username,
        CoupGame.sixthName == user.username)).count()
    LoveLetterCount = db.session.query(LoveLetterGame).filter(or_(
        LoveLetterGame.winnerName == user.fullname,
        LoveLetterGame.secondName == user.fullname,
        LoveLetterGame.thirdName == user.fullname,
        LoveLetterGame.fourthName == user.fullname,
        LoveLetterGame.fifthName == user.fullname,
        LoveLetterGame.sixthName == user.fullname,
        LoveLetterGame.winnerName == user.username,
        LoveLetterGame.secondName == user.username,
        LoveLetterGame.thirdName == user.username,
        LoveLetterGame.fourthName == user.username,
        LoveLetterGame.fifthName == user.username,
        LoveLetterGame.sixthName == user.username)).count()
    MunchkinCount = db.session.query(MunchkinGame).filter(or_(
        MunchkinGame.winnerName == user.fullname,
        MunchkinGame.secondName == user.fullname,
        MunchkinGame.thirdName == user.fullname,
        MunchkinGame.fourthName == user.fullname,
        MunchkinGame.fifthName == user.fullname,
        MunchkinGame.sixthName == user.fullname,
        MunchkinGame.winnerName == user.username,
        MunchkinGame.secondName == user.username,
        MunchkinGame.thirdName == user.username,
        MunchkinGame.fourthName == user.username,
        MunchkinGame.fifthName == user.username,
        MunchkinGame.sixthName == user.username)).count()
    TheMindCount = db.session.query(TheMindGame).filter(or_(
        TheMindGame.playerone == user.fullname,
        TheMindGame.playertwo == user.fullname,
        TheMindGame.playerthree == user.fullname,
        TheMindGame.playerfour == user.fullname,
        TheMindGame.playerone == user.username,
        TheMindGame.playertwo == user.username,
        TheMindGame.playerthree == user.username,
        TheMindGame.playerfour == user.username)).count()
    JustOneCount = db.session.query(JustOneGame).filter(or_(
        JustOneGame.playerone == user.fullname,
        JustOneGame.playertwo == user.fullname,
        JustOneGame.playerthree == user.fullname,
        JustOneGame.playerfour == user.fullname,
        JustOneGame.playerfive == user.fullname,
        JustOneGame.playersix == user.fullname,
        JustOneGame.playerseven == user.fullname,
        JustOneGame.playerone == user.username,
        JustOneGame.playertwo == user.username,
        JustOneGame.playerthree == user.username,
        JustOneGame.playerfour == user.username,
        JustOneGame.playerfive == user.username,
        JustOneGame.playersix == user.username,
        JustOneGame.playerseven == user.username)).count()
    
    counts = {
        'DomionionCount': DominionCount,
        'MoonrakersCount': MoonrakersCount,
        'ClankCount': ClankCount,
        'LordsofWaterdeepCount': LordsofWaterdeepCount,
        'HeatCount': HeatCount,
        'SpaceBaseCount': SpaceBaseCount,
        'CosmicEncounterCount': CosmicEncounterCount,
        'CatanCount': CatanCount,
        'SushiGoPartyCount': SushiGoPartyCount,
        'ExplodingKittensCount': ExplodingKittensCount,
        'MagicTheGatheringCount': MagicTheGatheringCount,
        'CoupCount': CoupCount,
        'LoveLetterCount': LoveLetterCount,
        'MunchkinCount': MunchkinCount,
        'TheMindCount': TheMindCount,
        'JustOneCount': JustOneCount
    }

    maxCount = max(counts.values())
    mostPlayed = [variable for variable, count in counts.items() if count == maxCount]

    return mostPlayed[0][:-5]

def calcMostWon(user):
    dominionWins = db.session.query(DominionGame).filter(or_(DominionGame.winnerName == user.username, DominionGame.winnerName == user.fullname)).count()
    moonrakersWins = db.session.query(MoonrakersGame).filter(or_(MoonrakersGame.winnerName == user.username, MoonrakersGame.winnerName == user.fullname)).count()
    clankWins = db.session.query(ClankGame).filter(or_(ClankGame.winnerName == user.username, ClankGame.winnerName == user.fullname)).count()
    lordsofwaterdeepWins = db.session.query(LordsofWaterdeepGame).filter(or_(LordsofWaterdeepGame.winnerName == user.username, LordsofWaterdeepGame.winnerName == user.fullname)).count()
    heatWins = db.session.query(HeatGame).filter(or_(HeatGame.winnerName == user.username, HeatGame.winnerName == user.fullname)).count()
    spacebasewins = db.session.query(SpaceBaseGame).filter(or_(SpaceBaseGame.winnerName == user.username, SpaceBaseGame.winnerName == user.fullname)).count()
    cosmicWins = db.session.query(CosmicEncounterGame).filter(or_(CosmicEncounterGame.winnerName == user.username, CosmicEncounterGame.winnerName == user.fullname)).count()
    catanWins = db.session.query(CatanGame).filter(or_(CatanGame.winnerName == user.username, CatanGame.winnerName == user.fullname)).count()
    sushigoWins = db.session.query(SushiGoPartyGame).filter(or_(SushiGoPartyGame.winnerName == user.username, SushiGoPartyGame.winnerName == user.fullname)).count()
    explodingkittensWins = db.session.query(ExplodingKittensGame).filter(or_(ExplodingKittensGame.winnerName == user.username, ExplodingKittensGame.winnerName == user.fullname)).count()
    magicthegatheringWins = db.session.query(MagicTheGatheringGame).filter(or_(MagicTheGatheringGame.winnerName == user.username, MagicTheGatheringGame.winnerName == user.fullname)).count()
    coupWins = db.session.query(CoupGame).filter(or_(CoupGame.winnerName == user.username, CoupGame.winnerName == user.fullname)).count()
    loveletterWins = db.session.query(LoveLetterGame).filter(or_(LoveLetterGame.winnerName == user.username, LoveLetterGame.winnerName == user.fullname)).count()
    munchkinWins = db.session.query(MunchkinGame).filter(or_(MunchkinGame.winnerName == user.username, MunchkinGame.winnerName == user.fullname)).count()
    themindWins = db.session.query(TheMindGame).filter(
        and_(
            TheMindGame.victory == 'Victory',
            or_(
                TheMindGame.playerone == user.username,
                TheMindGame.playerone == user.fullname,
                TheMindGame.playertwo == user.username,
                TheMindGame.playertwo == user.fullname,
                TheMindGame.playerthree == user.username,
                TheMindGame.playerthree == user.fullname,
                TheMindGame.playerfour == user.username,
                TheMindGame.playerfour == user.fullname,
            )
        )
    ).count()

    counts = {
        'DomionionCount': dominionWins,
        'ClankCount': clankWins,
        'MoonrakersCount': moonrakersWins,
        'LordsofWaterdeepCount': lordsofwaterdeepWins,
        'HeatCount': heatWins,
        'SpaceBaseCount': spacebasewins,
        'CosmicEncounterCount': cosmicWins,
        'CatanCount': catanWins,
        'MagicTheGatheringCount': magicthegatheringWins,
        'CoupCount': coupWins,
        'LoveLetterCount': loveletterWins,
        'MunchkinCount': munchkinWins,
        'TheMindCount': themindWins,
        'SushiGoPartyCount': sushigoWins,
        'ExplodingKittensCount': explodingkittensWins
    }

    maxCount = max(counts.values())
    mostWon = [variable for variable, count in counts.items() if count == maxCount]

    return mostWon[0][:-5]

def calcBestFriend(user):
    bestFriend = ""
    maxCount = 0
    user_friends = user.friends.all()

    for friend in user_friends:
        DominionCount = db.session.query(DominionGame).filter(and_(
            or_(
                DominionGame.winnerName == friend.fullname,
                DominionGame.secondName == friend.fullname,
                DominionGame.thirdName == friend.fullname,
                DominionGame.fourthName == friend.fullname,
                DominionGame.winnerName == friend.username,
                DominionGame.secondName == friend.username,
                DominionGame.thirdName == friend.username,
                DominionGame.fourthName == friend.username
            ), or_( 
                DominionGame.winnerName == user.fullname,
                DominionGame.secondName == user.fullname,
                DominionGame.thirdName == user.fullname,
                DominionGame.fourthName == user.fullname,
                DominionGame.winnerName == user.username,
                DominionGame.secondName == user.username,
                DominionGame.thirdName == user.username,
                DominionGame.fourthName == user.username
            ))).count()

        CatanCount = db.session.query(CatanGame).filter(and_(
            or_(
                CatanGame.winnerName == friend.fullname,
                CatanGame.secondName == friend.fullname,
                CatanGame.thirdName == friend.fullname,
                CatanGame.fourthName == friend.fullname,
                CatanGame.winnerName == friend.username,
                CatanGame.secondName == friend.username,
                CatanGame.thirdName == friend.username,
                CatanGame.fourthName == friend.username
            ), or_(
                CatanGame.winnerName == user.fullname,
                CatanGame.secondName == user.fullname,
                CatanGame.thirdName == user.fullname,
                CatanGame.fourthName == user.fullname,
                CatanGame.winnerName == user.username,
                CatanGame.secondName == user.username,
                CatanGame.thirdName == user.username,
                CatanGame.fourthName == user.username
            ))).count()
        
        ClankCount = db.session.query(ClankGame).filter(and_(
            or_(
                ClankGame.winnerName == friend.fullname,
                ClankGame.secondName == friend.fullname,
                ClankGame.thirdName == friend.fullname,
                ClankGame.fourthName == friend.fullname,
                ClankGame.winnerName == friend.username,
                ClankGame.secondName == friend.username,
                ClankGame.thirdName == friend.username,
                ClankGame.fourthName == friend.username
            ), or_( 
                ClankGame.winnerName == user.fullname,
                ClankGame.secondName == user.fullname,
                ClankGame.thirdName == user.fullname,
                ClankGame.fourthName == user.fullname,
                ClankGame.winnerName == user.username,
                ClankGame.secondName == user.username,
                ClankGame.thirdName == user.username,
                ClankGame.fourthName == user.username
            ))).count()

        LordsofWaterdeepCount = db.session.query(LordsofWaterdeepGame).filter(and_(
            or_(
                LordsofWaterdeepGame.winnerName == friend.fullname,
                LordsofWaterdeepGame.secondName == friend.fullname,
                LordsofWaterdeepGame.thirdName == friend.fullname,
                LordsofWaterdeepGame.fourthName == friend.fullname,
                LordsofWaterdeepGame.fifthName == friend.fullname,
                LordsofWaterdeepGame.winnerName == friend.username,
                LordsofWaterdeepGame.secondName == friend.username,
                LordsofWaterdeepGame.thirdName == friend.username,
                LordsofWaterdeepGame.fourthName == friend.username,
                LordsofWaterdeepGame.fifthName == friend.username
            ), or_(
                LordsofWaterdeepGame.winnerName == user.fullname,
                LordsofWaterdeepGame.secondName == user.fullname,
                LordsofWaterdeepGame.thirdName == user.fullname,
                LordsofWaterdeepGame.fourthName == user.fullname,
                LordsofWaterdeepGame.fifthName == user.fullname,
                LordsofWaterdeepGame.winnerName == user.username,
                LordsofWaterdeepGame.secondName == user.username,
                LordsofWaterdeepGame.thirdName == user.username,
                LordsofWaterdeepGame.fourthName == user.username,
                LordsofWaterdeepGame.fifthName == user.username
            ))).count()
        
        MagicTheGatheringCount = db.session.query(MagicTheGatheringGame).filter(and_(
            or_(
                MagicTheGatheringGame.winnerName == friend.fullname,
                MagicTheGatheringGame.secondName == friend.fullname,
                MagicTheGatheringGame.thirdName == friend.fullname,
                MagicTheGatheringGame.fourthName == friend.fullname,
                MagicTheGatheringGame.fifthName == friend.fullname,
                MagicTheGatheringGame.winnerName == friend.username,
                MagicTheGatheringGame.secondName == friend.username,
                MagicTheGatheringGame.thirdName == friend.username,
                MagicTheGatheringGame.fourthName == friend.username,
                MagicTheGatheringGame.fifthName == friend.username
            ), or_(
                MagicTheGatheringGame.winnerName == user.fullname,
                MagicTheGatheringGame.secondName == user.fullname,
                MagicTheGatheringGame.thirdName == user.fullname,
                MagicTheGatheringGame.fourthName == user.fullname,
                MagicTheGatheringGame.fifthName == user.fullname,
                MagicTheGatheringGame.winnerName == user.username,
                MagicTheGatheringGame.secondName == user.username,
                MagicTheGatheringGame.thirdName == user.username,
                MagicTheGatheringGame.fourthName == user.username,
                MagicTheGatheringGame.fifthName == user.username
            ))).count()

        CoupCount = db.session.query(CoupGame).filter(and_(
            or_(
                CoupGame.winnerName == friend.fullname,
                CoupGame.secondName == friend.fullname,
                CoupGame.thirdName == friend.fullname,
                CoupGame.fourthName == friend.fullname,
                CoupGame.fifthName == friend.fullname,
                CoupGame.sixthName == friend.fullname,
                CoupGame.winnerName == friend.username,
                CoupGame.secondName == friend.username,
                CoupGame.thirdName == friend.username,
                CoupGame.fourthName == friend.username,
                CoupGame.fifthName == friend.username,
                CoupGame.sixthName == friend.username
            ), or_(
                CoupGame.winnerName == user.fullname,
                CoupGame.secondName == user.fullname,
                CoupGame.thirdName == user.fullname,
                CoupGame.fourthName == user.fullname,
                CoupGame.fifthName == user.fullname,
                CoupGame.sixthName == user.fullname,
                CoupGame.winnerName == user.username,
                CoupGame.secondName == user.username,
                CoupGame.thirdName == user.username,
                CoupGame.fourthName == user.username,
                CoupGame.fifthName == user.username,
                CoupGame.sixthName == user.username
            ))).count()

        LoveLetterCount = db.session.query(LoveLetterGame).filter(and_(
            or_(
                LoveLetterGame.winnerName == user.fullname,
                LoveLetterGame.secondName == friend.fullname,
                LoveLetterGame.thirdName == friend.fullname,
                LoveLetterGame.fourthName == friend.fullname,
                LoveLetterGame.fifthName == friend.fullname,
                LoveLetterGame.sixthName == friend.fullname,
                LoveLetterGame.winnerName == friend.username,
                LoveLetterGame.secondName == friend.username,
                LoveLetterGame.thirdName == friend.username,
                LoveLetterGame.fourthName == friend.username,
                LoveLetterGame.fifthName == friend.username,
                LoveLetterGame.sixthName == friend.username),
            or_(
                LoveLetterGame.winnerName == user.fullname,
                LoveLetterGame.secondName == user.fullname,
                LoveLetterGame.thirdName == user.fullname,
                LoveLetterGame.fourthName == user.fullname,
                LoveLetterGame.fifthName == user.fullname,
                LoveLetterGame.sixthName == user.fullname,
                LoveLetterGame.winnerName == user.username,
                LoveLetterGame.secondName == user.username,
                LoveLetterGame.thirdName == user.username,
                LoveLetterGame.fourthName == user.username,
                LoveLetterGame.fifthName == user.username,
                LoveLetterGame.sixthName == user.username))).count()
        
        MunchkinCount = db.session.query(MunchkinGame).filter(and_(
            or_(
                MunchkinGame.winnerName == friend.fullname,
                MunchkinGame.secondName == friend.fullname,
                MunchkinGame.thirdName == friend.fullname,
                MunchkinGame.fourthName == friend.fullname,
                MunchkinGame.fifthName == friend.fullname,
                MunchkinGame.sixthName == friend.fullname,
                MunchkinGame.winnerName == friend.username,
                MunchkinGame.secondName == friend.username,
                MunchkinGame.thirdName == friend.username,
                MunchkinGame.fourthName == friend.username,
                MunchkinGame.fifthName == friend.username,
                MunchkinGame.sixthName == friend.username
            ), or_(
                MunchkinGame.winnerName == user.fullname,
                MunchkinGame.secondName == user.fullname,
                MunchkinGame.thirdName == user.fullname,
                MunchkinGame.fourthName == user.fullname,
                MunchkinGame.fifthName == user.fullname,
                MunchkinGame.sixthName == user.fullname,
                MunchkinGame.winnerName == user.username,
                MunchkinGame.secondName == user.username,
                MunchkinGame.thirdName == user.username,
                MunchkinGame.fourthName == user.username,
                MunchkinGame.fifthName == user.username,
                MunchkinGame.sixthName == user.username
            ))).count()

        TheMindCount = db.session.query(TheMindGame).filter(and_(
            or_(
                TheMindGame.playerone == friend.fullname,
                TheMindGame.playertwo == friend.fullname,
                TheMindGame.playerthree == friend.fullname,
                TheMindGame.playerfour == friend.fullname,
                TheMindGame.playerone == friend.username,
                TheMindGame.playertwo == friend.username,
                TheMindGame.playerthree == friend.username,
                TheMindGame.playerfour == friend.username
            ), or_(
                TheMindGame.playerone == user.fullname,
                TheMindGame.playertwo == user.fullname,
                TheMindGame.playerthree == user.fullname,
                TheMindGame.playerfour == user.fullname,
                TheMindGame.playerone == user.username,
                TheMindGame.playertwo == user.username,
                TheMindGame.playerthree == user.username,
                TheMindGame.playerfour == user.username
            ))).count()

        JustOneCount = db.session.query(JustOneGame).filter(and_(
            or_(
                JustOneGame.playerone == friend.fullname,
                JustOneGame.playertwo == friend.fullname,
                JustOneGame.playerthree == friend.fullname,
                JustOneGame.playerfour == friend.fullname,
                JustOneGame.playerfive == friend.fullname,
                JustOneGame.playersix == friend.fullname,
                JustOneGame.playerseven == friend.fullname,
                JustOneGame.playerone == friend.username,
                JustOneGame.playertwo == friend.username,
                JustOneGame.playerthree == friend.username,
                JustOneGame.playerfour == friend.username,
                JustOneGame.playerfive == friend.username,
                JustOneGame.playersix == friend.username,
                JustOneGame.playerseven == friend.username
            ), or_(
                JustOneGame.playerone == user.fullname,
                JustOneGame.playertwo == user.fullname,
                JustOneGame.playerthree == user.fullname,
                JustOneGame.playerfour == user.fullname,
                JustOneGame.playerfive == user.fullname,
                JustOneGame.playersix == user.fullname,
                JustOneGame.playerseven == user.fullname,
                JustOneGame.playerone == user.username,
                JustOneGame.playertwo == user.username,
                JustOneGame.playerthree == user.username,
                JustOneGame.playerfour == user.username,
                JustOneGame.playerfive == user.username,
                JustOneGame.playersix == user.username,
                JustOneGame.playerseven == user.username
            ))).count()

        if DominionCount > maxCount:
            maxCount = DominionCount
            bestFriend = friend.fullname
        if CatanCount > maxCount:
            maxCount = CatanCount
            bestFriend = friend.fullname
        if ClankCount > maxCount:
            maxCount = ClankCount
            bestFriend = friend.fullname
        if LordsofWaterdeepCount > maxCount:
            maxCount = LordsofWaterdeepCount
            bestFriend = friend.fullname
        if MagicTheGatheringCount > maxCount:
            maxCount = MagicTheGatheringCount
            bestFriend = friend.fullname
        if CoupCount > maxCount:
            maxCount = CoupCount
            bestFriend = friend.fullname
        if LoveLetterCount > maxCount:
            maxCount = LoveLetterCount
            bestFriend = friend.fullname
        if MunchkinCount > maxCount:
            maxCount = MunchkinCount
            bestFriend = friend.fullname
        if TheMindCount > maxCount:
            maxCount = LoveLetterCount
            bestFriend = friend.fullname
        if JustOneCount > maxCount:
            maxCount = LoveLetterCount
            bestFriend = friend.fullname

    return bestFriend

def processGames(user, recentGamesList, game_list, gameType):
    for game in game_list:
        new_game = {}
        if game.winnerName == user.username:
            new_game['winnerName'] = user.fullname
        else:
            new_game['winnerName'] = game.winnerName
        if game.secondName == user.username:
            new_game['secondName'] = user.fullname
        else:
            new_game['secondName'] = game.secondName
        if game.thirdName == user.username:
            new_game['thirdName'] = user.fullname
        else:
            new_game['thirdName'] = game.thirdName

        new_game['game_id'] = game.game_id
        new_game['game_type'] = gameType
        new_game['current_date'] = game.date
        new_game['game_poster'] = findPosterName(game.poster_id)

        recentGamesList.append(new_game)

    return recentGamesList

def findPosterName(passedID):
    user = User.query.filter(User.id == passedID).first()
    return user.fullname

def findRecentGames(user):
    recentGames = []
    dominion_games = DominionGame.query.filter(or_(
        DominionGame.winnerName.in_([user.fullname, user.username]),
        DominionGame.secondName.in_([user.fullname, user.username]),
        DominionGame.thirdName.in_([user.fullname, user.username]),
        DominionGame.fourthName.in_([user.fullname, user.username]),
    )).with_entities(DominionGame.game_id, DominionGame.winnerName, DominionGame.secondName, DominionGame.thirdName, DominionGame.date, DominionGame.poster_id, literal('Dominion').label('game_type')).all()
    recentGames = processGames(user, recentGames, dominion_games,'Dominion')

    moon_games = MoonrakersGame.query.filter(or_(
        MoonrakersGame.winnerName.in_([user.fullname, user.username]),
        MoonrakersGame.secondName.in_([user.fullname, user.username]),
        MoonrakersGame.thirdName.in_([user.fullname, user.username]),
        MoonrakersGame.fourthName.in_([user.fullname, user.username]),
        MoonrakersGame.fifthName.in_([user.fullname, user.username]),
    )).with_entities(MoonrakersGame.game_id, MoonrakersGame.winnerName, MoonrakersGame.secondName, MoonrakersGame.thirdName, MoonrakersGame.date, MoonrakersGame.poster_id, literal('Moonrakers').label('game_type')).all()
    recentGames = processGames(user, recentGames, moon_games, 'Moonrakers')
    clank_games = ClankGame.query.filter(or_(
        ClankGame.winnerName.in_([user.fullname, user.username]),
        ClankGame.secondName.in_([user.fullname, user.username]),
        ClankGame.thirdName.in_([user.fullname, user.username]),
        ClankGame.fourthName.in_([user.fullname, user.username]),
    )).with_entities(ClankGame.game_id, ClankGame.winnerName, ClankGame.secondName, ClankGame.thirdName, ClankGame.date, ClankGame.poster_id, literal('Clank').label('game_type')).all()
    recentGames = processGames(user, recentGames, clank_games, 'Clank')

    lords_games = LordsofWaterdeepGame.query.filter(or_(
        LordsofWaterdeepGame.winnerName.in_([user.fullname, user.username]),
        LordsofWaterdeepGame.secondName.in_([user.fullname, user.username]),
        LordsofWaterdeepGame.thirdName.in_([user.fullname, user.username]),
        LordsofWaterdeepGame.fourthName.in_([user.fullname, user.username]),
        LordsofWaterdeepGame.fifthName.in_([user.fullname, user.username]),
    )).with_entities(LordsofWaterdeepGame.game_id, LordsofWaterdeepGame.winnerName, LordsofWaterdeepGame.secondName, LordsofWaterdeepGame.thirdName, LordsofWaterdeepGame.date, LordsofWaterdeepGame.poster_id, literal('Lords of the Waterdeep').label('game_type')).all()
    recentGames = processGames(user, recentGames, lords_games, 'Lords of Waterdeep')

    heat_games = HeatGame.query.filter(or_(
        HeatGame.winnerName.in_([user.fullname, user.username]),
        HeatGame.secondName.in_([user.fullname, user.username]),
        HeatGame.thirdName.in_([user.fullname, user.username]),
        HeatGame.fourthName.in_([user.fullname, user.username]),
        HeatGame.fifthName.in_([user.fullname, user.username]),
        HeatGame.sixthName.in_([user.fullname, user.username]),
    )).with_entities(HeatGame.game_id, HeatGame.winnerName, HeatGame.secondName, HeatGame.thirdName, HeatGame.date, HeatGame.poster_id, literal('Heat: Pedal to the Metal').label('game_type')).all()
    recentGames = processGames(user, recentGames, heat_games, 'Heat')

    space_games = SpaceBaseGame.query.filter(or_(
        SpaceBaseGame.winnerName.in_([user.fullname, user.username]),
        SpaceBaseGame.secondName.in_([user.fullname, user.username]),
        SpaceBaseGame.thirdName.in_([user.fullname, user.username]),
        SpaceBaseGame.fourthName.in_([user.fullname, user.username]),
        SpaceBaseGame.fifthName.in_([user.fullname, user.username]),
    )).with_entities(SpaceBaseGame.game_id, SpaceBaseGame.winnerName, SpaceBaseGame.secondName, SpaceBaseGame.thirdName, SpaceBaseGame.date, SpaceBaseGame.poster_id, literal('Space Base').label('game_type')).all()
    recentGames = processGames(user, recentGames, space_games, 'Space Base')

    cosmic_games = CosmicEncounterGame.query.filter(or_(
        CosmicEncounterGame.winnerName.in_([user.fullname, user.username]),
        CosmicEncounterGame.secondName.in_([user.fullname, user.username]),
        CosmicEncounterGame.thirdName.in_([user.fullname, user.username]),
        CosmicEncounterGame.fourthName.in_([user.fullname, user.username]),
        CosmicEncounterGame.fifthName.in_([user.fullname, user.username]),
    )).with_entities(CosmicEncounterGame.game_id, CosmicEncounterGame.winnerName, CosmicEncounterGame.secondName, CosmicEncounterGame.thirdName, CosmicEncounterGame.date, CosmicEncounterGame.poster_id, literal('Cosmic Encounter').label('game_type')).all()
    recentGames = processGames(user, recentGames, cosmic_games, 'Cosmic Encounter')

    catan_games = CatanGame.query.filter(or_(
        CatanGame.winnerName.in_([user.fullname, user.username]),
        CatanGame.secondName.in_([user.fullname, user.username]),
        CatanGame.thirdName.in_([user.fullname, user.username]),
        CatanGame.fourthName.in_([user.fullname, user.username]),
    )).with_entities(CatanGame.game_id, CatanGame.winnerName, CatanGame.secondName, CatanGame.thirdName, CatanGame.date, CatanGame.poster_id, literal('Catan').label('game_type')).all()
    recentGames = processGames(user, recentGames, catan_games, 'Catan')

    exploding_games = ExplodingKittensGame.query.filter(or_(
        ExplodingKittensGame.winnerName.in_([user.fullname, user.username]),
        ExplodingKittensGame.secondName.in_([user.fullname, user.username]),
        ExplodingKittensGame.thirdName.in_([user.fullname, user.username]),
        ExplodingKittensGame.fourthName.in_([user.fullname, user.username]),
        ExplodingKittensGame.fifthName.in_([user.fullname, user.username]),
        ExplodingKittensGame.sixthName.in_([user.fullname, user.username]),
        ExplodingKittensGame.seventhName.in_([user.fullname, user.username]),
        ExplodingKittensGame.eighthName.in_([user.fullname, user.username]),
        ExplodingKittensGame.ninthName.in_([user.fullname, user.username]),
        ExplodingKittensGame.tenthName.in_([user.fullname, user.username]),
    )).with_entities(ExplodingKittensGame.game_id, ExplodingKittensGame.winnerName, ExplodingKittensGame.secondName, ExplodingKittensGame.thirdName, ExplodingKittensGame.date, ExplodingKittensGame.poster_id, literal('Exploding Kittens').label('game_type')).all()
    recentGames = processGames(user, recentGames, exploding_games, 'Exploding Kittens')

    sushi_games = SushiGoPartyGame.query.filter(or_(
        SushiGoPartyGame.winnerName.in_([user.fullname, user.username]),
        SushiGoPartyGame.secondName.in_([user.fullname, user.username]),
        SushiGoPartyGame.thirdName.in_([user.fullname, user.username]),
        SushiGoPartyGame.fourthName.in_([user.fullname, user.username]),
        SushiGoPartyGame.fifthName.in_([user.fullname, user.username]),
        SushiGoPartyGame.sixthName.in_([user.fullname, user.username]),
        SushiGoPartyGame.seventhName.in_([user.fullname, user.username]),
        SushiGoPartyGame.eighthName.in_([user.fullname, user.username]),
    )).with_entities(SushiGoPartyGame.game_id, SushiGoPartyGame.winnerName, SushiGoPartyGame.secondName, SushiGoPartyGame.thirdName, SushiGoPartyGame.date, SushiGoPartyGame.poster_id, literal('Sushi Go Party').label('game_type')).all()
    recentGames = processGames(user, recentGames, sushi_games, 'Sushi Go Party')

    magic_games = MagicTheGatheringGame.query.filter(or_(
        MagicTheGatheringGame.winnerName.in_([user.fullname, user.username]),
        MagicTheGatheringGame.secondName.in_([user.fullname, user.username]),
        MagicTheGatheringGame.thirdName.in_([user.fullname, user.username]),
        MagicTheGatheringGame.fourthName.in_([user.fullname, user.username]),
        MagicTheGatheringGame.fifthName.in_([user.fullname, user.username]),
    )).with_entities(MagicTheGatheringGame.game_id, MagicTheGatheringGame.winnerName, MagicTheGatheringGame.secondName, MagicTheGatheringGame.thirdName, MagicTheGatheringGame.date, literal('Magic: The Gathering').label('game_type')).all()

    for game in magic_games:
        new_game = {}
        if game.winnerName == user.username:
            new_game['winnerName'] = user.fullname
        else:
            new_game['winnerName'] = game.winnerName
        if game.secondName == user.username:
            new_game['secondName'] = user.fullname
        else:
            new_game['secondName'] = game.secondName
        if game.thirdName == user.username:
            new_game['thirdName'] = user.fullname
        else:
            new_game['thirdName'] = game.thirdName

        new_game['game_id'] = game.game_id
        new_game['game_type'] = 'Magic: The Gathering'
        new_game['current_date'] = game.date
        recentGames.append(new_game)

    munchkin_games = MunchkinGame.query.filter(or_(
        MunchkinGame.winnerName.in_([user.fullname, user.username]),
        MunchkinGame.secondName.in_([user.fullname, user.username]),
        MunchkinGame.thirdName.in_([user.fullname, user.username]),
        MunchkinGame.fourthName.in_([user.fullname, user.username]),
        MunchkinGame.fifthName.in_([user.fullname, user.username]),
        MunchkinGame.sixthName.in_([user.fullname, user.username]),
    )).with_entities(MunchkinGame.game_id, MunchkinGame.winnerName, MunchkinGame.secondName, MunchkinGame.thirdName, MunchkinGame.date, MunchkinGame.poster_id, literal('Munchkin').label('game_type')).all()
    recentGames = processGames(user, recentGames, munchkin_games, 'Munchkin')

    coup_games = CoupGame.query.filter(or_(
        CoupGame.winnerName.in_([user.fullname, user.username]),
        CoupGame.secondName.in_([user.fullname, user.username]),
        CoupGame.thirdName.in_([user.fullname, user.username]),
        CoupGame.fourthName.in_([user.fullname, user.username]),
        CoupGame.fifthName.in_([user.fullname, user.username]),
        CoupGame.sixthName.in_([user.fullname, user.username]),
    )).with_entities(CoupGame.game_id, CoupGame.winnerName, CoupGame.secondName, CoupGame.thirdName, CoupGame.date, literal('Coup').label('game_type')).all()

    for game in coup_games:
        new_game = {}
        if game.winnerName == user.username:
            new_game['winnerName'] = user.fullname
        else:
            new_game['winnerName'] = game.winnerName
        if game.secondName == user.username:
            new_game['secondName'] = user.fullname
        else:
            new_game['secondName'] = game.secondName
        if game.thirdName == user.username:
            new_game['thirdName'] = user.fullname
        else:
            new_game['thirdName'] = game.thirdName

        new_game['game_id'] = game.game_id
        new_game['game_type'] = 'Coup'
        new_game['current_date'] = game.date
        recentGames.append(new_game)

    love_letter_games = LoveLetterGame.query.filter(or_(
        LoveLetterGame.winnerName.in_([user.fullname, user.username]),
        LoveLetterGame.secondName.in_([user.fullname, user.username]),
        LoveLetterGame.thirdName.in_([user.fullname, user.username]),
        LoveLetterGame.fourthName.in_([user.fullname, user.username]),
        LoveLetterGame.fifthName.in_([user.fullname, user.username]),
        LoveLetterGame.sixthName.in_([user.fullname, user.username]),
    )).with_entities(LoveLetterGame.game_id, LoveLetterGame.winnerName, LoveLetterGame.secondName, LoveLetterGame.thirdName, LoveLetterGame.date, literal('Love Letter').label('game_type')).all()

    for game in love_letter_games:
        new_game = {}
        if game.winnerName == user.username:
            new_game['winnerName'] = user.fullname
        else:
            new_game['winnerName'] = game.winnerName
        if game.secondName == user.username:
            new_game['secondName'] = user.fullname
        else:
            new_game['secondName'] = game.secondName
        if game.thirdName == user.username:
            new_game['thirdName'] = user.fullname
        else:
            new_game['thirdName'] = game.thirdName

        new_game['game_id'] = game.game_id
        new_game['game_type'] = 'Love Letter'
        new_game['current_date'] = game.date
        recentGames.append(new_game)

    mind_games = TheMindGame.query.filter(or_(
        TheMindGame.playerone.in_([user.fullname, user.username]),
        TheMindGame.playertwo.in_([user.fullname, user.username]),
        TheMindGame.playerthree.in_([user.fullname, user.username]),
        TheMindGame.playerfour.in_([user.fullname, user.username]),
    )).with_entities(TheMindGame.game_id, TheMindGame.playerone, TheMindGame.playertwo, TheMindGame.victory, TheMindGame.date, literal('The Mind').label('game_type')).all()

    for game in mind_games:
        new_game = {}
        if game.victory == 'Yes':
            new_game['winnerName'] = "Victory"

        if game.victory == 'No':
            new_game['winnerName'] = "Defeat"

        if game.playerone == user.username:
            new_game['secondName'] = user.fullname
        else:
            new_game['secondName'] = game.playerone
        if game.playertwo == user.username:
            new_game['thirdName'] = user.fullname
        else:
            new_game['thirdName'] = game.playertwo

        new_game['game_id'] = game.game_id
        new_game['game_type'] = 'The Mind'
        new_game['current_date'] = game.date
        recentGames.append(new_game)

    just_one_games = JustOneGame.query.filter(or_(
        JustOneGame.playerone.in_([user.fullname, user.username]),
        JustOneGame.playertwo.in_([user.fullname, user.username]),
        JustOneGame.playerthree.in_([user.fullname, user.username]),
        JustOneGame.playerfour.in_([user.fullname, user.username]),
        JustOneGame.playerfive.in_([user.fullname, user.username]),
        JustOneGame.playersix.in_([user.fullname, user.username]),
        JustOneGame.playerseven.in_([user.fullname, user.username]),
    )).with_entities(JustOneGame.game_id, JustOneGame.playerone, JustOneGame.playertwo, JustOneGame.victory, JustOneGame.date, literal('Just One').label('game_type')).all()

    for game in just_one_games:
        new_game = {}
        new_game['winnerName'] = game.victory

        if game.playerone == user.username:
            new_game['secondName'] = user.fullname
        else:
            new_game['secondName'] = game.playerone
        if game.playertwo == user.username:
            new_game['thirdName'] = user.fullname
        else:
            new_game['thirdName'] = game.playerone

        new_game['game_id'] = game.game_id
        new_game['game_type'] = 'Just One'
        new_game['current_date'] = game.date
        recentGames.append(new_game)

    sortedGames = sorted(recentGames, key=lambda x: x['game_id'], reverse=True)

    return sortedGames

def findFriendsGames(user):
    user = current_user
    user_friends = user.friends.all()
    friendsGames = []

    for friend in user_friends:
        print(friend.username)
        dominion_games = DominionGame.query.filter(or_(
            DominionGame.winnerName.in_([friend.fullname, friend.username]),
            DominionGame.secondName.in_([friend.fullname, friend.username]),
            DominionGame.thirdName.in_([friend.fullname, friend.username]),
            DominionGame.fourthName.in_([friend.fullname, friend.username]),
        )).with_entities(DominionGame.game_id, DominionGame.winnerName, DominionGame.secondName, DominionGame.thirdName, DominionGame.date, DominionGame.poster_id, literal('Dominion').label('game_type')).all()
        friendsGames = processGames(friend, friendsGames, dominion_games,'Dominion')

        moon_games = MoonrakersGame.query.filter(or_(
            MoonrakersGame.winnerName.in_([friend.fullname, friend.username]),
            MoonrakersGame.secondName.in_([friend.fullname, friend.username]),
            MoonrakersGame.thirdName.in_([friend.fullname, friend.username]),
            MoonrakersGame.fourthName.in_([friend.fullname, friend.username]),
            MoonrakersGame.fifthName.in_([friend.fullname, friend.username]),
        )).with_entities(MoonrakersGame.game_id, MoonrakersGame.winnerName, MoonrakersGame.secondName, MoonrakersGame.thirdName, MoonrakersGame.date, MoonrakersGame.poster_id, literal('Moonrakers').label('game_type')).all()
        friendsGames = processGames(friend, friendsGames, moon_games, 'Moonrakers')
        clank_games = ClankGame.query.filter(or_(
            ClankGame.winnerName.in_([friend.fullname, friend.username]),
            ClankGame.secondName.in_([friend.fullname, friend.username]),
            ClankGame.thirdName.in_([friend.fullname, friend.username]),
            ClankGame.fourthName.in_([friend.fullname, friend.username]),
        )).with_entities(ClankGame.game_id, ClankGame.winnerName, ClankGame.secondName, ClankGame.thirdName, ClankGame.date, ClankGame.poster_id, literal('Clank').label('game_type')).all()
        friendsGames = processGames(friend, friendsGames, clank_games, 'Clank')

        lords_games = LordsofWaterdeepGame.query.filter(or_(
            LordsofWaterdeepGame.winnerName.in_([friend.fullname, friend.username]),
            LordsofWaterdeepGame.secondName.in_([friend.fullname, friend.username]),
            LordsofWaterdeepGame.thirdName.in_([friend.fullname, friend.username]),
            LordsofWaterdeepGame.fourthName.in_([friend.fullname, friend.username]),
            LordsofWaterdeepGame.fifthName.in_([friend.fullname, friend.username]),
        )).with_entities(LordsofWaterdeepGame.game_id, LordsofWaterdeepGame.winnerName, LordsofWaterdeepGame.secondName, LordsofWaterdeepGame.thirdName, LordsofWaterdeepGame.date, LordsofWaterdeepGame.poster_id, literal('Lords of the Waterdeep').label('game_type')).all()
        friendsGames = processGames(friend, friendsGames, lords_games, 'Lords of Waterdeep')

        heat_games = HeatGame.query.filter(or_(
            HeatGame.winnerName.in_([friend.fullname, friend.username]),
            HeatGame.secondName.in_([friend.fullname, friend.username]),
            HeatGame.thirdName.in_([friend.fullname, friend.username]),
            HeatGame.fourthName.in_([friend.fullname, friend.username]),
            HeatGame.fifthName.in_([friend.fullname, friend.username]),
            HeatGame.sixthName.in_([friend.fullname, friend.username]),
        )).with_entities(HeatGame.game_id, HeatGame.winnerName, HeatGame.secondName, HeatGame.thirdName, HeatGame.date, HeatGame.poster_id, literal('Heat: Pedal to the Metal').label('game_type')).all()
        friendsGames = processGames(friend, friendsGames, heat_games, 'Heat')

        space_games = SpaceBaseGame.query.filter(or_(
            SpaceBaseGame.winnerName.in_([friend.fullname, friend.username]),
            SpaceBaseGame.secondName.in_([friend.fullname, friend.username]),
            SpaceBaseGame.thirdName.in_([friend.fullname, friend.username]),
            SpaceBaseGame.fourthName.in_([friend.fullname, friend.username]),
            SpaceBaseGame.fifthName.in_([friend.fullname, friend.username]),
        )).with_entities(SpaceBaseGame.game_id, SpaceBaseGame.winnerName, SpaceBaseGame.secondName, SpaceBaseGame.thirdName, SpaceBaseGame.date, SpaceBaseGame.poster_id, literal('Space Base').label('game_type')).all()
        friendsGames = processGames(friend, friendsGames, space_games, 'Space Base')

        cosmic_games = CosmicEncounterGame.query.filter(or_(
            CosmicEncounterGame.winnerName.in_([friend.fullname, friend.username]),
            CosmicEncounterGame.secondName.in_([friend.fullname, friend.username]),
            CosmicEncounterGame.thirdName.in_([friend.fullname, friend.username]),
            CosmicEncounterGame.fourthName.in_([friend.fullname, friend.username]),
            CosmicEncounterGame.fifthName.in_([friend.fullname, friend.username]),
        )).with_entities(CosmicEncounterGame.game_id, CosmicEncounterGame.winnerName, CosmicEncounterGame.secondName, CosmicEncounterGame.thirdName, CosmicEncounterGame.date, CosmicEncounterGame.poster_id, literal('Cosmic Encounter').label('game_type')).all()
        friendsGames = processGames(user, friendsGames, cosmic_games, 'Cosmic Encounter')

        catan_games = CatanGame.query.filter(or_(
            CatanGame.winnerName.in_([friend.fullname, friend.username]),
            CatanGame.secondName.in_([friend.fullname, friend.username]),
            CatanGame.thirdName.in_([friend.fullname, friend.username]),
            CatanGame.fourthName.in_([friend.fullname, friend.username]),
        )).with_entities(CatanGame.game_id, CatanGame.winnerName, CatanGame.secondName, CatanGame.thirdName, CatanGame.date, CatanGame.poster_id, literal('Catan').label('game_type')).all()
        friendsGames = processGames(user, friendsGames, catan_games, 'Catan')

        exploding_games = ExplodingKittensGame.query.filter(or_(
            ExplodingKittensGame.winnerName.in_([friend.fullname, friend.username]),
            ExplodingKittensGame.secondName.in_([friend.fullname, friend.username]),
            ExplodingKittensGame.thirdName.in_([friend.fullname, friend.username]),
            ExplodingKittensGame.fourthName.in_([friend.fullname, friend.username]),
            ExplodingKittensGame.fifthName.in_([friend.fullname, friend.username]),
            ExplodingKittensGame.sixthName.in_([friend.fullname, friend.username]),
            ExplodingKittensGame.seventhName.in_([friend.fullname, friend.username]),
            ExplodingKittensGame.eighthName.in_([friend.fullname, friend.username]),
            ExplodingKittensGame.ninthName.in_([friend.fullname, friend.username]),
            ExplodingKittensGame.tenthName.in_([friend.fullname, friend.username]),
        )).with_entities(ExplodingKittensGame.game_id, ExplodingKittensGame.winnerName, ExplodingKittensGame.secondName, ExplodingKittensGame.thirdName, ExplodingKittensGame.date, ExplodingKittensGame.poster_id, literal('Exploding Kittens').label('game_type')).all()
        friendsGames = processGames(user, friendsGames, exploding_games, 'Exploding Kittens')

        sushi_games = SushiGoPartyGame.query.filter(or_(
            SushiGoPartyGame.winnerName.in_([friend.fullname, friend.username]),
            SushiGoPartyGame.secondName.in_([friend.fullname, friend.username]),
            SushiGoPartyGame.thirdName.in_([friend.fullname, friend.username]),
            SushiGoPartyGame.fourthName.in_([friend.fullname, friend.username]),
            SushiGoPartyGame.fifthName.in_([friend.fullname, friend.username]),
            SushiGoPartyGame.sixthName.in_([friend.fullname, friend.username]),
            SushiGoPartyGame.seventhName.in_([friend.fullname, friend.username]),
            SushiGoPartyGame.eighthName.in_([friend.fullname, friend.username]),
        )).with_entities(SushiGoPartyGame.game_id, SushiGoPartyGame.winnerName, SushiGoPartyGame.secondName, SushiGoPartyGame.thirdName, SushiGoPartyGame.date, SushiGoPartyGame.poster_id, literal('Sushi Go Party').label('game_type')).all()
        friendsGames = processGames(user, friendsGames, sushi_games, 'Sushi Go Party')

        munchkin_games = MunchkinGame.query.filter(or_(
            MunchkinGame.winnerName.in_([friend.fullname, friend.username]),
            MunchkinGame.secondName.in_([friend.fullname, friend.username]),
            MunchkinGame.thirdName.in_([friend.fullname, friend.username]),
            MunchkinGame.fourthName.in_([friend.fullname, friend.username]),
            MunchkinGame.fifthName.in_([friend.fullname, friend.username]),
            MunchkinGame.sixthName.in_([friend.fullname, friend.username]),
        )).with_entities(MunchkinGame.game_id, MunchkinGame.winnerName, MunchkinGame.secondName, MunchkinGame.thirdName, MunchkinGame.date, MunchkinGame.poster_id, literal('Munchkin').label('game_type')).all()
        friendsGames = processGames(friend, friendsGames, munchkin_games, 'Munchkin')

    friendsGames = sorted(friendsGames, key=lambda x: x['game_id'], reverse=True)

    return friendsGames

@app.route('/api/recent-games/<int:page>')
@login_required
def get_recent_games(page):
    offset = (page - 1) * 12
    user = current_user
    recent_games = findRecentGames(user)
    friendsGames = findFriendsGames(current_user)

    combinedGames = recent_games + friendsGames
    uniqueGames = {game['game_id']: game for game in combinedGames}
    combinedGames = sorted(uniqueGames.values(), key=lambda x: x['game_id'], reverse=True)
    nextGameSet = combinedGames[offset:offset + 12]
    
    return jsonify(nextGameSet)