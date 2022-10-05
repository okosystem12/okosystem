
import {nanoid} from '../../../../../../webpack/node_modules/nanoid/non-secure';

export const componentItem = (elem = {id: nanoid(), value: ''}) =>`<div class="component__item" data-component-id="${elem.id}">
<input class="component__input form-control" value="${elem.value}">
<button class="btn btn-danger component__remove" type="button" title="Удалить"><span class="glyphicon glyphicon-remove" aria-hidden="true"></span></button>
</div>`;