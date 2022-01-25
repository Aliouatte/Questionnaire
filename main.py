# questionnaire (QCM) : Poser Question

# Version 1 : Façon ordinaire : 

# def trouver_la_capitale(question,r1,r2,r3,r4,bonne_reponse):
#     global score
#     print("QUESTION")
#     print(" ",question)
#     print("  ",r1)
#     print("  ",r2)
#     print("  ",r3)
#     print("  ",r4)
#     reponse = input("votre réponse : ")
#     if reponse == bonne_reponse:
#         print("bravo ! Vous avez trouvé la bonne réponse")
#         score += 1
#     else:
#         print("Erreur, la bonne reponse est",bonne_reponse)
#     print()

# score = 0
# trouver_la_capitale("quelle est la capitale de la France :"," (a) Alger"," (b) Paris"," (c) Rome"," (d) Marseille","b")
# trouver_la_capitale("quelle est la capitale de l'Italie :"," (a) Venise"," (b) Sicile"," (c) Rome"," (d) Milan","c")
# print("score final : ",score)



# Version 2 :  en utilisant les Listes ..... : ##### Session 18 a refaire pour s'ameliorer


# Gestion des erreurs :
def demander_reponse_numerique(min,max):
    reponse_str = input("Votre réponse entre " + str(min) +" et " + str(max) + " :")
    try:
        reponse_int = int(reponse_str)
        if min <= reponse_int <= max : 
            return reponse_int
        print("ERREUR : vous devez donner un nombre entre",min, "et", max)
    except:
        print("ERREUR : vous devez donner un nombre")
    return demander_reponse_numerique(min,max)




def trouver_la_capitale2(question):
    choix = question[1]
    bonne_reponse = question[2]
    
    print("QUESTION")
    print("  " + question[0])
    for i in range(len(choix)):
        print("  ", i+1, "-", choix[i])

    print()
    resultat_correct = False
    reponse_int = demander_reponse_numerique(1,len(choix))
    
    if choix[reponse_int-1].lower() == bonne_reponse.lower():
        print("Bonne réponse")
        resultat_correct = True     
    else:
        print("Mauvaise réponse") 
    print()
    return resultat_correct




def lancer_questionnaire(question):
    score = 0
    for question in questionnaire:
        if trouver_la_capitale2(question):
            score += 1
    print("score final : ",score)


question1 = ("Quelle est la capitale de la France : ",("Alger","Paris","Rome","Marseille"),"Paris")
question2 = ("Quelle est la capitale de la l'Italie : ",("Venise","Sicile","Rome","Milan"),"Rome")
questionnaire = (question1,question2)
lancer_questionnaire(questionnaire)
# trouver_la_capitale2(question1)
# trouver_la_capitale2(question2)









