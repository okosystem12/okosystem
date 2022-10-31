
export const corruptControl = (data = {}) =>
    `<div>${data.corrupt__info}</div>
<div class="corrupt__control">
<button type="button" class="btn btn-success corrupt__confirm" data-id="${data.id}" title="Подтвердить"><span class="glyphicon glyphicon-ok"></span></button>
<button type="button" class="btn btn-danger corrupt__reject" data-id="${data.id}" title="Отмена"><span class="glyphicon glyphicon-remove"></span></button>
</div>
`;