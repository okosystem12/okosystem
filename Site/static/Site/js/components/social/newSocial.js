import {nanoid} from '../../../../../../webpack/node_modules/nanoid/non-secure/index';

export const newSocial = (id = nanoid()) =>
    `<form class="social-item" data-social="${id}">
<div class="form-group social-item__input">
<input type="text" class="form-control" name="socialValue">
</div>
<div></div>
<div>
<button type="submit" class="btn btn-success social-item__add" title="Сохранить"><span class="glyphicon glyphicon-ok"></span></button>
<button type="button" class="btn btn-danger social-item__remove" data-social="${id}" title="Отмена"><span class="glyphicon glyphicon-remove"></span></button>
</div>
</form>`;