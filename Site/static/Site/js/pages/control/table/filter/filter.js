import {input} from "../../../../utils/table/filter/input";
import {select} from "../../../../utils/table/filter/select";
import {vchList} from "../../../../storage/app/vchList";

export const filter = (table) => [
    // def(table, 'Страны', 'type', {value: 'countries', title: 'Отображать только', text: 'Страны'})
    input(table, 'ФИО', 'username', {value: '', title: 'ФИО', text: ''}),
    select(table, 'Место военной службы', 'vch', {
        value: '',
        title: 'Место военной службы',
        text: ''
    }, vchList.value.map(el => {
        return {id: el.id, title: el.number}
    })),
];