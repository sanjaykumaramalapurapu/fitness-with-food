from flask import Flask, render_template, request, session
from rice import calories_badmintion
from rice import *
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Set a secret key for session management

@app.route('/')
def index():
    session.clear()
    return render_template('index.html')

@app.route('/diet_calculators')
def diet_calculators():
    return render_template('diet_calculators.html')

@app.route('/workout')
def workout():
    return render_template('workout.html')
@app.route('/warmup')
def warmup():
    return render_template('warmup.html')
@app.route('/Abs')
def Abs():
    return render_template('Abs.html')
@app.route('/chest')
def chest():
    return render_template('chest.html')
@app.route('/legs')
def legs():
    return render_template('legs.html')
@app.route('/Tips')
def Tips():
    return render_template('Tips.html')
@app.route('/breakfast', methods=['GET', 'POST'])
def breakfast():
    if request.method == 'POST':
        if 'Egg_whites' in request.form:
            Egg_whites = int(request.form['Egg_whites'])
            egg_protein = Egg_whites * 3.6
            caloriesConsumed_egg = Egg_whites * 17
            session['Egg_whites'] = Egg_whites
            session['egg_protein'] = egg_protein
            session['caloriesConsumed_egg'] = caloriesConsumed_egg
        elif 'sprouts_grams' in request.form:
            sprouts_grams = int(request.form['sprouts_grams'])
            caloriesConsumed_Sprouts = sprouts_grams * 0.29
            session['sprouts_grams'] = sprouts_grams
            session['caloriesConsumed_Sprouts'] = caloriesConsumed_Sprouts
        elif 'oats_Grams' in request.form:
            oats_Grams = int(request.form['oats_Grams'])
            caloriesConsumed_oats = oats_Grams * 0.71
            session['oats_Grams'] = oats_Grams
            session['caloriesConsumed_oats'] = caloriesConsumed_oats
        elif 'bread_jam' in request.form:
            bread_jam = int(request.form['bread_jam'])
            caloriesConsumed_bread = bread_jam * 250
            session['bread_jam'] = bread_jam
            session['caloriesConsumed_bread'] = caloriesConsumed_bread
        elif 'idly' in request.form:
            idly = int(request.form['idly'])
            caloriesConsumed_idly = idly * 58
            session['idly'] = idly
            session['caloriesConsumed_idly'] = caloriesConsumed_idly
        elif 'Dosa' in request.form:
            Dosa = int(request.form['Dosa'])
            caloriesConsumed_dosa = Dosa * 191
            session['Dosa'] = Dosa
            session['caloriesConsumed_dosa'] = caloriesConsumed_dosa
        elif 'Poori' in request.form:
            Poori = int(request.form['Poori'])
            caloriesConsumed_Poori = Poori * 128
            session['Poori'] = Poori
            session['caloriesConsumed_Poori'] = caloriesConsumed_Poori
        elif 'Vada' in request.form:
            Vada = int(request.form['Vada'])
            caloriesConsumed_Vada = Vada * 135
            session['Vada'] = Vada
            session['caloriesConsumed_Vada'] = caloriesConsumed_Vada
        elif 'Mysore_Bonda' in request.form:
            Mysore_Bonda = int(request.form['Mysore_Bonda'])
            caloriesConsumed_Mysore_Bonda = Mysore_Bonda * 60
            session['Mysore_Bonda'] = Mysore_Bonda
            session['caloriesConsumed_Mysore_Bonda'] = caloriesConsumed_Mysore_Bonda

        # Render breakfast.html with updated values from session
        return render_template('breakfast.html',
                               Egg_whites=session.get('Egg_whites'),
                               egg_protein=session.get('egg_protein'),
                               caloriesConsumed_egg=session.get('caloriesConsumed_egg'),
                               sprouts_grams=session.get('sprouts_grams'),
                               caloriesConsumed_Sprouts=f"{session.get('caloriesConsumed_Sprouts'):.3f}" if session.get('caloriesConsumed_Sprouts') is not None else None,
                               oats_Grams=session.get('oats_Grams'),
                               caloriesConsumed_oats=f"{session.get('caloriesConsumed_oats'):.3f}" if session.get(
            'caloriesConsumed_oats') is not None else None,
                                bread_jam=session.get('bread_jam'),
                               caloriesConsumed_bread=session.get('caloriesConsumed_bread'),
                               idly=session.get('idly'),
                               caloriesConsumed_idly=session.get('caloriesConsumed_idly'),
                               Dosa=session.get('Dosa'),
                               caloriesConsumed_dosa=session.get('caloriesConsumed_dosa'),
                               Poori=session.get('Poori'),
                               caloriesConsumed_Poori=session.get('caloriesConsumed_Poori'),
                               Vada=session.get('Vada'),
                               caloriesConsumed_Vada=session.get('caloriesConsumed_Vada'),
                               Mysore_Bonda=session.get('Mysore_Bonda'),
                               caloriesConsumed_Mysore_Bonda=session.get('caloriesConsumed_Mysore_Bonda'))
    session.clear()
    return render_template('breakfast.html')

@app.route('/lunch', methods=['GET', 'POST'])
def lunch():
    if request.method == 'POST':
        if 'rice_grams' in request.form:
            rice_grams = int(request.form['rice_grams'])
            caloriesConsumed_rice=rice_grams*1.29
            session['rice_grams']=rice_grams
            session['caloriesConsumed_rice']=caloriesConsumed_rice
        elif 'Biriyani_Grams' in request.form:
            Biriyani_Grams=int(request.form['Biriyani_Grams'])
            caloriesConsumed_biriyani=Biriyani_Grams*1.63
            session['Biriyani_Grams']=Biriyani_Grams
            session['caloriesConsumed_biriyani']=caloriesConsumed_biriyani
        elif 'chapathi' in request.form:
            chapathi=int(request.form['chapathi'])
            caloriesConsumed_chapathi=chapathi*120
            session['chapathi']=chapathi
            session['caloriesConsumed_chapathi']=caloriesConsumed_chapathi
        elif 'Dal' in request.form:
            Dal=int(request.form['Dal'])
            Dal_protien=Dal*0.0529
            caloriesConsumed_Dal=Dal*1.01
            session['Dal']=Dal
            session['Dal_protien']=Dal_protien
            session['caloriesConsumed_Dal']=caloriesConsumed_Dal
        elif 'chicken_curry_Grams' in request.form:
            chicken_curry_Grams=int(request.form['chicken_curry_Grams'])
            chicken_protien=chicken_curry_Grams*0.31
            caloriesConsumed_chicken=chicken_curry_Grams*1.65
            session['chicken_curry_Grams']=chicken_curry_Grams
            session['chicken_protien']=chicken_protien
            session['caloriesConsumed_chicken']=caloriesConsumed_chicken
        elif 'mutton_curry_Grams' in request.form:
            mutton_curry_Grams=int(request.form['mutton_curry_Grams'])
            mutton_protien=mutton_curry_Grams*0.26
            caloriesConsumed_mutton=mutton_curry_Grams*2.32
            session['mutton_curry_Grams']=mutton_curry_Grams
            session['mutton_protien']=mutton_protien
            session['caloriesConsumed_mutton']=caloriesConsumed_mutton
        elif 'sambar_rice_Grams' in request.form:
            sambar_rice_Grams=int(request.form['sambar_rice_Grams'])
            caloriesConsumed_sambar=sambar_rice_Grams*2.14
            session['sambar_rice_Grams']=sambar_rice_Grams
            session['caloriesConsumed_sambar']=caloriesConsumed_sambar
        elif 'Potato_curry_grams' in request.form:
            Potato_curry_grams=int(request.form['Potato_curry_grams'])
            caloriesConsumed_Potato=Potato_curry_grams*0.83
            session['Potato_curry_grams']=Potato_curry_grams
            session['caloriesConsumed_Potato']=caloriesConsumed_Potato
        elif 'Paneer_curry_grams' in request.form:
            Paneer_curry_grams=int(request.form['Paneer_curry_grams'])
            protien_Paneer=Paneer_curry_grams*0.072
            caloriesConsumed_Paneer=Paneer_curry_grams*1.55
            session['Paneer_curry_grams']=Paneer_curry_grams
            session['protien_Paneer']=protien_Paneer
            session['caloriesConsumed_Paneer']=caloriesConsumed_Paneer
        elif 'mushroom_curry_grams' in request.form:
            mushroom_curry_grams=int(request.form['mushroom_curry_grams'])
            caloriesConsumed_mushroom=mushroom_curry_grams*0.678
            session['mushroom_curry_grams']=mushroom_curry_grams
            session['caloriesConsumed_mushroom']=caloriesConsumed_mushroom
        elif 'fish_curry' in request.form:
            fish_curry=int(request.form['fish_curry'])
            fish_protien=fish_curry*8
            caloriesConsumed_fish=fish_curry*36
            session['fish_curry']=fish_curry
            session['fish_protien']=fish_protien
            session['caloriesConsumed_fish']=caloriesConsumed_fish
        elif 'prawns_curry_grams' in request.form:
            prawns_curry_grams=int(request.form['prawns_curry_grams'])
            caloriesConsumed_prawns=prawns_curry_grams*1.05
            session['prawns_curry_grams']=prawns_curry_grams
            session['caloriesConsumed_prawns']=caloriesConsumed_prawns
        elif 'curd_rice_grams' in request.form:
            curd_rice_grams=int(request.form['curd_rice_grams'])
            caloriesConsumed_curd=curd_rice_grams*1
            session['curd_rice_grams']=curd_rice_grams
            session['caloriesConsumed_curd']=caloriesConsumed_curd
        return render_template('lunch.html',
                               rice_grams=session.get('rice_grams'),
                               caloriesConsumed_rice=session.get('caloriesConsumed_rice'),
                               Biriyani_Grams=session.get('Biriyani_Grams'),
                               caloriesConsumed_biriyani=session.get('caloriesConsumed_biriyani'),
                               chapathi=session.get('chapathi'),
                               caloriesConsumed_chapathi=session.get('caloriesConsumed_chapathi'),
                               Dal=session.get('Dal'),
                               Dal_protien=session.get('Dal_protien'),
                               caloriesConsumed_Dal=session.get('caloriesConsumed_Dal'),
                               chicken_curry_Grams=session.get('chicken_curry_Grams'),
                               chicken_protien=session.get('chicken_protien'),
                               caloriesConsumed_chicken=session.get('caloriesConsumed_chicken'),
                               mutton_curry_Grams=session.get('mutton_curry_Grams'),
                               mutton_protien=session.get('mutton_protien'),
                               caloriesConsumed_mutton=session.get('caloriesConsumed_mutton'),
                               sambar_rice_Grams=session.get('sambar_rice_Grams'),
                               caloriesConsumed_sambar=session.get('caloriesConsumed_sambar'),
                               Potato_curry_grams=session.get('Potato_curry_grams'),
                               caloriesConsumed_Potato=session.get('caloriesConsumed_Potato'),
                               Paneer_curry_grams=session.get('Paneer_curry_grams'),
                               protien_Paneer=session.get('protien_Paneer'),
                               caloriesConsumed_Paneer=session.get('caloriesConsumed_Paneer'),
                               mushroom_curry_grams=session.get('mushroom_curry_grams'),
                               caloriesConsumed_mushroom=session.get('caloriesConsumed_mushroom'),
                               fish_curry=session.get('fish_curry'),
                               fish_protien=session.get('fish_protien'),
                               caloriesConsumed_fish=session.get('caloriesConsumed_fish'),
                               prawns_curry_grams=session.get('prawns_curry_grams'),
                               caloriesConsumed_prawns=session.get('caloriesConsumed_prawns'),
                               curd_rice_grams=session.get('curd_rice_grams'),
                               caloriesConsumed_curd=session.get('caloriesConsumed_curd'))
    session.clear()
    return render_template('lunch.html')
@app.route('/snacks', methods=['GET', 'POST'])
def snacks():
    if request.method == 'POST':
        if 'samosa' in request.form:
            samosa = int(request.form['samosa'])
            caloriesConsumed_samosa=samosa*262
            session['samosa']=samosa
            session['caloriesConsumed_samosa']=caloriesConsumed_samosa
        elif 'Noodles_grams' in request.form:
            Noodles_grams = int(request.form['Noodles_grams'])
            caloriesConsumed_Noodles=Noodles_grams*1.38
            session['Noodles_grams']=Noodles_grams
            session['caloriesConsumed_Noodles']=caloriesConsumed_Noodles
        elif 'chat_grams' in request.form:
            chat_grams = int(request.form['chat_grams'])
            caloriesConsumed_chat=chat_grams*3.17
            session['chat_grams']=chat_grams
            session['caloriesConsumed_chat']=caloriesConsumed_chat
        elif 'mirchi_bajji' in request.form:
            mirchi_bajji = int(request.form['mirchi_bajji'])
            caloriesConsumed_mirchi=mirchi_bajji*160
            session['mirchi_bajji']=mirchi_bajji
            session['caloriesConsumed_mirchi']=caloriesConsumed_mirchi
        elif 'pani_puri' in request.form:
            pani_puri = int(request.form['pani_puri'])
            caloriesConsumed_pani_puri=pani_puri*36
            session['pani_puri']=pani_puri
            session['caloriesConsumed_pani_puri']=caloriesConsumed_pani_puri
        elif 'sandwhich' in request.form:
            sandwhich = int(request.form['sandwhich'])
            caloriesConsumed_sandwhich=sandwhich*252
            session['sandwhich']=sandwhich
            session['caloriesConsumed_sandwhich']=caloriesConsumed_sandwhich
        elif 'puffs' in request.form:
            puffs = int(request.form['puffs'])
            caloriesConsumed_puffs=puffs*85
            session['puffs']=puffs
            session['caloriesConsumed_puffs']=caloriesConsumed_puffs
        elif 'coffee' in request.form:
            coffee = int(request.form['coffee'])
            caloriesConsumed_coffee=coffee*40
            session['coffee']=coffee
            session['caloriesConsumed_coffee']=caloriesConsumed_coffee
        elif 'Tea' in request.form:
            Tea = int(request.form['Tea'])
            caloriesConsumed_Tea=Tea*92
            session['Tea']=Tea
            session['caloriesConsumed_Tea']=caloriesConsumed_Tea
        elif 'milk' in request.form:
            milk = int(request.form['milk'])
            caloriesConsumed_milk=milk*382
            session['milk']=milk
            session['caloriesConsumed_milk']=caloriesConsumed_milk
        return render_template('snacks.html',
                               samosa=session.get('samosa'),
                               caloriesConsumed_samosa=session.get('caloriesConsumed_samosa'),
                               Noodles_grams=session.get('Noodles_grams'),
                               caloriesConsumed_Noodles=session.get('caloriesConsumed_Noodles'),
                               chat_grams=session.get('chat_grams'),
                               caloriesConsumed_chat=session.get('caloriesConsumed_chat'),
                               mirchi_bajji=session.get('mirchi_bajji'),
                               caloriesConsumed_mirchi=session.get('caloriesConsumed_mirchi'),
                               pani_puri=session.get('pani_puri'),
                               caloriesConsumed_pani_puri=session.get('caloriesConsumed_pani_puri'),
                               sandwhich=session.get('sandwhich'),
                               caloriesConsumed_sandwhich=session.get('caloriesConsumed_sandwhich'),
                               puffs=session.get('puffs'),
                               caloriesConsumed_puffs=session.get('caloriesConsumed_puffs'),
                               coffee=session.get('coffee'),
                               caloriesConsumed_coffee=session.get('caloriesConsumed_coffee'),
                               Tea=session.get('Tea'),
                               caloriesConsumed_Tea=session.get('caloriesConsumed_Tea'),
                               milk=session.get('milk'),
                               caloriesConsumed_milk=session.get('caloriesConsumed_milk'))
    session.clear()
    return render_template('snacks.html')
@app.route('/sports', methods=['GET', 'POST'])
def sports():
    if request.method == 'POST':
        if 'weight_badmintion' in request.form:
            weight_badmintion = int(request.form['weight_badmintion'])
            minutes_badmintion = int(request.form['minutes_badmintion'])
            caloriesConsumed_badmintion=calories_badmintion(weight_badmintion,minutes_badmintion)
            session['weight_badmintion']=weight_badmintion
            session['minutes_badmintion']=minutes_badmintion
            session['caloriesConsumed_badmintion']=caloriesConsumed_badmintion
        if 'weight_run' in request.form:
            weight_run = int(request.form['weight_run'])
            speed = int(request.form['speed'])
            minutes_run = int(request.form['minutes_run'])
            caloriesConsumed_run = calories_run(weight_run, speed,minutes_run)
            session['weight_run'] = weight_run
            session['speed'] = speed
            session['minutes_run'] = minutes_run
            session['caloriesConsumed_run'] = caloriesConsumed_run
        if 'weight_swim' in request.form:
            weight_swim = int(request.form['weight_swim'])
            minutes_swim = int(request.form['minutes_swim'])
            caloriesConsumed_swim = calories_swim(weight_swim, minutes_swim)
            session['weight_swim'] = weight_swim
            session['minutes_swim'] = minutes_swim
            session['caloriesConsumed_swim'] = caloriesConsumed_swim
        if 'weight_cycle' in request.form:
            weight_cycle = int(request.form['weight_cycle'])
            minutes_cycle = int(request.form['minutes_cycle'])
            caloriesConsumed_cycle = calories_cycle(weight_cycle, minutes_cycle)
            session['weight_cycle'] = weight_cycle
            session['minutes_cycle'] = minutes_cycle
            session['caloriesConsumed_cycle'] = caloriesConsumed_cycle
        if 'weight_boxing' in request.form:
            weight_boxing = int(request.form['weight_boxing'])
            minutes_boxing = int(request.form['minutes_boxing'])
            caloriesConsumed_boxing = calories_boxing(weight_boxing, minutes_boxing)
            session['weight_boxing'] = weight_boxing
            session['minutes_boxing'] = minutes_boxing
            session['caloriesConsumed_boxing'] = caloriesConsumed_boxing
        return render_template('sports.html',
                               weight_badmintion=session.get('weight_badmintion'),
                               minutes_badmintion=session.get('minutes_badmintion'),
                               caloriesConsumed_badmintion=session.get('caloriesConsumed_badmintion'),
                               weight_run=session.get('weight_run'),
                               speed=session.get('speed'),
                               minutes_run=session.get('minutes_run'),
                               caloriesConsumed_run=session.get('caloriesConsumed_run'),
                               weight_swim=session.get('weight_swim'),
                               minutes_swim=session.get('minutes_swim'),
                               caloriesConsumed_swim=session.get('caloriesConsumed_swim'),
                               weight_cycle=session.get('weight_cycle'),
                               minutes_cycle=session.get('minutes_cycle'),
                               caloriesConsumed_cycle=session.get('caloriesConsumed_cycle'),
                               weight_boxing=session.get('weight_boxing'),
                               minutes_boxing=session.get('minutes_boxing'),
                               caloriesConsumed_boxing=session.get('caloriesConsumed_boxing')
                               )

    session.clear()
    return render_template('sports.html')
if __name__ == '__main__':
    app.run(debug=True)




