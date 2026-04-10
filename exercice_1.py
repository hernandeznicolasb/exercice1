from typing import OrderedDict


def AfficherBlock(dico):
      dico=OrderedDict(sorted(dico.items(), key=lambda x : x[0]))
      Max_largeur=100
      space=" "
      line="-"
      VerticalLine="|"
      lines=line*Max_largeur
      for cle,bloc in dico.items():
            l = lines
            print(space+l)
            for key,sentence in bloc.items():
                 str= space*(Max_largeur-len(sentence))
                 str=str+sentence
                 str_=VerticalLine+str+VerticalLine
                 if isinstance(key, int):#Les phrases qu'on veut afficher ont une clé numérique dans le dictionnaire
                  print(str_)
            ll = lines + "\n"
            print(space+ll)


dico={1:{1:"Le code propre facilite la maintenance"},
      2:{1:"Tester souvent évite beaucoup d erreurs",
         "E":"Cette phrase ne doit pas s afficher"},
      3:{1:"Cette phrase ne doit pas s afficher",
         "E":"Un bon code doit rester simple et clair",
         3:"La simplicité améliore la qualité du code",
         4:"Refactoriser améliore la compréhension"}}
#pour changer l'ordre des bloc, changez le numéro (la clé)
# quand on mets "E" c'est pour ne pas afficher la phrase
AfficherBlock(dico)
