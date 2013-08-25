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
                 Column('prof_statut', Integer(),
                         ForeignKey('statut_membre.statmembre_pk')),
                 autoload=autoload,
                 extend_existing=True)


def getEtudiant(metadata):
    autoload = False
    if metadata.bind.has_table('etudiant'):
        autoload = True
    return Table('etudiant', metadata,
                 Column('eleve_pk', Integer(),
                        Sequence('etudiant_eleve_pk_seq'),
                        primary_key=True),
                 Column('eleve_nom', Text()),
                 Column('eleve_prenom', Text()),
                 Column('eleve_classe', Text()),
                 Column('eleve_prof_titulaire_01_fk', Integer(),
                         ForeignKey('professeur.prof_pk')),
                 Column('eleve_prof_titulaire_02_fk', Integer(),
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
                         ForeignKey('etudiant.eleve_pk')),
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
                 Column('eventact_evenement', Text()),
                 Column('eventact_sanction', Text()),
                 Column('eventact_document_attache', Boolean(), default=False),
                 Column('eventact_intervenant', Text()),
                 Column('eventact_etat_publication_fk', Integer(),
                         ForeignKey('etat_publication.etat_pk')),
                 Column('eventact_dossier_diciplinaire_fk', Integer(),
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
                 Column('eventactlogmodif_auteur', Text()),
                 Column('eventactlogmodif_evenement_acte_fk', Integer(),
                         ForeignKey('evenement_acte.eventact_pk')),
                 autoload=autoload,
                 extend_existing=True)
