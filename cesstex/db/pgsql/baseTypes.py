# -*- coding: utf-8 -*-
"""
cesstex.db.pgsql

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl

$Id: baseTypes.py 5772 2009-05-20 15:59:55Z schminitz $
"""
from z3c.sqlalchemy.mapper import MappedClassBase


class EtatPublication(MappedClassBase):
    c = None


class StatutMembre(MappedClassBase):
    c = None


class Professeur(MappedClassBase):
    c = None


class Etudiant(MappedClassBase):
    c = None


class DossierDisciplinaire(MappedClassBase):
    c = None


class EvenementActe(MappedClassBase):
    c = None


class EvenementActeDocument(MappedClassBase):
    c = None


class EvenementActeLogModification(MappedClassBase):
    c = None


class LogOperation(MappedClassBase):
    c = None
