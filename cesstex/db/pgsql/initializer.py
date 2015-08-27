from z3c.sqlalchemy import Model
from z3c.sqlalchemy.interfaces import IModelProvider
from zope.interface import implements

from sqlalchemy import desc
from sqlalchemy.orm import mapper, relationship


from cesstex.db.pgsql.baseTypes import (EtatPublication,
                                        StatutMembre,
                                        Ecole,
                                        Implantation,
                                        Professeur,
                                        EleveDossierDisciplinaire,
                                        DossierDisciplinaire,
                                        EvenementActe,
                                        EvenementActeDocument,
                                        EvenementActeLogModification,
                                        LogOperation)

from cesstex.db.pgsql.tables import (getEtatPublication,
                                     getStatutMembre,
                                     getEcole,
                                     getImplantation,
                                     getProfesseur,
                                     getEleveDossierDisciplinaire,
                                     getDossierDisciplinaire,
                                     getEvenementActe,
                                     getEvenementActeDocument,
                                     getEvenementActeLogModification,
                                     getLogOperation)


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

        ecoleTable = getEcole(metadata)
        ecoleTable.create(checkfirst=True)

        implantationTable = getImplantation(metadata)
        implantationTable.create(checkfirst=True)

        professeurTable = getProfesseur(metadata)
        professeurTable.create(checkfirst=True)

        eleveDossierDisciplinaireTable = getEleveDossierDisciplinaire(metadata)
        eleveDossierDisciplinaireTable.create(checkfirst=True)

        dossierDisciplinaireTable = getDossierDisciplinaire(metadata)
        dossierDisciplinaireTable.create(checkfirst=True)

        evenementActeTable = getEvenementActe(metadata)
        evenementActeTable.create(checkfirst=True)

        evenementActeDocumentTable = getEvenementActeDocument(metadata)
        evenementActeDocumentTable.create(checkfirst=True)

        evenementActeLogModificationTable = getEvenementActeLogModification(metadata)
        evenementActeLogModificationTable.create(checkfirst=True)

        logOperationTable = getLogOperation(metadata)
        logOperationTable.create(checkfirst=True)

        mapper(EtatPublication, etatPublicationTable)

        mapper(StatutMembre, statutMembreTable)

        mapper(Ecole, ecoleTable)

        mapper(Implantation, implantationTable)

        mapper(DossierDisciplinaire, dossierDisciplinaireTable,
               properties={'student': relationship(EleveDossierDisciplinaire),
                           'auteur': relationship(Professeur)})

        mapper(Professeur, professeurTable,
               properties={'statut': relationship(StatutMembre,
                                     primaryjoin=(professeurTable.c.prof_statut_fk == statutMembreTable.c.statmembre_pk)),
                           'ecole': relationship(Ecole,
                                     primaryjoin=(professeurTable.c.prof_ecole_fk == ecoleTable.c.ecole_pk))})

        mapper(EleveDossierDisciplinaire, eleveDossierDisciplinaireTable,
               properties={'dossierEleve': relationship(DossierDisciplinaire,
                                           primaryjoin=(dossierDisciplinaireTable.c.dosdis_eleve_fk == eleveDossierDisciplinaireTable.c.eleve_pk)),
                           'titulaire01': relationship(Professeur,
                                          primaryjoin=(eleveDossierDisciplinaireTable.c.eleve_prof_titulaire_01_fk == professeurTable.c.prof_pk),
                                          order_by=[eleveDossierDisciplinaireTable.c.eleve_nom]),
                           'titulaire02': relationship(Professeur,
                                          primaryjoin=(eleveDossierDisciplinaireTable.c.eleve_prof_titulaire_02_fk == professeurTable.c.prof_pk)),
                           'educateurReferent': relationship(Professeur,
                                                primaryjoin=(eleveDossierDisciplinaireTable.c.eleve_educateur_referent_fk == professeurTable.c.prof_pk),
                                                order_by=[eleveDossierDisciplinaireTable.c.eleve_nom])})

        mapper(EvenementActe, evenementActeTable,
               properties={'etat': relationship(EtatPublication,
                                   primaryjoin=(evenementActeTable.c.eventact_etat_publication_fk == etatPublicationTable.c.etat_pk),
                                   order_by=[etatPublicationTable.c.etat_titre]),
                           'auteur': relationship(Professeur,
                                     primaryjoin=(evenementActeTable.c.eventact_auteur_creation_fk == professeurTable.c.prof_pk)),
                           'dossier': relationship(DossierDisciplinaire,
                                      primaryjoin=(evenementActeTable.c.eventact_dossier_diciplinaire_fk == dossierDisciplinaireTable.c.dosdis_pk),
                                      order_by=[desc(dossierDisciplinaireTable.c.dosdis_date_creation)]),
                           'documentAttache': relationship(EvenementActeDocument,
                                              primaryjoin=(evenementActeTable.c.eventact_pk == evenementActeDocumentTable.c.eventactdoc_eventact_fk))})

        mapper(EvenementActeDocument, evenementActeDocumentTable,
               properties={'auteur': relationship(Professeur,
                                        primaryjoin=(evenementActeDocumentTable.c.eventactdoc_auteur_creation_fk == professeurTable.c.prof_pk)),
                           'evenement': relationship(EvenementActe,
                                        primaryjoin=(evenementActeDocumentTable.c.eventactdoc_eventact_fk == evenementActeTable.c.eventact_pk)),
                           'dossier': relationship(DossierDisciplinaire,
                                      primaryjoin=(evenementActeDocumentTable.c.eventactdoc_dossier_disciplinaire_fk == dossierDisciplinaireTable.c.dosdis_pk))})

        mapper(EvenementActeLogModification, evenementActeLogModificationTable,
               properties={'logmodif': relationship(EvenementActe,
                                       primaryjoin=(evenementActeLogModificationTable.c.eventactlogmodif_evenement_acte_fk == evenementActeTable.c.eventact_pk),
                                       order_by=[evenementActeLogModificationTable.c.eventactlogmodif_date_modification])})

        mapper(LogOperation, logOperationTable)

        metadata.create_all()
        return model
