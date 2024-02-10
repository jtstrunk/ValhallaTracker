from app import app, db
from flask_login import UserMixin

# Create the database tables
with app.app_context():

    class CosmicEncounterGame(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        game_id = db.Column(db.Integer, nullable=False)
        firstName = db.Column(db.String(50), nullable=False)
        firstScore = db.Column(db.Integer, nullable=False)
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

    db.session.commit()
 
    db.create_all()

#     class Cards(db.Model):
#         id = db.Column(db.Integer, primary_key=True)
#         cardName = db.Column(db.String(50), nullable=False)
#         cardSet = db.Column(db.String(50), nullable=False)

#     class Village(db.Model):
#         id = db.Column(db.Integer, primary_key=True)
#         cardName = db.Column(db.String(50), db.ForeignKey('cards.cardName'), nullable=False)
#         card = db.relationship('Cards', backref='village')

#     class Cantrip(db.Model):
#         id = db.Column(db.Integer, primary_key=True)
#         cardName = db.Column(db.String(50), db.ForeignKey('cards.cardName'), nullable=False)
#         card = db.relationship('Cards', backref='cantrip')

#     class Gainer(db.Model):
#         id = db.Column(db.Integer, primary_key=True)
#         cardName = db.Column(db.String(50), db.ForeignKey('cards.cardName'), nullable=False)
#         card = db.relationship('Cards', backref='gainer')

#     class Sifter(db.Model):
#         id = db.Column(db.Integer, primary_key=True)
#         cardName = db.Column(db.String(50), db.ForeignKey('cards.cardName'), nullable=False)
#         card = db.relationship('Cards', backref='sifter')

#     class Trasher(db.Model):
#         id = db.Column(db.Integer, primary_key=True)
#         cardName = db.Column(db.String(50), db.ForeignKey('cards.cardName'), nullable=False)
#         card = db.relationship('Cards', backref='trasher')

#     class NonterminalDraw(db.Model):
#         id = db.Column(db.Integer, primary_key=True)
#         cardName = db.Column(db.String(50), db.ForeignKey('cards.cardName'), nullable=False)
#         card = db.relationship('Cards', backref='nonterminalDraw')

#     class TerminalDraw(db.Model):
#         id = db.Column(db.Integer, primary_key=True)
#         cardName = db.Column(db.String(50), db.ForeignKey('cards.cardName'), nullable=False)
#         card = db.relationship('Cards', backref='terminalDraw')

#     class TerminalSilver(db.Model):
#         id = db.Column(db.Integer, primary_key=True)
#         cardName = db.Column(db.String(50), db.ForeignKey('cards.cardName'), nullable=False)
#         card = db.relationship('Cards', backref='terminalSilver')

#     class Action(db.Model):
#         id = db.Column(db.Integer, primary_key=True)
#         cardName = db.Column(db.String(50), db.ForeignKey('cards.cardName'), nullable=False)
#         card = db.relationship('Cards', backref='action')

#     class Attack(db.Model):
#         id = db.Column(db.Integer, primary_key=True)
#         cardName = db.Column(db.String(50), db.ForeignKey('cards.cardName'), nullable=False)
#         card = db.relationship('Cards', backref='attack')

#     class Victory(db.Model):
#         id = db.Column(db.Integer, primary_key=True)
#         cardName = db.Column(db.String(50), db.ForeignKey('cards.cardName'), nullable=False)
#         card = db.relationship('Cards', backref='victory')

#     class Treasure(db.Model):
#         id = db.Column(db.Integer, primary_key=True)
#         cardName = db.Column(db.String(50), db.ForeignKey('cards.cardName'), nullable=False)
#         card = db.relationship('Cards', backref='treasure')

#     class Reaction(db.Model):
#         id = db.Column(db.Integer, primary_key=True)
#         cardName = db.Column(db.String(50), db.ForeignKey('cards.cardName'), nullable=False)
#         card = db.relationship('Cards', backref='reaction')

#     class Duration(db.Model):
#         id = db.Column(db.Integer, primary_key=True)
#         cardName = db.Column(db.String(50), db.ForeignKey('cards.cardName'), nullable=False)
#         card = db.relationship('Cards', backref='duration')  


#     # actions = [
#     #     Action(cardName="Artisan"),
#     #     Action(cardName="Bandit"),
#     #     Action(cardName="Bureaucrat"),
#     #     Action(cardName="Cellar"),
#     #     Action(cardName="Chapel"),
#     #     Action(cardName="Council_Room"),
#     #     Action(cardName="Festival"),
#     #     Action(cardName="Harbinger"),
#     #     Action(cardName="Laboratory"),
#     #     Action(cardName="Library"),
#     #     Action(cardName="Market"),
#     #     Action(cardName="Merchant"),
#     #     Action(cardName="Militia"),
#     #     Action(cardName="Mine"),
#     #     Action(cardName="Moat"),
#     #     Action(cardName="Moneylender"),
#     #     Action(cardName="Poacher"),
#     #     Action(cardName="Remodel"),
#     #     Action(cardName="Sentry"),
#     #     Action(cardName="Smithy"),
#     #     Action(cardName="Throne_Room"),
#     #     Action(cardName="Vassal"),
#     #     Action(cardName="Village"),
#     #     Action(cardName="Witch"),
#     #     Action(cardName="Workshop"),
#     #     Action(cardName="Bazaar"),
#     #     Action(cardName="Blockade"),
#     #     Action(cardName="Caravan"),
#     #     Action(cardName="Corsair"),
#     #     Action(cardName="Cutpurse"),
#     #     Action(cardName="Fishing_Village"),
#     #     Action(cardName="Haven"),
#     #     Action(cardName="Island"),
#     #     Action(cardName="Lighthouse"),
#     #     Action(cardName="Lookout"),
#     #     Action(cardName="Merchant_Ship"),
#     #     Action(cardName="Monkey"),
#     #     Action(cardName="Native_Village"),
#     #     Action(cardName="Outpost"),
#     #     Action(cardName="Pirate"),
#     #     Action(cardName="Sailor"),
#     #     Action(cardName="Salvager"),
#     #     Action(cardName="Sea_Chart"),
#     #     Action(cardName="Sea_Witch"),
#     #     Action(cardName="Smugglers"),
#     #     Action(cardName="Tactician"),
#     #     Action(cardName="Tide_Pools"),
#     #     Action(cardName="Treasure_Map"),
#     #     Action(cardName="Treasury"),
#     #     Action(cardName="Warehouse"),
#     #     Action(cardName="Wharf"),
#     #     Action(cardName="Baron"),
#     #     Action(cardName="Bridge"),
#     #     Action(cardName="Conspirator"),
#     #     Action(cardName="Courtier"),
#     #     Action(cardName="Courtyard"),
#     #     Action(cardName="Diplomat"),
#     #     Action(cardName="Ironworks"),
#     #     Action(cardName="Lurker"),
#     #     Action(cardName="Masquerade"),
#     #     Action(cardName="Mill"),
#     #     Action(cardName="Mining_Village"),
#     #     Action(cardName="Minion"),
#     #     Action(cardName="Nobles"),
#     #     Action(cardName="Pawn"),
#     #     Action(cardName="Patrol"),
#     #     Action(cardName="Replace"),
#     #     Action(cardName="Secret Passage"),
#     #     Action(cardName="Shanty Town"),
#     #     Action(cardName="Steward"),
#     #     Action(cardName="Swindler"),
#     #     Action(cardName="Torturer"),
#     #     Action(cardName="Trading_Post"),
#     #     Action(cardName="Upgrade"),
#     #     Action(cardName="Wishing_Well")
#     # ]

#     # for action in actions:
#     #     db.session.add(action)

#     # durations = [
#     #     Duration(cardName="Caravan"),
#     #     Duration(cardName="Fishing_Village"),
#     #     Duration(cardName="Haven"),
#     #     Duration(cardName="Lighthouse"),
#     #     Duration(cardName="Merchant_Ship"),
#     #     Duration(cardName="Monkey"),
#     #     Duration(cardName="Outpost"),
#     #     Duration(cardName="Sailor"),
#     #     Duration(cardName="Tactician"),
#     #     Duration(cardName="Tide_Pools"),
#     #     Duration(cardName="Wharf"),
#     #     Duration(cardName="Blockade"),
#     #     Duration(cardName="Sea_Witch"),
#     #     Duration(cardName="Corsair"),
#     #     Duration(cardName="Pirate")
#     # ]

#     # for duration in durations:
#     #     db.session.add(duration)

#     # sifters = [
#     #     Sifter(cardName="Cellar"),
#     #     Sifter(cardName="Warehouse"),
#     #     Sifter(cardName="Sea_Witch"),
#     #     Sifter(cardName="Diplomat"),
#     #     Sifter(cardName="Secret_Passage")
#     # ]

#     # for sifter in sifters:
#     #     db.session.add(sifter)

#     # db.session.commit()

#     # # Treasure types
#     # treasures = [
#     #     Treasure(cardName="Harem"),
#     #     Treasure(cardName="Astrolabe")
#     # ]

#     # for treasure in treasures:
#     #     db.session.add(treasure)

#     # db.session.commit()

#     # # Attack types
#     # attacks = [
#     #     Attack(cardName="Bandit"),
#     #     Attack(cardName="Bureaucrat"),
#     #     Attack(cardName="Militia"),
#     #     Attack(cardName="Witch"),
#     #     Attack(cardName="Blockade"),
#     #     Attack(cardName="Corsair"),
#     #     Attack(cardName="Cutpurse"),
#     #     Attack(cardName="Sea_Witch"),
#     #     Attack(cardName="Swindler"),
#     #     Attack(cardName="Minion"),
#     #     Attack(cardName="Replace"),
#     #     Attack(cardName="Torturer")
#     # ]

#     # for attack in attacks:
#     #     db.session.add(attack)

#     # db.session.commit()

#     # # Gainer types
#     # gainers = [
#     #     Gainer(cardName="Workshop"),
#     #     Gainer(cardName="Ironworks")
#     # ]

#     # for gainer in gainers:
#     #     db.session.add(gainer)

#     # terminal_draws = [
#     #     TerminalDraw(cardName="Council_Room"),
#     #     TerminalDraw(cardName="Library"),
#     #     TerminalDraw(cardName="Moat"),
#     #     TerminalDraw(cardName="Smithy"),
#     #     TerminalDraw(cardName="Witch"),
#     #     TerminalDraw(cardName="Wharf"),
#     #     TerminalDraw(cardName="Sea_Witch"),
#     #     TerminalDraw(cardName="Nobles"),
#     #     TerminalDraw(cardName="Patrol"),
#     #     TerminalDraw(cardName="Torturer")
#     # ]

#     # for terminal_draw in terminal_draws:
#     #     db.session.add(terminal_draw)

#     # db.session.commit()

#     # # Victory types
#     # victories = [
#     #     Victory(cardName="Gardens"),
#     #     Victory(cardName="Island"),
#     #     Victory(cardName="Duke"),
#     #     Victory(cardName="Nobles"),
#     #     Victory(cardName="Harem"),
#     #     Victory(cardName="Mill")
#     # ]

#     # for victory in victories:
#     #     db.session.add(victory)

#     # db.session.commit()

#     # # Cantrip types
#     # cantrips = [
#     #     Cantrip(cardName="Harbinger"),
#     #     Cantrip(cardName="Merchant"),
#     #     Cantrip(cardName="Poacher"),
#     #     Cantrip(cardName="Treasury"),
#     #     Cantrip(cardName="Haven"),
#     #     Cantrip(cardName="Caravan"),
#     #     Cantrip(cardName="Sea_Chart"),
#     #     Cantrip(cardName="Sentry"),
#     #     Cantrip(cardName="Courtyard")
#     # ]

#     # for cantrip in cantrips:
#     #     db.session.add(cantrip)

#     # db.session.commit()

#     # # NonterminalDraw types
#     # nonterminal_draws = [
#     #     NonterminalDraw(cardName="Laboratory"),
#     #     NonterminalDraw(cardName="Tide Pools"),
#     #     NonterminalDraw(cardName="Wishing_Well")
#     # ]

#     # for nonterminal_draw in nonterminal_draws:
#     #     db.session.add(nonterminal_draw)

#     # db.session.commit()

#     # # TerminalSilver types
#     # terminal_silvers = [
#     #     TerminalSilver(cardName="Bridge"),
#     #     TerminalSilver(cardName="Conspirator"),
#     #     TerminalSilver(cardName="Steward"),
#     #     TerminalSilver(cardName="Swindler")
#     # ]

#     # for terminal_silver in terminal_silvers:
#     #     db.session.add(terminal_silver)

#     # db.session.commit()

#     # # Village types
#     # villages = [
#     #     Village(cardName="Village"),
#     #     Village(cardName="Festival"),
#     #     Village(cardName="Bazaar"),
#     #     Village(cardName="Fishing_Village"),
#     #     Village(cardName="Native_Village"),
#     #     Village(cardName="Fishing Village"),
#     #     Village(cardName="Mining_Village"),
#     #     Village(cardName="Shanty_Town"),
#     #     Village(cardName="Nobles")
#     # ]

#     # for village in villages:
#     #     db.session.add(village)

#     # db.session.commit()

#     # # Reaction types
#     # reactions = [
#     #     Reaction(cardName="Moat"),
#     #     Reaction(cardName="Pirate"),
#     #     Reaction(cardName="Diplomat")
#     # ]

#     # for reaction in reactions:
#     #     db.session.add(reaction)

#     # db.session.commit()

#     # # Trasher types
#     # trashers = [
#     #     Trasher(cardName="Lurker"),
#     #     Trasher(cardName="Steward"),
#     #     Trasher(cardName="Trading_Post")
#     # ]

#     # for trasher in trashers:
#     #     db.session.add(trasher)

#     card_list = [
#         {"cardName": "Artisan", "cardSet": "Dominion SE"},
#         {"cardName": "Bandit", "cardSet": "Dominion SE"},
#         {"cardName": "Bureaucrat", "cardSet": "Dominion SE"},
#         {"cardName": "Cellar", "cardSet": "Dominion SE"},
#         {"cardName": "Chapel", "cardSet": "Dominion SE"},
#         {"cardName": "Council_Room", "cardSet": "Dominion SE"},
#         {"cardName": "Festival", "cardSet": "Dominion SE"},
#         {"cardName": "Gardens", "cardSet": "Dominion SE"},
#         {"cardName": "Harbinger", "cardSet": "Dominion SE"},
#         {"cardName": "Laboratory", "cardSet": "Dominion SE"},
#         {"cardName": "Library", "cardSet": "Dominion SE"},
#         {"cardName": "Market", "cardSet": "Dominion SE"},
#         {"cardName": "Merchant", "cardSet": "Dominion SE"},
#         {"cardName": "Militia", "cardSet": "Dominion SE"},
#         {"cardName": "Mine", "cardSet": "Dominion SE"},
#         {"cardName": "Moat", "cardSet": "Dominion SE"},
#         {"cardName": "Moneylender", "cardSet": "Dominion SE"},
#         {"cardName": "Poacher", "cardSet": "Dominion SE"},
#         {"cardName": "Remodel", "cardSet": "Dominion SE"},
#         {"cardName": "Sentry", "cardSet": "Dominion SE"},
#         {"cardName": "Smithy", "cardSet": "Dominion SE"},
#         {"cardName": "Throne_Room", "cardSet": "Dominion SE"},
#         {"cardName": "Vassel", "cardSet": "Dominion SE"},
#         {"cardName": "Village", "cardSet": "Dominion SE"},
#         {"cardName": "Witch", "cardSet": "Dominion SE"},
#         {"cardName": "Workshop", "cardSet": "Dominion SE"},
#         {"cardName": "Astrolabe", "cardSet": "Seaside SE"},
#         {"cardName": "Bazaar", "cardSet": "Seaside SE"},
#         {"cardName": "Blockade", "cardSet": "Seaside SE"},
#         {"cardName": "Caravan", "cardSet": "Seaside SE"},
#         {"cardName": "Corsair", "cardSet": "Seaside SE"},
#         {"cardName": "Cutpurse", "cardSet": "Seaside SE"},
#         {"cardName": "Fishing_Village", "cardSet": "Seaside SE"},
#         {"cardName": "Haven", "cardSet": "Seaside SE"},
#         {"cardName": "Island", "cardSet": "Seaside SE"},
#         {"cardName": "Lighthouse", "cardSet": "Seaside SE"},
#         {"cardName": "Lookout", "cardSet": "Seaside SE"},
#         {"cardName": "Merchant Ship", "cardSet": "Seaside SE"},
#         {"cardName": "Monkey", "cardSet": "Seaside SE"},
#         {"cardName": "Native_village", "cardSet": "Seaside SE"},
#         {"cardName": "Outpost", "cardSet": "Seaside SE"},
#         {"cardName": "Pirate", "cardSet": "Seaside SE"},
#         {"cardName": "Sailor", "cardSet": "Seaside SE"},
#         {"cardName": "Salvager", "cardSet": "Seaside SE"},
#         {"cardName": "Sea_Chart", "cardSet": "Seaside SE"},
#         {"cardName": "Sea_Witch", "cardSet": "Seaside SE"},
#         {"cardName": "Smugglers", "cardSet": "Seaside SE"},
#         {"cardName": "Tactician", "cardSet": "Seaside SE"},
#         {"cardName": "Tide_Pools", "cardSet": "Seaside SE"},
#         {"cardName": "Treasure_Map", "cardSet": "Seaside SE"},
#         {"cardName": "Treasury", "cardSet": "Seaside SE"},
#         {"cardName": "Wharf", "cardSet": "Seaside SE"},
#         {"cardName": "Baron", "cardSet": "Intrigue SE"},
#         {"cardName": "Bridge", "cardSet": "Intrigue SE"},
#         {"cardName": "Conspirator", "cardSet": "Intrigue SE"},
#         {"cardName": "Courtier", "cardSet": "Intrigue SE"},
#         {"cardName": "Courtyard", "cardSet": "Intrigue SE"},
#         {"cardName": "Diplomat", "cardSet": "Intrigue SE"},
#         {"cardName": "Duke", "cardSet": "Intrigue SE"},
#         {"cardName": "Harem", "cardSet": "Intrigue SE"},
#         {"cardName": "Ironworks", "cardSet": "Intrigue SE"},
#         {"cardName": "Lurker", "cardSet": "Intrigue SE"},
#         {"cardName": "Masquerade", "cardSet": "Intrigue SE"},
#         {"cardName": "Mill", "cardSet": "Intrigue SE"},
#         {"cardName": "Mining Village", "cardSet": "Intrigue SE"},
#         {"cardName": "Minion", "cardSet": "Intrigue SE"},
#         {"cardName": "Nobles", "cardSet": "Intrigue SE"},
#         {"cardName": "Pawn", "cardSet": "Intrigue SE"},
#         {"cardName": "Patrol", "cardSet": "Intrigue SE"},
#         {"cardName": "Replace", "cardSet": "Intrigue SE"},
#         {"cardName": "Secret_Passage", "cardSet": "Intrigue SE"},
#         {"cardName": "Shanty_Town", "cardSet": "Intrigue SE"},
#         {"cardName": "Steward", "cardSet": "Intrigue SE"},
#         {"cardName": "Swindler", "cardSet": "Intrigue SE"},
#         {"cardName": "Torturer", "cardSet": "Intrigue SE"},
#         {"cardName": "Trading_Post", "cardSet": "Intrigue SE"},
#         {"cardName": "Upgrade", "cardSet": "Intrigue SE"},
#         {"cardName": "Wishing_Well", "cardSet": "Intrigue SE"}
#     ]

#     for card in card_list:
#         new_card = Cards(cardName=card["cardName"], cardSet=card["cardSet"])
#         db.session.add(new_card)

#     db.session.commit()
 

#     # db.create_all()