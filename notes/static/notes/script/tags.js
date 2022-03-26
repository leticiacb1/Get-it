function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

document.addEventListener("DOMContentLoaded", function () {
  // Sorteia classes de cores aleatoriamente para os cards
  let cards_tags = document.getElementsByClassName("card_tag");

  for (let i = 0; i < cards_tags.length; i++) {
    let card = cards_tags[i];

    card.className += ` card-color-${getRandomInt(
      1,
      5
    )} card-rotation-${getRandomInt(1, 11)}`;

  }

});