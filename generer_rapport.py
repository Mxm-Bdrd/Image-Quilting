#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

# =============================================================================
# CSS Styles
# =============================================================================
def obtenir_css(accent_color="#4fc3f7"):
    return f"""
        @import url('https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@400;600;700&family=Fira+Code:wght@400;500&display=swap');
        * {{ box-sizing: border-box; }}
        body {{
            font-family: 'Source Sans Pro', -apple-system, BlinkMacSystemFont, sans-serif;
            margin: 0; padding: 0;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            min-height: 100vh; color: #e8e8e8;
        }}
        .container {{ max-width: 1400px; margin: 0 auto; padding: 30px 20px; }}
        header {{ text-align: center; padding: 40px 0; border-bottom: 2px solid rgba(255,255,255,0.1); margin-bottom: 40px; }}
        h1 {{ font-size: 2.5em; font-weight: 700; color: #fff; margin: 0 0 15px 0; text-shadow: 0 2px 10px rgba(0,0,0,0.3); }}
        .subtitle {{ font-size: 1.2em; color: #a0a0a0; margin: 0; line-height: 1.5; }}
        .date-badge {{ display: inline-block; background: rgba(255,255,255,0.1); padding: 8px 20px; border-radius: 20px; margin-top: 20px; font-size: 0.9em; color: #b0b0b0; }}
        .image-section {{ background: rgba(255,255,255,0.05); backdrop-filter: blur(10px); border-radius: 16px; padding: 30px; margin-bottom: 40px; border: 1px solid rgba(255,255,255,0.1); box-shadow: 0 8px 32px rgba(0,0,0,0.2); }}
        .image-section h2 {{ color: {accent_color}; font-size: 1.6em; margin: 0 0 25px 0; padding-bottom: 15px; border-bottom: 2px solid {accent_color}40; }}
        h3 {{ color: #e0e1dd; font-size: 1.3em; margin: 30px 0 20px 0; }}
        h3::before {{ content: ''; display: inline-block; width: 4px; height: 24px; background: {accent_color}; margin-right: 12px; border-radius: 2px; vertical-align: middle; }}
        .algorithm-box {{ background: rgba(0,0,0,0.3); padding: 20px; border-radius: 8px; margin: 15px 0; border-left: 4px solid {accent_color}; }}
        .algorithm-box h4 {{ color: {accent_color}; margin: 0 0 10px 0; }}
        .algorithm-box p {{ margin: 5px 0; line-height: 1.6; }}
        .discussion-box {{ border-left: 4px solid #f9a826; background: rgba(249, 168, 38, 0.1); }}
        .discussion-box h4 {{ color: #f9a826; }}

        .figure-container {{ display: flex; flex-direction: column; align-items: center; justify-content: center; margin: 20px 0; padding: 15px; background: rgba(0,0,0,0.2); border-radius: 12px; }}
        .figure-container img {{ max-width: 95%; max-height: 600px; border-radius: 8px; box-shadow: 0 4px 20px rgba(0,0,0,0.3); outline: none; cursor: zoom-in; transition: transform 0.2s; }}
        .figure-container img:hover {{ transform: scale(1.02); }}
        .figure-caption {{ margin-top: 10px; font-style: italic; color: #a0a0a0; font-size: 1em; text-align: center; }}

        .image-grid {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; margin: 30px 0; }}
        .image-grid-item {{ position: relative; border-radius: 12px; overflow: hidden; background: rgba(0,0,0,0.3); cursor: zoom-in; transition: transform 0.2s; flex: 0 1 400px; max-width: 100%; }}
        .image-grid-item:hover {{ transform: translateY(-5px); box-shadow: 0 8px 25px rgba(0,0,0,0.5); }}
        .image-grid-item img {{ width: 100%; height: auto; display: block; }}
        .image-grid-item .image-label {{ position: absolute; bottom: 0; left: 0; right: 0; background: linear-gradient(to top, rgba(0,0,0,0.8), transparent); color: #fff; padding: 15px 10px 10px; font-size: 0.9em; text-align: center; }}

        .lightbox {{ display: none; position: fixed; z-index: 9999; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.9); animation: fadeIn 0.3s; overflow: auto; }}
        .lightbox.active {{ display: flex; align-items: center; justify-content: center; }}
        .lightbox-content {{ margin: auto; padding: 20px; display: flex; align-items: center; justify-content: center; }}
        .lightbox-content img {{ max-width: 95vw; max-height: 95vh; object-fit: contain; border-radius: 8px; box-shadow: 0 0 30px rgba(0,0,0,0.8); transition: transform 0.3s ease; transform: scale(1.2); cursor: zoom-out; }}
        .lightbox-content img.fit-screen {{ transform: scale(1); cursor: zoom-in; }}
        .lightbox-close {{ position: fixed; top: 20px; right: 40px; color: #fff; font-size: 40px; font-weight: bold; cursor: pointer; z-index: 10000; }}
        .lightbox-close:hover {{ color: {accent_color}; }}
        @keyframes fadeIn {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
        footer {{ text-align: center; padding: 30px; color: #666; font-size: 0.9em; }}
    """

# =============================================================================
# Composants HTML
# =============================================================================
def document_html(titre, sous_titre, icone, contenu, accent_color="#4fc3f7"):
    date_str = datetime.now().strftime("%d %B %Y à %H:%M")
    css = obtenir_css(accent_color)
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{titre}</title>
    <style>{css}</style>
</head>
<body>
    <div id="lightbox" class="lightbox" onclick="closeLightbox(event)">
        <span class="lightbox-close">&times;</span>
        <div class="lightbox-content"><img id="lightbox-img" src="" alt=""></div>
    </div>
    <div class="container">
        <header>
            <h1>{icone} {titre}</h1>
            <p class="subtitle">{sous_titre}</p>
            <div class="date-badge">Généré le {date_str}</div>
        </header>
        {contenu}
        <footer></footer>
    </div>
    <script>
        function openLightbox(img) {{
            const lbImg = document.getElementById('lightbox-img');
            lbImg.src = img.src; lbImg.className = ''; 
            document.getElementById('lightbox').classList.add('active');
            document.body.style.overflow = 'hidden';
        }}
        function closeLightbox(event) {{
            const lightbox = document.getElementById('lightbox');
            if (event.target === lightbox || event.target.classList.contains('lightbox-close') || event.target.classList.contains('lightbox-content')) {{
                lightbox.classList.remove('active'); document.body.style.overflow = 'auto';
            }}
        }}
        document.getElementById('lightbox-img').addEventListener('click', function(e) {{
            this.classList.toggle('fit-screen'); e.stopPropagation(); 
        }});
        document.addEventListener('keydown', e => {{ 
            if (e.key === 'Escape') {{
                document.getElementById('lightbox').classList.remove('active'); document.body.style.overflow = 'auto';
            }}
        }});
    </script>
</body>
</html>
"""

def section(titre, contenu, icone=""):
    return f'<div class="image-section"><h2><span class="icon">{icone}</span> {titre}</h2>{contenu}</div>'

def figure(chemin_img, legende="", alt=""):
    alt = alt or legende
    html_legende = f'<p class="figure-caption">{legende}</p>' if legende else ""
    return f'<div class="figure-container"><img src="{chemin_img}" alt="{alt}" onclick="openLightbox(this)">{html_legende}</div>'

def grille_images(images, titre=""):
    items = ""
    for img in images:
        items += f'<div class="image-grid-item" onclick="openLightbox(this.querySelector(\'img\'))"><img src="{img["src"]}" alt="{img["label"]}"><div class="image-label">{img["label"]}</div></div>'
    html_titre = f'<h3>{titre}</h3>' if titre else ""
    return f'{html_titre}<div class="image-grid">{items}</div>'

def boite_texte(titre, description, is_discussion=False):
    classe = "algorithm-box discussion-box" if is_discussion else "algorithm-box"
    return f'<div class="{classe}"><h4>{titre}</h4><p>{description}</p></div>'

# =============================================================================
# Génération
# =============================================================================
def generer_rapport():
    contenu = ""

    # SANS CHEVAUCHEMENT
    contenu_p1 = boite_texte("Approche",
                                     "Pour commencer, j'ai fait une boucle qui va piger des blocs carrés au hasard dans l'image source et qui les place côte à côte. Le résultat est très boff, mais c'est un point de départ pour ajouter le chevauchement dans la partie 2.")
    parametres_p1 = """
        <ul>
            <li><b>outsize :</b> (500, 500)</li>
            <li><b>patchsize :</b> 50</li>
            <li>Toutes les textures choisies sont libres de droit et ont été prises sur 'epictura.fr'.</li>
        </ul>
        """
    contenu_p1 += boite_texte("Paramètres", parametres_p1)

    images_p1 = [
        {"src": "textures/bricks_small.jpg", "label": "Texture de base"},
        {"src": "textures/text_small.jpg", "label": "Texture de base"},
        {"src": "textures/white_small.jpg", "label": "Texture de base"},
        {"src": "P1/bricks.jpg", "label": "Synthèse aléatoire"},
        {"src": "P1/text.jpg", "label": "Synthèse aléatoire"},
        {"src": "P1/white.jpg", "label": "Synthèse aléatoire"},
        {"src": "textures/bois.png", "label": "Texture de base"},
        {"src": "textures/marbre.png", "label": "Texture de base"},
        {"src": "textures/vitre.png", "label": "Texture de base"},
        {"src": "P1/bois.png", "label": "Synthèse aléatoire"},
        {"src": "P1/marbre.png", "label": "Synthèse aléatoire"},
        {"src": "P1/vitre.png", "label": "Synthèse aléatoire"}
    ]
    contenu_p1 += grille_images(images_p1, "")

    contenu_p1 += boite_texte("Discussion",
                                        "Les transitions entre les blocs sont très abruptes et on voit une genre de grille. La texture globale ne fait pas de sens. Pas grand chose à dire de plus.",
                                        is_discussion=True)
    contenu += section("Texture échantillonnée aléatoirement", contenu_p1, icone="")


    # AVEC CHEVAUCHEMENT
    contenu_p2 = boite_texte("Approche",
                                     "Pour cette étape, chaque nouveau bloc chevauche les blocs précédemment placés à gauche et/ou en haut. L'algorithme calcule la SDC dans la zone de chevauchement pour évaluer le fit. Un bloc est choisi aléatoirement dans ceux dont l'erreur est inférieure à (1 + tolérance)*erreur_minimale. Le overlap contrôle à quel point les carrés se chevauchent.")
    parametres_p2 = """
        <ul>
            <li><b>outsize :</b> (300, 300)</li>
            <li><b>patchsize :</b> 31</li>
            <li><b>overlap :</b> 7</li>
            <li><b>tol :</b> 0.1</li>
            <li>Toutes les textures choisies sont libres de droit et ont été prises sur 'epictura.fr'.</li>
        </ul>
        """
    contenu_p2 += boite_texte("Paramètres", parametres_p2)

    images_p2 = [
        {"src": "textures/bricks_small.jpg", "label": "Texture de base"},
        {"src": "textures/text_small.jpg", "label": "Texture de base"},
        {"src": "textures/white_small.jpg", "label": "Texture de base"},
        {"src": "P2/bricks.jpg", "label": "Chevauchement simple"},
        {"src": "P2/text.jpg", "label": "Chevauchement simple"},
        {"src": "P2/white.jpg", "label": "Chevauchement simple"},
        {"src": "textures/bois.png", "label": "Texture de base"},
        {"src": "textures/marbre.png", "label": "Texture de base"},
        {"src": "textures/vitre.png", "label": "Texture de base"},
        {"src": "P2/bois.png", "label": "Chevauchement simple"},
        {"src": "P2/marbre.png", "label": "Chevauchement simple"},
        {"src": "P2/vitre.png", "label": "Chevauchement simple"}
    ]
    contenu_p2 += grille_images(images_p2, "")

    contenu_p2 += boite_texte("Discussion",
                                        "C'est une grosse amélioration par rapport à la méthode aléatoire. Les textures s'alignent vraiment mieux, mais si on regarde de proche, on voit encore des lignes droites là où les blocs écrase les anciens, surtout sur les textures plus définies comme le marbre ou le 'white' fourni. Je suis assez surpris que le texte marche aussi bien avec cet algorithme, malgré que la langue est devenue inexistante. Les paramètres affichés plus haut sont ceux que je garde et qui fonctionne le mieux pour l'ensemble des textures.",
                                        is_discussion=True)
    contenu += section("Chevauchement de blocs", contenu_p2, icone="")


    # RECHERCHE DE JOINTS
    contenu_p3 = boite_texte("Approche",
                                     "Pour essayer de régler le problème des coupures visibles, j'ai implémenté un algorithme qui calcule le chemin de moindre coût dans la zone de chevauchement, ce qui permet de fusionner les blocs en suivant une ligne autre q'une ligne droite. Cela devrait donner un meilleur résultat que le simple chevauchement. La façon de faire est à peu près écrit dans l'énoncé.")
    parametres_p3 = """
            <ul>
                <li><b>outsize :</b> (300, 300)</li>
                <li><b>patchsize :</b> 31</li>
                <li><b>overlap :</b> 7</li>
                <li><b>tol :</b> 0.1</li>
                <li>Toutes les textures choisies sont libres de droit et ont été prises sur 'epictura.fr'.</li>
            </ul>
            """
    contenu_p3 += boite_texte("Paramètres", parametres_p3)

    images_p3 = [
        {"src": "textures/bricks_small.jpg", "label": "Texture de base"},
        {"src": "textures/text_small.jpg", "label": "Texture de base"},
        {"src": "textures/white_small.jpg", "label": "Texture de base"},
        {"src": "P2/bricks.jpg", "label": "Recherche de joint"},
        {"src": "P2/text.jpg", "label": "Recherche de joint"},
        {"src": "P2/white.jpg", "label": "Recherche de joint"},
        {"src": "textures/bois.png", "label": "Texture de base"},
        {"src": "textures/marbre.png", "label": "Texture de base"},
        {"src": "textures/vitre.png", "label": "Texture de base"},
        {"src": "P3/bois.png", "label": "Recherche de joint"},
        {"src": "P3/marbre.png", "label": "Recherche de joint"},
        {"src": "P3/vitre.png", "label": "Recherche de joint"}
    ]
    contenu_p3 += grille_images(images_p3, "")

    contenu_p3 += boite_texte("Discussion",
                                        "Premièrement, je remarque que le temps de calcul est un peu long. Deuxièmement, j'ai garder les mêmes paramètres que précédemment étant donné qu'ils donnent le meilleur résultat globale. J'ai remarquer cependant que la résolution des textures jouent beaucoup pour le chevauchement et le patchsize (évidemment, je n'avais juste pas remarquer avant). Je vais donc changer les valeurs des paramètres par photo pour ma section personnelle, vu que mes photos vont avoir le même problème. Pour ce qui est des résultats, je suis surpris que l'algo donne des pires résultats que le chevauchement simple. Je crois qu'il s'agit d'une erreur dans mon code, ou peut-être que je n'ai pas trouver le sweet spot (malgré beaucoup d'essaie-erreur). Les textures plus unies donnent quand même un résultat acceptable malgré tout (brique et bois).",
                                        is_discussion=True)
    contenu += section("Recherche de joint", contenu_p3, icone="")


    # TRANSFERT DE TEXTURE
    contenu_p4 = boite_texte("Approche",
                                     "Pour la dernière étape, j'ai modifié ma fonction de coupe pour qu'elle ne gère pas juste le chevauchement, mais qu'elle essaie aussi de matcher l'intensité des pixels d'une image cible. J'utilise le paramètre alpha pour balancer entre prioriser la texture ou la forme de l'image cible selon l'équation Coût = alpha*SDC_{chevauchement} + (1-alpha)*SDC_{cible} (écrite en latex). Je reprends une grosse partie du code de quilt_cut.<li>Tous les visages choisis sont libres de droit et ont été pris sur 'fr.dreamstime.com'.</li>")
    parametres_p4_feynman = """
        <ul>
            <li><b>patchsize :</b> 39</li>
            <li><b>overlap :</b> 21</li>
            <li><b>tol :</b> 0.01</li>
            <li><b>alpha :</b> 0.1</li>
        </ul>
        """
    contenu_p4 += boite_texte("Paramètres Feynman", parametres_p4_feynman)

    images_p4_feynman = [
        {"src": "transfert/feynman.png", "label": "Image cible"},
        {"src": "textures/white_small.jpg", "label": "Texture"},
        {"src": "P4/feynman.png", "label": "Transfert"}
    ]
    contenu_p4 += grille_images(images_p4_feynman, "")

    parametres_p4_sketch = """
            <ul>
                <li><b>patchsize :</b> 49</li>
                <li><b>overlap :</b> 25</li>
                <li><b>tol :</b> 0.01</li>
                <li><b>alpha :</b> 0.1</li>
            </ul>
            """
    contenu_p4 += boite_texte("Paramètres Sketch", parametres_p4_sketch)

    images_p4_sketch = [
        {"src": "transfert/sketch.png", "label": "Image cible"},
        {"src": "textures/marbre.png", "label": "Texture"},
        {"src": "P4/sketch.png", "label": "Transfert"}
    ]
    contenu_p4 += grille_images(images_p4_sketch, "")

    parametres_p4_smile = """
            <ul>
                <li><b>patchsize :</b> 37</li>
                <li><b>overlap :</b> 21</li>
                <li><b>tol :</b> 0.1</li>
                <li><b>alpha :</b> 0.1</li>
            </ul>
            """
    contenu_p4 += boite_texte("Paramètres Smile", parametres_p4_smile)

    images_p4_smile = [
        {"src": "transfert/smile.png", "label": "Image cible"},
        {"src": "textures/text_small.jpg", "label": "Texture"},
        {"src": "P4/smile.png", "label": "Transfert"}
    ]
    contenu_p4 += grille_images(images_p4_smile, "")

    parametres_p4_lion = """
            <ul>
                <li><b>patchsize :</b> 61</li>
                <li><b>overlap :</b> 25</li>
                <li><b>tol :</b> 0.01</li>
                <li><b>alpha :</b> 0.05</li>
            </ul>
            """
    contenu_p4 += boite_texte("Paramètres Lion", parametres_p4_lion)

    images_p4_lion = [
        {"src": "transfert/lion.png", "label": "Image cible"},
        {"src": "textures/bois.png", "label": "Texture"},
        {"src": "P4/lion.png", "label": "Transfert"}
    ]
    contenu_p4 += grille_images(images_p4_lion, "")

    contenu_p4 += boite_texte("Discussion",
                                        "J'ai remarqué que le transfert fonctionne bien si les contrastes de l'image cible sont forts. Un alpha trop près de 1 ignore le visage, mais un alpha trop bas ignore la texture et refait l'effet non voulu de grille d'avant. J'ai aussi remarqué que le patchsize ne doit pas être trop grand et le overlap trop petit. Un fois que j'ai trouvé un bon sweet spot, j'obtiens de très bons résultats. Le transfert 2 et 4 sont impécable et j'adore à quel point le marbre garde ces marques noirs naturelles même en reproduisant le sketch. Le lion est peu visible et je trouve ça parfait car il 'overwhelm' pas la texture du bois. J'ai encore essayé de faire marcher la texture du text mais j'ai décider de l'inclure comme échec car je n'étais pas capable de faire aligner les mots en même temps d'avoir la forme du smile.",
                                        is_discussion=True)
    contenu += section("Transfert de texture", contenu_p4, icone="")

    # MES PHOTOS
    contenu_p5 = boite_texte("Approche","Sans changer le code de ma section précédente, je teste mon algorithme sur mes photos.")

    parametres_p5_1 = """
        <ul>
            <li><b>patchsize :</b> 71</li>
            <li><b>overlap :</b> 19</li>
            <li><b>tol :</b> 0.1</li>
            <li><b>alpha :</b> 0.3</li>
        </ul>
        """
    contenu_p5 += boite_texte("Paramètres pour moi", parametres_p5_1)

    images_p5_1 = [
        {"src": "personnelles/MaPhoto1.png", "label": "Image cible"},
        {"src": "textures/marbre.png", "label": "Texture"},
        {"src": "P5/Max.png", "label": "Transfert"}
    ]
    contenu_p5 += grille_images(images_p5_1, "")

    parametres_p5_2 = """
        <ul>
            <li><b>patchsize :</b> 71</li>
            <li><b>overlap :</b> 19</li>
            <li><b>tol :</b> 0.1</li>
            <li><b>alpha :</b> 0.01</li>
        </ul>
        """
    contenu_p5 += boite_texte("Paramètres d'Ahsoka", parametres_p5_2)

    images_p5_2 = [
        {"src": "personnelles/MaPhoto3.png", "label": "Image cible"},
        {"src": "textures/vitre.png", "label": "Texture"},
        {"src": "P5/Ahsoka.png", "label": "Transfert"}
    ]
    contenu_p5 += grille_images(images_p5_2, "")

    parametres_p5_3 = """
        <ul>
            <li><b>patchsize :</b> 31</li>
            <li><b>overlap :</b> 9</li>
            <li><b>tol :</b> 0.1</li>
            <li><b>alpha :</b> 0.01</li>
        </ul>
        """
    contenu_p5 += boite_texte("Paramètres de Oli", parametres_p5_3)

    images_p5_3 = [
        {"src": "personnelles/mog.png", "label": "Image cible"},
        {"src": "textures/white_small.jpg", "label": "Texture"},
        {"src": "P5/Oli.png", "label": "Transfert"}
    ]
    contenu_p5 += grille_images(images_p5_3, "")

    contenu_p5 += boite_texte("Discussion",
                              "Pour mes photos, je voulais jouer avec le alpha pour tester les limites. J'essayer un mini valeur avec une texture de vitre qui ne fonctionnait pas avant. Avec la photo de mon chien, je suis quand même arrivé à un résultat subtil en forçant la texture sur le visage avec un très petit alpha. Pour mes deux autres photos, les résultats sont acceptables et la définition des personnes est visible, quoiqu'un peu forcé sur mon ami Oli.",
                              is_discussion=True)
    contenu += section("Mes photos", contenu_p5, icone="")

    # =========================================================================
    # GÉNÉRATION HTML
    # =========================================================================
    sous_titre = "Maxime Bédard"
    html_final = document_html("<strong>Synthèse et Transfert de Textures</strong>", sous_titre, "",
                               contenu)

    nom_fichier = "index.html"
    with open(nom_fichier, "w", encoding="utf-8") as f:
        f.write(html_final)

if __name__ == '__main__':
    generer_rapport()