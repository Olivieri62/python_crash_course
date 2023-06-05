
#Initiation de la liste
guest_list=["Papa","Véronique","Manon","Arnaud","Gaëlle"]
print(f"Bonjour {guest_list[0]}, je t'invite à mon annivesaire le 30 mai à 21H00")
print(f"Bonjour {guest_list[1]}, je t'invite à mon annivesaire le 30 mai à 21H00")
print(f"Bonjour {guest_list[2]}, je t'invite à mon annivesaire le 30 mai à 21H00")
print(f"Bonjour {guest_list[3]}, je t'invite à mon annivesaire le 30 mai à 21H00")
print(f"Bonjour {guest_list[4]}, je t'invite à mon annivesaire le 30 mai à 21H00")
print(f"{guest_list[2]} ne pourra pas venir. J'invite Nathalie")
guest_list[2] = "Nathalie"
print(f"Bonjour {guest_list[0]}, je t'invite à mon annivesaire le 30 mai à 21H00")
print(f"Bonjour {guest_list[1]}, je t'invite à mon annivesaire le 30 mai à 21H00")
print(f"Bonjour {guest_list[2]}, je t'invite à mon annivesaire le 30 mai à 21H00")
print(f"Bonjour {guest_list[3]}, je t'invite à mon annivesaire le 30 mai à 21H00")
print(f"Bonjour {guest_list[4]}, je t'invite à mon annivesaire le 30 mai à 21H00")

#Ajout d'invités
print ("J'ai trouvé une plus grande table")
guest_list.insert(0,"Christophe")
guest_list.insert(3,"Pascale")
guest_list.append("Joffrey")
print(f"Bonjour {guest_list[0]}, je t'invite à mon annivesaire le 30 mai à 21H00")
print(f"Bonjour {guest_list[1]}, je t'invite à mon annivesaire le 30 mai à 21H00")
print(f"Bonjour {guest_list[2]}, je t'invite à mon annivesaire le 30 mai à 21H00")
print(f"Bonjour {guest_list[3]}, je t'invite à mon annivesaire le 30 mai à 21H00")
print(f"Bonjour {guest_list[4]}, je t'invite à mon annivesaire le 30 mai à 21H00")
print(f"Bonjour {guest_list[5]}, je t'invite à mon annivesaire le 30 mai à 21H00")
print(f"Bonjour {guest_list[6]}, je t'invite à mon annivesaire le 30 mai à 21H00")
print(f"Bonjour {guest_list[7]}, je t'invite à mon annivesaire le 30 mai à 21H00")

#Retrait d'invités
invite_retire = guest_list.pop()
print(f"Je suis désolé, {invite_retire}, je ne peux plus t'inviter à mon anniversaire")
invite_retire = guest_list.pop()
print(f"Je suis désolé, {invite_retire}, je ne peux plus t'inviter à mon anniversaire")
invite_retire = guest_list.pop()
print(f"Je suis désolé, {invite_retire}, je ne peux plus t'inviter à mon anniversaire")
invite_retire = guest_list.pop()
print(f"Je suis désolé, {invite_retire}, je ne peux plus t'inviter à mon anniversaire")
invite_retire = guest_list.pop()
print(f"Je suis désolé, {invite_retire}, je ne peux plus t'inviter à mon anniversaire")
invite_retire = guest_list.pop()
print(f"Je suis désolé, {invite_retire}, je ne peux plus t'inviter à mon anniversaire")
del guest_list[1]
del guest_list[0]
print(guest_list)
