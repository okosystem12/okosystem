import {input} from "../../../../utils/table/filter/input";
import {select} from "../../../../utils/table/filter/select";
import {usersList} from "../../../../storage/archive/usersList";
import {corruptInfoList} from "../../../../storage/archive/corruptInfoList";
import {userShortName} from "../../../../utils/user/userShortName";

export const filter = (table) => [
    // input(table, 'ФИО', 'username', {value: '', title: 'ФИО', text: ''}),
    select(table, 'Пользователь', true, 'user', {
        value: '',
        title: 'Пользователь',
        text: ''
    }, usersList.value.map(el => {
        return {id: el.id, title: userShortName(el)}
    })),
    select(table, 'Тип нарушения', true, 'corruptInfo', {
        value: '',
        title: 'Тип нарушения',
        text: ''
    }, corruptInfoList.value.map(el => {
        return {id: el.id, title: `${el.value} - ${el.info}`}
    })),
    select(table, 'Тип материалов', true, 'corruptType', {
        value: '',
        title: 'Тип материалов',
        text: ''
    }, [
        {id:0,title:'Пост'},
        {id:1,title:'Видео'},
        {id:2,title:'Сообщество'},
        {id:3,title:'Фото'},
        {id:4,title:'Личная информация'},
    ]),
    // select(table, 'Статус', true, 'status', {
    //     value: '',
    //     title: 'Статус',
    //     text: ''
    // }, statusList.value.map(el => {
    //     return {id: el.id, title: el.name, group: el.stage__name}
    // })),
    // select(table, 'Социальные сети', false, 'social', {
    //     value: '',
    //     title: 'Социальные сети',
    //     text: ''
    // }, [{id: 0, title: 'Есть'}, {id: 1, title: 'Нет'}]),
];