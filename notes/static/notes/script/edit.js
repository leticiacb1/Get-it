function close_update_card(icon_close){
    let overlay = document.querySelector(".overlay")
    overlay.style.display="none"
}

function update_card(btn) {
    // Ativada quando clicado no icone de editar
    // Ativar overlay
    let overlay = document.querySelector(".overlay");
    overlay.style.display = "block";

    // localizar formulário que contem informações do card:
    let form_card = btn.parentElement.parentElement.parentElement;

    let old_title = form_card.children[1].getAttribute("value")
    let old_desc = form_card.children[2].getAttribute("value")
    let id = form_card.children[3].getAttribute("value")
    let old_tag = form_card.children[4].getAttribute("value")

    let title_to_edit = document.querySelector("#edit-Title")
    let desc_to_edit = document.querySelector("#edit-Detalhes")
    let tag_to_edit = document.querySelector("#edit_tag")
    let id_notEdit = document.querySelector('#id_notEdit')

    // Atualizando o valor do formulario de edit para o valor do card
    title_to_edit.setAttribute("value", old_title)
    desc_to_edit.setAttribute("value", old_desc)
    id_notEdit.setAttribute("value", id)
    tag_to_edit.setAttribute("value", old_tag)
}