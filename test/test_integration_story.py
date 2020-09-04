from app.location import Location
from app.parser import Parser
from app.story import Story
from pytest import mark

sentence_extracts_url = [
    (
        "Hello ! Qu'elle est l'adresse exacte du chateau de Guédelon ?",
        "Guédelon ou le château de Guédelon est un chantier médiéval de construction historique d'un château fort, débuté en 1997, selon les techniques et les matériaux utilisés au Moyen Âge.\nCe projet architectural situé à Treigny dans l'Yonne, dans une ancienne carrière désaffectée au centre d'une forêt et proche d'un étang, à une trentaine de kilomètres au sud-ouest d'Auxerre, vise à améliorer les connaissances en castellologie et en  archéologie expérimentale. Tout en développant une réflexion du type « art et traditions populaires », il met en scène dans un déroulement réel la construction d'un programme monumental, ce qui le différencie des parcs à thème.",
        "https://fr.wikipedia.org/w/index.php?curid=10551",
    ),
    (
        "Ah! L'horloge astronomique de Besançon, j'aimerais y retourner ! Peux-tu me pointer l'endroit sur la carte ?",
        "L'Horloge astronomique de la cathédrale Saint-Jean de Besançon est une horloge astronomique considérée comme un chef-d'œuvre du genre, construite par Auguste-Lucien Vérité au XIXe siècle. Elle fait suite à l'horloge astronomique de Constant Flavien Bernardin, construite vers 1850-1855, au fonctionnement compliqué et défectueux, disparue (ou intégrée dans celle de Vérité) vers 1860.",
        "https://fr.wikipedia.org/w/index.php?curid=945824",
    ),
    (
        "Salut ! Je voudrais toucher la Chouette de Dijon mais je n'arrive pas à la trouver. Où est-elle ?",
        "L’église Notre-Dame de Dijon, considérée comme un chef-d'œuvre d'architecture gothique du XIIIe siècle, est située au cœur des 97 hectares du secteur sauvegardé de Dijon, inscrit depuis le 4 juillet 2015 au patrimoine mondial de l'UNESCO. Elle s'élève place Notre-Dame, à proximité du Palais des ducs et des États de Bourgogne et en face de la rue Musette. On estime que l'édifice actuel a été construit des années 1220 aux années 1250 environ.\nCette église abrite la statue de Notre-Dame de Bon-Espoir, auparavant appelée Vierge noire. Elle s'orne aussi de deux symboles de la ville de Dijon : le Jacquemart et la chouette.\nL'église a été classée au titre des monuments historiques par la liste de 1840.\nLa chapelle de l'Assomption, la sacristie et la galerie les reliant à l'église sont inscrites au titre des monuments historiques depuis le 5 juillet 2002.",
        "https://fr.wikipedia.org/w/index.php?curid=1918775",
    ),
]


@mark.parametrize(
    "input_user, extract_place, url_place", sentence_extracts_url
)
def test_story_return_correct_extract_and_url_for_several_location(
    input_user, extract_place, url_place
):

    parser = Parser(input_user)
    location = Location(parser)
    location.get_location()
    story = Story(location)

    story.about()

    assert story.extract == extract_place
    assert story.url == url_place
