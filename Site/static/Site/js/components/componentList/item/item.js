import {nanoid} from '../../../../../../../webpack/node_modules/nanoid/non-secure/index';

export const item = (elem = {id: nanoid(), value: ''}) =>
    `<div class="component__item input-group" data-component-id="${elem.id}">
<input class="component__input form-control" value="${elem.value}">
<span class="input-group-btn">
<button class="btn btn-danger component__remove" type="button" title="Удалить">
<span class="glyphicon glyphicon-remove" aria-hidden="true"></span>
</button>
</span>
</div>`;