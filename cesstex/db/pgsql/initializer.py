from z3c.sqlalchemy import Model
from z3c.sqlalchemy.interfaces import IModelProvider
from zope.interface import implements

from sqlalchemy import desc
from sqlalchemy.orm import mapper, relationship


from cesstex.db.pgsql.baseTypes import (EtatPublication, StatutMembre,
                                        Professeur, Etudiant, DossierDisciplinaire,
                                        EvenementActe, EvenementActeLogModification)

from cesstex.db.pgsql.tables import (getEtatPublication, getStatutMembre,
                                     getProfesseur, getEtudiant, getDossierDisciplinaire,
                                     getEvenementActe, getEvenementActeLogModification)


class CesstexModel(object):
    """
    A model providers provides information about the tables to be used
    and the mapper classes.
    """
    implements(IModelProvider)

    def getModel(self, metadata=None):
        """
        cesstex
        """
        model = Model()
        model.metadata = metadata

        etatPublicationTable = getEtatPublication(metadata)
        etatPublicationTable.create(checkfirst=True)

        statutMembreTable = getStatutMembre(metadata)
        statutMembreTable.create(checkfirst=True)

        professeurTable = getProfesseur(metadata)
        professeurTable.create(checkfirst=True)

        etudiantTable = getEtudiant(metadata)
        etudiantTable.create(checkfirst=True)

        dossierDisciplinaireTable = getDossierDisciplinaire(metadata)
        dossierDisciplinaireTable.create(checkfirst=True)

        evenementActeTable = getEvenementActe(metadata)
        evenementActeTable.create(checkfirst=True)

        evenementActeLogModificationTable = getEvenementActeLogModification(metadata)
        evenementActeLogModificationTable.create(checkfirst=True)

        mapper(EtatPublication, etatPublicationTable)

        mapper(StatutMembre, statutMembreTable)

        mapper(Professeur, professeurTable,
               properties={'statut': relationship(StatutMembre)})

        mapper(Etudiant, etudiantTable,
               properties={'titulaire01': relationship(Professeur,
                                          primaryjoin=(etudiantTable.c.eleve_prof_titulaire_01_fk == professeurTable.c.prof_pk),
                                          order_by=[etudiantTable.c.eleve_nom]),
                           'titulaire02': relationship(Professeur,
                                          primaryjoin=(etudiantTable.c.eleve_prof_titulaire_02_fk == professeurTable.c.prof_pk)),
                           'educateurReferent': relationship(Professeur,
                                                primaryjoin=(etudiantTable.c.eleve_educateur_referent_fk == professeurTable.c.prof_pk),
                                                order_by=[etudiantTable.c.eleve_nom])})

        mapper(DossierDisciplinaire, dossierDisciplinaireTable,
               properties={'student': relationship(Etudiant),
                           'auteur': relationship(Professeur)})

        mapper(EvenementActe, evenementActeTable,
               properties={'etat': relationship(EtatPublication,
                                   primaryjoin=(evenementActeTable.c.eventact_etat_publication_fk == etatPublicationTable.c.etat_pk),
                                   order_by=[etatPublicationTable.c.etat_titre]),
                           'dossier': relationship(DossierDisciplinaire,
                                      primaryjoin=(evenementActeTable.c.eventact_dossier_diciplinaire_fk == dossierDisciplinaireTable.c.dosdis_pk),
                                      order_by=[desc(dossierDisciplinaireTable.c.dosdis_date_creation)])})

        mapper(EvenementActeLogModification, evenementActeLogModificationTable,
               properties={'logmodif': relationship(EvenementActe,
                                       primaryjoin=(evenementActeLogModificationTable.c.eventactlogmodif_evenement_acte_fk == evenementActeTable.c.eventact_pk),
                                       order_by=[evenementActeLogModificationTable.c.eventactlogmodif_date_modification])})

        metadata.create_all()
        return model
