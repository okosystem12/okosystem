import {input} from "../../../../utils/table/filter/input";
import {select} from "../../../../utils/table/filter/select";
import {vchList} from "../../../../storage/app/vchList";
import {statusList} from "../../../../storage/control/statusList";

export const filter = (table) => [
    input(table, 'ФИО', 'username', {value: '', title: 'ФИО', text: ''}),
    select(table, 'Место военной службы', true, 'vch', {
        value: '',
        title: 'Место военной службы',
        text: ''
    }, vchList.value.map(el => {
        return {id: el.id, title: el.number}
    })),
    select(table, 'Статус', true, 'status', {
        value: '',
        title: 'Статус',
        text: ''
    }, statusList.value.map(el => {
        return {id: el.id, title: el.name, group: el.stage__name}
    })),
    select(table, 'Социальные сети', false, 'social', {
        value: '',
        title: 'Социальные сети',
        text: ''
    }, [{id: 0, title: 'Есть'}, {id: 1, title: 'Нет'}]),
];