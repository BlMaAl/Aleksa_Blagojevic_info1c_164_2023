"""Gestion des "routes" FLASK et des données pour les genres.
Fichier : gestion_genres_crud.py
Auteur : OM 2021.03.16
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.Image.gestion_image_wtf_forms import AjouterImage
from APP_FILMS_164.Image.gestion_image_wtf_forms import DeleteImage
from APP_FILMS_164.Image.gestion_image_wtf_forms import UpdateImage

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /image_afficher
    
    Test : ex : http://127.0.0.1:5575/image_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_image_sel = 0 >> tous les genres.
                id_image_sel = "n" affiche le genre dont l'id est "n"
"""


@app.route("/image_afficher/<string:order_by>/<int:id_image_sel>", methods=['GET', 'POST'])
def image_afficher(order_by, id_image_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_image_sel == 0:
                    strsql_genres_afficher = """SELECT id_question_reponse, question, question_image, reponse, reponse_image, date FROM t_question_reponse ORDER BY id_question_reponse ASC"""
                    mc_afficher.execute(strsql_genres_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_utilisateurs"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du genre sélectionné avec un nom de variable
                    valeur_id_user_selected_dictionnaire = {"value_id_user_selected": id_image_sel}
                    strsql_genres_afficher = """SELECT id_question_reponse, question, question_image, reponse, reponse_image, date FROM t_question_reponse WHERE id_question_reponse = %(value_id_user_selected)s"""

                    mc_afficher.execute(strsql_genres_afficher, valeur_id_user_selected_dictionnaire)
                else:
                    strsql_genres_afficher = """SELECT id_question_reponse, question, question_image, reponse, reponse_image, date FROM t_question_reponse ORDER BY id_question_reponse DESC"""

                    mc_afficher.execute(strsql_genres_afficher)

                data_genres = mc_afficher.fetchall()

                print("data_genres ", data_genres, " Type : ", type(data_genres))

                # Différencier les messages si la table est vide.
                if not data_genres and id_image_sel == 0:
                    flash("""La table "t_utilisateurs" est vide. !!""", "warning")
                elif not data_genres and id_image_sel > 0:
                    # Si l'utilisateur change l'id_utilisateur dans l'URL et que le genre n'existe pas,
                    flash(f"Le genre demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "utilisateur" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données textes affichés !!", "success")

        except Exception as Exception_genres_afficher:
            raise ExceptionGenresAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{image_afficher.__name__} ; "
                                          f"{Exception_genres_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("Image/image_afficher.html", data=data_genres)


"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /genres_ajouter
    
    Test : ex : http://127.0.0.1:5575/genres_ajouter
    
    Paramètres : sans
    
    But : Ajouter un genre pour un film
    
    Remarque :  Dans le champ "name_genre_html" du formulaire "Image/genres_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/image_ajouter_wtf", methods=['GET', 'POST'])
def image_ajouter_wtf():
    form = AjouterImage()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                question_user_wtf = form.question_user_wtf.data
                question_image_user_wtf = form.question_image_user_wtf.data
                reponse_user_wtf = form.reponse_user_wtf.data
                reponse_image_user_wtf = form.reponse_image_user_wtf.data
                date_user_wtf = form.date_user_wtf.data


                valeurs_insertion_dictionnaire = {"value_question_user": question_user_wtf,
                                                  "value_question_image_user": question_image_user_wtf,
                                                  "value_reponse_user": reponse_user_wtf,
                                                  "value_reponse_image_user": reponse_image_user_wtf,
                                                  "value_date_user": date_user_wtf
                                                  }
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_inserutilisateur = """INSERT INTO t_question_reponse (id_question_reponse,question,question_image,reponse,reponse_image,date) 
                VALUES (NULL,%(value_question_user)s,%(value_question_image_user)s,%(value_reponse_user)s,%(value_reponse_image_user)s,%(value_date_user)s) """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_inserutilisateur, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('image_afficher', order_by='DESC', id_image_sel=0))

        except Exception as Exception_genres_ajouter_wtf:
            raise ExceptionGenresAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{image_ajouter_wtf.__name__} ; "
                                            f"{Exception_genres_ajouter_wtf}")

    return render_template("Image/image_ajouter_wtf.html", form=form)


"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /genre_update
    
    Test : ex cliquer sur le menu "genres" puis cliquer sur le bouton "EDIT" d'un "genre"
    
    Paramètres : sans
    
    But : Editer(update) un genre qui a été sélectionné dans le formulaire "image_afficher.html"
    
    Remarque :  Dans le champ "nom_user_update_wtf" du formulaire "Image/image_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/image_update_wtf", methods=['GET', 'POST'])
def image_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_utilisateur"
    id_image_update = request.values['id_image_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update = UpdateImage()
    try:
        print(" on submit ", form_update.validate_on_submit())
        if form_update.validate_on_submit():
            # Récupèrer la valeur du champ depuis "image_update_wtf.html" après avoir cliqué sur "SUBMIT".
            # Puis la convertir en lettres minuscules.

            question_user_update = form_update.question_user_update_wtf.data
            question_image_user_update = form_update.question_image_user_update_wtf.data
            reponse_user_update = form_update.reponse_user_update_wtf.data
            reponse_image_user_update = form_update.reponse_image_user_update_wtf.data
            date_user_update = form_update.date_user_update_wtf.data

            valeur_update_dictionnaire = {"value_id_image_update": id_image_update,
                                          "value_question_user_update": question_user_update,
                                          "value_question_image_user_update": question_image_user_update,
                                          "value_reponse_user_update": reponse_user_update,
                                          "value_reponse_image_user_update": reponse_image_user_update,
                                          "value_date_user_update": date_user_update
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_image = """UPDATE t_question_reponse SET question = %(value_question_user_update)s, 
            question_image = %(value_question_image_user_update)s, 
            reponse = %(value_reponse_user_update)s,
            reponse_image = %(value_reponse_image_user_update)s,
            date = %(value_date_user_update)s WHERE id_question_reponse = %(value_id_image_update)s ; """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_image, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Affiche seulement la valeur modifiée, "ASC" et l'"id_user_update"
            return redirect(url_for('image_afficher', order_by="ASC", id_image_sel=id_image_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_utilisateur" et "nom_utilisateur" de la "utilisateur"
            str_sql_id_user = "SELECT id_question_reponse,question,question_image,reponse,reponse_image,date FROM t_question_reponse " \
                               "WHERE id_question_reponse = %(value_id_image_update)s"
            valeur_select_dictionnaire = {"value_id_image_update": id_image_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_user, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom genre" pour l'UPDATE
            data_image = mybd_conn.fetchone()
            print("data_image ", data_image, " type ", type(data_image), " genre ",
                  data_image["question"])

            # Afficher la valeur sélectionnée dans les champs du formulaire "image_update_wtf.html"
            form_update.question_user_update_wtf.data = data_image["question"]
            form_update.question_image_user_update_wtf.data = data_image["question_image"]
            form_update.reponse_user_update_wtf.data = data_image["reponse"]
            form_update.reponse_image_user_update_wtf.data = data_image["reponse_image"]
            form_update.date_user_update_wtf.data = data_image["date"]

    except Exception as Exception_genre_update_wtf:
        raise ExceptionGenreUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{image_update_wtf.__name__} ; "
                                      f"{Exception_genre_update_wtf}")

    return render_template("Image/image_update_wtf.html", form_update=form_update)


"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /genre_delete
    
    Test : ex. cliquer sur le menu "genres" puis cliquer sur le bouton "DELETE" d'un "genre"
    
    Paramètres : sans
    
    But : Effacer(delete) un genre qui a été sélectionné dans le formulaire "image_afficher.html"
    
    Remarque :  Dans le champ "nom_genre_delete_wtf" du formulaire "Image/image_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/image_delete", methods=['GET', 'POST'])
def image_delete_wtf():
    data_films_attribue_genre_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_utilisateur"
    id_image_delete = request.values['id_image_btn_delete_html']

    # Objet formulaire pour effacer le genre sélectionné.
    form_delete = DeleteImage()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("image_afficher", order_by="ASC", id_image_sel=0))

            if form_delete.submit_btn_conf_del.data:
                # Récupère les données afin d'afficher à nouveau
                # le formulaire "Image/image_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                # data_films_attribue_genre_delete = session['data_films_attribue_genre_delete']
                # print("data_films_attribue_genre_delete ", data_films_attribue_genre_delete)

                flash(f"Effacer le genre de façon définitive de la BD !!!", "danger")
                # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
                # On affiche le bouton "Effacer genre" qui va irrémédiablement EFFACER le genre
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_image": id_image_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                # str_sql_delete_films_genre = """DELETE FROM utilisateur_film WHERE fk_genre = %(value_id_user)s"""
                str_sql_delete_image = """DELETE FROM t_question_reponse WHERE id_question_reponse = %(value_id_image)s"""
                # Manière brutale d'effacer d'abord la "fk_genre", même si elle n'existe pas dans la "utilisateur_film"
                # Ensuite on peut effacer le genre vu qu'il n'est plus "lié" (INNODB) dans la "utilisateur_film"
                with DBconnection() as mconn_bd:
                    # mconn_bd.execute(str_sql_delete_films_genre, valeur_delete_dictionnaire)
                    mconn_bd.execute(str_sql_delete_image, valeur_delete_dictionnaire)

                flash(f"Image définitivement effacé !!", "success")
                print(f"Image définitivement effacé !!")

                # afficher les données
                return redirect(url_for('image_afficher', order_by="ASC", id_image_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_image_delete": id_image_delete}
            print(id_image_delete, type(id_image_delete))

            # Requête qui affiche tous les films_genres qui ont le genre que l'utilisateur veut effacer
            str_sql_genres_films_delete = """SELECT id_user_film, nom_film, id_utilisateur, nom_utilisateur FROM utilisateur_film 
                                            INNER JOIN t_film ON utilisateur_film.fk_film = t_film.id_film
                                            INNER JOIN t_utilisateurs ON utilisateur_film.fk_genre = t_utilisateurs.id_utilisateur
                                            WHERE fk_genre = %(value_id_user)s"""

            with DBconnection() as mydb_conn:
                # mydb_conn.execute(str_sql_genres_films_delete, valeur_select_dictionnaire)
                # data_films_attribue_genre_delete = mydb_conn.fetchall()
                # print("data_films_attribue_genre_delete...", data_films_attribue_genre_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "Image/image_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                # session['data_films_attribue_genre_delete'] = data_films_attribue_genre_delete

                # Opération sur la BD pour récupérer "id_utilisateur" et "nom_utilisateur" de la "utilisateur"
                str_sql_id_image = "SELECT id_question_reponse, question, question_image, reponse, reponse_image, date FROM t_question_reponse WHERE id_question_reponse = %(value_id_image_delete)s"

                mydb_conn.execute(str_sql_id_image, valeur_select_dictionnaire)
                # Une seule valeur est suffisante "fetchone()",
                # vu qu'il n'y a qu'un seul champ "nom genre" pour l'action DELETE
                data_image = mydb_conn.fetchone()
                print("data_image ", data_image, " type ", type(data_image), " genre ",
                      data_image["question"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "image_delete_wtf.html"
            form_delete.question_user_delete_wtf.data = data_image["question"]
            form_delete.question_image_user_delete_wtf.data = data_image["question_image"]
            form_delete.reponse_user_delete_wtf.data = data_image["reponse"]
            form_delete.reponse_image_user_delete_wtf.data = data_image["reponse_image"]
            form_delete.date_user_delete_wtf.data = data_image["date"]

            # Le bouton pour l'action "DELETE" dans le form. "image_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_genre_delete_wtf:
        raise ExceptionGenreDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{image_delete_wtf.__name__} ; "
                                      f"{Exception_genre_delete_wtf}")

    return render_template("Image/image_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del)
