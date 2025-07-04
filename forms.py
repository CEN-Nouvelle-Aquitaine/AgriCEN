from flask_wtf import FlaskForm
from wtforms import (
    StringField, DecimalField, DateField, HiddenField, TextAreaField, 
    IntegerField, SubmitField, SelectField, SelectMultipleField, RadioField
)
from wtforms.validators import DataRequired, Optional, NumberRange, Length

class CombinedForm(FlaskForm):

    # Champs Contrat
    surf_contractualisee = DecimalField(
        'Surface contractualisée (ha)', 
        validators=[
            DataRequired(), 
            NumberRange(min=0.1, max=100, message="La surface contractualisée doit être comprise entre 0.1 et 100 hectares.")
        ]
    )
    date_signature = DateField('Date de signature', validators=[DataRequired()])
    date_fin = DateField('Date de fin', validators=[DataRequired()])
    date_prise_effet = DateField('Date de prise d\'effet', validators=[DataRequired()])
    latitude = HiddenField('Latitude', validators=[Optional()])
    longitude = HiddenField('Longitude', validators=[Optional()])

    # Champs type_contrat
    appellation_contrat = SelectField(
        'Type de contrat', 
        choices=[],  # Les choix seront définis dynamiquement
        validators=[DataRequired()],
        coerce=int  # Convertit les données soumises en `int` automatiquement
    )
    

    # Champs Société
    nom_societe = StringField('Nom de la société', validators=[DataRequired(), Length(max=100)])
    contact = StringField('Contact', validators=[DataRequired(), Length(max=100)])
    remarques = TextAreaField('Remarques', validators=[Optional(), Length(max=300)])

    # Champs Agriculteur
    nom_agri = StringField("Nom de l'exploitant(e)", validators=[DataRequired(), Length(max=100)])
    prenom_agri = StringField("Prénom de l'exploitant(e)", validators=[DataRequired(), Length(max=50)])
    date_naissance = DateField('Date de naissance', validators=[Optional()])

    # Champs Site CEN
    nom_site = StringField('Site(s) CEN concerné(s)',validators=[DataRequired(), Length(max=100)], render_kw={"placeholder": "Saisissez le nom d'un site", "style": "background-color: #e9ecef; color: #6c757d;"})
    code_site = StringField('Code(s) site(s)', validators=[DataRequired()], render_kw={"readonly": True, "style": "background-color: #e9ecef; color: #6c757d;"})

    # Champs pour Type de Milieu
    type_milieu = SelectMultipleField(
        'Types de milieu',
        choices=[],  # Les choix seront définis dynamiquement
        validators=[DataRequired()],
        coerce=int  # Convertit les données soumises en `int` automatiquement
    )


    # Champs pour Type de Production
    type_production = SelectMultipleField(
        'Types de production', 
        choices=[],  # Les choix seront définis dynamiquement
        validators=[DataRequired()], #Essayer de trouver un validateur personnalisé pour SelectMultipleField car lorsqu'aucune valeur n'est sélectionnée, le champ renvoie une liste vide ([]) et DataRequired() ne considère pas une liste vide comme une valeur invalide, donc la validation passe silencieusement.
        coerce=int  # Convertit les données soumises en `int` automatiquement
    )

    mode_production = SelectField(
        'Mode de production',
        choices=[],  # Les choix seront définis dynamiquement
        validators=[DataRequired()],
        coerce=int  # Convertit les données soumises en int automatiquement
    )
    
    # Champs pour Produits Finis
    produit_fini = SelectMultipleField(
        'Produits finis', 
        choices=[],  # Les choix seront définis dynamiquement
        validators=[DataRequired()],
        coerce=int  # Convertit les données soumises en `int` automatiquement
    )

    # Champs pour Referent
    nom_referent = StringField('Nom de la personne référente', validators=[DataRequired(), Length(max=100)])
    prenom_referent = StringField('Prénom de la personne référente', validators=[DataRequired(), Length(max=50)])


    siret = StringField(
        "Numéro SIRET",
        validators=[
            DataRequired(message="Le numéro SIRET est requis."),
            Length(min=14, max=14, message="Le numéro SIRET doit contenir exactement 14 chiffres.")
        ]
    )
    adresse_etablissement = StringField(
        "Adresse complète de l'établissement",
        validators=[Optional(), Length(max=200)]
    )
    tranche_effectif = StringField(
        "Tranche d'effectif salarié de l'établissement",
        validators=[Optional(), Length(max=50)]
    )
    categorie_juridique = StringField(
        "Catégorie juridique",
        validators=[Optional(), Length(max=100)]
    )
    activite_principale = StringField(
        "Activité principale",
        validators=[Optional(), Length(max=100)]
    )

    fetch_sirene = SubmitField('Rechercher via l''API de l''INSEE')
    submit = SubmitField('Enregistrer les données')