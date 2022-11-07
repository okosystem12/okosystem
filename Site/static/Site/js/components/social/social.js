import {nanoid} from '../../../../../../webpack/node_modules/nanoid/non-secure/index';
import {link} from "../link";
import {dateFormat} from "../../utils/date/dateFormat";

export const social = (s = {}, id = nanoid()) =>
    `<div class="social-list" data-social="${id}">
${link(`${s.prefix}${s.value}`)}
<div class="social-list__date" data-confirmed="${id}">${s.confirmedAt ? `Подтверждено ${ dateFormat(s.confirmedAt)}` : `Требует подтверждения`}</div>
<div>
<button type="button" ${s.confirmedAt && 'disabled'} class="btn btn-success social-list__confirm" data-id="${s.id}" data-confirmed="${id}" title="Подтвердить"><span class="glyphicon glyphicon-ok"></span></button>
<button type="button" class="btn btn-danger social-list__reject" data-id="${s.id}" data-social="${id}" title="Отмена"><span class="glyphicon glyphicon-remove"></span></button>
</div></div>`;
