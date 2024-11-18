from django.shortcuts import render
from .models import Equipement
from .models import Character
from django.shortcuts import render, get_object_or_404, redirect
from .forms import MoveForm


def post_list(request):
    characters = Character.objects.all()  # Récupère tous les personnages
    equipements = Equipement.objects.all()  # Récupère tous les équipements
    form = MoveForm()  # Initialise le formulaire
    
    if request.method == "POST":
        print("Formulaire soumis avec les données :", request.POST)  # Ajout de débogage
        form = MoveForm(request.POST)
        if form.is_valid():
            print("Formulaire valide :", form.cleaned_data)  # Ajout de débogage
            
            # Effectuez les actions nécessaires avec les données du formulaire
             # Récupérer les données du formulaire
            id_character = form.cleaned_data['id_character']  # ID du personnage
            nouveau_lieu = form.cleaned_data['lieu']  # Le nouveau lieu sélectionné
              
            # Récupérer l'instance existante de Character
            personnage = Character.objects.get(id_character=id_character)
            
            # Récupérer l'ancien lieu du personnage
            ancien_lieu = personnage.lieu
            ancien_lieu.disponibilite = "Libre"
            ancien_lieu.save()

            # Déplacer le personnage vers le nouveau lieu
            personnage.lieu = nouveau_lieu
            personnage.save()

            # Mettre à jour le nouveau lieu pour le rendre occupé
            nouveau_lieu.disponibilite = "Occupé"
            nouveau_lieu.save()
            
            # Rediriger après la soumission
            print( "Le personnage a été déplacé avec succès !")
            return redirect('post_list')  # Recharge la page principale

            # fin des trucs annexes 

        else:
            print("Erreurs du formulaire :", form.errors)  # Débogage des erreurs


    return render(request, 'blog/post_list.html', {
        'form': form,
        'characters': characters,
        'equipements': equipements
    })