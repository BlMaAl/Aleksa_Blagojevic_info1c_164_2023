"""
    Fichier : gestion_genres_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp


class AjouterUtilisateur(FlaskForm):
    """
        Dans le formulaire "image_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_user_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    prenom_genre_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"

    nom_user_wtf = StringField("Mettre le nom ", validators=[Length(min=2, max=100, message="min 2 max 100"),
                                                                   Regexp(nom_user_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])
    prenom_user_wtf = StringField("Mettre le prenom", validators=[Length(min=2, max=100, message="min 2 max 100"),
                                            Regexp(prenom_genre_regexp,
                                                   message="Pas de chiffres, de caractères "
                                                           "spéciaux, "
                                                           "d'espace à double, de double "
                                                           "apostrophe, de double trait union")
                                            ])

    submit = SubmitField("Enregistrer texte")


class FormWTFUpdateGenre(FlaskForm):
    """
        Dans le formulaire "image_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_user_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    prenom_user_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    
    nom_user_update_wtf = StringField("Mettre le texte à convertire ", validators=[Length(min=2, max=100, message="min 2 max 100"),
                                                                          Regexp(nom_user_update_regexp,
                                                                                 message="Pas de chiffres, de "
                                                                                         "caractères "
                                                                                         "spéciaux, "
                                                                                         "d'espace à double, de double "
                                                                                         "apostrophe, de double trait "
                                                                                         "union")
                                                                          ])
    prenom_user_update_wtf = StringField("Mettre le texte à convertire ", validators=[Length(min=2, max=100, message="min 2 max 100"),
                                                                           Regexp(prenom_user_update_regexp,
                                                                                  message="Pas de chiffres, de "
                                                                                          "caractères "
                                                                                          "spéciaux, "
                                                                                          "d'espace à double, de double "
                                                                                          "apostrophe, de double trait "
                                                                                          "union")
                                                                           ])
    date_genre_wtf_essai = DateField("Essai date", validators=[InputRequired("Date obligatoire"),
                                                               DataRequired("Date non valide")])
    submit = SubmitField("Update genre")


class FormWTFDeleteGenre(FlaskForm):
    """
        Dans le formulaire "image_delete_wtf.html"

        nom_genre_delete_wtf : Champ qui reçoit la valeur du genre, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "genre".
        submit_btn_annuler : Bouton qui permet d'afficher la table "utilisateur".
    """
    nom_genre_delete_wtf = StringField("Effacer ce genre")
    submit_btn_del = SubmitField("Effacer genre")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
