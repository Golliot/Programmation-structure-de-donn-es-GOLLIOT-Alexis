Ton fichier est plutôt propre et bien écrit, même s'il manque de commentaires, et tu as quelques tests.

Pour la logique, le seul souci que je vois est la mise à jour d'une entrée qui ne marche pas, même si tu as pensé à ce cas avec la ligne `self.__values[indice][i][1] == value`. Le souci est d'un que tu as mis `==` au lieu d'un seul signe, et ensuite les tuples ne sont pas mutables et tu ne peux pas les modifier; tu dois donc mettre à jour le tuple lui même, donc quelque chose comme ca `self.__values[indice][i] = (key, value)`. Pour aller plus vite, au lieu d'utiliser `verifClé`, tu peux juste après cette ligne écrire `return`, qui arrête la fonction directement, et donc si tu sors de ta boucle for, tu peux faire directement l'ajout de ton tuple.

Sinon, tout semble bien fonctionner sans souci.

Voici le lien du corrigé si jamais: https://github.com/thomas-vinet/Mines-TD-PSD