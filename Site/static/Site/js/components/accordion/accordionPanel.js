import {nanoid} from '../../../../../../webpack/node_modules/nanoid/non-secure/index';

export const accordionPanel = (title = '', count =0, content = '', parentId = nanoid(), id = nanoid(), panelId = nanoid()) => `
<div class="panel panel-default">
    <div class="panel-heading" role="tab" id="${id}">
        <h4 class="panel-title">
            <a class="collapsed accordion-event" role="button" data-toggle="collapse" data-parent="#${parentId}" href="#${panelId}" aria-expanded="false">
                <span>${title}</span>
                <span class="label label-danger" title="Ожидает">${count}</span>
            </a>
        </h4>
    </div>
    <div id="${panelId}" class="panel-collapse collapse" role="tabpanel" aria-labelledby="${id}" aria-expanded="false" style="height: 0px;">
        <div class="panel-body">${content}</div>
    </div>
</div>`;