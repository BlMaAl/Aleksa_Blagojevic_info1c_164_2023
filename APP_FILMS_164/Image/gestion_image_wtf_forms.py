"""
    Fichier : gestion_genres_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, NumberRange, DataRequired
from wtforms.validators import Regexp
from wtforms.widgets import TextArea


class AjouterImage(FlaskForm):
    """
        Dans le formulaire "image_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    question_user_wtf = StringField("Nom de la question ", validators=[Length(min=2, max=2000, message="min 2 max 20")
                                                                       ])
    question_image_user_wtf = StringField("Image de la question ", widget=TextArea())

    reponse_user_wtf = StringField("Nom de la réponse ", validators=[Length(min=2, max=2000, message="min 2 max 20")
                                                                ])
    reponse_image_user_wtf = StringField("Image de la réponse ", widget=TextArea())

    date_user_wtf = DateField("Date de sortie du film", validators=[InputRequired("Date obligatoire"),
                                                                                 DataRequired("Date non valide")])

    submit = SubmitField("Enregistrer la question")


class UpdateImage(FlaskForm):
    """
        Dans le formulaire "image_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    question_user_update_wtf = StringField("Nom de la question ", validators=[Length(min=2, max=2000, message="min 2 max 20")
                                                                       ])
    question_image_user_update_wtf = StringField("Image de la question ", widget=TextArea())

    reponse_user_update_wtf = StringField("Nom de la réponse ", validators=[Length(min=2, max=2000, message="min 2 max 20")
                                                                     ])
    reponse_image_user_update_wtf = StringField("Image de la réponse ", widget=TextArea())

    date_user_update_wtf = DateField("Date de sortie du film", validators=[InputRequired("Date obligatoire"),
                                                                                 DataRequired("Date non valide")])
    submit = SubmitField("Update film")


class DeleteImage(FlaskForm):
    """
        Dans le formulaire "image_delete_wtf.html"

        nom_genre_delete_wtf : Champ qui reçoit la valeur du genre, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "genre".
        submit_btn_annuler : Bouton qui permet d'afficher la table "utilisateur".
    """
    question_user_delete_wtf = StringField("Effacer la question")
    question_image_user_delete_wtf = StringField("Effacer l'image de la question")
    reponse_user_delete_wtf = StringField("Effacer la réponse")
    reponse_image_user_delete_wtf = StringField("Effacer l'image de la réponse")
    date_user_delete_wtf = StringField("Effacer la date")
    submit_btn_conf_del = SubmitField("Effacer la question/réponse")
    submit_btn_del = SubmitField("Confirmer la suppression")
    submit_btn_annuler = SubmitField("Annuler")
