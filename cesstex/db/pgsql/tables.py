# -*- coding: utf-8 -*-

from sqlalchemy import (Table, Column, Integer, Text, Sequence,
                        func, DateTime, Boolean, ForeignKey)


def getEtatPublication(metadata):
    autoload = False
    if metadata.bind.has_table('etat_publication'):
        autoload = True
    return Table('etat_publication', metadata,
                 Column('etat_pk', Integer(),
                        Sequence('etat_publication_etat_pk_seq'),
                        primary_key=True),
                 Column('etat_titre', Text()),
                 autoload=autoload,
                 extend_existing=True)


def getStatutMembre(metadata):
    autoload = False
    if metadata.bind.has_table('statut_membre'):
        autoload = True
    return Table('statut_membre', metadata,
                 Column('statmembre_pk', Integer(),
                        Sequence('statut_membre_statmembre_pk_seq'),
                        primary_key=True),
                 Column('statmembre_statut', Text()),
                 autoload=autoload,
                 extend_existing=True)


def getEcole(metadata):
    autoload = False
    if metadata.bind.has_table('ecole'):
        autoload = True
    return Table('ecole', metadata,
                 Column('ecole_pk', Integer(),
                        Sequence('ecole_ecole_pk_seq'),
                        primary_key=True),
                 Column('ecole_nom', Text()),
                 autoload=autoload,
                 extend_existing=True)


def getImplantation(metadata):
    autoload = False
    if metadata.bind.has_table('implantation'):
        autoload = True
    return Table('implantation', metadata,
                 Column('implantation_pk', Integer(),
                        Sequence('implantation_implantation_pk_seq'),
                        primary_key=True),
                 Column('implantation_nom', Text()),
                 Column('implantation_adresse', Text()),
                 Column('implantation_code_postal', Text()),
                 Column('implantation_localite', Text()),
                 autoload=autoload,
                 extend_existing=True)


def getClasseIsm(metadata):
    autoload = False
    if metadata.bind.has_table('classe_ism'):
        autoload = True
    return Table('classe_ism', metadata,
                 Column('classeism_pk', Integer(),
                        Sequence('classe_ism_classeism_pk_seq'),
                        primary_key=True),
                 Column('classeism_nom', Text()),
                 Column('classeism_titulaire_01_fk', Integer(),
                        ForeignKey('professeur.prof_pk')),
                 Column('classeism_titulaire_02_fk', Integer(),
                        ForeignKey('professeur.prof_pk')),
                 autoload=autoload,
                 extend_existing=True)


def getEleveIsm(metadata):
    autoload = False
    if metadata.bind.has_table('eleve_ism'):
        autoload = True
    return Table('eleve_ism', metadata,
                 Column('eleveism_pk', Integer(),
                        Sequence('eleve_ism_eleveism_pk_seq'),
                        primary_key=True),
                 Column('eleveism_nom', Text()),
                 Column('eleveism_prenom', Text()),
                 Column('eleveism_login', Text()),
                 Column('eleveism_pass', Text()),
                 Column('eleveism_email', Text()),
                 Column('eleveism_classe_fk', Integer(),
                        ForeignKey('classe_ism.classeism_pk')),
                 autoload=autoload,
                 extend_existing=True)


def getProfesseur(metadata):
    autoload = False
    if metadata.bind.has_table('professeur'):
        autoload = True
    return Table('professeur', metadata,
                 Column('prof_pk', Integer(),
                        Sequence('professeur_prof_pk_seq'),
                        primary_key=True),
                 Column('prof_nom', Text()),
                 Column('prof_prenom', Text()),
                 Column('prof_email', Text()),
                 Column('prof_login', Text()),
                 Column('prof_pass', Text()),
                 Column('prof_email_id', Text()),
                 Column('prof_actif', Boolean(), default=True),
                 Column('prof_statut_fk', Integer(),
                        ForeignKey('statut_membre.statmembre_pk')),
                 Column('prof_ecole_fk', Integer(),
                        ForeignKey('ecole.ecole_pk')),
                 autoload=autoload,
                 extend_existing=True)


def getEleveDossierDisciplinaire(metadata):
    autoload = False
    if metadata.bind.has_table('eleve_dossier_disciplinaire'):
        autoload = True
    return Table('eleve_dossier_disciplinaire', metadata,
                 Column('eleve_pk', Integer(),
                        Sequence('eleve_dossier_disciplinaire_eleve_pk_seq'),
                        primary_key=True),
                 Column('eleve_nom', Text()),
                 Column('eleve_prenom', Text()),
                 Column('eleve_classe', Text()),
                 Column('eleve_prof_titulaire_01_fk', Integer(),
                        ForeignKey('professeur.prof_pk')),
                 Column('eleve_prof_titulaire_02_fk', Integer(),
                        ForeignKey('professeur.prof_pk')),
                 Column('eleve_educateur_referent_fk', Integer(),
                        ForeignKey('professeur.prof_pk')),
                 autoload=autoload,
                 extend_existing=True)


def getDossierDisciplinaire(metadata):
    autoload = False
    if metadata.bind.has_table('dossier_disciplinaire'):
        autoload = True
    return Table('dossier_disciplinaire', metadata,
                 Column('dosdis_pk', Integer(),
                        Sequence('dossier_disciplinaire_dosdis_pk_seq'),
                        primary_key=True),
                 Column('dosdis_id', Text()),
                 Column('dosdis_date_creation', DateTime(), default=func.now()),
                 Column('dosdis_annee_scolaire', Integer()),
                 Column('dosdis_actif', Boolean(), default=True),
                 Column('dosdis_eleve_fk', Integer(),
                        ForeignKey('eleve_dossier_disciplinaire.eleve_pk')),
                 Column('dosdis_auteur_fk', Integer(),
                        ForeignKey('professeur.prof_pk')),
                 autoload=autoload,
                 extend_existing=True)


def getEvenementActe(metadata):
    autoload = False
    if metadata.bind.has_table('evenement_acte'):
        autoload = True
    return Table('evenement_acte', metadata,
                 Column('eventact_pk', Integer(),
                        Sequence('evenement_acte_eventact_pk_seq'),
                        primary_key=True),
                 Column('eventact_date_creation', DateTime(), default=func.now()),
                 Column('eventact_auteur_creation', Text()),
                 Column('eventact_evenement', Text()),
                 Column('eventact_sanction', Text()),
                 Column('eventact_document_attache', Boolean(), default=False),
                 Column('eventact_intervenant', Text()),
                 Column('eventact_numero_ordre', Integer()),
                 Column('eventact_auteur_creation_fk', Integer(),
                        ForeignKey('professeur.prof_pk')),
                 Column('eventact_etat_publication_fk', Integer(),
                        ForeignKey('etat_publication.etat_pk')),
                 Column('eventact_dossier_diciplinaire_fk', Integer(),
                        ForeignKey('dossier_disciplinaire.dosdis_pk')),
                 autoload=autoload,
                 extend_existing=True)


def getEvenementActeDocument(metadata):
    autoload = False
    if metadata.bind.has_table('evenement_acte_document'):
        autoload = True
    return Table('evenement_acte_document', metadata,
                 Column('eventactdoc_pk', Integer(),
                        primary_key=True),
                 Column('eventactdoc_date_creation', DateTime(), default=func.now()),
                 Column('eventactdoc_nom_fichier', Text()),
                 Column('eventactdoc_auteur_creation_fk', Integer(),
                        ForeignKey('professeur.prof_pk')),
                 Column('eventactdoc_eventact_fk', Integer(),
                        ForeignKey('evenement_acte.eventact_pk')),
                 Column('eventactdoc_dossier_disciplinaire_fk', Integer(),
                        ForeignKey('dossier_disciplinaire.dosdis_pk')),
                 autoload=autoload,
                 extend_existing=True)


def getEvenementActeLogModification(metadata):
    autoload = False
    if metadata.bind.has_table('evenement_acte_log_modification'):
        autoload = True
    return Table('evenement_acte_log_modification', metadata,
                 Column('eventactlogmodif_pk', Integer(),
                        Sequence('evenement_acte_log_modification_eventactlogmodif_pk_seq'),
                        primary_key=True),
                 Column('eventactlogmodif_date_modification', DateTime(), default=func.now()),
                 Column('eventactlogmodif_auteur_modification', Text()),
                 Column('eventactlogmodif_evenement_acte_fk', Integer(),
                        ForeignKey('evenement_acte.eventact_pk')),
                 autoload=autoload,
                 extend_existing=True)


def getLogOperation(metadata):
    autoload = False
    if metadata.bind.has_table('log_operation'):
        autoload = True
    return Table('log_operation', metadata,
                 Column('logoperation_pk', Integer(),
                        Sequence('log_operation_log_operation_pk_seq'),
                        primary_key=True),
                 Column('logoperation_date', DateTime(), default=func.now()),
                 Column('logoperation_auteur', Text()),
                 Column('logoperation_type_operation', Text()),
                 Column('logoperation_auteur_fk', Integer()),
                 Column('logoperation_dosdis_fk', Integer()),
                 Column('logoperation_evenement_acte_fk', Integer()),
                 autoload=autoload,
                 extend_existing=True)
