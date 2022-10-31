import {materials} from "../../utils/render/materials";

export const corruptElem = (data = {}) =>
    `<div style="grid-row: span ${data.corruptList.length};">
<b>${data.materialsType}</b>
<br>
${materials(data.materials)}</div>`;